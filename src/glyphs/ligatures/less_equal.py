from glyphs.ligatures.comparison import ComparisonLigatureGlyph


class LessEqualGlyph(ComparisonLigatureGlyph):
    """Ligature glyph for <="""

    name = "less_equal_liga"
    components = ["less_than_sign", "equals_sign"]
