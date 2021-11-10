import numpy as np
import pygame
from pygame.locals import RESIZABLE
import scipy.ndimage.filters


class AntPheromone:
    """
    An array that contains the concentration of a pheromone at every pixel
    """

    def __init__(self, name, width, height):
        """
        :param name: string name
        #:param game: game class
        """
        self.name = name
        self.width = width
        self.height = height
        self.array = np.zeros((width, height, 3))
        self.dissipation_factor = 0.4
        self.decay_factor = 0.999

    def draw(self, pixels: list, color: tuple):
        """
        updates array
        :param pixels: list of (x,y) pixel positions
        :param color: (R,G,B) color on a scale from 0 to 255
        :return: updated array
        """
        for pixel in pixels:
            r = color[0]
            g = color[1]
            b = color[2]
            x = pixel[0]
            y = pixel[1]
            if x< self.width and y< self.height:
                self.array[x, y, :] = [r, g, b]
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

        if w<wo or h<ho:
            self.array = self.array[0:w, 0:h]
        if wo<w:
            self.array = np.pad(self.array, ((0,w-wo),(0,0),(0,0)))
        if ho<h:
            self.array = np.pad(self.array, ((0, 0), (0, h-ho), (0, 0)))


        return self.array


if __name__ == '__main__':
    done: bool = False
    screen = pygame.display.set_mode((500, 500),RESIZABLE)
    ph = AntPheromone("test", 500, 500)
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
        if i < 500:
            ph.draw([(i, 15)], (255, 255, 255))
        i = i + 1
        pygame.surfarray.blit_array(screen, ph.array)
        pygame.display.flip()
