import pygame
from pygame import RESIZABLE


class Controller:
    """
    handles user input
    """

    def check_input(self, window):
        """
        takes in the game main class as window
        call to check input every tick
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                window.done = True
            elif event.type == pygame.KEYDOWN:  # If user pressed a key
                if event.key == pygame.K_ESCAPE:  # escape key is an escape
                    window.done = True
            elif event.type == pygame.VIDEORESIZE:
                window.view.screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)
                window.view.width = event.w
                window.view.height = event.h
                window.model.pheromones.resize(event.w, event.h)
            elif event.type == pygame.MOUSEBUTTONDOWN:  # when mouse button is clicked
                if pygame.mouse.get_pressed()[0]:  # left mouse button click
                    pos = pygame.mouse.get_pos()
                    clb = [b for b in window.model.burrowlist if b.rect.collidepoint(pos)]
                    for b in clb:
                        b.spawn_ant()
