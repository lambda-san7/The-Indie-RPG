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
    def __init__(self,name,file,size=(),collidable=False):
        self.sprite = sprite(file,w=size[0],h=size[1]).sprite
        self.w = size[0]
        self.h = size[1]
        self.collidable = collidable
        self.name = name
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
    prop("vending machine","vending machine.gif",(52,80),collidable=True),  
    prop("vending machine","vending machine 2.gif",(52,80),collidable=True), 
    prop("power line","pole_1.gif",(100,198)),
    prop("power line","pole_2.gif",(100,198)),
    prop("wires","wire contector.gif",(100,198)),
    prop("711","convenience_store.gif",(200,198),collidable=True),
    prop("light","street_light.gif",(100,198)),
    prop("car","car_1.gif",(174,90),collidable=True),
    prop("car","car_2.gif",(200,100),collidable=True),
    prop("car","car_3.gif",(200,100),collidable=True),
    prop("stop","stop_sign.gif",(52,80)),
    prop("house","house_1.gif",(200,396),collidable=True),
    prop("house","house_2.gif",(200,396),collidable=True),
    prop("bush","bush.gif",(52,44),collidable=True),
    prop("bush","bush2.gif",(52,44),collidable=True),
]
#1 = vending machine 
#2 = vending machine
#3 = pole
#
#
#
#
#
#


location = None

class tokyo:
    loc_map = [
        [5, 5, 1, 0, 0, 1, 5, 5, 5, 5, 5, 1, 0, 0, 1, 5, 5, 5, 5, 5, ],
        [5, 5, 1, 0, 0, 1, 5, 5, 5, 5, 5, 1, 0, 0, 1, 5, 5, 5, 5, 5, ],
        [1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, ],
        [0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, ],
        [0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, ], 
        [1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, ], 
        [5, 5, 1, 0, 0, 1, 4, 4, 5, 4, 4, 1, 0, 0, 1, 5, 5, 5, 5, 5, ], 
        [5, 5, 1, 0, 0, 1, 4, 4, 5, 4, 4, 1, 0, 0, 1, 5, 5, 5, 5, 5, ], 
        [5, 5, 1, 0, 0, 1, 4, 4, 5, 4, 4, 1, 2, 2, 1, 1, 1, 1, 1, 1, ], 
        [5, 5, 1, 0, 0, 1, 4, 4, 5, 5, 5, 1, 0, 0, 3, 0, 0, 0, 3, 0, ], 
        [5, 5, 1, 0, 0, 1, 4, 4, 5, 4, 4, 1, 0, 0, 3, 0, 0, 0, 3, 0, ], 
        [5, 5, 1, 0, 0, 1, 5, 5, 5, 4, 4, 1, 1, 1, 1, 1, 2, 2, 1, 1, ], 
        [5, 5, 1, 0, 0, 1, 4, 4, 5, 4, 4, 4, 5, 4, 4, 1, 0, 0, 1, 5, ], 
        [5, 5, 1, 0, 0, 1, 4, 4, 5, 4, 4, 4, 5, 4, 4, 1, 0, 0, 1, 5, ], 
        [1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, ], 
        [0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, ], 
        [0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, ], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    ]
    prop_map = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0,12, 0, 0, 0, 0, ],
        [0, 0,11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], 
        [0, 0, 0, 0, 0, 0, 0,14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    ]
    def render(loc_map):
        x = 0
        y = 0
        for i in loc_map:
            for o in loc_map[loc_map.index(i)]:
                tiles[o].render(x,y)
                x += 50
            x = 0
            y += 50
            
    def renderProps(prop_map):
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
                        collisions.append((x, y, w, h, props[o].name))
        return collisions
    
location = tokyo

def placeBlock(type,x,y):
    if type == "road":
        tokyo.loc_map[y][x] = 0
    if type == "side":
        tokyo.loc_map[y][x] = 1
    if type == "cross hori":
        tokyo.loc_map[y][x] = 2
    if type == "cross vert":
        tokyo.loc_map[y][x] = 3
    if type == "grass":
        tokyo.loc_map[y][x] = 4
    if type == "conc":
        tokyo.loc_map[y][x] = 5