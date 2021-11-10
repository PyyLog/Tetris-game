# ------------------------------------------------------------------------------
# Name:        Grand Projet IN211
# Purpose:     Tetris
#
# Authors:     KANTANE Pritam Charles and BUSSIERE Edgar
# Class:       2PF2
#
# Created:     08/11/2020
# ------------------------------------------------------------------------------
import pygame

screen_w = 600
screen_h = 700

class Grid:
    def __init__(self):
        self.width = 300
        self.height = 660
        self.block = 30
        self.tlx = 30
        self.tly = 30
        self.black = (0, 0, 0)

    def make_grid(self, second_grid):
        grid = [[self.black for _ in range(10)] for _ in range(22)]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (j, i) in second_grid:
                    grid[i][j] = second_grid[(j, i)]
        return grid

    def draw_grid(self, screen, grid):
        for i in range(len(grid)):
            pygame.draw.line(screen, (255, 255, 255), (self.tlx, self.tly +
                                                       i * self.block), (self.tlx + self.width, self.tly + i * self.block))
            for j in range(len(grid[i])):
                pygame.draw.line(screen, (255, 255, 255), (self.tlx +
                                                           j * self.block, self.tly), (self.tlx + j * self.block, self.tly + self.height))
                pygame.draw.rect(screen, (0, 200, 200),
                                 (self.tlx, self.tly, self.width, self.height), 4)

    def draw_win(self, screen, grid):
        pygame.display.update()
        screen.fill(self.black)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                pygame.draw.rect(
                    screen, grid[i][j], (self.tlx + j * self.block, self.tly + i * self.block, self.block, self.block), 0)
        self.draw_grid(screen, grid)

    def draw_little_grid(self, screen, next_tetriminos):
        text_pos_w = screen_w * 2 / 3 - 15
        text_pos_h = screen_h / 3
        text_tlx = text_pos_w - 40
        text_tly = text_pos_h
        rect_width = 230
        rect_height = 230
        text_font = pygame.font.SysFont('segoe script', 25)
        label2 = text_font.render("Next Piece", True, (255, 255, 255))
        screen.blit(label2, [text_pos_w, text_pos_h])
        pygame.draw.rect(screen, (255, 255, 255), (text_tlx, text_tly, rect_width, rect_height), 2)

        grid_np = [[self.black for _ in range(6)] for _ in range(5)]
        for i in range(len(grid_np)):
            for j in range(len(grid_np[i])):
                pygame.draw.rect(screen, grid_np[i][j],
                                 (text_tlx + 40 + j * self.block, text_tly + 60 + i * self.block, self.block, self.block), 1)
        for i in range(len(grid_np)):
            pygame.draw.line(screen, (255, 255, 255), (text_tlx + 40, text_tly + 60 + i * self.block),
                             (text_tlx + 40 + 150, text_tly + 60 + i * self.block))
            for j in range(len(grid_np[i])):
                pygame.draw.line(screen, (255, 255, 255), (text_tlx + 40 + j * self.block, text_tly + 60),
                                 (text_tlx + 40 + j * self.block, text_tly + 60 + 120))

        pygame.draw.line(screen, (255, 0, 0), (text_tlx, text_tly), (text_tlx + rect_height, text_tly + rect_width), 4)
        pygame.draw.line(screen, (255, 0, 0), (text_tlx + rect_width, text_tly), (text_tlx, text_tly + rect_width), 4)
