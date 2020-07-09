import json
from pathlib import Path
from typing import Tuple
from collections import defaultdict

import requests


def parse_txt(txt: str, invert: bool = False) -> defaultdict:
    """Parse txt from unicode.org"""
    data = defaultdict(list)

    for i, line in enumerate(txt.split("\n")):
        if line.startswith("#"):
            continue
        elif not i:  # skip the first line
            continue
        if not line:
            continue

        # print(line)
        a, b = parse_line(line)

        if invert:
            data[b] += [a]
        else:
            data[a] += [b]
    
    return data


def parse_line(line: str) -> Tuple[str, str]:
    """Parse a line from txt"""
    if "#*" in line:  # indicates that the character is not an XID character
        line = line.replace("#*", "#")

    _, line = line.split("#", maxsplit=1)
    return line[3], line[7]


confusables_url = "https://www.unicode.org/Public/security/latest/confusables.txt"
confusables_poplist = []

intencional_url = "https://www.unicode.org/Public/security/latest/intentional.txt"
intencional_poplist = ["d"]  # the only one that is not the same visually ( d !~ ԁ )


options = [[intencional_url, intencional_poplist, False],
           [confusables_url, confusables_poplist, True]]

path_data = Path(__file__).parent / "../unicode_obfuscate/data"

if __name__ == "__main__":
    path_data.mkdir(exist_ok=True)

    for url, poplist, invert in options:
        r = requests.get(url)
        data = parse_txt(r.text, invert=invert)

        for char in poplist:
            data.pop(char)

        json_name = url.rsplit("/", maxsplit=1)[-1].replace(".txt", ".json")

        with open(path_data / json_name, "w") as f:
            json.dump(data, f, indent=4)