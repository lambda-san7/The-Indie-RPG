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
    def __init__(self,file,size=(),collidable=False):
        self.sprite = sprite(file,w=size[0],h=size[1]).sprite
        self.w = size[0]
        self.h = size[1]
        self.collidable = collidable
    def render(self, x, y):
        window.blit(self.sprite,(x - camera.x, y - camera.y))

class none_holder:
    w = 0
    h = 0
    def render(x,y):
        pass

tiles = [
    tile("road.gif"),
    tile("sidewalk tiles.gif"),
    tile("crosswalk_horizontal.gif"),
    tile("crosswalk_vertical.gif"),
    tile("grass.gif"),
    tile("concrete.gif"),
]

props = [
    none_holder,
    prop("vending machine.gif",(52,80),collidable=True),
    prop("vending machine 2.gif",(52,80),collidable=True),
    prop("pole_1.gif",(100,198)),
    prop("pole_2.gif",(100,198)),
    prop("wire contector.gif",(100,198)),
    prop("convenience_store.gif",(200,198),collidable=True),
    prop("street_light.gif",(100,198)),
    prop("car_1.gif",(200,100),collidable=True),
    prop("car_2.gif",(200,100),collidable=True),
    prop("car_3.gif",(200,100),collidable=True),
]

location = None

class tokyo:
    loc_map = [
        [5,5,1,0,0,1,5,5,4,5,5,4,5,5,4,5,5,4,5,5,1,0,0,1,5,5,4,5,5,4,5,5],
        [5,5,1,0,0,1,5,5,4,5,5,4,5,5,4,5,5,4,5,5,1,0,0,1,5,5,4,5,5,4,5,5],
        [1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1],
        [0,0,3,0,0,3,0,0,0,0,0,0,0,3,0,0,3,0,0,0,3,0,0,3,0,3,0,0,3,0,0,0],
        [0,0,3,0,0,3,0,0,0,0,0,0,0,3,0,0,3,0,0,0,3,0,0,3,0,3,0,0,3,0,0,0],
        [1,1,1,2,2,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1],
    ]
    prop_map = [
        [0,0,0,0,0,0,0,0,0,0,2,1],
        [0,0,0,0,0,0,6,0,0,0],
        [5,3,5,5,5,4],
        [8,0,0,0,0],
        [0,0,0,0,0,0,0,10],
        [0,7,0,0,0],
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
                props[o].render(x,(y - props[o].h) + 50)
                x += 50
            x = 0
            y += 50
    def collision(prop_map):
        collisions = []
        for i, sublist in enumerate(prop_map):
            for j, o in enumerate(sublist):
                if o != 0:
                    if props[o].collidable:
                        x = j * 50 
                        y = ((i * 50) - props[o].h) + 50
                        w = props[o].w
                        h = props[o].h
                        collisions.append((x, y, w, h))
        return collisions