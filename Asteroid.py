import random


class Asteroid:
    def __init__(self, world):
        self.pos = self._newPos(world)  # [Y, X, Z]
        self.size = (1, 1, 1)
        world.addCube(self.pos, self.size, 4)

    def _newPos(self, world):
        return [random.randint(0, world.getSize()[0]), random.randint(0, world.getSize()[1]), 10]

    def destroy(self, world):
        world.removeCube(self.pos, self.size)

    def getPos(self):
        return self.pos

    def getY(self):
        return self.pos[0]

    def getX(self):
        return self.pos[1]

    def getZ(self):
        return self.pos[2]

    def update(self, world):
        world.removeCube(self.pos, self.size)
        self.pos[2] -= 1
        world.addCube(self.pos, self.size, 4)
