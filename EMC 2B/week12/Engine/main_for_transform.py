import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import *
from LoadMesh import *
from Camera import *

pygame.init()

# project settings
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')
# objectVariable = classname() #instantiation
# cube = LoadMesh("teapot.obj", GL_LINE_LOOP)
cube = Cube(GL_LINE_LOOP)
camera = Camera()


def initialise():
    glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
    glColor(drawing_color)

    # projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 1000.0)

def init_camera():
    # modelview
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)
    camera.update(screen.get_width(), screen.get_height())

def draw_xyz():
    glLineWidth(5)
    sphere = gluNewQuadric()
    #x
    glBegin(GL_LINES)
    glColor(1, 0, 0)
    glVertex3f(-1000, 0, 0)
    glVertex3f(1000, 0, 0)
    glEnd()

    glPushMatrix()
    glTranslated(1, 0, 0)
    gluSphere(sphere, 0.05, 10, 10)
    glPopMatrix()

    # y
    glBegin(GL_LINES)
    glColor(0, 1, 0)
    glVertex3f(0, -1000, 0)
    glVertex3f(0, 1000, 0)
    glEnd()

    glPushMatrix()
    glTranslated(0, 1, 0)
    gluSphere(sphere, 0.05, 10, 10)
    glPopMatrix()

    # z
    glBegin(GL_LINES)
    glColor(0, 0, 1)
    glVertex3f(0, 0, -1000)
    glVertex3f(0, 0, 1000)
    glEnd()

    glPushMatrix()
    glTranslated(0, 0, 1)
    gluSphere(sphere, 0.05, 10, 10)
    glPopMatrix()

    glColor(1, 1, 1)
    glLineWidth(1)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_xyz()
    init_camera()
    glPushMatrix()
    glTranslated(0.5, 0.5, 0.5)
    cube.draw()     #obj.methodName()
    glTranslate(0, 1, 0)
    cube.draw()
    glTranslate(0, 1, 0)
    cube.draw()
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
                pygame.event.set_grab(False)
                pygame.mouse.set_visible(True)
            if event.key == K_SPACE:
                pygame.event.set_grab(True)
                pygame.mouse.set_visible(False)
    display()
    pygame.display.flip()
pygame.quit()