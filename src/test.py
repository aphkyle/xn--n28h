import playsound, pathlib,time

if not pathlib.Path("assets").exists():
    ASSETS = pathlib.Path("..") / "assets"
else:
    ASSETS = pathlib.Path("assets")

playsound.playsound(ASSETS / "BoxCat-Games-Assignment.wav", block=False)
time.sleep(64)