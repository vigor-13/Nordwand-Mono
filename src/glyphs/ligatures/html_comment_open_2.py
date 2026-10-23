from glyphs.ligatures.spaced import SpacedLigatureGlyph
from glyphs.special.exclamation_mark import ExclamationMarkGlyph
from glyphs.special.hyphen_minus import HyphenMinusGlyph
from glyphs.special.less_than_sign_2 import LessThenSign2Glyph


class HtmlCommentOpen2Glyph(SpacedLigatureGlyph):
    """Ligature glyph for <!-- under `ss03`"""

    name = "html_comment_open_liga_2"
    component_classes = [LessThenSign2Glyph, ExclamationMarkGlyph, HyphenMinusGlyph, HyphenMinusGlyph]
    number_characters = 4
    shifts = (0.35, 0.25, 0.1, -0.3)
