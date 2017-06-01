import fileinput
import numpy as np


BOARD_SIZE = 3


def main():
    print("Enter board:")
    board = parse_board(read_board())
    validate_board(board)
    if has_winner(board):
        print("This board has a winner!")
    else:
        print("This board has no winner.")


def read_board():
    for line in fileinput.input():
        yield line


def parse_board(raw_board):
    parsed = []
    for line in raw_board:
        line = line.strip('\n')
        line = (0 if i == ' ' else i for i in line)
        line = (1 if i in ['x', 'X'] else i for i in line)
        line = [-1 if i in ['o', 'O'] else i for i in line]
        parsed.append(line)
    return parsed


def validate_board(board, size=BOARD_SIZE):
    if len(board) > size:
        raise ValueError("Board is not of size %sx%s" % (size, size))
    for line in board:
        if len(line) > size:
            raise ValueError("Line '%s' is not if size %s" % (line, size))
        for char in line:
            if char not in [0, -1, 1]:
                raise ValueError("Invalid character in board: '%s'" % char)


def has_winner(board, size=BOARD_SIZE):
    board = np.array(board)
    return any([
        size in np.absolute(board.sum(0)),
        size in np.absolute(board.sum(1)),
        size == np.absolute(board.trace()),
        size == np.absolute(board[::-1].trace()),
    ])


if __name__ == '__main__':
    main()


def test_starting_board_has_no_winner():
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert has_winner(board) is False

def test_row_winner():
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [1, 1, 1],
    ]
    assert has_winner(board) is True

def test_column_winner():
    board = [
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
    ]
    assert has_winner(board) is True

def test_main_diagonal_winner():
    board = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]
    assert has_winner(board) is True

def test_second_diagonal_winner():
    board = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0],
    ]
    assert has_winner(board) is True

def test_no_winner_two_players():
    board = [
        [-1, 0, 1],
        [1, 1, -1],
        [-1, 0, 0],
    ]
    assert has_winner(board) is False


def test_two_players_winner():
    board = [
        [-1, 0, 1],
        [-1, 1, -1],
        [-1, 1, 0],
    ]
    assert has_winner(board) is True


def test_parse_board():
    raw = [
        'oxx\n',
        'x o\n',
        ' xo\n',
    ]
    expected = [
        [-1,  1,  1],
        [ 1,  0, -1],
        [ 0,  1, -1],
    ]
    assert parse_board(raw) == expected
