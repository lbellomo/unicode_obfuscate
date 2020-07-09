import pytest
from random import seed

from unicode_obfuscate import Obfuscator


text = "Nobody expext the spanish inquisition!"


def test_invalid_kind():
    with pytest.raises(ValueError):
        obfuscator = Obfuscator(kind="invalid_kind")  # noqa: F841


def test_valid_kind():
    for kind in ["intentional", "confusables"]:
        obfuscator = Obfuscator(kind=kind)
        assert type(obfuscator) == Obfuscator


def test_intentional():
    obfuscator = Obfuscator(kind="intentional")
    res = obfuscator.obfuscate(text)
    assert res == "Νοbοdу ехрехt tһе ѕраnіѕһ іnquіѕіtіοnǃ"


def test_prob():
    seed(42)
    obfuscator = Obfuscator(kind="intentional")
    res = obfuscator.obfuscate(text, prob=0.5)
    assert res == "Nοbοdy exрехt the sрaniѕh іnquіѕіtion!"
