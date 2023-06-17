import pygame
from enviornment import tokyo
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

            self.foward_walk_1 = sprite("foward_walk_1.gif",w=size,h=size).sprite
            self.foward_walk_2 = sprite("foward_walk_2.gif",w=size,h=size).sprite

            self.left_walk_1 = sprite("left_walk_1.gif",w=size,h=size).sprite
            self.left_walk_2 = sprite("left_walk_2.gif",w=size,h=size).sprite

            self.back_walk_1 = sprite("backward_walk_1.gif",w=size,h=size).sprite
            self.back_walk_2 = sprite("backward_walk_2.gif",w=size,h=size).sprite

            self.right_walk_1 = sprite("right_walk_1.gif",w=size,h=size).sprite
            self.right_walk_2 = sprite("right_walk_2.gif",w=size,h=size).sprite
    def __init__(self):
        self.sprites = self.sprites(50)
        self.x = 50
        self.y = 50
        self.w = 50
        self.h = 50
        self.sprite = self.sprites.foward_idle
        self.spd = 3
        self.walk_frame = 1
        self.facing = "foward"
    def render(self):
        window.blit(self.sprite,(self.x - camera.x, self.y - camera.y))
    def controller(self):
        if self.facing == "foward":
            self.sprite = self.sprites.foward_idle
        if self.facing == "left":
            self.sprite = self.sprites.left_idle
        if self.facing == "back":
            self.sprite = self.sprites.back_idle
        if self.facing == "right":
            self.sprite = self.sprites.right_idle

        if pygame.key.get_pressed()[pygame.K_LSHIFT]:
            self.spd = 5
        else:
            self.spd = 3
            pass

        if pygame.key.get_pressed()[pygame.K_w]:
            tokyo.collision(tokyo.prop_map)
            if self.y + 40 <= 0:
                return
            for i in tokyo.collision(tokyo.prop_map):
                if self.collision(i,(self.x,self.y - self.spd)):
                    return
            if self.walk_frame == 9:
                self.walk_frame = 1
            if self.walk_frame in range(1,4):
                self.sprite = eval(f"self.sprites.back_walk_1")
            if self.walk_frame in range(5,8):
                self.sprite = eval(f"self.sprites.back_walk_2")
            self.y -= self.spd
            self.facing = "back"
            self.walk_frame += 1
            
        if pygame.key.get_pressed()[pygame.K_a]:
            if self.x <= 0:
                return
            for i in tokyo.collision(tokyo.prop_map):
                if self.collision(i, (self.x - self.spd,self.y)):
                    return
            if self.walk_frame == 9:
                self.walk_frame = 1
            if self.walk_frame in range(1,4):
                self.sprite = eval(f"self.sprites.left_walk_1")
            if self.walk_frame in range(5,8):
                self.sprite = eval(f"self.sprites.left_walk_2")
            self.x -= self.spd
            self.facing = "left"
            self.walk_frame += 1
            
        if pygame.key.get_pressed()[pygame.K_s]:
            if self.y + 50 >= len(tokyo.loc_map) * 50:
                return
            for i in tokyo.collision(tokyo.prop_map):
                if self.collision(i,(self.x, self.y + self.spd)):
                    return
            if self.walk_frame == 9:
                self.walk_frame = 1
            if self.walk_frame in range(1,4):
                self.sprite = eval(f"self.sprites.foward_walk_1")
            if self.walk_frame in range(5,8):
                self.sprite = eval(f"self.sprites.foward_walk_2")
            self.y += self.spd
            self.facing = "foward"
            self.walk_frame += 1
            
        if pygame.key.get_pressed()[pygame.K_d]:
            if self.x + 50 >= len(tokyo.loc_map[0]) * 50:
                return
            for i in tokyo.collision(tokyo.prop_map):
                if self.collision(i,(self.x + self.spd,self.y)):
                    return
            if self.walk_frame == 9:
                self.walk_frame = 1
            if self.walk_frame in range(1,4):
                self.sprite = eval(f"self.sprites.right_walk_1")
            if self.walk_frame in range(5,8):
                self.sprite = eval(f"self.sprites.right_walk_2")
            self.x += self.spd
            self.facing = "right"
            self.walk_frame += 1
        
        if pygame.key.get_pressed()[pygame.K_e]:
            for i in tokyo.collision(tokyo.prop_map):
                if self.collision(i,(self.x,self.y - 50)):
                    print(i[4])
                    if i[4] == "711":
                        print("you want a slushie?")

    def collision(self,obj,player):
        x = obj[0]
        y = obj[1]
        w = obj[2]
        h = obj[3]
        if (player[0] + 10 < x + w and
            player[0] + 40 > x and
            player[1] + 40 < y + h and 
            player[1] + 50 > y):
            return True
        return False
                

thePlayer = player()