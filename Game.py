import pygame, random, Engine, player, world, Asteroid
from pygame.locals import *

def Game(screen):
    continuer = True
    w = world.World((5, 6, 10))
    p = player.Player([0, 0, 1], w)
    asteroids = [Asteroid.Asteroid(w)]
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                return "Quit"
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    p.move((1, 0, 0), w)
                elif event.key == K_DOWN:
                    p.move((-1, 0, 0), w)
                elif event.key == K_LEFT:
                    p.move((0, -1, 0), w)
                elif event.key == K_RIGHT:
                    p.move((0, 1, 0), w)
                elif event.key == K_SPACE:
                    p.shoot(w)
        for a in asteroids:
            a.update(w)
            if a.getZ() < 0:
                asteroids.remove(a)
                asteroids.append(Asteroid.Asteroid(w))
                if random.randint(0, 10) == 4:
                    asteroids.append(Asteroid.Asteroid(w))
        continuer = not p.update(w, asteroids)
        Engine.drawScreen(screen, p, w)
        pygame.display.update()
        pygame.time.wait(20)
    return ["EndScreen", p.getScore()]
