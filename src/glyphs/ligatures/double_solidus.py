from glyphs.ligatures.spaced import SpacedLigatureGlyph
from glyphs.special.solidus import SolidusGlyph


class DoubleSolidusGlyph(SpacedLigatureGlyph):
    """Ligature glyph for //"""

    name = "double_solidus_liga"
    component_classes = [SolidusGlyph, SolidusGlyph]
    number_characters = 2
    shifts = (0.2, -0.2)
