import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import *
from Camera import *

pygame.init()

# project settings
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Coordinate Space and Camera')
# objectVariable = classname() #instantiation
cube = Cube(GL_LINE_LOOP)
camera = Camera()

def initialise():
    glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
    glColor(drawing_color)

    # projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 1000.0) #fovy, aspect ratio, zNear, zFar

def init_camera():
    # modelview
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)
    camera.update(screen.get_width(), screen.get_height())

def draw_world_axes():
    glLineWidth(4)
    glBegin(GL_LINES)
    glColor(1, 0, 0)
    glVertex3d(1000, 0, 0)
    glVertex3d(-1000, 0, 0)
    glEnd()

    glLineWidth(4)
    glBegin(GL_LINES)
    glColor(0, 1, 0)
    glVertex3d(0, 1000, 0)
    glVertex3d(0, -1000, 0)
    glEnd()

    glLineWidth(4)
    glBegin(GL_LINES)
    glColor(0, 0, 1)
    glVertex3d(0, 0, 1000)
    glVertex3d(0, 0, -1000)
    glEnd()


    #sphere
    sphere = gluNewQuadric()
    glColor(1, 0, 0)
    glPushMatrix()
    glTranslated(1, 0, 0)
    gluSphere(sphere, 0.05, 10, 10)
    glPopMatrix()

    glColor(0, 1, 0)
    glPushMatrix()
    glTranslated(0, 1, 0)
    gluSphere(sphere, 0.05, 10, 10)
    glPopMatrix()

    glColor(0, 0, 1)
    glPushMatrix()
    glTranslated(0, 0, 1)
    gluSphere(sphere, 0.05, 10, 10)
    glPopMatrix()

    #revert color back to white
    glLineWidth(1)
    glColor(1, 1, 1)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    init_camera()
    draw_world_axes()
    glPushMatrix()
    # cube.draw(pygame.Vector3(0.5, 1.5, 0.5))
    # cube.draw(pygame.Vector3(0, 1, 0))
    for z in range(10):
        for x in range(10):
            cube.draw(pygame.Vector3(x, 0.5, z))

    glPopMatrix()


done = False
initialise()
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.mouse.set_visible(True)
                pygame.event.set_grab(False)
            if event.key == K_SPACE:
                pygame.mouse.set_visible(False)
                pygame.event.set_grab(True)

    display()
    pygame.display.flip()
pygame.quit()