from glyphs.ligatures.spaced import SpacedLigatureGlyph
from glyphs.special.greater_than_sign_2 import GreaterThenSign2Glyph
from glyphs.special.solidus import SolidusGlyph


class SelfClosingTag2Glyph(SpacedLigatureGlyph):
    """Ligature glyph for /> under `ss03`"""

    name = "self_closing_tag_liga_2"
    component_classes = [SolidusGlyph, GreaterThenSign2Glyph]
    number_characters = 2
    shifts = (0.15, -0.15)
