import numpy as np
import pygame
from pygame.locals import RESIZABLE
import pheromonearray

if __name__ == '__main__':
    done: bool = False
    screen = pygame.display.set_mode((500, 500), RESIZABLE)
    ph = pheromonearray.PheromoneArray(500, 500)
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
