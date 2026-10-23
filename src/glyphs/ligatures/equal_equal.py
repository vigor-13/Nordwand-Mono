from glyphs.ligatures.equality import EqualityLigatureGlyph


class EqualEqualGlyph(EqualityLigatureGlyph):
    """Ligature glyph for =="""

    name = "equal_equal_liga"
    components = ["equals_sign", "equals_sign"]
    number_characters = 2
