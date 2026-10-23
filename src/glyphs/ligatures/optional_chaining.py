from glyphs.ligatures.spaced import SpacedLigatureGlyph
from glyphs.special.full_stop import FullStopGlyph
from glyphs.special.question_mark import QuestionMarkGlyph


class OptionalChainingGlyph(SpacedLigatureGlyph):
    """Ligature glyph for ?."""

    name = "optional_chaining_liga"
    component_classes = [QuestionMarkGlyph, FullStopGlyph]
    number_characters = 2
    shifts = (0.1, -0.3)
