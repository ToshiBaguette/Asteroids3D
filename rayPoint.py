class RayPoint:
    def __init__(self, pos, vector):
        self.pos = pos
        self.vector = vector

    def update(self, world):
        self.pos = [self.pos[0] + self.vector[0], self.pos[1] + self.vector[1], self.pos[2] + self.vector[2]]
        if 0 <= self.pos[0] < world.getSize()[0] and 0 <= self.pos[1] < world.getSize()[1] and 0 <= self.pos[2] < world.getSize()[2]:
            return world.getMap()[int(self.pos[0])][int(self.pos[1])][int(self.pos[2])]
        else:
            if self.pos[0] >= world.getSize()[0]:
                return 2
            elif self.pos[0] < 0:
                return 3
            else:
                return 1
    def printPoint(self):
        print("Y: " + str(self.pos[0]) + " X: " + str(self.pos[1]) + " Z: " + str(self.pos[2]))
