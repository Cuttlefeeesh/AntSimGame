import pygame.sprite
import random
import numpy as np


class Ant(pygame.sprite.Sprite):
    """
    a little bug that brings home the bacon
    """

    def __init__(self, pos, model):
        """
        :param pos: [x, y] pixel position
        """
        pygame.sprite.Sprite.__init__(self, model)  # adds to antlist
        self.pos = np.array(pos)  # [x, y] used for graphing
        self.xpos = self.pos  # [x,y] used for smooth motion, float
        self.size = 2
        self.model = model
        self.speed = 2  # pixels moved per tick
        self.velocity = np.array([0, 0])  # [x,y]

    def wander(self):
        """
        searching for food. random walk.
        """
        velchange = np.add(np.random.rand(2), [-0.5, -0.5]) # a random vector with legs between -0.5 and 0.5
        self.velocity = np.add(self.velocity, velchange) # add to velocity
        speed = np.linalg.norm(self.velocity) # magnitude of the velocity
        if speed > self.speed:
            self.velocity = self.velocity * (self.speed/speed)
        # if velocity has exceeded top speed, cap it at top speed

    def move(self):
        """
        adds velocity to position
        """
        self.xpos = np.add(self.xpos , self.velocity)
        # self.xact = self.xact + self.velocity[0]
        # self.yact = self.yact + self.velocity[1]
        for i in range(len(self.xpos)):
            self.pos[i] = int(round(self.xpos[i]))
        # self.x = int(round(self.xact))
        # self.y = int(round(self.yact))

    def update(self):
        """
        state machine to determine behavior
        updates position of ant
        """
        self.wander()
        self.move()


class AntBurrow(pygame.sprite.Sprite):
    """
    stores food and spawns ants
    """

    def __init__(self, pos, model):
        """
        :param pos: [x,y] pixel position
        """
        pygame.sprite.Sprite.__init__(self, model.burrowlist)
        self.x = pos[0]
        self.y = pos[1]
        self.size = 7  # length of side in pixels
        self.model = model

        self.spawn_ant()  # start with one ant

    def spawn_ant(self):
        """
        returns an instance of the ant class
        """
        return Ant([self.x, self.y], self.model.antlist)


class AntList(pygame.sprite.Group):
    """
    list of all ants in the game
    .add adds a sprite to group
    .remove removes a sprite from group
    .update runs update method of every sprite in group
    .draw blits the image of every sprite in group
    """


class BurrowList(pygame.sprite.Group):
    """
    list of all burrows in game
    """
