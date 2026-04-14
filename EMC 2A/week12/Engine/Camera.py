import pygame
from OpenGL.GLU import *
from math import *

class Camera:

    def __init__(self):
        self.eye = pygame.math.Vector3(0, 0, 0)
        self.up = pygame.math.Vector3(0, 1, 0)
        self.right = pygame.math.Vector3(1, 0, 0)       #right(x-axis)
        self.forward = pygame.math.Vector3(0, 0, 1)     #forward towards z(screen)
        self.look = self.eye + self.forward
        self.key_sensitivity = 1

    def update(self, w, h):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.eye -= self.forward * self.key_sensitivity
        if keys[pygame.K_UP]:
            self.eye += self.forward * self.key_sensitivity
        if keys[pygame.K_RIGHT]:
            self.eye += self.right * self.key_sensitivity
        if keys[pygame.K_LEFT]:
            self.eye -= self.right * self.key_sensitivity

        self.look = self.eye + self.forward
        gluLookAt(
            self.eye.x, self.eye.y, self.eye.z,
            self.look.x, self.look.y, self.look.z,
            self.up.x, self.up.y, self.up.z
        )