import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos_x: int, pos_y: int, surface: pygame.Surface) -> None:
        super().__init__()
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)

    def update(self) -> None:
        pass

    def set_position(self, pos_x: int, pos_y: int):
        self.rect.topleft = (pos_x, pos_y)
