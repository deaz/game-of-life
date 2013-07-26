import random


class CellGrid:
    def __init__(self, cols_count, rows_count, cells=[]):
        self.cells = [[(random.randrange(2) == 1) for i in range(rows_count)] for i in range(cols_count)]

        self.cells = cells
        self.cells[1][0] = True
        self.cells[2][1] = True
        self.cells[0][2] = True
        self.cells[1][2] = True
        self.cells[2][2] = True

        self.cells_to_check = {(i, j) for i in range(cols_count) for j in range(rows_count)}
        self.cols_count = cols_count
        self.rows_count = rows_count

    def _count_neighbour_cells(self, cell):
        count = 0
        neighbours = self._get_neighbours(cell)
        for (i, j) in neighbours:
            if self.cells[i % self.cols_count][j % self.rows_count]:
                count += 1
        return count

    def _get_neighbours(self, cell):
        neighbours = set()
        x, y = cell
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i != x or j != y:
                    neighbours.add((i, j))
        return neighbours

    def update(self):
        new_cells = [[self.cells[i][j] for j in range(self.rows_count)] for i in range(self.cols_count)]
        new_cells_to_check = set()
        for cell in self.cells_to_check:
            count = self._count_neighbour_cells(cell)
            x, y = cell
            x = x % self.cols_count
            y = y % self.rows_count
            if self.cells[x][y] is True and (count < 2 or count > 3):
                new_cells[x][y] = False
                new_cells_to_check.add(cell)
                new_cells_to_check.update(self._get_neighbours(cell))
            elif self.cells[x][y] is False and count == 3:
                new_cells[x][y] = True
                new_cells_to_check.add(cell)
                new_cells_to_check.update(self._get_neighbours(cell))
        self.cells = new_cells
        self.cells_to_check = new_cells_to_check

    def get_alive_cells(self):
        return {(i, j) for i in range(self.cols_count) for j in range(self.rows_count) if self.cells[i][j]}
