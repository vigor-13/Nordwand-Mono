from glyphs.ligatures.long_right_arrow import LongRightArrowGlyph
from glyphs.special.greater_than_sign_2 import GreaterThenSign2Glyph


class LongRightArrow2Glyph(LongRightArrowGlyph):
    """Ligature glyph for --> with the wide `ss03` arrow head"""

    name = "long_right_arrow_liga_2"
    components = ["hyphen_minus", "hyphen_minus", "greater_than_sign_2"]
    span = GreaterThenSign2Glyph.span
