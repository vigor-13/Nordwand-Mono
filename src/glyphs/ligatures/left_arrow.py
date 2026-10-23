from glyphs import LigatureGlyph
from draw.chevron import draw_chevron
from glyphs.special.less_than_sign import LessThenSignGlyph
from draw.rect import draw_rect


class LeftArrowGlyph(LigatureGlyph):
    """Ligature glyph for <-, the mirror image of ->"""

    name = "left_arrow_liga"
    components = ["less_than_sign", "hyphen_minus"]
    feature_tags = (
        "liga",
        "ss02",
    )
    number_characters = 2
    width_ratio = 0.88
    side_offset = 0.05
    span = LessThenSignGlyph.span
    gap = 0.0
    stroke_ratio = 1.2

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        h = dc.parenthesis_length * self.span
        s = dc.stroke_x
        s2 = self.stroke_ratio * dc.stroke_x
        x2 = 2 * dc.window_width - self.side_offset * dc.window_width
        g = self.gap * dc.window_width
        x_tip = dc.window_width - b.x2
        draw_chevron(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            x_tip,
            dc.window_width - b.x1,
            dc.math,
            h,
            delta=s2,
        )
        draw_rect(
            pen,
            x_tip + s2 + g,
            dc.math - s / 2,
            x2,
            dc.math + s / 2,
        )
