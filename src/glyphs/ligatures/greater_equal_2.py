from glyphs.ligatures.greater_equal import GreaterEqualGlyph


class GreaterEqual2Glyph(GreaterEqualGlyph):
    """Ligature glyph for >= under `ss03`, same shape"""

    name = "greater_equal_liga_2"
    components = ["greater_than_sign_2", "equals_sign"]
