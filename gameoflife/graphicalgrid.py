import multiprocessing
from .cellgrid import CellGrid


class GraphicalGrid(CellGrid):
    def __init__(self, cols_count, rows_count, cell_width, canvas):
        super().__init__(cols_count, rows_count)
        self.cell_width = cell_width
        self.canvas = canvas
        self.old_rects = {}
        self.recv_conn, self.send_conn = multiprocessing.Pipe(False)

    def draw(self):
        if not self.recv_conn.poll():
            raise BufferEmpty()
        alive_cells = self.recv_conn.recv()
        old_cells_indices = set(self.old_rects.keys())
        cells_to_remove = old_cells_indices.difference(alive_cells)
        cells_to_draw = alive_cells.difference(old_cells_indices)
        for cell in cells_to_remove:
            self.canvas.delete(self.old_rects[cell])
            del self.old_rects[cell]
        for (i, j) in cells_to_draw:
            rect = self.canvas.create_rectangle(i * (self.cell_width+1) + 2,
                                                j * (self.cell_width+1) + 2,
                                                (i+1) * (self.cell_width+1),
                                                (j+1) * (self.cell_width+1),
                                                fill="black")
            self.old_rects[(i, j)] = rect

    def update(self):
        super().update()
        self.send_conn.send(self.get_alive_cells())


class BufferEmpty(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'Buffer is empty'
