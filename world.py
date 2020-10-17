class World:
    def __init__(self, size):
        self.size = size
        self.world = self._createWorld()

    def _createWorld(self):
        return [[[0 for i in range(self.size[2])] for j in range(self.size[1])] for h in range(self.size[0])]

    def addCube(self, pos, size, type):
        for i in range(size[0]):
            for j in range(size[1]):
                for h in range(size[2]):
                    if 0 <= pos[0] + i < self.size[0] and 0 <= pos[1] + j < self.size[1] and 0 <= pos[2] + h < self.size[2]:
                        self.world[pos[0]+i][pos[1]+j][pos[2]+h] = type
    def removeCube(self, pos, size):
        for i in range(size[0]):
            for j in range(size[1]):
                for h in range(size[2]):
                    if 0 <= pos[0] + i < self.size[0] and 0 <= pos[1] + j < self.size[1] and 0 <= pos[2] + h < self.size[2]:
                        self.world[pos[0]+i][pos[1]+j][pos[2]+h] = 0

    def getMap(self):
        return self.world

    def getSize(self):
        return self.size

    def printMap(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                for h in range(self.size[2]):
                    print(self.world[i][j][h], end=" ")
                print("\n", end="")
            print("\n\n\n")