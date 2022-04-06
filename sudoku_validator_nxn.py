import math


class Sudoku(object):
    puzzle = [[]]

    def __init__(self, data):
        self.puzzle = data

    def is_valid(self):
        # validate dimensions first
        if not valid_dimensions(self.puzzle):
            return False
        max_number = len(self.puzzle)

        # validate numbers
        for i in range(max_number):
            for j in range(max_number):
                if not valid_number(self.puzzle, i, j):
                    return False
        return True


def valid_dimensions(puzzle):
    rows = len(puzzle)
    # ahora debo chequear que tenga la misma cantidad de columnas en todas las filas
    cols = None
    for i in range(rows):
        if i == 0:
            cols = len(puzzle[i])
        else:
            if len(puzzle[i]) != cols:
                return False
    return True


def is_in_the_row(board, row, column):
    count = 0
    max_value = len(board)
    for n in board[row]:
        if n == board[row][column]:
            count += 1
    return count >= 2


def is_in_the_column(board, row, column):
    count = 0
    for n in range(len(board)):
        if board[n][column] == board[row][column]:
            count += 1
    return count >= 2


def is_in_the_square(board, row, column):
    sqroot = int(math.sqrt(len(board)))
    start_row_index = row - row % sqroot
    start_col_index = column - column % sqroot
    count = 0
    for i in range(start_row_index, start_row_index + sqroot):
        for j in range(start_col_index, start_col_index + sqroot):
            if board[i][j] == board[row][column]:
                count += 1
    return count >= 2


def valid_number(board, row, column):
    # validate type first
    if not isinstance(board[row][column], int) or isinstance(board[row][column], bool):
        return False
    if not board[row][column] <= len(board) or not board[row][column] > 0:
        return False
    # validate number in board
    return (
        True
        if (not is_in_the_row(board, row, column))
        and (not is_in_the_column(board, row, column))
        and (not is_in_the_square(board, row, column))
        else False
    )


# tests

goodSudoku1 = Sudoku(
    [
        [7, 8, 4, 1, 5, 9, 3, 2, 6],
        [5, 3, 9, 6, 7, 2, 8, 4, 1],
        [6, 1, 2, 4, 3, 8, 7, 5, 9],
        [9, 2, 8, 7, 1, 5, 4, 6, 3],
        [3, 5, 7, 8, 4, 6, 1, 9, 2],
        [4, 6, 1, 9, 2, 3, 5, 8, 7],
        [8, 7, 6, 3, 9, 4, 2, 1, 5],
        [2, 4, 3, 5, 6, 1, 9, 7, 8],
        [1, 9, 5, 2, 8, 7, 6, 3, 4],
    ]
)

goodSudoku2 = Sudoku([[1, 4, 2, 3], [3, 2, 4, 1], [4, 1, 3, 2], [2, 3, 1, 4]])

# Invalid Sudoku
badSudoku1 = Sudoku(
    [
        [0, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
    ]
)

badSudoku2 = Sudoku([[1, 2, 3, 4, 5], [1, 2, 3, 4], [1, 2, 3, 4], [1]])

print(goodSudoku1.is_valid())
print(goodSudoku2.is_valid())
print(badSudoku1.is_valid())
print(badSudoku2.is_valid())
