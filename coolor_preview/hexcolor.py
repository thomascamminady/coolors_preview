import re
from dataclasses import dataclass


@dataclass
class HexColor:
    def __init__(self, hex: str):
        if not self._is_valid_color(hex):
            raise Exception(f"{hex} is not a valid hex color.")
        self.hex = hex.lower()

    def _is_valid_color(self, hex: str):
        match = re.search(r"^#(?:[0-9a-fA-F]{3}){1,2}$", hex)
        if match:
            return True
        else:
            return False

    def __repr__(self):
        return self.hex
