# unicode obfuscate

Replace unicode characters with visually similar ones.

## Instalation 

Be sure to use python >= 3.7

```bash
pip install unicode_obfuscate
```

## Usage

Simple usage:

```python
>>> from unicode_obfuscate import Obfuscator
>>> text = "And Now for Something Completely Different"
>>> obfuscator = Obfuscator()
>>> new_text = obfuscator.obfuscate(text)
>>> new_text
'Αnd Νοw fοr Ѕοmеtһіng Сοmрlеtеlу Dіffеrеnt'
>>> text == new_text
False

# You can also pass a probability to change only some characters.
>>> obfuscator.obfuscate(text, prob=0.3) 
'And Νow for Ѕomething Сompletely Different'
```

There are two different datasets to map the characters:
- intencional: A very short list with very similar characters (Only one option for each character). The data is taken from [here](https://www.unicode.org/Public/security/latest/intentional.txt).
- confusables: A gigantic list of characters (and multiple possible characters for each one). The data is taken from [here](https://www.unicode.org/Public/security/latest/confusables.txt).


By default, `intencional` is used but it can change with keyword `kind`:

```python
# this uses the dataset 'intencional'
>>> obfuscator = Obfuscator()  

# this uses the dataset 'confusables'
>>> obfuscator = Obfuscator(kind="confusables")  
```

