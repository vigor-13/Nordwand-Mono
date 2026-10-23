from glyphs.ligatures.spaced import SpacedLigatureGlyph
from glyphs.special.question_mark import QuestionMarkGlyph


class DoubleQuestionMarkGlyph(SpacedLigatureGlyph):
    """Ligature glyph for ??"""

    name = "double_question_mark_liga"
    component_classes = [QuestionMarkGlyph, QuestionMarkGlyph]
    number_characters = 2
    shifts = (0.12, -0.12)
