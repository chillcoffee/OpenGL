import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
#seatwork2: import numpy

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Basic Graphics Primitives')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)  #seatwork1: make the point appear at the center


def plot_graph():
    glBegin(GL_POINTS)
    glVertex2f(0, 0)
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
    plot_graph()    #seatwork3: plot this line f(x) = e raise to cos (2pix)
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
