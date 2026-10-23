from glyphs.ligatures.comparison import ComparisonLigatureGlyph


class GreaterEqualGlyph(ComparisonLigatureGlyph):
    """Ligature glyph for >="""

    name = "greater_equal_liga"
    components = ["greater_than_sign", "equals_sign"]
    points_left = False
