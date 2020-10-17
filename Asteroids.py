import pygame, Game, End, Title


def init():
    pygame.init()
    pygame.display.set_caption('Asteroids 3D')

def asteroids():
    continuer = True
    gameState = ["EndScreen", 50]
    screen = pygame.display.set_mode((600, 600))
    while continuer:
        if gameState[0] == "TitleScreen":
            gameState = Title.Title(screen)
        elif gameState[0] == "GameScreen":
            gameState = Game.Game(screen)
        elif gameState[0] == "EndScreen":
            gameState = End.End(screen, gameState[1])
        elif gameState[0] == "Quit":
            continuer = False

init()
asteroids()
pygame.quit()