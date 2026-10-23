from glyphs.ligatures.spaced import SpacedLigatureGlyph
from glyphs.special.vertical_line import VerticalLineGlyph


class DoubleVerticalLineGlyph(SpacedLigatureGlyph):
    """Ligature glyph for ||"""

    name = "double_vertical_line_liga"
    component_classes = [VerticalLineGlyph, VerticalLineGlyph]
    number_characters = 2
    shifts = (0.25, -0.25)
