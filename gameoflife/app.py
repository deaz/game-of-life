import tkinter as tk
from multiprocessing import Process
from .graphicalgrid import BufferEmpty
from .game import Game


class App(tk.Tk):
    CELL_WIDTH = 5
    COLS_COUNT = 100
    ROWS_COUNT = 100
    DRAW_DELAY = 100

    def __init__(self):
        super().__init__()

        canvas_width = App.COLS_COUNT * (1+App.CELL_WIDTH) + 1
        canvas_height = App.ROWS_COUNT * (1+App.CELL_WIDTH) + 1

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

        self.game = Game(App.COLS_COUNT, App.ROWS_COUNT, App.CELL_WIDTH, canvas)

        updating_process = Process(target=self._update)
        updating_process.daemon = True
        updating_process.start()
        self._started = True
        self._draw_id = self.after(0, self._draw)

    def _update(self):
        while True:
            self.game.update()

    def _draw(self):
        try:
            self.game.draw()
        except BufferEmpty:
            if self._started:
                self._draw_id = self.after(10, self._draw)
        else:
            if self._started:
                self._draw_id = self.after(App.DRAW_DELAY, self._draw)

    def _start(self):
        if not self._started:
            self._started = True
            self._draw_id = self.after(0, self._draw)

    def _stop(self):
        self._started = False
        self.after_cancel(self._draw_id)