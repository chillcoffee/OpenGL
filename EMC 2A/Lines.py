import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import map_value

pygame.init()

screen_width = 1000
screen_height = 800

ortho_width = 640
ortho_height = 480

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Basic Graphics Primitives - Different GL_LINE Parameters')
#GATEPASS: MAKE DIFFERENT LINE STRIP FOR EVERY MOUSEUP

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D (0, ortho_width, 0, ortho_height)


def plot_point(point):
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()


def plot_lines(point):
    # glBegin(GL_LINES)         #every two dots glVertex will plot a line
    # glBegin(GL_LINE_LOOP)     #draw line from first point to last point and connect like a loop
    glBegin(GL_LINE_STRIP)      #continues lines but no loop
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()


done = False
init_ortho()
glPointSize(10)
glColor(1, 0, 1, 1)
points = []
mouse_down = False
while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = True
        elif event.type == MOUSEBUTTONUP:
            mouse_down = False
        elif event.type == MOUSEMOTION and mouse_down:
            p = pygame.mouse.get_pos()
            print(f"{p[0], p[1]}")
            points.append((map_value(0, screen_width, 0, ortho_width, p[0]),
                           map_value(0, screen_height, ortho_height,0, p[1])))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    plot_lines(points)

    pygame.display.flip()
    # pygame.time.wait(100)     #do not wait to see the curve
pygame.quit()
