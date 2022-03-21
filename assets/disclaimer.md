I do not own the `WORD_LIST_COMPRESSED` file,
The original `txt` file can be found [here](https://raw.githubusercontent.com/InnovativeInventor/dict4schools/master/safedict_full.txt)
and should be under The Unlicense License [(OSI)](https://opensource.org/licenses/unlicense)
The code i used to generate this is:
```py
import pathlib
import ast
import zlib
import urllib.request as request

word = request.urlopen("https://raw.githubusercontent.com/InnovativeInventor/dict4schools/master/safedict_full.txt")
lst = (word.read().decode()).split("\n")

p = pathlib.Path("assets")
p.mkdir(parents=True, exist_ok=True)

with (p / "WORDS_LIST_COMPRESSED").open("wb") as file:
    file.write(zlib.compress(''.join(lst).encode()))
```