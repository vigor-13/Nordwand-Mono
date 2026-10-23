from glyphs.ligatures.less_equal import LessEqualGlyph


class LessEqual2Glyph(LessEqualGlyph):
    """Ligature glyph for <= under `ss03`, same shape"""

    name = "less_equal_liga_2"
    components = ["less_than_sign_2", "equals_sign"]
