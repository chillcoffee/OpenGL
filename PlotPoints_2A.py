import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np  #todo: seatwork 3: import and install numpy
import math


pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Basic Graphics Primitives')


def init_ortho():   #setup camera
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 4, 1, -1)  #todo: seatwork1: make the point appear at the center
    #todo seatwork5: zoom in to show the curves of the graph


def plot_graph():
    glBegin(GL_POINTS)
    px: GL_DOUBLE   #todo: seatwork3: plot the graph of the line
    py: GL_DOUBLE
    for px in np.arange(0, 4, 0.005):  # todo: seatwork4: change the arange params to fill the entire screen with the graph
        py = math.exp(-px) * math.cos(2 * math.pi * px)
        glVertex2f(px, py)
    glEnd()


done = False
init_ortho()
glPointSize(5)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_graph()
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
