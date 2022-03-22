import pathlib, zlib

if not pathlib.Path("assets").exists():
    ASSETS = pathlib.Path("..") / "assets"
else:
    ASSETS = pathlib.Path("assets")
WORD_LIST_FILE = ASSETS / "WORDS_LIST_COMPRESSED"
with WORD_LIST_FILE.open("rb") as file:
    temp = zlib.decompress(file.read()).decode()
    WORD_LIST = [temp[i : i + 5] for i in range(0, len(temp), 5)]
print(WORD_LIST)