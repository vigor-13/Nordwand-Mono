from abc import abstractmethod

from fontTools.pens.transformPen import TransformPen

from glyphs import LigatureGlyph


class SpacedLigatureGlyph(LigatureGlyph):
    """Ligature that keeps its characters' own shapes and only pulls them closer.

    `shifts` moves each component horizontally, in cells (positive is right).
    """

    shifts: tuple[float, ...] = ()

    @property
    @abstractmethod
    def component_classes(self) -> list: ...

    @property
    def components(self):
        return [cls.name for cls in self.component_classes]

    def lift(self, dc) -> float:
        """Vertical move applied to every component."""
        return 0

    def draw(self, pen, dc):
        w = dc.window_width
        y = self.lift(dc)
        for i, (cls, shift) in enumerate(zip(self.component_classes, self.shifts)):
            cls().draw(TransformPen(pen, (1, 0, 0, 1, (i + shift) * w, y)), dc)
