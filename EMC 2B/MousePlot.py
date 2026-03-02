import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math
from Utils import map_value

pygame.init()
screen_width = 1000
screen_height = 800
ortho_width = 640
ortho_height = 480

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Plotting Points Using Mouse')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, ortho_width, 0, ortho_height)


def plot_points():
    glColor(0, 1, 0, 1)
    for l in points:
        glBegin(GL_LINE_STRIP)
        for coord in l:
            glVertex2f(coord[0], coord[1])
        glEnd()


done = False
init_ortho()
glLineWidth(1)
points = []
line = []
mousedown = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
            line = []
            points.append(line)
        elif event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
        elif event.type == pygame.MOUSEMOTION and mousedown:
            p = pygame.mouse.get_pos()
            line.append((map_value(0, screen_width, 0, ortho_width, p[0]),
                         map_value(0, screen_height, ortho_height, 0, p[1])))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_points()
    pygame.display.flip()
pygame.quit()
