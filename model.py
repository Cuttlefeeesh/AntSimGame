import antburrow
import antlist
import burrowlist
from pheromonearray import PheromoneArray


class Model:
    """
    Stores the game state
    """

    def __init__(self, game):
        self.antlist = antlist.AntList()
        self.burrowlist = burrowlist.BurrowList()
        self.pheromones = PheromoneArray(game.view.width, game.view.height)

        # start with one nest
        antburrow.AntBurrow([100, 100], game, self)

    def update(self):
        for ant in self.antlist:
            ant.update()
        self.pheromones.decay()
