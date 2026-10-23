from draw.chevron import draw_chevron
from draw.rect import draw_rect
from glyphs import ContextualLigatureGlyph
from glyphs.special.equals_sign import EqualsSignGlyph


class ComparisonLigatureGlyph(ContextualLigatureGlyph):
    """`<=` / `>=` drawn as ≤ / ≥ over two cells: a chevron above a bar on the baseline.

    `<==` / `<=>` and the like stay unligated.
    """

    feature_tags = ("liga",)
    forbidden_neighbors = ["equals_sign", "less_than_sign", "greater_than_sign"]
    number_characters = 2
    points_left = True
    half_width = 0.48  # chevron and bar half width, in cells
    span = 0.5
    stroke_ratio = 1.2
    bar_gap = 0.75  # gap between chevron and bar, in bar strokes

    def draw(self, pen, dc):
        w = dc.window_width
        s = EqualsSignGlyph().horizontal_bar_stroke(dc)
        s2 = self.stroke_ratio * dc.stroke_x
        h = dc.parenthesis_length * self.span
        y_bar = s / 2  # the bar sits on the baseline
        y_chevron = y_bar + s / 2 + self.bar_gap * s + h / 2
        left, right = w - self.half_width * w, w + self.half_width * w
        tip, back = (left, right) if self.points_left else (right, left)
        draw_chevron(pen, s2, s2, tip, back, y_chevron, h, delta=s2)
        draw_rect(pen, left, y_bar - s / 2, right, y_bar + s / 2)
