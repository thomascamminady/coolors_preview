import re

from coolor_preview.hexcolor import HexColor
from coolor_preview.palette import Palette


def is_valid_url(url):
    pattern = r"^https://coolors\.co/palette/(?:[0-9a-fA-F]{6}-)*[0-9a-fA-F]{6}$"
    if re.match(pattern, url):
        return True
    return False


def url2palette(url: str) -> Palette:
    if not is_valid_url(url):
        raise Exception(f"This does not look like a coolors url: {url}")

    return Palette(
        [HexColor(f"#{hex_code}") for hex_code in url.split("/")[-1].split("-")]
    )
