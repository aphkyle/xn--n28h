import random
import pathlib
import zlib
import threading

import playsound

from rich import box
from rich.panel import Panel
from rich.align import Align

from textual.app import App
from textual.widget import Widget
from textual.widgets import Placeholder, Button
from textual.reactive import Reactive

globals()["evil"] = 1
globals()["you_can_now_speak"] = 0
globals()["dont_say_anything"] = 1
motive = [
    "YOU CAN DO THIS!",
    "COME ON!",
    "DO IT MATE",
    "NICE WORK, KEEP IT GOING",
    "DONT FEEL BAD",
    "GOOD JOB",
    "KEEP IT UP",
    "NICE",
    "COOL",
    "ZAMN",
    "DAMN",
    "YOU CAN DO BETTER",
]
mean = [
    "haha 😈",
    "im evil 😈",
    "im so evil 😈",
    "😈😈😈",
    ">:)",
    "protecting human from victory 😈",
    "im very evil 😈",
    "it took me so long to write these 😈",
    "nice one, can you do the next one though 😈",
    "good luck 😈",
    "oh this one is hard 😈",
    "MUAHAHAHAHA 😈"
]

if not pathlib.Path("assets").exists():
    ASSETS = pathlib.Path("..") / "assets"
else:
    ASSETS = pathlib.Path("assets")
WORD_LIST_FILE = ASSETS / "dictionary" / "WORDS_LIST_COMPRESSED"
with WORD_LIST_FILE.open("rb") as file:
    temp = zlib.decompress(file.read()).decode()
    WORD_LIST = [temp[i : i + 5] for i in range(0, len(temp), 5)]


def check(answer, given):
    if answer == given:
        return (
            f"[black on dark_olive_green2 bold]{answer.upper()}[/black on dark_olive_green2 bold]",
            1,
        )
    correct = ""
    incorrect = ""
    construct = ["", "", "", "", ""]  # basically mutable string
    for idx, ac, gc in zip(range(len(answer)), answer, given):
        if ac == gc:
            correct += ac
            construct[
                idx
            ] = f"[black on dark_olive_green2 bold]{gc}[/black on dark_olive_green2 bold]"
            incorrect += " "
        else:
            correct += " "
            incorrect += gc
    for idx, gc in enumerate(incorrect):
        if gc != " ":
            if answer.count(gc) == correct.count(gc):
                construct[idx] = f"[white on grey54 bold]{gc}[/white on grey54 bold]"
            else:
                construct[
                    idx
                ] = f"[black on light_goldenrod1 bold]{gc}[/black on light_goldenrod1 bold]"
    return "".join(construct), 0


class PanelWidget(Widget):
    mouse_over = Reactive(False)

    def __init__(self, text, title) -> None:
        self.text = text
        self.title = title
        super().__init__()

    def render(self):
        return Panel(
            Align(
                self.text,
                "center",
            ),
            title=self.title,
        )


