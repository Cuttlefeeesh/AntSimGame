import numpy as np
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

    def sniff(self, loc: list):
        """
        smell the pheromones at a list of positions
        :param loc: list of positions to sample
        :return: list of pheromone values at each position
        """
        smells = []
        for pos in loc:
            smells.append(self.array[pos[0] - 1, pos[1] - 1, :])
        return smells
