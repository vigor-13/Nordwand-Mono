from glyphs.ligatures.spaced import SpacedLigatureGlyph
from glyphs.special.less_than_sign import LessThenSignGlyph
from glyphs.special.solidus import SolidusGlyph


class ClosingTagGlyph(SpacedLigatureGlyph):
    """Ligature glyph for </"""

    name = "closing_tag_liga"
    component_classes = [LessThenSignGlyph, SolidusGlyph]
    number_characters = 2
    shifts = (0.15, -0.15)
