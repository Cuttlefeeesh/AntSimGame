import pygame.sprite
import numpy as np


class Ant(pygame.sprite.Sprite):
    """
    a little bug that brings home the bacon
    """

    def __init__(self, pos, model, game):
        """
        :param pos: [x, y] pixel position
        """
        pygame.sprite.Sprite.__init__(self, model.antlist)  # adds to antlist
        self.pos = np.array(pos)  # [x, y] used for graphing
        self.xpos = self.pos  # [x,y] used for smooth motion, float
        self.size = 2
        self.model = model
        self.game = game
        self.speed = 2  # pixels moved per tick
        self.velocity = np.array([0, 0])  # [x,y]

    def wander(self, game):
        """
        searching for food. random walk.
        """
        velchange = np.add(np.random.rand(2), [-0.5, -0.5])  # a random vector with legs between -0.5 and 0.5
        self.velocity = np.add(self.velocity, velchange)  # add to velocity
        speed = np.linalg.norm(self.velocity)  # magnitude of the velocity
        if speed > self.speed:
            self.velocity = self.velocity * (
                        self.speed / speed)  # if velocity has exceeded top speed, cap it at top speed

        # bounce off the walls
        if self.xpos[0] + self.velocity[0] >= game.view.width or self.xpos[0] + self.velocity[0] <= 0:
            self.velocity[0] = -1 * self.velocity[0]
        if self.xpos[1] + self.velocity[1] >= game.view.height or self.xpos[1] + self.velocity[1] <= 0:
            self.velocity[1] = -1 * self.velocity[1]

    def move(self):
        """
        adds velocity to position
        """
        self.xpos = np.add(self.xpos, self.velocity)
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
        hungry = True

        if hungry:
            self.game.model.pheromones.add((self.pos),(0,0,255))
            self.wander(self.game)


        self.move()
