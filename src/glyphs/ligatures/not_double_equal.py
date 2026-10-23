from glyphs.ligatures.equality import EqualityLigatureGlyph


class NotDoubleEqualGlyph(EqualityLigatureGlyph):
    """Ligature glyph for !=="""

    name = "not_double_equal_liga"
    components = ["exclamation_mark", "equals_sign", "equals_sign"]
    number_characters = 3
    negated = True
