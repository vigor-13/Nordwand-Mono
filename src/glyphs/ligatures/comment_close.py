from glyphs.ligatures.spaced import SpacedLigatureGlyph
from glyphs.special.asterisk import AsteriskGlyph
from glyphs.special.solidus import SolidusGlyph


class CommentCloseGlyph(SpacedLigatureGlyph):
    """Ligature glyph for */"""

    name = "comment_close_liga"
    component_classes = [AsteriskGlyph, SolidusGlyph]
    number_characters = 2
    shifts = (0.12, -0.12)
