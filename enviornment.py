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

class prop:
    def __init__(self,file,size=()):
        self.sprite = sprite(file,w=size[0],h=size[1]).sprite
    def render(self, x, y):
        window.blit(self.sprite,(x - camera.x, y - camera.y))

class none_holder:
    def render(x,y):
        pass

tiles = [
    tile("road.gif"),
    tile("sidewalk tiles.gif"),
    tile("crosswalk_horizontal.gif"),
]

props = [
    none_holder,
    prop("vending machine.gif",(100,100)),
]

location = None

class tokyo:
    loc_map = [
        [1,2,2,1,1],
        [1,0,0,1,1],
        [0,0,0,1,1],
        [0,0,0,1,1],
        [1,1,1,1,1],
    ]
    prop_map = [
        [0,0,0,0,1],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ]
    def render(loc_map, prop_map):
        x = 0
        y = 0
        for i in loc_map:
            for o in loc_map[loc_map.index(i)]:
                tiles[o].render(x,y)
                x += 50
            x = 0
            y += 50

        x = 0
        y = 0
        for i in prop_map:
            for o in prop_map[prop_map.index(i)]:
                props[o].render(x,y + 50)
                x += 50
            x = 0
            y += 50