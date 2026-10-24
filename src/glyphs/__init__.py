from abc import ABC, abstractmethod


class Glyph(ABC):
    accent_x_offset: int = 0

    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def unicode(self) -> str: ...

    @property
    @abstractmethod
    def offset(self) -> int: ...

    number_characters: int = 1
    font_feature: dict = None
    alternative_character_comment: str = None
    default_italic: bool = False
    italic_only: bool = False

    @abstractmethod
    def draw(self, pen, dc) -> None: ...

    def extra_cut(self, dc) -> int:
        return 0.66 * max(0, dc.stroke_x - dc.default_stroke)

    def diag_stroke_dampening(self, ratio, stroke, coef=0.25):
        from math import exp

        ds = max(stroke - 85, 0) / 85
        # If ds > 0, we add some dampening, other we let as is
        if ds <= 0:
            return ratio * stroke

        delta = exp(-ds * coef)
        sx = delta * stroke * ratio
        return sx


class InfiniteLigatureGlyph(Glyph):
    """Glyph whose horizontal bars can join across any number of cells."""

    ligature_dent_stroke = 0.5
    ligature_junction_width = 0.5

    @abstractmethod
    def horizontal_bar_heights(self, dc) -> tuple[float, ...]: ...

    @abstractmethod
    def horizontal_bar_stroke(self, dc) -> float: ...

    @abstractmethod
    def horizontal_bar_bounds(self, dc) -> tuple[float, float]: ...

    def draw_non_horizontal(self, pen, dc) -> None:
        pass

    def draw(self, pen, dc) -> None:
        self._draw_joined(pen, dc, join_left=False, join_right=False)

    def _draw_joined(self, pen, dc, join_left, join_right) -> None:
        from draw.rect import draw_rect

        stroke = self.horizontal_bar_stroke(dc)
        dent = stroke * self.ligature_dent_stroke
        junction_width = stroke * self.ligature_junction_width
        x1, x2 = self.horizontal_bar_bounds(dc)
        if join_left:
            x1 = junction_width / 2
        if join_right:
            x2 = dc.window_width - junction_width / 2

        self.draw_non_horizontal(pen, dc)
        for y in self.horizontal_bar_heights(dc):
            draw_rect(pen, x1, y - stroke / 2, x2, y + stroke / 2)
            if join_right:
                draw_rect(
                    pen,
                    dc.window_width - junction_width / 2,
                    y - dent / 2,
                    dc.window_width + junction_width / 2,
                    y + dent / 2,
                )

    def ligature_forms(self):
        return [
            InfiniteLigatureForm(self, "start", join_left=False, join_right=True),
            InfiniteLigatureForm(self, "middle", join_left=True, join_right=True),
            InfiniteLigatureForm(self, "end", join_left=True, join_right=False),
        ]


class InfiniteLigatureForm(Glyph):
    """One contextual joining form of an :class:`InfiniteLigatureGlyph`."""

    generated_only = True
    name = None
    unicode = None
    offset = 0
    number_characters = 1
    font_feature = None
    default_italic = False
    italic_only = False
    feature_tags = ("dlig",)

    def __init__(self, source, position, join_left, join_right):
        self.source = source
        self.source_name = source.name
        self.position = position
        self.join_left = join_left
        self.join_right = join_right
        self.name = f"{source.name}_liga_{position}"

    def draw(self, pen, dc):
        self.source._draw_joined(
            pen,
            dc,
            join_left=self.join_left,
            join_right=self.join_right,
        )


class LigatureGlyph(Glyph):
    """Base class for ligature glyphs.

    Subclasses must define `components` — a list of glyph names that
    this ligature replaces (e.g. ["low_line", "low_line"] for "__").
    Set `feature_tags` to one or more OpenType tags; enabling any listed
    feature activates the ligature.
    """

    unicode = None
    offset = 0
    feature_tags = ("liga",)

    @property
    @abstractmethod
    def components(self) -> list[str]: ...

    def parts(self):
        """One glyph per cell, so every character keeps its own glyph."""
        return [LigaturePartGlyph(self, i) for i in range(self.number_characters)]


class LigaturePartGlyph(Glyph):
    """One cell of a multi-cell ligature, cut out of the full drawing.

    Editors and browsers handle one glyph per character far better than one
    glyph spanning several characters (e.g. when syntax highlighting puts
    `-` and `>` in different elements). The outer cells keep anything drawn
    past the ligature's edges.
    """

    generated_only = True
    name = None
    unicode = None
    offset = 0
    number_characters = 1
    font_feature = None
    default_italic = False
    italic_only = False

    def __init__(self, source, index):
        self.source = source
        self.index = index
        self.name = f"{source.name}.{index + 1}"

    def draw(self, pen, dc):
        import pathops
        from fontTools.pens.transformPen import TransformPen

        full = pathops.Path()
        self.source.draw(pathops.PathPen(full), dc)
        w = dc.window_width
        far = 10 * w
        last = self.source.number_characters - 1
        x1 = -far if self.index == 0 else self.index * w
        x2 = far if self.index == last else (self.index + 1) * w
        cell = pathops.Path()
        cell_pen = pathops.PathPen(cell)
        cell_pen.moveTo((x1, -far))
        cell_pen.lineTo((x2, -far))
        cell_pen.lineTo((x2, far))
        cell_pen.lineTo((x1, far))
        cell_pen.closePath()
        part = pathops.op(full, cell, pathops.PathOp.INTERSECTION)
        part.draw(TransformPen(pen, (1, 0, 0, 1, -self.index * w, 0)))


class ContextualLigatureGlyph(LigatureGlyph):
    """Ligature that only fires when not adjacent to `forbidden_neighbors`.

    Useful for capped-length ligatures: e.g. `==` and `===` ligate, but
    `====` and longer stay unligated. Set `forbidden_neighbors` to the
    glyph names whose presence on either side disqualifies the match
    (typically the ligature's own component glyph).
    """

    forbidden_neighbors: list[str] = []
    feature_tags = ("calt",)
