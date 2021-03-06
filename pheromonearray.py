import numpy as np
from pheromone import Pheromone


class PheromoneArray(Pheromone):
    """
    An array that contains the concentration of all pheromones and food at every pixel
    """

    def __init__(self, width, height):

        Pheromone.__init__(self, width, height, 3)

        self.red = Pheromone(width, height)
        self.green = Pheromone(width, height, 0, 1)  # Food
        self.blue = Pheromone(width, height)

        self.phlist = [self.red, self.green, self.blue]
        self.refresh()

    def decay(self):
        for ph in self.phlist:
            ph.decay()

    def refresh(self):
        self.array = np.stack([self.red.array, self.green.array, self.blue.array], 2)
        return self.array

    def draw(self, pixels: list, color: tuple):
        i = 0
        for ph in self.phlist:
            ph.draw(pixels, color[i])
            i += 1
        self.refresh()

    def resize(self, w, h):
        for ph in self.phlist:
            ph.resize(w, h)
        self.refresh()

    def drawsquare(self, pos: tuple, size: int, color: tuple):
        """
        :param color: (R,G,B)
        :param pos: (x,y) pixel position
        :param size: width of square (preferably even)
        """
        if size == 1:
            plist = [pos]
        else:
            add = round((size - 1) / 2)  # round down to an even number
            plist = []
            for x in range(pos[0] - add, pos[0] + add):
                for y in range(pos[1] - add, pos[1] + add):
                    plist.append((x, y))
        self.draw(plist, color)

    def add(self, pos: tuple, color: tuple):
        """
        add pheromones to a single pixel location
        :param pos: (x,y)
        :param color: (R,G,B) on 0-255 scale
        """
        now = np.asarray(self.sniff([pos])[0])
        color = np.asarray(color)
        newcolor = []
        for i in range(len(now)):
            newcolor.append(min(255, now[i] + color[i]))
            i += 1
        self.draw([pos], tuple(newcolor))
