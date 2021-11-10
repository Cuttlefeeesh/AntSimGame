import PIL
from PIL import Image
import numpy as np
import pygame
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
        self.array = np.zeros((width, height,3))
        self.dissipation_factor = 7
        self.decay_factor = 0.1

    def image(self):
        """
        :return: an image of the pheromone density
        """
        return PIL.Image.fromarray(self.array, "RGB")

    def draw(self, pixels, color):
        """
        updates array
        :param pixels: list of (x,y) pixel positions
        :param color: (R,G,B) color on a scale from 0 to 255
        :return:updated array
        """
        pixel = None
        for pixel in pixels:
            r = color[0]
            g = color[1]
            b = color[2]
            x = pixel[0]
            y=pixel[1]
            self.array[x,y,:] = [r, g, b]
        return self.array

    def decay(self):
        blurred = scipy.ndimage.filters.gaussian_filter(self.array, sigma=self.dissipation_factor)
        subtractor = self.decay_factor*np.ones(np.shape(self.array))
        self.array = blurred - subtractor

if __name__ == '__main__':
    done: bool = False
    screen = pygame.display.set_mode((500,500))
    ph = AntPheromone("test", 500, 500)
    ph.draw([(10,10), (10,11), (11,10),(11,11)],[255,255,255])

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.surfarray.blit_array(screen, ph.array)
        #screen.blit(array.image(),(0,0))
        pygame.display.flip()
