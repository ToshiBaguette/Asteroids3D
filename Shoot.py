class Shoot:
    def __init__(self, pos, world):
        self.pos = pos[:]
        self.size = (1, 1, 1)
        world.addCube(self.pos, self.size, 6)

    def getPos(self):
        return self.pos

    def getY(self):
        return self.pos[0]

    def getX(self):
        return self.pos[1]

    def getZ(self):
        return self.pos[2]

    def delete(self, world):
        world.removeCube(self.pos, self.size)

    def update(self, world):
        world.removeCube(self.pos, self.size)
        self.pos[2] += 1
        world.addCube(self.pos, self.size, 6)
