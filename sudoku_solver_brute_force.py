puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

solution = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]


def is_in_the_row(puzzle, row, n):
    return n in puzzle[row]


def is_in_the_column(puzzle, column, n):
    return n in [puzzle[i][column] for i in range(9)]


def is_in_the_region(puzzle, row, column, n):
    row_start_index = row - row % 3
    column_start_index = column - column % 3
    for i in range(row_start_index, row_start_index + 3):
        for j in range(column_start_index, column_start_index + 3):
            if puzzle[i][j] == n:
                return True
    return False


def search_free_square(puzzle):
    for i in range(9):
        for j in range(9):
            if not puzzle[i][j]:
                return (i, j)
    return None


def is_completed(puzzle):
    for i in range(9):
        for j in range(9):
            if not puzzle[i][j]:
                return False
    return True


def sudoku(puzzle):

    coords = search_free_square(puzzle)
    if coords:
        (row, column) = coords
        for n in range(1, 10):
            if (
                (not is_in_the_row(puzzle, row, n))
                and (not is_in_the_column(puzzle, column, n))
                and (not is_in_the_region(puzzle, row, column, n))
            ):
                # si el numero en cuestion es un numero valido, lo inserto
                puzzle[row][column] = n
                if sudoku(puzzle):
                    return puzzle  # si alguno de mis hijos me retorna un puzzle, significa que lo pude terminar y lo retorno
        # si no sirvio ninguno de estos numeros, pongo un 0 en mi lugar asi lo vacio,
        # retorno a quien me llamo un false para que luego, la funcion search_free_square pueda volver a encontrar estos bloques libres
        puzzle[row][column] = 0
    return is_completed(puzzle)


# Test
print(sudoku(puzzle) == solution)
