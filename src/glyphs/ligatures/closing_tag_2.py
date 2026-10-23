from glyphs.ligatures.spaced import SpacedLigatureGlyph
from glyphs.special.less_than_sign_2 import LessThenSign2Glyph
from glyphs.special.solidus import SolidusGlyph


class ClosingTag2Glyph(SpacedLigatureGlyph):
    """Ligature glyph for </ under `ss03`"""

    name = "closing_tag_liga_2"
    component_classes = [LessThenSign2Glyph, SolidusGlyph]
    number_characters = 2
    shifts = (0.15, -0.15)
