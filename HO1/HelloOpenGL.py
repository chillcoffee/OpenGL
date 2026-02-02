import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("OpenGL in Python")


#camera setup orthographic projection for 2D
def init_ortho():
    glMatrixMode(GL_PROJECTION)  #camera
    glLoadIdentity()  #clear screen clear drawings
    gluOrtho2D(0, 640, 0, 480)  #setup view of camera means 0,0 of the window is at lowerleft corner


done = False
init_ortho()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)  #setup opengl to start drawing in model coordinate system
    glLoadIdentity()    #clear the modelview

    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2i(100, 50)
    glVertex2i(630, 450)
    glEnd()

    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
