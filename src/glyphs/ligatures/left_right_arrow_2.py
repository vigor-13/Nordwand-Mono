from glyphs.ligatures.left_right_arrow import LeftRightArrowGlyph
from glyphs.special.less_than_sign_2 import LessThenSign2Glyph


class LeftRightArrow2Glyph(LeftRightArrowGlyph):
    """Ligature glyph for <-> with the wide `ss03` arrow heads"""

    name = "left_right_arrow_liga_2"
    components = ["less_than_sign_2", "hyphen_minus", "greater_than_sign_2"]
    span = LessThenSign2Glyph.span
