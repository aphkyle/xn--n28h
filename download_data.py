import pathlib
import ast
import zlib
import urllib.request as request

word = request.urlopen(
    "https://raw.githubusercontent.com/InnovativeInventor/dict4schools/master/safedict_full.txt"
)
lst = (word.read().decode()).split("\n")

p = pathlib.Path("assets")
p.mkdir(parents=True, exist_ok=True)

with (p / "WORDS_LIST_COMPRESSED").open("wb") as file:
    file.write(zlib.compress("".join(lst).encode()))
