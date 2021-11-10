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
from src.grid import screen_h, screen_w
from src.pieces import *


class GameMechanics:
    def __init__(self):
        self.black = (0, 0, 0)

    def check_collisions(self, tetriminos, grid):
        good_pos = [[(j, i) for j in range(10) if grid[i][j] == self.black] for i in range(22)]
        good_pos = [i for param in good_pos for i in param]
        piece = convert_piece(tetriminos)

        for pos in piece:
            if pos not in good_pos:
                if pos[1] > -1:
                    return False
        return True

    def check_row_and_score(self, grid, second_grid, score):
        for i in range(0, len(grid)):
            if self.black not in grid[i]:
                for z in range(0, len(grid[i])):
                    for j in range(0, len(grid[i])):
                        second_grid[(j, i - z)] = grid[i - (z + 1)][j]
                score += 25
                tetris_line_clear = pygame.mixer.Sound("assets/tetrislineclear.mp3")
                tetris_line_clear.play()
                pygame.time.wait(25)
        return score

    def game_speed_up(speed, score):
        if score <= 1000:
            new_speed = 0.3
            return new_speed
        elif score <= 2000:
            new_speed = 0.25
            return new_speed
        elif score <= 3500:
            new_speed = 0.2
            return new_speed
        elif score <= 5000:
            new_speed = 0.15
            return new_speed
        elif score <= 8000:
            new_speed = 0.1
            return new_speed
        else:
            return speed

    def game_over(self, screen, grid):
        if grid[0][1] != self.black or grid[0][3] != self.black or grid[0][5] != self.black or grid[0][7] != self.black or grid[0][7] != self.black:
            text_font = pygame.font.SysFont('segoe script', 70, True)
            label6 = text_font.render('GAMEOVER', True, (255, 255, 255))
            screen.blit(label6, [screen_h / 2 - 300, screen_w / 2])
            pygame.display.flip()
            pygame.mixer.stop()
            tetris_game_over = pygame.mixer.Sound("assets/GAMEOVER.mp3")
            tetris_game_over.play()
            pygame.time.wait(4500)
            return False
        else:
            return True
