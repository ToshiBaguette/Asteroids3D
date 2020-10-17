import camera, Shoot, Asteroid

class Player:
    def __init__(self, pos, world):
        self.pos = pos
        self.score = 0
        self.camera = camera.Camera([2, 3, 0])
        self.shoots = []
        world.addCube(self.pos, (1, 1, 1), 5)

    def view(self, world):
        return self.camera._view(world)

    def move(self, direction, world):
        if 0 <= self.pos[0]+direction[0] < world.getSize()[0] and 0 <= self.pos[1]+direction[1] < world.getSize()[1] and 0 <= self.pos[2]+direction[2] < world.getSize()[2]:
            world.removeCube(self.pos, (1, 1, 1))
            self.pos[0] += direction[0]
            self.pos[1] += direction[1]
            self.pos[2] += direction[2]
            world.addCube(self.pos, (1, 1, 1), 5)

    def shoot(self, world):
        self.shoots.append(Shoot.Shoot(self.pos[:], world))

    def update(self, world, asteroids):
        self.incScore(1)
        for s in self.shoots:
            s.update(world)
            for a in asteroids:
                if s.getPos() == a.getPos():
                    self.incScore(50)
                    asteroids.remove(a)
                    asteroids.append(Asteroid.Asteroid(world))
                    s.delete(world)
                    self.shoots.remove(s)
                    break
            if s.getZ() >= world.getSize()[2]:
                self.shoots.remove(s)
        for a in asteroids:
            if a.getPos() == self.getPos():
                return True
        return False

    def getPos(self):
        return self.pos

    def getY(self):
        return self.pos[0]

    def getX(self):
        return self.pos[1]

    def getZ(self):
        return self.pos[2]

    def incScore(self, inc):
        self.score += inc

    def getScore(self):
        return self.score