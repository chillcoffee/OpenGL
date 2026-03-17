import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from w4_2Utils import map_value

pygame.init()

screen_width = 1000
screen_height = 800

ortho_width = 640
ortho_height = 480

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Simple Paint')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, ortho_width, 0, ortho_height)


def plot_point(point):
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()


def plot_lines():
    for l in points:
        glBegin(GL_LINE_STRIP)
        for coords in l:
            glVertex2f(coords[0], coords[1])
        glEnd()

def save_drawing():
    f = open("w5_8drawing.txt", "w")
    f.write(str(len(points)) + "\n")
    for l in points:
        f.write(str(len(l)) + "\n")
        for coords in l:
            f.write(str(coords[0]) +" "+str(coords[1])+"\n")
    f.close()
    print("Done saving drawing to file.")


def load_drawing():
    f = open("w5_8drawing.txt", "r")
    num_of_lines = int(f.readline())   #3 read first line of txt file
    global points
    global line
    points = []         #empty the points
    for line in range(num_of_lines):
        line = []
        points.append(line)
        num_of_coords = int(f.readline())       #156
        """
        list comprehension
        list_variable = [x for x in iterable]
        sample in Math:
        S = {x² : x in {0 ... 9}}
        V = (1, 2, 4, 8, ..., 2¹²)
        M = {x | x in S and x even}
        
        S = {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
        V = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096}
        M = {0, 4, 16, 36, 64}
        """
        for coord in range(num_of_coords):
            px, py = [float(value) for value in next(f).split()]    #next(f) advance the cursor to next readLine
            line.append((px, py))
    print("Loaded coordinates from file.")


done = False
init_ortho()
glPointSize(10)
glColor(1, 0, 1, 1)
points = []
line = []
mouse_down = False
while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                save_drawing()
            elif event.key == pygame.K_l:
                load_drawing()
            elif event.key == pygame.K_SPACE:
                points = []
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = True
            line = []
            points.append(line)
        elif event.type == MOUSEBUTTONUP:
            mouse_down = False
        elif event.type == MOUSEMOTION and mouse_down:
            p = pygame.mouse.get_pos()
            line.append((map_value(0, screen_width, 0, ortho_width, p[0]),
                         map_value(0, screen_height, ortho_height, 0, p[1])))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_lines()
    pygame.display.flip()
pygame.quit()
