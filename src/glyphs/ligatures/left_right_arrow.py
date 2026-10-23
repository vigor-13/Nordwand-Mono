from glyphs import LigatureGlyph
from draw.chevron import draw_chevron
from glyphs.special.less_than_sign import LessThenSignGlyph
from draw.rect import draw_rect


class LeftRightArrowGlyph(LigatureGlyph):
    """Ligature glyph for <->, the heads of <- and -> joined by one bar"""

    name = "left_right_arrow_liga"
    components = ["less_than_sign", "hyphen_minus", "greater_than_sign"]
    feature_tags = (
        "liga",
        "ss02",
    )
    number_characters = 3
    width_ratio = 0.88
    span = LessThenSignGlyph.span
    stroke_ratio = 1.2

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        h = dc.parenthesis_length * self.span
        s = dc.stroke_x
        s2 = self.stroke_ratio * dc.stroke_x
        w = dc.window_width
        left_tip = w - b.x2
        right_tip = b.x2 + 2 * w
        draw_chevron(
            pen, dc.stroke_x, dc.stroke_y, left_tip, w - b.x1, dc.math, h, delta=s2
        )
        draw_chevron(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            right_tip,
            b.x1 + 2 * w,
            dc.math,
            h,
            delta=s2,
        )
        draw_rect(
            pen, left_tip + s2, dc.math - s / 2, right_tip - s2, dc.math + s / 2
        )
