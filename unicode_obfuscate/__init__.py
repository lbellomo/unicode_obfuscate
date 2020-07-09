__version__ = "0.1.1"
__all__ = ["Obfuscator"]

import json
from pathlib import Path
from typing import Optional
from random import random, choice


class Obfuscator:
    def __init__(self, kind: str = "intentional"):
        """
        Replace unicode characters with visually similar ones.

        Parameters
        ----------
        kind : str
            The dataset to map the characters. Possible options are:
                - intencional: A very short list with very similar
                  characters (Only one option for each character).
                - confusables: A gigantic list of characters
                  (and multiple possible characters for each one).
        """
        path_json = Path(__file__).parent / "data" / f"{kind}.json"
        if not path_json.exists():
            raise ValueError(f"'{kind}' is not  a valid kind.")

        with open(path_json) as f:
            self._data = json.load(f)

    def _process_char(self, char: str, prob: Optional[float] = None) -> str:
        if not prob and char in self._data:
            return choice(self._data[char])
        elif char in self._data and random() < prob:
            return choice(self._data[char])
        else:
            return char

    def obfuscate(self, text: str, prob: Optional[float] = None) -> str:
        """ 
        Obfuscate the text.

        Parameters
        ----------
        text : str
            The text to obfuscate.
        prob: float
            The probability of change each character. 
            For 1 change in each possible character.
        
        Returns
        -------
        str
            The new text.
        """
        return "".join(self._process_char(char, prob) for char in text)
