import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("First Pygame Window")

#camera
def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()        #clearing the matrix
    gluOrtho2D(-100,900, 600, -10)    #left, right, top, bottom


init_ortho()    #method call fro camera
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glPointSize(25)
    glBegin(GL_POINTS)
    glColor(1, 0, 0, 1)
    glVertex2i(0, 0)

    glColor(0, 1, 0, 1) #green
    glVertex2i(500, 400)

    glColor(0, 0, 1, 1)
    glVertex2i(6, -4)
    glEnd()

    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()


















