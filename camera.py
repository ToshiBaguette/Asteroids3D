import rayPoint

"""
1 = murs (noir)
2 = plafond (noir)
3 = sol (noir)
4 = objet (marron)
5 = joueur (jaune)
6 = tir (blanc)
"""

class Camera:
    def __init__(self, pos):
        self.pos = pos

    def _view(self, world):
        view = [[(0, 0, 0) for i in range(120)] for j in range(120)]
        for i in range(120):
            for j in range(120):
                vector = ((60 - i)/59, (j - 60)/59, 0.25)
                rp = rayPoint.RayPoint(self.pos, vector)
                object = 0
                while object == 0:
                    object = rp.update(world)
                if 1 <= object <= 3:
                    view[j][i] = (0, 0, 0)
                elif object == 4:
                    view[j][i] = (237, 91, 24)
                elif object == 5:
                    view[j][i] = (207, 197, 6)
                elif object == 6:
                    view[j][i] = (255, 255, 255)
        return view

    def setPos(self, pos):
        self.pos = pos[:]
    def setX(self, x):
        self.pos[1] = x
    def setZ(self, z):
        self.pos[2] = z
    def setY(self, y):
        self.pos[0] = y
