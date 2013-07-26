from graphicalgrid import GraphicalGrid

class Game():
    def __init__(self, cols_count, rows_count, cell_width, canvas):
        self.canvas_width = cols_count * (1 + cell_width) + 1
        self.canvas_height = rows_count * (1 + cell_width) + 1
        self.cols_count = cols_count
        self.rows_count = rows_count
        self.cell_width = cell_width
        self.canvas = canvas
        
        self.cell_grid = GraphicalGrid(cols_count, rows_count, cell_width, canvas)
        
        self._draw_grid()
        
    def _draw_grid(self):
        for i in range(self.rows_count + 1):
            self.canvas.create_line(0, i * (self.cell_width + 1) + 1, 
                                    self.canvas_width, i * (self.cell_width + 1) + 1, fill="red")
        for i in range(self.cols_count + 1):
            self.canvas.create_line(i * (self.cell_width + 1) + 1, 0, 
                                    i * (self.cell_width + 1) + 1, self.canvas_height + 1, fill="red")
                                    
    def draw(self):
        self.cell_grid.draw()
        
    def update(self):
        self.cell_grid.update()
