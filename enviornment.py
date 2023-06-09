import pygame
from assets import (
    sprite,
    window,
    camera,
)

class tile:
    def __init__(self,file):
        self.sprite = sprite(file,w=50,h=50).sprite
    def render(self, x, y):
        window.blit(self.sprite,(x - camera.x, y - camera.y))

road = tile("road.gif")
sidewalk = tile("sidewalk tiles.gif")

location = None

class tokyo:
    loc_map = [
        [sidewalk,road,sidewalk],
        [sidewalk,road,sidewalk],
        [road,road,sidewalk],
    ]
    def render(loc_map):
        x = 0
        y = 0
        for i in loc_map:
            for o in loc_map[loc_map.index(i)]:
                o.render(x,y)
                x += 50
            x = 0
            y += 50