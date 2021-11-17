import pygame.sprite
from antclass import Ant


class AntBurrow(pygame.sprite.Sprite):
    """
    stores food and spawns ants
    """

    def __init__(self, pos, game, model):
        """
        :param pos: [x,y] pixel position
        """
        pygame.sprite.Sprite.__init__(self, model.burrowlist)
        self.x = pos[0]
        self.y = pos[1]
        self.size = 7  # length of side in pixels
        self.model = model
        self.game = game
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

        self.spawn_ant()  # start with one ant

    def spawn_ant(self):
        """
        returns an instance of the ant class
        """
        return Ant([self.x, self.y], self.model, self.game)
