from glyphs.ligatures.spaced import SpacedLigatureGlyph
from glyphs.special.greater_than_sign import GreaterThenSignGlyph
from glyphs.special.solidus import SolidusGlyph


class SelfClosingTagGlyph(SpacedLigatureGlyph):
    """Ligature glyph for />"""

    name = "self_closing_tag_liga"
    component_classes = [SolidusGlyph, GreaterThenSignGlyph]
    number_characters = 2
    shifts = (0.15, -0.15)
