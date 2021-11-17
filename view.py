import pygame
from pygame import RESIZABLE


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
        self.antcolor = (250, 250, 250)  # ant color
        self.burrowcolor = (77, 44, 12)  # burrow color

        self.draw_background() # todo remove

    def update(self):
        #self.draw_background()
        self.draw_pheromones(self.game)
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

    def draw_pheromones(self, game):
        array = game.model.pheromones.array
        pygame.surfarray.blit_array(game.view.screen, array)

        """
        #pixel by pixel update: slow and it's hard to convert colors
        array[150:155, 150:155] = (255,0,0)

        ph_list=[]
        for i in range(pheromones.shape[0]):
            for j in range(pheromones.shape[1]):
                ph_list.append(self.screen.unmap_rgb(pheromones[i,j]))
        ph_array = np.asarray(ph_list).reshape((self.width,self.height,4))
        red_array = ph_array[:,:,0]/255 # convert to 0 to 1 scale
        red_array = red_array - 0.1*np.ones(red_array.shape) #subtract a bit

        red_array = red_array*255 # return to 255 scale
        final_array = np.zeros(pheromones.shape)
        for i in range(pheromones.shape[0]):
            for j in range(pheromones.shape[1]):
                final_array[i,j] = self.screen.map_rgb(ph_array[i,j,0], ph_array[i,j,1], red_array[i,j])

        array[0:pheromones.shape[0], 0:pheromones.shape[1]] = final_array
        """

        #array.close()