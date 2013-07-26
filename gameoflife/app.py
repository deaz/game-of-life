import tkinter as tk
from .game import Game

CELL_WIDTH = 5
COLS_COUNT = 100
ROWS_COUNT = 100
started = False


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        canvas_width = COLS_COUNT * (1 + CELL_WIDTH) + 1
        canvas_height = ROWS_COUNT * (1 + CELL_WIDTH) + 1

        controlsFrame = tk.Frame(self, width=150)
        canvasFrame = tk.Frame(self, width=canvas_width, height=canvas_height)
        controlsFrame.pack(side="left", fill="both", expand=1)
        canvasFrame.pack(side="right", fill="both")
        canvas = tk.Canvas(canvasFrame, bg="white",
                           width=canvas_width,
                           height=canvas_height)
        canvas.pack()
        start_button = tk.Button(controlsFrame, text="Start", command=self._start)
        start_button.pack(fill="x")
        stop_button = tk.Button(controlsFrame, text="Stop", command=self._stop)
        stop_button.pack(fill="x")

        self.game = Game(COLS_COUNT, ROWS_COUNT, CELL_WIDTH, canvas)

        self._started = True
        self._update()

    def _update(self):
        self.game.update()
        self.game.draw()
        if self._started:
            self.after(100, self._update)

    def _start(self):
        if not self._started:
            self._started = True
            self._update()

    def _stop(self):
        self._started = False
