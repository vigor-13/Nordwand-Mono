from glyphs.ligatures.spaced import SpacedLigatureGlyph
from glyphs.special.ampersand import AmpersandGlyph


class DoubleAmpersandGlyph(SpacedLigatureGlyph):
    """Ligature glyph for &&"""

    name = "double_ampersand_liga"
    component_classes = [AmpersandGlyph, AmpersandGlyph]
    number_characters = 2
    shifts = (0.1, -0.1)
