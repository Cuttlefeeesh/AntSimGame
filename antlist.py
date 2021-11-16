import pygame.sprite


class AntList(pygame.sprite.Group):
    """
    list of all ants in the game
    .add adds a sprite to group
    .remove removes a sprite from group
    .update runs update method of every sprite in group
    .draw blits the image of every sprite in group
    """