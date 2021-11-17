import pygame

from controller import Controller
from model import Model
from view import View


class AntGame:
    """
    Contains the game
    """

    def __init__(self):
        pygame.init()
        self.view = View(self) # needs to be initialized before the model
        self.model = Model(self)
        self.controller = Controller()
        self.clock = pygame.time.Clock()
        self.done = False

    def main_loop(self):
        while not self.done:
            self.controller.check_input(self)
            self.model.update()
            self.view.update()
            self.clock.tick(30)
        pygame.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MainWindow = AntGame()
    MainWindow.main_loop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
