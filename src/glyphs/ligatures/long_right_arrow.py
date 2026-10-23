from glyphs import LigatureGlyph
from draw.chevron import draw_chevron
from glyphs.special.greater_than_sign import GreaterThenSignGlyph
from draw.rect import draw_rect


class LongRightArrowGlyph(LigatureGlyph):
    """Ligature glyph for -->, a -> with a bar over three cells"""

    name = "long_right_arrow_liga"
    components = ["hyphen_minus", "hyphen_minus", "greater_than_sign"]
    feature_tags = (
        "liga",
        "ss02",
    )
    number_characters = 3
    width_ratio = 0.88
    side_offset = 0.05
    span = GreaterThenSignGlyph.span
    stroke_ratio = 1.2

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        h = dc.parenthesis_length * self.span
        s = dc.stroke_x
        s2 = self.stroke_ratio * dc.stroke_x
        x_tip = b.x2 + 2 * dc.window_width
        draw_chevron(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            x_tip,
            b.x1 + 2 * dc.window_width,
            dc.math,
            h,
            delta=s2,
        )
        draw_rect(
            pen,
            self.side_offset * dc.window_width,
            dc.math - s / 2,
            x_tip - s2,
            dc.math + s / 2,
        )
