import pygame 
import assets
from assets import (
    dir_path,
    window,
    center,
    text,
    camera
)
from player import thePlayer as player
from enviornment import tokyo

running = True

fps = 60

clock = pygame.time.Clock()

visible = False

########################
# SCENES
########################

scene = None

class hi:
    def handle():
        window.fill((50,50,50))


#    lambda : (
 #       window.fill((50,50,50)),
  #      msg := assets.text(10,"I'm tired of tools only having typed out docs..."),
   #     msg.render(10,10),
    #    hover_button := assets.button("Hover over me!", 32, (255, 255, 255)),
     #   (hover_button := assets.button("So mine is interactive...", 32, (255, 255, 255))) if hover_button.hover() else None
      #  hover_button.render()

scene = None


class game:
    def handle():
        window.fill((50,50,50))
        camera.x, camera.y = player.x - (pygame.display.Info().current_w / 2), player.y - (pygame.display.Info().current_h / 2)
        tokyo.render(tokyo.loc_map,tokyo.prop_map)
        player.render()
        player.controller()

########################
# GAME LOOP
########################

scene = game

while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
    clock.tick(fps)
    scene.handle()
    pygame.display.update()

pygame.quit