class Wordle(Placeholder):
    def __init__(
        self,
        answer,
        panel: PanelWidget,
        title,
        aslkfjslhjdfgklj=(
            1 + 1 - 1 - 1 / 1 / 2 / 3 / 4 / 5 / 6 / 7 * 1212809548 * 0 - 1
        ),
    ) -> None:
        self. saljklksjrioqushfkj = 0
        self.fjlghkjlaslaskhjfdlk = aslkfjslhjdfgklj
        self.title = title
        self.panel = panel
        self.answer = answer
        self.tries = 0
        self.win = False
        self.temp_word = ""
        self.text = ""
        self.static_text = ""
        super().__init__()

    def render(self):
        return Panel(
            Align(
                self.static_text
                + f"[white on grey54 bold]{self.text}[white on grey54 bold]",
                "center",
            ),
            title=self.title,
            border_style=("yellow" if self.mouse_over else "red")
            if self.fjlghkjlaslaskhjfdlk
            else ("green" if self.mouse_over else "blue"),
            box=box.HEAVY if self.has_focus else box.ROUNDED,
            style=self.style,
            height=self.height,
        )

    def checked(self, e=0):
        temp = self.panel.text
        self.tries += 1
        self.static_text += self.text + "\n"
        self.text = ""
        if self.win:
            self.panel.text = (
                "yay, you won!"
                if self.fjlghkjlaslaskhjfdlk + 1023 == 2 ** 10 - 1
                else "you won, i lost 👿"
            )
            self.panel.refresh()
        elif self.tries > 5:
            self.panel.text = (
                f"oof, you lost, AND THE WORD IS '{self.answer.upper()}'!!"
                if self.fjlghkjlaslaskhjfdlk + 1023 == 2 ** 10 - 1
                else f"i won, you lost 😈, the word is '{self.answer.upper()}'"
            )
            self.panel.refresh()
        else:
            self.panel.text = random.choice(
                mean if self.fjlghkjlaslaskhjfdlk else motive
            )
        if e:
            self.panel.text = f"{temp} and {self.panel.text}"
        self.panel.refresh()

    async def on_key(self, key):
        if not self.win and self.tries < 6:
            if key.key.isalpha() and len(key.key) == 1 and len(self.temp_word) < 5:
                self.temp_word += key.key.upper()
            elif key.key == "ctrl+h":  # ctrl+h is somehow identified as backspace
                self.temp_word = self.temp_word[:-1]
            elif key.key == "enter":
                if self.temp_word.lower() in WORD_LIST and len(self.temp_word) == 5:
                    if self.fjlghkjlaslaskhjfdlk and random.random() < 0.3:
                        self. saljklksjrioqushfkj = True
                        self.temp_word = random.choice(WORD_LIST)
                        self.panel.text = "I'VE CHANGED YOUR WORD HAHAHA 😈"
                        self.panel.refresh()
                    elif self.fjlghkjlaslaskhjfdlk and random.random() < 0.2:
                        self. saljklksjrioqushfkj = True
                        self.tries += 1
                        self.panel.text = "YOU'VE LOST A TRY 😈"
                        self.panel.refresh()
                    else:
                        self. saljklksjrioqushfkj = False
                    output = check(self.answer.upper(), self.temp_word.upper())
                    self.text = output[0]
                    self.win = output[1]
                    self.checked(dont_say_anything if (self. fjlghkjlaslaskhjfdlk and self. saljklksjrioqushfkj) else you_can_now_speak)
                    self.temp_word = ""
                    self.refresh()
                    return
                elif len(self.temp_word) != 5:
                    self.panel.text = "Whoopsie, the word is too short!"
                    self.panel.refresh()
                else:
                    self.panel.text = "Whoopsie, not in word list!"
                    self.panel.refresh()
            self.text = self.temp_word
            self.refresh()

    async def reset(self, answer, panel):
        self.panel = panel
        self.answer = answer
        self.tries = 0
        self.win = False
        self.temp_word = ""
        self.text = ""
        self.static_text = ""
        self.panel.text = "RESTARTED!"
        self.refresh()
        self.panel.refresh()


class MyApp(App):
    async def on_load(self):
        # executor = ThreadPoolExecutor(2)
        # loop = asyncio.get_running_loop()
        
        # loop.run_in_executor(executor, self.music)
        t = threading.Thread(target=music)
        t.daemon = True
        t.start()
        # sorry, i couldn't figure out how to do the above thingy,
        # so i chose the easiest way :sunglasses:
        
        self.answer_panel1 = PanelWidget("", "NORMAL WORDLE")
        self.answer_panel2 = PanelWidget("", "EVIL WORDLE TWIN")
        self.wordle_widget1 = Wordle(
            random.choice(WORD_LIST), self.answer_panel1, "WORDLE"
        )
        self.wordle_widget2 = Wordle(
            random.choice(WORD_LIST), self.answer_panel2, "WORDLE'S EVIL TWIN", evil
        )
        self.restart_button = Button("RESTART", name="restart")
        self.quit_button = Button("QUIT", name="quit", style="white on red")

    async def on_key(self, event) -> None:
        await self.wordle_widget1.on_key(event)
        await self.wordle_widget2.on_key(event)

    async def on_mount(self) -> None:
        await self.view.dock(self.wordle_widget1, size=8)
        await self.view.dock(self.wordle_widget2, size=8)
        await self.view.dock(self.answer_panel1, size=3)
        await self.view.dock(self.answer_panel2, size=3)
        await self.view.dock(self.restart_button, size=3)
        await self.view.dock(self.quit_button, size=3)

    async def handle_button_pressed(self, message):
        if isinstance(message.sender, Button):
            if message.sender.name == "restart":
                await self.wordle_widget1.reset(
                    random.choice(WORD_LIST), self.answer_panel1
                )
                await self.wordle_widget2.reset(
                    random.choice(WORD_LIST), self.answer_panel2
                )
                self.refresh()
            elif message.sender.name == "quit":
                self.console.bell()  # lil troll because im evil
                await self.action_quit()

def music():
    while True:
        try:
            playsound.playsound(ASSETS / "music" / "BoxCat-Games-Assignment.wav", block=True)
        except KeyboardInterrupt:
            quit()

MyApp.run(title="Wordle",) # log="textual.log") # for debugging
