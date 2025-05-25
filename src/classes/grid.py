import pygame
from typing import List, Tuple, Dict
from src.classes.pieces import Piece, convert_piece
from src.constants import *


class Grid:
    """
    Class to create and manage the Tetris grids.
    """
    def __init__(self):
        self.width = 300
        self.height = 660
        self.block = 30
        self.tlx = 30
        self.tly = 30
        self.black = BLACK

    def make_grid(self, second_grid: Dict[Tuple[int, int], Tuple[int, int, int]]) -> list:
        """
        Create a grid for the game.
        """
        grid = [[self.black for _ in range(10)] for _ in range(22)]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (j, i) in second_grid:
                    grid[i][j] = second_grid[(j, i)]
        return grid

    def draw_grid(self, screen: pygame.Surface, grid: List[List[Tuple[int, int, int]]]) -> None:
        """
        Draw the grid on the screen.
        """
        for i in range(len(grid)):
            pygame.draw.line(screen, WHITE, (self.tlx, self.tly +
                                                       i * self.block), (self.tlx + self.width, self.tly + i * self.block))
            for j in range(len(grid[i])):
                pygame.draw.line(screen, WHITE, (self.tlx +
                                                           j * self.block, self.tly), (self.tlx + j * self.block, self.tly + self.height))
                pygame.draw.rect(screen, CYAN,
                                 (self.tlx, self.tly, self.width, self.height), 4)

    def draw_win(self, screen: pygame.Surface, grid: List[List[Tuple[int, int, int]]]) -> None:
        """
        Draw the window screen with the grid.
        """
        pygame.display.update()
        screen.fill(self.black)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                pygame.draw.rect(
                    screen, grid[i][j], (self.tlx + j * self.block, self.tly + i * self.block, self.block, self.block), 0)
        self.draw_grid(screen, grid)

    def draw_next_piece(self, screen: pygame.Surface, next_tetriminos: Piece) -> None:
        """
        Draw the next piece on the screen.
        """
        text_pos_w = SCREEN_W * 2 / 3 - 15
        text_pos_h = SCREEN_H / 3 + 10
        text_tlx = text_pos_w - 40
        text_tly = SCREEN_H / 3
        rect_width = 230
        rect_height = 230
        text_font = pygame.font.SysFont(NEXT_PIECE_TEXT_FONT, NEXT_PIECE_TEXT_SIZE)
        label2 = text_font.render("Next Piece", True, WHITE)
        screen.blit(label2, [text_pos_w, text_pos_h])
        pygame.draw.rect(screen, WHITE, (text_tlx, text_tly, rect_width, rect_height), 2)

        grid_np = [[self.black for _ in range(6)] for _ in range(5)]

        # Add the next piece to the grid
        if next_tetriminos.name == 'I':
            x = 2
            y = 2
        elif next_tetriminos.name == 'J':
            x = 2
            y = 3
        else :
            x = 1
            y = 3

        temp_piece = Piece(x, y, next_tetriminos.tetriminos, next_tetriminos.name)

        piece_positions = convert_piece(temp_piece)

        # Place the piece in the grid
        for pos in piece_positions:
            x, y = pos
            if 0 <= x < 6 and 0 <= y < 5:
                grid_np[y][x] = next_tetriminos.color

        # Draw the grid with the piece
        for i in range(len(grid_np)):
            for j in range(len(grid_np[i])):
                pygame.draw.rect(screen, grid_np[i][j],
                                 (text_tlx + 40 + j * self.block, text_tly + 60 + i * self.block,
                                  self.block, self.block), 0)

        # Draw grid lines
        for i in range(len(grid_np)):
            pygame.draw.line(screen, (255, 255, 255),
                             (text_tlx + 40, text_tly + 60 + i * self.block),
                             (text_tlx + 40 + 150, text_tly + 60 + i * self.block))
            for j in range(len(grid_np[i])):
                pygame.draw.line(screen, (255, 255, 255),
                                 (text_tlx + 40 + j * self.block, text_tly + 60),
                                 (text_tlx + 40 + j * self.block, text_tly + 60 + 120))
