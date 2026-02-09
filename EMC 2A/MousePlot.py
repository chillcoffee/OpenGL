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
pygame.display.set_caption('Basic Graphics Primitives - Plot Points Using Mouse')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D (0, ortho_width, 0, ortho_height)
    # gluOrtho2D(0, 640, 0, 480)
    # gluOrtho2D(0, 1000, 800, 0)     #camera is looking from 800 y to zero (y) kaya its flipped
    #mapping or scaling => position the openGL xy points with respect to the pygame window


def plot_point(point):
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])  #point is passed as a list x sa index 0 and y sa index 1
    glEnd()


done = False
init_ortho()
glPointSize(10)
glColor(1, 0, 1, 1)
points = []  #empty list of points of tuples for points ex: [(point 1), (point 1), (point 3)]
while not done:
    p = None  #declare a point p
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            p = pygame.mouse.get_pos()  #get the x,y kung saan si user nag left_click
            print(f"{p[0], p[1]}")
            # points.append(p)                #append the new x,y position of the mouse to the list
            # points.append((map_value(0, screen_width, 0, 640, p[0]),
            #                map_value(0, screen_height, 480, 0, p[1])))  # triple parenthesis because tuple

            points.append((map_value(0, screen_width, 0, ortho_width, p[0]),
                           map_value(0, screen_height, ortho_height,0, p[1])))   #triple parenthesis because tuple

    glClear(
        GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  #point disappear because we are clearing the screen coz we are using double buffer
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # if p is not None:     #call plot_point only if nag click si user
    #     plot_point(p)

    plot_point(points)  #call the function and ipasa du list which is global

    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
