import random
import time

test1 = [
    [9, 0, 0, 0, 8, 0, 0, 0, 1],
    [0, 0, 0, 4, 0, 6, 0, 0, 0],
    [0, 0, 5, 0, 7, 0, 3, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 4, 0],
    [4, 0, 1, 0, 6, 0, 5, 0, 8],
    [0, 9, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 7, 0, 3, 0, 2, 0, 0],
    [0, 0, 0, 7, 0, 5, 0, 0, 0],
    [1, 0, 0, 0, 4, 0, 0, 0, 7],
]
solution1 = [
    [9, 2, 6, 5, 8, 3, 4, 7, 1],
    [7, 1, 3, 4, 2, 6, 9, 8, 5],
    [8, 4, 5, 9, 7, 1, 3, 6, 2],
    [3, 6, 2, 8, 5, 7, 1, 4, 9],
    [4, 7, 1, 2, 6, 9, 5, 3, 8],
    [5, 9, 8, 3, 1, 4, 7, 2, 6],
    [6, 5, 7, 1, 3, 8, 2, 9, 4],
    [2, 8, 4, 7, 9, 5, 6, 1, 3],
    [1, 3, 9, 6, 4, 2, 8, 5, 7],
]

test2 = [
    [0, 0, 5, 0, 0, 0, 8, 0, 0],
    [0, 2, 0, 8, 0, 9, 0, 7, 0],
    [3, 0, 0, 0, 4, 0, 0, 0, 1],
    [0, 3, 0, 2, 0, 6, 0, 1, 0],
    [0, 0, 2, 0, 0, 0, 5, 0, 0],
    [0, 7, 0, 5, 0, 4, 0, 6, 0],
    [2, 0, 0, 0, 6, 0, 0, 0, 4],
    [0, 8, 0, 4, 0, 2, 0, 9, 0],
    [0, 0, 7, 0, 0, 0, 2, 0, 0],
]
solution2 = [
    [7, 1, 5, 6, 2, 3, 8, 4, 9],
    [6, 2, 4, 8, 1, 9, 3, 7, 5],
    [3, 9, 8, 7, 4, 5, 6, 2, 1],
    [5, 3, 9, 2, 7, 6, 4, 1, 8],
    [4, 6, 2, 1, 9, 8, 5, 3, 7],
    [8, 7, 1, 5, 3, 4, 9, 6, 2],
    [2, 5, 3, 9, 6, 7, 1, 8, 4],
    [1, 8, 6, 4, 5, 2, 7, 9, 3],
    [9, 4, 7, 3, 8, 1, 2, 5, 6],
]

test3 = [
    [0, 8, 0, 0, 5, 0, 0, 2, 0],
    [6, 0, 0, 0, 0, 7, 0, 0, 5],
    [0, 0, 0, 2, 0, 9, 0, 0, 0],
    [0, 1, 7, 0, 0, 0, 9, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 9, 0, 0, 0, 8, 6, 0],
    [0, 0, 0, 8, 0, 3, 0, 0, 0],
    [9, 0, 0, 6, 0, 0, 0, 0, 2],
    [0, 5, 0, 0, 1, 0, 0, 3, 0],
]
solution3 = [
    [7, 8, 3, 4, 5, 6, 1, 2, 9],
    [6, 9, 2, 1, 8, 7, 3, 4, 5],
    [1, 4, 5, 2, 3, 9, 6, 7, 8],
    [8, 1, 7, 3, 6, 2, 9, 5, 4],
    [5, 6, 4, 7, 9, 8, 2, 1, 3],
    [3, 2, 9, 5, 4, 1, 8, 6, 7],
    [4, 7, 6, 8, 2, 3, 5, 9, 1],
    [9, 3, 1, 6, 7, 5, 4, 8, 2],
    [2, 5, 8, 9, 1, 4, 7, 3, 6],
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


def get_all_free_squares(puzzle):
    res = []
    for i in range(9):
        for j in range(9):
            if not puzzle[i][j]:
                res.append((i, j))
    return res


def sudoku(puzzle):
    free_squares = get_all_free_squares(puzzle)
    # por cada free square, le asigno un numero random hasta que consiga el resultado

    while 1:
        for square in free_squares:
            print(square)
            visited = set([])
            (row, col) = square
            rand = random.randint(1, 9)
            print("random ", rand, " for", square)
            while len(visited) < 9:
                if (
                    (not is_in_the_column(puzzle, col, rand))
                    and (not is_in_the_row(puzzle, row, rand))
                    and (not is_in_the_region(puzzle, row, col, rand))
                    and (not rand in visited)
                ):
                    puzzle[row][col] = rand
                    break
                else:
                    # tiro otro random y bloqueo ese numero. Si tengo 9 bloqueados, tengo que empezar desde el principio de free_squares, ya que no tengo solucion por este camino
                    visited.add(rand)
                    rand = random.randint(1, 9)
        print("Finished 1 loop. Puzzle completed?", is_completed(puzzle))
        print(puzzle)
        time.sleep(2)
        if is_completed(puzzle):
            break
    return puzzle


# Test
print(sudoku(test1))
# print(sudoku(test1) == solution1)
# print(sudoku(test2) == solution2)
# print(sudoku(test3) == solution3)
