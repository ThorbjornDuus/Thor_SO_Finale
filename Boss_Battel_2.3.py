"""
Boss Battel
"""

import arcade
import math
import os
import random

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Boss Battel"
tid = 1
t = tid


CHARACTER_SCALING = 0.7
projektil_scaling = 0.5
GRAVITY = 1
Boss_SCALING = 1
PLAYER_MOVEMENT_SPEED = 7
Player_JUMP_SPEED = 15
TILE_SCALING = 0.5
player_position = (300, 400)
start_hastighed = 600
angle = 3
tryk = False

#vi opretter en classe funktion til vores projektiler som holde styr på vores variabler og metoder
class projektil():
    def __init__(self, x, y):
        self.start_hastighed = 10
        self.angle = math.pi * 0.4
        self.start_x = 400
        self.start_y = 300
        self.pos = (x, y)
        self.tryk = False
        self.tid = 0
        self.x = 0
        self.y = 0
#vi kan lave en funktion sem beskriver en retningsvektor der bestemmer projektilets retning og rute
    def update(self, delta_tid):
        #print(self.)
        if self.tryk:
            self.tid += delta_tid
            projektil_x = start_hastighed * math.cos(self.angle) * self.tid + self.x
            projektil_y = start_hastighed * math.sin(self.angle) * self.tid - 1 * 150 * self.tid ** 2 + self.y
            #print(px,py)
            self.pos = (projektil_x, projektil_y)

#vi laver en funktion som tegner vores projektil
    def draw(self):
        x, y = self.pos
        arcade.draw_circle_filled(x, y, 5, arcade.color.RED)


#vi kan lave en class funktion der hedder GameWindow som holder styr på alle de variabler og moetoder vi
#skal bruge til at definere og tegner vores player, boss, projektieler og så vidre
class GameWindow(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.scene = None
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None
        self.projektil_list = None
        self.tryk = False
        self.projektil = None
        arcade.set_background_color(arcade.csscolor.GREY)

#vi kan lave en funktion der tegner projektilet når mussen bliver trykket
    def on_mouse_press(self, x, y, button, modifiers):
        self.projektil = projektil(x, y)
        self.projektil.x = self.player_sprite.center_x
        self.projektil.y = self.player_sprite.center_y

#så kan vi lave en funktion der laver hele vores scene og alle vores sprites
    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        image_source = ":resources:images/animated_characters/robot/robot_fall.png"
        self.scene = arcade.Scene()
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 100

        self.scene.add_sprite("Player", self.player_sprite)
        self.projektil_list = list()
        self.projektil_list.append(projektil(*player_position))

        image_source = ":resources:images/enemies/saw.png"
        self.Boss_sprite = arcade.Sprite(image_source, Boss_SCALING)
        self.Boss_sprite.center_x = 440
        self.Boss_sprite.center_y = 630
        self.scene.add_sprite("Boss", self.Boss_sprite)
        self.Boss_list = arcade.SpriteList()

        #for i in range(100, 300, 300):
            #wall=arcade.sprite(":resources:images/tiles/stoneHalf.png", TILE_SCALING)
            #self.scene.add_sprite("Walls", wall)


        for x in range(0, 900, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 35
            self.scene.add_sprite("Walls", wall)
            self.wall_list.append(wall)

            self.physics_engine = arcade.PhysicsEnginePlatformer(
                self.player_sprite, self.wall_list, GRAVITY)
        pass

# vi kan lave en masse if/elif statemetns som styre voeres bevægelse og affyrigs funktion
    def on_key_press(self, key, modifiers):
            if key == arcade.key.SPACE:
                self.projektil.tryk = True
            elif key == arcade.key.UP:
             self.player_sprite.change_y = Player_JUMP_SPEED
            elif key == arcade.key.LEFT:
             self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
             self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

#endu en update funktion til at registere vores projektil og hvor det befinder sig, samt en physics engine der holder stør på vores charather
    def on_update(self, delta_time):
        self.physics_engine.update()
        if self.projektil:
            self.projektil.update(delta_time)




#vi kan lave en funktion der tegner vores projektil efter det er blevet afyrret og tegner vores scene
    def on_draw(self):
        self.clear()
        self.scene.draw()
        if self.projektil:
            self.projektil.draw()

#vi definere vores main funktion så den kalder de endividuelle information der er nødvendige for at køre koden
def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

#til sidste laver vi et if state ment som køre vores main funktion
if __name__ == "__main__":
    main()