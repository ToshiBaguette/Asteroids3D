import pygame, Engine, player, world, Asteroid
from pygame.locals import *


def drawScreen(screen, selection, player, world):
    screen.fill((0, 0, 0))
    view = player.view(world)
    for i in range(120):
        for j in range(120):
            if view[i][j] != (0, 0, 0):
                pygame.draw.rect(screen, view[i][j], (i*5, j*5, 5, 5))

    # Affichage LOGO
    fontLogo = pygame.font.SysFont("Impact", 45)
    logo = fontLogo.render("A S T E R O I D S  3 D", False, (255, 255, 255))
    screen.blit(logo, (142, 10))

    # Affiche menus
    fontObj = pygame.font.SysFont("Comic Sans MS", 24)
    color = (255, 255, 255)
    if selection == 0:
        color = (245, 209, 7)
    playTxt = fontObj.render("JOUER", False, color)
    color = (255, 255, 255)
    if selection == 1:
        color = (245, 209, 7)
    quitTxt = fontObj.render("QUITTER", False, color)
    screen.blit(playTxt, (30, 150))
    screen.blit(quitTxt, (30, 180))

def Title(screen):
    continuer = True
    w = world.World((4, 4, 8))
    p = player.Player([0, -1, 0], w)
    asteroids = [Asteroid.Asteroid(w) for i in range(7)]
    selection = 0
    while continuer:
        for e in pygame.event.get():
            if e.type == QUIT:
                return ["Quit"]
            elif e.type == KEYDOWN:
                if e.key == K_UP and selection == 1:
                    selection = 0
                elif e.key == K_DOWN and selection == 0:
                    selection = 1
                elif e.key == K_RETURN:
                    if selection == 0:
                        return ["GameScreen"]
                    else:
                        return ["Quit"]

        for a in asteroids:
            a.update(w)
            if a.getZ() < 0:
                asteroids.remove(a)
                asteroids.append(Asteroid.Asteroid(w))
        drawScreen(screen, selection, p, w)
        pygame.display.update()