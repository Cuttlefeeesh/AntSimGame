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
        self.dissipation_factor = 0.4
        self.decay_factor = 0.999

    def draw(self, pixels: list, color: tuple):
        """
        updates array
        :param pixels: list of (x,y) pixel positions
        :param color: (R,G,B) color on a scale from 0 to 255
        :return: updated array
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
        subtractor = self.decay_factor*blurred#np.ones(np.shape(self.array))
        self.array =  subtractor

if __name__ == '__main__':
    done: bool = False
    screen = pygame.display.set_mode((500,500))
    ph = AntPheromone("test", 500, 500)
    ph.draw([(10,10), (10,11), (11,10),(11,11)],(255,255,255))
    i = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        ph.decay()
        ph.draw([(np.random.randint(0,500), np.random.randint(0,500))],(np.random.randint(0,256),np.random.randint(0,256),np.random.randint(0,256)))
        if i < 500:
            ph.draw([(i, 15)], (255,255,255))
        i = i+1
        pygame.surfarray.blit_array(screen, ph.array)
        pygame.display.flip()
