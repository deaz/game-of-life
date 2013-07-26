from tkinter import *
from .game import Game

CELL_WIDTH = 5
COLS_COUNT = 100
ROWS_COUNT = 100
started = False


def update():
    game.update()
    game.draw()
    if started:
        root.after(100, update)


def start():
    global started
    if not started:
        started = True
        update()


def stop():
    global started
    started = False
    root.after_cancel(update)


def main():
    global root, canvas, game
    canvas_width = COLS_COUNT * (1 + CELL_WIDTH) + 1
    canvas_height = ROWS_COUNT * (1 + CELL_WIDTH) + 1

    root = Tk()
    controlsFrame = Frame(root, width=150)
    canvasFrame = Frame(root, width=canvas_width, height=canvas_height)
    controlsFrame.pack(side="left", fill="both", expand=1)
    canvasFrame.pack(side="right", fill="both")
    canvas = Canvas(canvasFrame, bg="white",
                    width=canvas_width,
                    height=canvas_height)
    canvas.pack()
    start_button = Button(controlsFrame, text="Start", command=start)
    start_button.pack(fill="x")
    stop_button = Button(controlsFrame, text="Stop", command=stop)
    stop_button.pack(fill="x")
    game = Game(COLS_COUNT, ROWS_COUNT, CELL_WIDTH, canvas)

    update()
    root.mainloop()


if __name__ == "__main__":
    main()
