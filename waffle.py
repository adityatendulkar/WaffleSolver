class Waffle:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [['-' for _ in range(cols)] for _ in range(rows)]
        self.colors = {'W': 'wrong', 'P': 'mispositioned', 'R': 'right'}

    def set_item(self, row, col, item, color):
        if not (0 <= row < self.rows) or not (0 <= col < self.cols):
            raise ValueError("Invalid row or column index")

        if item != '-' and color not in self.colors:
            raise ValueError("Invalid color")

        self.grid[row][col] = item + color

    def get_item(self, row, col):
        if not (0 <= row < self.rows) or not (0 <= col < self.cols):
            raise ValueError("Invalid row or column index")

        return self.grid[row][col]

    def display(self):
        for row in self.grid:
            print(' '.join(row))

waffle = Waffle(3, 3)
waffle.set_item(0, 0, 'A', 'W')
waffle.set_item(1, 1, 'B', 'P')
waffle.set_item(2, 2, 'C', 'R')
waffle.display()