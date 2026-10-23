from glyphs.ligatures.spaced import SpacedLigatureGlyph
from glyphs.special.asterisk import AsteriskGlyph
from glyphs.special.solidus import SolidusGlyph


class CommentOpenGlyph(SpacedLigatureGlyph):
    """Ligature glyph for /*"""

    name = "comment_open_liga"
    component_classes = [SolidusGlyph, AsteriskGlyph]
    number_characters = 2
    shifts = (0.12, -0.12)
