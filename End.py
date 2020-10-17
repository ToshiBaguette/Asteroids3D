import pygame, Engine, player, world, Asteroid, os
from pygame.locals import *


def drawScreen(screen, score, bestScore, color, player, world):
    screen.fill((0, 0, 0))
    view = player.view(world)
    for i in range(120):
        for j in range(120):
            if view[i][j] != (0, 0, 0):
                pygame.draw.rect(screen, view[i][j], (i*5, j*5, 5, 5))

    fontLogo = pygame.font.SysFont("Impact", 45)
    logo = fontLogo.render("A S T E R O I D S  3 D", False, (255, 255, 255))
    screen.blit(logo, (142, 10))

    fontObj = pygame.font.SysFont("Comic Sans MS", 24)
    endTxt = fontObj.render("Partie Terminée !", False, (255, 255, 255))
    scoreTxt = fontObj.render("Score Final : " + str(score), False, (255, 255, 255))
    bestTxt = fontObj.render("Record : " + str(bestScore), False, (255, 255, 255))
    screen.blit(endTxt, (200, 170))
    screen.blit(scoreTxt, (200, 200))
    screen.blit(bestTxt, (200, 230))

    fontContinue = pygame.font.SysFont("Comic Sans MS", 20)
    contTxt = fontContinue.render("Appuyez sur n'importe quelle touche", False, (color, color, color))
    screen.blit(contTxt, (140, 280))

def End(screen, score):
    continuer = True
    w = world.World((4, 4, 8))
    p = player.Player([0, -1, 0], w)
    colorContinue = 252
    minus = True
    if not os.path.isfile("score.txt"):
        f = open("score.txt", "w")
        f.close()
    f = open("score.txt", "r")
    bestScore = score
    test = f.readline()
    f.close()
    print("Test : " + test + "TEST")
    if test != "" and score < int(test):
        bestScore = int(test)
    else:
        f = open("score.txt", "w")
        f.write(str(score))
        f.close()
    asteroids = [Asteroid.Asteroid(w) for i in range(7)]
    while continuer:
        for e in pygame.event.get():
            if e.type == QUIT:
                return ["Quit"]
            elif e.type == KEYDOWN:
                return ["TitleScreen"]
        for a in asteroids:
            a.update(w)
            if a.getZ() < 0:
                asteroids.remove(a)
                asteroids.append(Asteroid.Asteroid(w))
        drawScreen(screen, score, bestScore, colorContinue, p, w)
        if colorContinue > 0 and minus:
            colorContinue -= 4
        else:
            minus = False
            colorContinue += 4
            if colorContinue == 252:
                minus = True
        pygame.display.update()
