from glyphs.ligatures.equality import EqualityLigatureGlyph


class TripleEqualGlyph(EqualityLigatureGlyph):
    """Ligature glyph for ==="""

    name = "triple_equal_liga"
    components = ["equals_sign", "equals_sign", "equals_sign"]
    number_characters = 3
