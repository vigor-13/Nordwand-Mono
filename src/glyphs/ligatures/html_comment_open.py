from glyphs.ligatures.spaced import SpacedLigatureGlyph
from glyphs.special.exclamation_mark import ExclamationMarkGlyph
from glyphs.special.hyphen_minus import HyphenMinusGlyph
from glyphs.special.less_than_sign import LessThenSignGlyph


class HtmlCommentOpenGlyph(SpacedLigatureGlyph):
    """Ligature glyph for <!--"""

    name = "html_comment_open_liga"
    component_classes = [LessThenSignGlyph, ExclamationMarkGlyph, HyphenMinusGlyph, HyphenMinusGlyph]
    number_characters = 4
    shifts = (0.35, 0.25, 0.1, -0.3)
