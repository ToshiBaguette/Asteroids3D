import pygame, player, world
from pygame.locals import *


# def start():
#     pygame.init()
#     pygame.display.set_caption("3DEngine")

def drawScreen(screen, player, world):
    screen.fill((0, 0, 0))
    # Impression rectangle aire de jeu
    pygame.draw.rect(screen, (6, 80, 207), (50, 50, 500, 450), 1)

    # Affichage score
    fontObj = pygame.font.SysFont("Comic Sans MS", 24)
    scoreTxt = fontObj.render("Score: " + str(player.getScore()), False, (255, 255, 255))
    screen.blit(scoreTxt, (10, 10))

    # Affichage Couleurs
    pygame.draw.rect(screen, (207, 197, 6), (30, 510, 30, 30))  # Joueur
    screen.blit(fontObj.render("Joueur", False, (255, 255, 255)), (65, 512))
    pygame.draw.rect(screen, (237, 91, 24), (30, 550, 30, 30))  # Asteroid
    screen.blit(fontObj.render("Astéroids", False, (255, 255, 255)), (65, 552))

    view = player.view(world)
    for i in range(120):
        for j in range(120):
            if view[i][j] != (0, 0, 0):
                pygame.draw.rect(screen, view[i][j], (i*5, j*5, 5, 5))

# def engine():
#     p = player.Player()
#     w = world.World((5, 100, 100))
#     w.addCube((0, 7, 8), (4, 2, 1), 4)
#     screen = pygame.display.set_mode((600, 600))
#     pygame.mouse.set_visible(0)
#     pygame.mouse.set_pos(300, 300)
#     continuer = True
#     while continuer:
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 continuer = False
#             if event.type == KEYDOWN:
#                 if event.key == K_UP:
#                     p.move((0, 0, 1), w)
#                 elif event.key == K_DOWN:
#                     p.move((0, 0, -1), w)
#                 elif event.key == K_LEFT:
#                     p.move((0, 1, 0), w)
#                 elif event.key == K_RIGHT:
#                     p.move((0, -1, 0), w)
#         drawScreen(screen, p, w)
#         pygame.display.update()
# start()
# engine()
