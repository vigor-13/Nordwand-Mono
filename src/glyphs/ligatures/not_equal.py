from glyphs.ligatures.equality import EqualityLigatureGlyph


class NotEqualGlyph(EqualityLigatureGlyph):
    """Ligature glyph for !="""

    name = "not_equal_liga"
    components = ["exclamation_mark", "equals_sign"]
    number_characters = 2
    negated = True
