import pygame
from constants import *
entityList = []
import math

class Entity:
    def __init__(self, (x, y, z), img):
        self.x = x
        self.y = y
        self.z = z
        self.img = img
        self.sprite = pygame.image.load(img)
        self.height = self.sprite.get_height()
        self.width = self.sprite.get_width()
        entityList.append(self)

    def draw(self, target_surface, horizon, (player_x, player_y, player_z)):
        distance = abs(float(player_z- self.z))
        print distance
        if distance <= 1 or distance >= 800:
            return 0
        surf = self.sprite
        scale =60/(distance+1)
        scaleFactor = 70
        surf = pygame.transform.scale(surf, ((self.width*scaleFactor)/(int(distance)+1), (self.height*scaleFactor)/(int(distance)+1)))
        surf.set_colorkey(WHITE)

        centre_x = target_surface.get_width() / 2
        centre_y = target_surface.get_height() / 2
        surf_x = self.x + centre_x - player_x
        surf_y = self.y + centre_y - player_y



        surf_x = surf_x + (surf_x - centre_x)*scale

        if self.z > player_z:
            target_surface.blit(surf, (surf_x - surf.get_width()/2, surf_y - surf.get_height()/2))

class Player:
    def __init__(self, (x,y,z)):
        self.x = x
        self.y = y
        self.z = z
        self.walkspeed = 1
        self.speed = 1
        self.accel = 1
        self.maxspeed = 1
        self.direction = 90 # in degrees
    def move(self):
        self.z += int(self.speed)
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.speed += self.accel
            if self.speed > self.maxspeed:
                self.speed = self.maxspeed
        else:
            self.speed -= self.accel
            if self.speed < 0:
                self.speed = 0

        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.z -= self.walkspeed
        if pygame.key.get_pressed()[pygame.K_z]:
            self.x -= self.walkspeed
        if pygame.key.get_pressed()[pygame.K_x]:
            self.x += self.walkspeed
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.z -= self.walkspeed
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.direction += 1
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.direction -= 1
        if pygame.key.get_pressed()[pygame.K_q]:
            self.y -= self.walkspeed
