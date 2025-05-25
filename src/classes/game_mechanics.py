import pygame
from typing import List, Tuple, Dict, Any
from src.classes.pieces import convert_piece
from src.constants import *


class GameMechanics:
    """
    Class to handle the game mechanics of Tetris, including collision detection,
    """
    def __init__(self):
        self.black: Tuple[int, int, int] = BLACK

    def check_collisions(self, tetriminos: Any, grid: List[List[Tuple[int, int, int]]]) -> bool:
        """
        Check if the current piece collides with the grid or goes out of bounds.
        """
        good_pos = [[(j, i) for j in range(10) if grid[i][j] == self.black] for i in range(22)]
        good_pos = [i for param in good_pos for i in param]
        piece = convert_piece(tetriminos)

        for pos in piece:
            if pos not in good_pos:
                if pos[1] > -1:
                    return False
        return True

    def check_row_and_score(
            self,
            grid: List[List[Tuple[int, int, int]]],
            second_grid: Dict[Tuple[int, int], Tuple[int, int, int]],
            score: int
    ) -> int:
        """
        Check if any rows are filled, clear them, and update the score.
        """
        lines_cleared = 0
        i = len(grid) - 1

        while i >= 0:
            if self.black not in grid[i]:
                for j in range(10):
                    if (j, i) in second_grid:
                        del second_grid[(j, i)]

                new_second_grid = {}
                for (x, y), color in second_grid.items():
                    if y < i:
                        new_second_grid[(x, y + 1)] = color
                    else:
                        new_second_grid[(x, y)] = color

                second_grid.clear()
                second_grid.update(new_second_grid)

                grid.pop(i)
                grid.insert(0, [self.black for _ in range(10)])

                lines_cleared += 1
                score += 50

                tetris_line_clear = pygame.mixer.Sound(TETRIS_LINE_CLEAR_AUDIO_PATH)
                tetris_line_clear.play()
                pygame.time.wait(CLEAR_ROWS_PAUSE_TIME)

            else:
                i -= 1

        return score

    def game_speed_up(self, speed: float, score: int) -> float:
        """
        Adjust the game speed based on the score.
        """
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
            new_speed = 0.12
            return new_speed
        else:
            return speed

    def game_over(self, screen: pygame.Surface, grid: List[List[Tuple[int, int, int]]]) -> bool:
        """
        Check if the game is over by checking if any blocks are in the top row.
        """
        for j in range(10):
            if grid[0][j] != self.black:
                text_font = pygame.font.SysFont(GAMEOVER_TEXT_FONT, GAMEOVER_TEXT_SIZE, True)
                label6 = text_font.render('GAMEOVER', True, WHITE)
                screen.blit(label6, [SCREEN_H / 2 - 300, SCREEN_W / 2])
                pygame.display.flip()
                pygame.mixer.stop()
                tetris_game_over = pygame.mixer.Sound(GAMEOVER_AUDIO_PATH)
                tetris_game_over.play()
                pygame.time.wait(GAMEOVER_PAUSE_TIME)
                return False

        return True
