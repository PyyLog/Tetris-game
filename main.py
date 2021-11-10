# ------------------------------------------------------------------------------
# Name:        Grand Projet IN211
# Purpose:     Tetris
#
# Authors:     KANTANE Pritam Charles and BUSSIERE Edgar
# Class:       2PF2
#
# Created:     08/11/2020
# ------------------------------------------------------------------------------
from src.grid import *
from src.game_mechanics import *

pygame.init()


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.grid_obj = Grid()
        self.game_mechanic = GameMechanics()

    def main(self):
        tetris_song = pygame.mixer.Sound("assets/Original tetris theme.mp3")
        tetris_song.play(50)
        second_grid = {}
        running = True
        change = False
        current_piece = get_piece()
        next_piece = get_piece()
        score = 0

        clock = pygame.time.Clock()
        timer = 0
        speed = 0.35

        while running:
            grid = self.grid_obj.make_grid(second_grid)
            for i in range(0, 4):
                score = self.game_mechanic.check_row_and_score(grid, second_grid, score)
            self.game_mechanic.game_speed_up(score)
            running = self.game_mechanic.game_over(self.screen, grid)

            clock.tick() # on récupère un tick : commence le chronomètre
            timer += clock.get_rawtime() # on ajoute temps chronométré
            if timer / 1000 > speed:  # si le temps est supérieur à la vitesse
                timer = 0  # le temps est réinitialisé
                current_piece.y += 1  # la pièce descend d'un rang
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
            self.grid_obj.draw_little_grid(screen, next_piece)
            text_font = pygame.font.SysFont('segoe script', 25)
            text_font2 = pygame.font.SysFont('segoe script', 15)
            label1 = pygame.image.load('assets/tetris_logo_mini.png')
            label2 = text_font.render("Score :", True, (255, 255, 255))
            label3 = text_font.render(str(score), True, (255, 255, 0))
            label5 = text_font2.render('By Pritam and Edgar', True, (255, 255, 255))
            label6 = pygame.image.load('assets/ooo.png')
            screen.blit(label1, [screen_w * 1.72 / 3, 24])
            screen.blit(label2, [screen_w * 1.75 / 3, 550])
            screen.blit(label3, [screen_w * 2.3 / 3, 550])
            screen.blit(label5, [screen_w * 1.70 / 3, 675])
            screen.blit(label6, [screen_w * 1.80 / 3, 275])

            pygame.display.flip()  # Actualise la fenêtre


screen = pygame.display.set_mode((screen_w, screen_h))
game = Game(screen)
game.main()
pygame.quit()
