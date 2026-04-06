import math

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
ortho_top = -100
ortho_bottom = 600

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Lindenmayer')

current_pos = (0, 0)
direction = np.array([0, 1, 0])
axiom = 'X'
rules = {
    # 'F': 'FF[+F][--FF][-F+F]',
    'X': 'F+[-F-XF-X][+FF][--XF[+X]][++F-X]'
}
draw_length = 10
turn_angle = 25
stack = []
instructions = ""
search_and_replace = 5

def run_rule(run_count):
    global instructions
    instructions = axiom
    for i in range(run_count):
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

def line_to(x, y):
    global current_pos
    glBegin(GL_LINE_STRIP)
    glVertex2f(current_pos[0], current_pos[1])
    glVertex2f(x, y)
    current_pos = (x, y)
    glEnd()

def reset_turtle():
    global current_pos
    global direction
    current_pos = (0, 0)
    direction = np.array([0, 1, 0])

def move_to(pos):
    global current_pos
    current_pos = (pos[0], pos[1])

def draw_turtle():
    global current_pos
    global direction
    for c in range(0, len(instructions)):
        if instructions[c] == 'F':
            forward(draw_length)
        elif instructions[c] == '+':
            rotate(turn_angle)
        elif instructions[c] == '-':
            rotate(-turn_angle)
        elif instructions[c] == '[':
            stack.append((current_pos, direction))
        elif instructions[c] == ']':
            current_vector = stack.pop()
            move_to(current_vector[0])
            direction = current_vector[1]

def forward(draw_length):
    new_x = current_pos[0] + direction[0] * draw_length
    new_y = current_pos[1] + direction[1] * draw_length
    line_to(new_x, new_y)

def rotate(angle):
    global direction
    new_direction = z_rotation(direction, math.radians(angle))
    direction = new_direction

init_ortho()
done = False
glLineWidth(1)
glPointSize(10)
run_rule(search_and_replace)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    reset_turtle()
    draw_turtle()
    pygame.display.flip()
pygame.quit()

