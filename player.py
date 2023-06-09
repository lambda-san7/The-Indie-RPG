import pygame
from assets import (
    sprite,
    window,
    camera,
)

class player:
    class sprites:
        def __init__(self, size):
            self.foward_idle = sprite("foward_idle.gif",w=size,h=size).sprite
            self.left_idle = sprite("left_idle.gif",w=size,h=size).sprite
            self.back_idle = sprite("backward_idle.gif",w=size,h=size).sprite
            self.right_idle = sprite("right_idle.gif",w=size,h=size).sprite
    def __init__(self):
        self.sprites = self.sprites(50)
        self.x = 50
        self.y = 50
        self.sprite = self.sprites.foward_idle
        self.spd = 5
    def render(self):
        window.blit(self.sprite,(self.x - camera.x, self.y - camera.y))
    def controller(self):
        if pygame.key.get_pressed()[pygame.K_w]:
            self.sprite = self.sprites.back_idle
            self.y -= self.spd
        if pygame.key.get_pressed()[pygame.K_a]:
            self.sprite = self.sprites.left_idle
            self.x -= self.spd
        if pygame.key.get_pressed()[pygame.K_s]:
            self.sprite = self.sprites.foward_idle
            self.y += self.spd
        if pygame.key.get_pressed()[pygame.K_d]:
            self.sprite = self.sprites.right_idle
            self.x += self.spd
    
thePlayer = player()