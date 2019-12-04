import numpy as np


def calculate_neighbours(board):
    """
    Returns number of neighbours of board cells.

    Funkcja zwraca tablicę która w polu [R, C] zwraca liczbę sąsiadów którą
    ma komórka board[R, C].
    Obowiązuje sąsiedztwo Moore'a tzn. za sąsiada uznajemy żywą komórkę
    stykającą się bokiem bokach lub na ukos od danej komórki,
    więc maksymalna ilość sąsiadów danej komórki wynosi 8.
    Funkcja ta powinna być zwektoryzowana, tzn. liczba operacji w bytecodzie
    Pythona nie powinna zależeć od rozmiaru macierzy.
    (1 pkt.)

    Podpowiedź: Czy jest możliwe obliczenie ilości np. lewych sąsiadów
    których ma każda z komórek w macierzy, następnie liczby prawych sąsiadów
    itp.
    Podpowiedź II: Proszę uważać na komówki na bokach i rogach planszy.

    :param board: 2D array of agents states.
    :type board: np.ndarray
    :param periodic
    """
    # rozmiar tablicy
    r = len(board)
    c = len(board[0])

    # Inicjalizacja tablicy zerami
    neighbour_board = np.array([[0 for x in range(c)] for y in range(r)])


    # wiem, ze bardzo brzydko
    for i in range(r):
        for j in range(c):

            # przeliczenie dla "srodka" bez przegow
            if (r -1 > i > 0) and (c - 1 > j > 0):

                neighbour_board[i][j] = sum(board[i-1][j-1:j+2]) + sum(board[i+1][j-1:j+2]) + board[i][j-1] + board[i][j+1]

            # brzeg gorny
            elif i == 0 and (0 < j < c - 1):
                neighbour_board[i][j] = sum(board[i+1][j-1:j+2]) + board[i][j-1] + board[i][j+1]
            # brzeg dolny
            elif i == r - 1 and (0 < j < c - 1):
                neighbour_board[i][j] = sum(board[i-1][j-1:j+2]) + board[i][j-1] + board[i][j+1]
            # brzeg lewy
            elif j == 0 and (0 < i < r - 1):
                neighbour_board[i][j] = sum(board[i+1][:2]) + sum(board[i-1][:2]) + board[i][j+1]
            # brzeg prawy
            elif j == c - 1 and (0 < i < r - 1):
                neighbour_board[i][j] = sum(board[i+1][j-1:]) + sum(board[i-1][j-1:]) + board[i][j-1]
            # rogi
            if i == 0 and j == 0:
                neighbour_board[i][j] = sum(board[i+1][:2]) + board[i][j+1]
            elif i == 0 and j == c - 1:
                neighbour_board[i][j] = sum(board[i+1][j-1:]) + board[i][j-1]
            elif i == r-1 and j == 0:
                neighbour_board[i][j] = sum(board[i-1][:2]) + board[i][j+1]
            elif i == r-1 and j == c-1:
                neighbour_board[i][j] = sum(board[i-1][j-1:]) + board[i][j-1]


    return neighbour_board


def iterate(board):
    """
    Returns next iteration step of given board.

    Funkcja pobiera planszę game of life i zwraca jej następną iterację.
    Zasady Game of life są takie:
    1. Komórka może być albo żywa (True) albo martwa (False).
    2. Jeśli komórka jest martwa i ma trzech sąsiadów to ożywa.
    3. Jeśli komórka jest żywa i ma mniej niż dwóch sąsiadów to umiera,
       jeśli ma więcej niż trzech sąsiadów również umiera.
       W przeciwnym wypadku (dwóch lub trzech sąsiadów) to żyje dalej.
    (1 pkt.)

    :param board: 2D array of agents states.
    :type board: np.ndarray
    :return: next board state
    :rtype: np.ndarray
    """

    neighbours = calculate_neighbours(board)

    # Sprawdzanie liczby sasiadow danej komorki i aplikacja mechaniki gry
    for i in range(len(neighbours)):
        for j in range(len(neighbours[0])):
            if neighbours[i][j] >= 3:
                board[i][j] = True
            elif neighbours[i][j] < 2:
                board[i][j] = False
            else:
                continue
    return board


if __name__ == '__main__':
    _board = np.array([
        [False, False, False,  True, False,  True],
        [ True, False,  True, False, False,  True],
        [ True,  True, False,  True,  True,  True],
        [False,  True,  True, False, False,  True],
        [False, False, False,  True, False, False],
        [False,  True,  True,  True, False,  True]
    ])
    calculate_neighbours(_board)
    assert (calculate_neighbours(_board) == np.array([
        [1, 2, 2, 1, 3, 1,],
        [2, 4, 3, 4, 6, 3,],
        [3, 5, 5, 3, 4, 3,],
        [3, 3, 4, 4, 5, 2,],
        [2, 4, 6, 3, 4, 2,],
        [1, 1, 3, 2, 3, 0,],
    ])).all()
    assert (iterate(_board) == np.array([
        [False, False, False, False, True, False],
        [ True, False,  True, False, False,  True],
        [ True, False, False,  True, False,  True],
        [True,  True, False, False, False,  True],
        [False, False, False,  True, False, False],
        [False, False,  True,  True, True, False],
    ])).all()

