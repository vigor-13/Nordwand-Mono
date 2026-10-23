from abc import abstractmethod

from draw.parallelogramm import draw_parallelogramm
from draw.rect import draw_rect
from glyphs import ContextualLigatureGlyph
from glyphs.special.equals_sign import EqualsSignGlyph


class EqualityLigatureGlyph(ContextualLigatureGlyph):
    """`==`-style ligature: the two `=` bars run unbroken across every cell.

    With `negated`, a slash at the slope of `/` crosses the bars (≠).
    Longer runs of `=` stay unligated.
    """

    feature_tags = ("liga",)
    forbidden_neighbors = ["equals_sign"]
    negated = False
    slash_ratio = 0.5  # slash size relative to `/`

    @property
    @abstractmethod
    def components(self) -> list[str]: ...

    def draw(self, pen, dc):
        eq = EqualsSignGlyph()
        s = eq.horizontal_bar_stroke(dc)
        x1 = eq.side_offset * dc.window_width
        x2 = self.number_characters * dc.window_width - x1
        for y in eq.horizontal_bar_heights(dc):
            draw_rect(pen, x1, y - s / 2, x2, y + s / 2)
        if self.negated:
            from glyphs.special.solidus import SolidusGlyph

            b = dc.body_bounds(offset=0, height="ascent")
            dx = self.slash_ratio * b.width / 2
            dy = self.slash_ratio * SolidusGlyph.height_ratio * dc.parenthesis_length / 2
            xc = self.number_characters * dc.window_width / 2
            draw_parallelogramm(
                pen, dc.stroke_x, dc.stroke_y, xc - dx, dc.math - dy, xc + dx, dc.math + dy
            )
