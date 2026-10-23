from glyphs.ligatures.left_arrow import LeftArrowGlyph
from glyphs.special.less_than_sign_2 import LessThenSign2Glyph


class LeftArrow2Glyph(LeftArrowGlyph):
    """Ligature glyph for <- with the wide `ss03` arrow head"""

    name = "left_arrow_liga_2"
    components = ["less_than_sign_2", "hyphen_minus"]
    span = LessThenSign2Glyph.span
