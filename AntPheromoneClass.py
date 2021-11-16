import numpy as np
import pygame
from pygame.locals import RESIZABLE
import scipy.ndimage.filters


class Pheromone:
    """
    General methods for the pheromone classes. Applies to 2D arrays.
    """

    def __init__(self, width, height, dissipation=0.4, decay=0.999):
        """
        #:param width: pixel width of screen
        #:param height: pixel height of screen
        #:param dissipation: diffusion rate
        #:param decay: fraction/1 of the value remaining at each time step
        """
        self.width = width
        self.height = height
        self.array = np.zeros((width, height))
        self.dissipation_factor = dissipation
        self.decay_factor = decay

    def draw(self, pixels: list, color: int):
        """
        updates array
        :param pixels: list of (x,y) pixel positions
        :param color: tuple of colors (R,G,B) or (int) color on a scale from 0 to 255
        :return: updated array
        """

        """
        if len(color)>1:
            colorlist = []
            for i in color:
                colorlist.append(i)
        else:
            colorlist = color
        
        if not len(colorlist) == self.depth:
            raise ValueError('Wrong number of colors')
        """
        for pixel in pixels:
            x = pixel[0]
            y = pixel[1]
            if x < self.width and y < self.height:
                self.array[x, y] = color
        return self.array

    def decay(self):
        blurred = scipy.ndimage.filters.gaussian_filter(self.array, sigma=self.dissipation_factor)
        subtracted = self.decay_factor * blurred  # np.ones(np.shape(self.array))
        self.array = subtracted

    def resize(self, w, h):
        wo = self.width
        ho = self.height
        self.width = w
        self.height = h

        if w < wo or h < ho:
            self.array = self.array[0:w, 0:h]
        if wo < w:
            self.array = np.pad(self.array, ((0, w - wo), (0, 0)))
        if ho < h:
            self.array = np.pad(self.array, ((0, 0), (0, h - ho)))

        return self.array


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


if __name__ == '__main__':
    done: bool = False
    screen = pygame.display.set_mode((500, 500), RESIZABLE)
    ph = PheromoneArray(500, 500)
    ph.draw([(10, 10), (10, 11), (11, 10), (11, 11)], (255, 255, 255))
    i = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.locals.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)
                ph.resize(event.w, event.h)

        ph.decay()
        ph.draw([(np.random.randint(0, 500), np.random.randint(0, 500))],
                (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256)))
        if i < ph.width:
            ph.draw([(i, 15)], (255, 0, 0))
            ph.draw([(i, 16)], (0, 255, 0))
            ph.draw([(i, 17)], (0, 0, 255))
        i = i + 1
        pygame.surfarray.blit_array(screen, ph.array)
        pygame.display.flip()
