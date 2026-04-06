from enum import Enum
import pygame
import sokobanbot as sok

game = sok.Sokoban(9, 9, 2, True, True)
game.reset()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                game.play_step([1, 0, 0, 0])  # UP
            elif event.key == pygame.K_s:
                game.play_step([0, 1, 0, 0])  # DOWN
            elif event.key == pygame.K_a:
                game.play_step([0, 0, 1, 0])  # LEFT
            elif event.key == pygame.K_d:
                game.play_step([0, 0, 0, 1])  # RIGHT
            elif event.key == pygame.K_r:
                game.reset()

    game._update_ui()
    clock.tick(60)