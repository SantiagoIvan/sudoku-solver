def is_in_the_row(board, row, column):
    count = 0
    for n in board[row]:
        if n == board[row][column]:
            count += 1
    return False if count < 2 else True


def is_in_the_column(board, row, column):
    count = 0
    for n in range(9):
        if board[n][column] == board[row][column]:
            count += 1
    return False if count < 2 else True


def is_in_the_square(board, row, column):
    start_row_index = row - row % 3
    start_col_index = column - column % 3
    count = 0
    for i in range(start_row_index, start_row_index + 3):
        for j in range(start_col_index, start_col_index + 3):
            if board[i][j] == board[row][column]:
                count += 1
    return False if count < 2 else True


def valid_number(board, row, column):
    return (
        True
        if (not is_in_the_row(board, row, column))
        and (not is_in_the_column(board, row, column))
        and (not is_in_the_square(board, row, column))
        else False
    )


def valid_solution(board):
    for row in range(9):
        for column in range(9):
            if not valid_number(board, row, column):
                return False
    return True
