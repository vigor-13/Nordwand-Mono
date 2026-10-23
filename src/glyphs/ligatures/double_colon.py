from glyphs.ligatures.spaced import SpacedLigatureGlyph
from glyphs.special.colon import ColonGlyph


class DoubleColonGlyph(SpacedLigatureGlyph):
    """Ligature glyph for ::"""

    name = "double_colon_liga"
    component_classes = [ColonGlyph, ColonGlyph]
    number_characters = 2
    shifts = (0.25, -0.25)

    def lift(self, dc):
        """Center the dots on the math axis, like `=`."""
        return dc.math - dc.x_height / 2
