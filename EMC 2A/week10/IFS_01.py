import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils2 import *

pygame.init()

screen_width = 800
screen_height = 800
ortho_left = -400
ortho_right = 400
ortho_top = 15
ortho_bottom = 15

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Iterative Function System')

current_position = (0, 0)
direction = np.array([0, 1, 0])
axiom = '-X'
rules = {
    # 'X': 'F+[-F-XF-X][+FF][--XF[+X]][++F-X]'
    # 'F': 'F+F−F−F+F'
    'F': 'FF',
    'X': 'F+[[X]-X]-F[-FX]+X'

}
draw_length = 3
turn_angle = 25
stack = []
search_and_replace = 5
instructions = ""
points = []
x = 0
y = 0


def run_rule(run_count):
    global instructions
    instructions = axiom
    for loop in range(run_count):
        old_system = instructions
        instructions = ""
        for c in range(0, len(old_system)):
            if old_system[c] in rules:
                instructions += rules[old_system[c]]
            else:
                instructions += old_system[c]
    print(instructions)

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)

def reset_turtle():
    global current_position
    global direction
    current_position = (0, 0)
    direction = np.array([0, 1, 0])

def draw_turtle():
    global x
    global y
    points.append((x, y))
    r = np.random.rand()
    if r < 0.1:
        x, y = 0.00 * x + 0.00 * y, 0.00 * x + 0.16 * y + 0.0
    elif r < 0.86:
        x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.60
    elif r < 0.93:
        x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
    else:
        x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 *y + 0.44


def draw_points():
    glPointSize(1)
    glBegin(GL_POINTS)
    for p in points:
        glVertex(p[0], p[1])
    glEnd()


init_ortho()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    reset_turtle()
    # draw_turtle()
    # draw_points()
    pygame.display.flip()
    pygame.time.wait(5)
pygame.quit()
