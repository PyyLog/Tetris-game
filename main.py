from src.classes.grid import Grid
from src.classes.game_mechanics import GameMechanics
from src.classes.pieces import get_piece, convert_piece, draw_piece
from src.constants import *
import pygame

pygame.init()


class Game:
    """
    Main class to run the Tetris game.
    """
    def __init__(self, screen):
        self.screen = screen
        self.grid_obj = Grid()
        self.game_mechanic = GameMechanics()

    def main(self) -> None:
        """
        Main function to run the Tetris game loop.
        """
        tetris_song = pygame.mixer.Sound(TETRIS_THEME_AUDIO_PATH)
        tetris_song.play(50)
        second_grid = {}
        running = True
        change = False
        current_piece = get_piece()
        next_piece = get_piece()
        score = 0

        clock = pygame.time.Clock()
        timer = 0
        speed = 0.1

        while running:
            grid = self.grid_obj.make_grid(second_grid)
            for i in range(0, 4):
                score = self.game_mechanic.check_row_and_score(grid, second_grid, score)
            speed = self.game_mechanic.game_speed_up(speed, score)
            running = self.game_mechanic.game_over(self.screen, grid)

            clock.tick()
            timer += clock.get_rawtime()
            if timer / 1000 > speed:
                timer = 0
                current_piece.y += 1
                if not self.game_mechanic.check_collisions(current_piece, grid):
                    current_piece.y -= 1
                    change = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        current_piece.x -= 1
                        if not self.game_mechanic.check_collisions(current_piece, grid):
                            current_piece.x += 1

                    elif event.key == pygame.K_RIGHT:
                        current_piece.x += 1
                        if not self.game_mechanic.check_collisions(current_piece, grid):
                            current_piece.x -= 1

                    elif event.key == pygame.K_SPACE:
                        current_piece.rotate += 1
                        if not self.game_mechanic.check_collisions(current_piece, grid):
                            current_piece.rotate -= 1

                    elif event.key == pygame.K_DOWN:
                        current_piece.y += 1
                        if not self.game_mechanic.check_collisions(current_piece, grid):
                            current_piece.y -= 1

            draw_piece(grid, current_piece)
            tetriminos_pos = convert_piece(current_piece)
            if change:
                for pos in tetriminos_pos:
                    second_grid[pos] = current_piece.color
                current_piece = next_piece
                next_piece = get_piece()
                change = False

            self.grid_obj.draw_win(screen, grid)
            self.grid_obj.draw_next_piece(screen, next_piece)
            text_font = pygame.font.SysFont(SCORE_TEXT_FONT, SCORE_TEXT_SIZE)
            label1 = pygame.image.load(TETRIS_LOGO_PATH)
            label2 = text_font.render("Score :", True, WHITE)
            label3 = text_font.render(str(score), True, YELLOW)
            screen.blit(label1, [SCREEN_W * 1.72 / 3, 24])
            screen.blit(label2, [SCREEN_W * 1.75 / 3, 550])
            screen.blit(label3, [SCREEN_W * 2.3 / 3, 550])

            pygame.display.flip()


screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
game = Game(screen)
game.main()
pygame.quit()
