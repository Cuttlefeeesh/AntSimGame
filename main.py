import pygame
from pygame.locals import RESIZABLE
import AntClass as Ant


class AntGame:
    """
    Contains the game
    """

    def __init__(self):
        pygame.init()
        self.model = Model(self)
        self.view = View(self)
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


class Model:
    """
    Stores the game state
    """

    def __init__(self, game):
        self.antlist = Ant.AntList()
        self.burrowlist = Ant.BurrowList()

        # start with one nest
        Ant.AntBurrow([100, 100], game, self)

    def update(self):
        for ant in self.antlist:
            ant.update()


class View:
    """
    Draws everything to the pygame window
    """

    def __init__(self, game, width=500, height=500):
        self.width = width  # sets width of screen (as a variable so we can use it later)
        self.height = height
        size = (self.width, self.height)
        self.screen = pygame.display.set_mode(size, RESIZABLE)  # create a pygame screen
        self.game = game

        # initialize colors
        self.bkgcolor = (200, 200, 200)  # background color
        self.antcolor = (10, 10, 10)  # ant color
        self.burrowcolor = (77, 44, 12)  # burrow color

    def update(self):
        self.draw_background()
        self.draw_ants()
        self.draw_burrows()
        pygame.display.flip()  # draw everything that's been put on the screen

    def draw_background(self):
        self.screen.fill(self.bkgcolor)

    def draw_ants(self):
        ant_array = pygame.PixelArray(self.screen)
        for ant in self.game.model.antlist:
            ant_array[ant.pos[0]:min(ant.pos[0] + ant.size, self.width), ant.pos[1]:min(ant.pos[1] + ant.size, self.height)] = self.antcolor
        ant_array.close()  # have to close or the screen surface is locked

    def draw_burrows(self):
        burrow_array = pygame.PixelArray(self.screen)
        for burrow in self.game.model.burrowlist:
            burrow_array[burrow.x:burrow.x + burrow.size, burrow.y:burrow.y + burrow.size] = self.burrowcolor
        burrow_array.close()


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
            elif event.type == pygame.locals.VIDEORESIZE:
                window.view.screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)
                window.view.width = event.w
                window.view.height = event.h



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MainWindow = AntGame()
    MainWindow.main_loop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
