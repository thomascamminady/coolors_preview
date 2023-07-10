from dataclasses import dataclass

from coolor_preview.hexcolor import HexColor


@dataclass
class Palette:
    def __init__(self, colors: list[HexColor]):
        self.colors = colors

    @property
    def get_hex(self) -> list[str]:
        """Returns palette as list of hex codes."""
        return [c.hex for c in self.colors]
