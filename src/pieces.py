# ------------------------------------------------------------------------------
# Name:        Grand Projet IN211
# Purpose:     Tetris
#
# Authors:     KANTANE Pritam Charles and BUSSIERE Edgar
# Class:       2PF2
#
# Created:     08/11/2020
# ------------------------------------------------------------------------------
import random

I = [[[1, 1, 1, 1]],
     [[1], [1], [1], [1]]]

O = [[[2, 2], [2, 2]]]

T = [[[3, 3, 3], [0, 3, 0]],
     [[3, 0], [3, 3], [3, 0]],
     [[0, 3, 0], [3, 3, 3]],
     [[0, 3], [3, 3], [0, 3]]]

L = [[[4, 4, 4], [4, 0, 0]],
     [[4, 0], [4, 0], [4, 4]],
     [[0, 0, 4], [4, 4, 4]],
     [[4, 4], [0, 4], [0, 4]]]

J = [[[5, 5, 5], [0, 0, 5]],
     [[5, 5], [5, 0], [5, 0]],
     [[5, 0, 0], [5, 5, 5]],
     [[0, 5], [0, 5], [5, 5]]]

S = [[[0, 6, 6], [6, 6, 0]],
     [[6, 0], [6, 6], [0, 6]]]

Z = [[[7, 7, 0], [0, 7, 7]],
     [[0, 7], [7, 7], [7, 0]]]

list_pieces = [I, T, L, J, S, Z]
colors_pieces = [(255, 165, 0), (255, 0, 0), (255, 255, 0),
                 (0, 0, 255), (127, 0, 255), (0, 255, 255), (0, 255, 0)]


class Piece:
    def __init__(self, x, y, tetriminos):
        self.x = x
        self.y = y
        self.tetriminos = tetriminos
        self.color = colors_pieces[list_pieces.index(tetriminos)]
        self.rotate = 0
        self.black = (0, 0, 0)


def get_piece():
    id_piece = random.randint(0, 5)
    return Piece(3, 0, list_pieces[id_piece])


def convert_piece(tetriminos):
    pos = []
    piece = tetriminos.tetriminos[tetriminos.rotate % len(tetriminos.tetriminos)]
    for i, line in enumerate(piece):
        for j, case in enumerate(line):
            if case != 0:
                pos.append((tetriminos.x + j, tetriminos.y + i - 2))
    return pos


def draw_piece(grid, current_piece):
    tetriminos_pos = convert_piece(current_piece)
    for i in tetriminos_pos:
        x, y = i
        if y > -1:
            grid[y][x] = current_piece.color
