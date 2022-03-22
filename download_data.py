import pathlib
import zlib
import urllib.request as request

word_lst = request.urlopen(
    "https://raw.githubusercontent.com/InnovativeInventor/dict4schools/master/safedict_full.txt"
)
lst = [word for word in (word_lst.read().decode()).split("\n") if len(word) == 5 and word.isalpha()]

p = pathlib.Path("assets")
p.mkdir(parents=True, exist_ok=True)

with (p / "WORDS_LIST_COMPRESSED").open("wb") as file:
    file.write(zlib.compress("".join(lst).encode()))
