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