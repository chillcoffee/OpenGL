import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


pygame.init()

screen_width = 800
screen_height = 800
ortho_left = -10
ortho_right = 10
ortho_top = -10
ortho_bottom = 10

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Midterm Exam')
#39
rules = {
    'F': 'FF',
    'X': 'F+[[X]-X]-F[-FX]+X'
}

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)

#36
def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex2i(-1, 1)
    glVertex2i(1, -1)
    glVertex2i(0, 1)
    glEnd()

#37
def save_to_file(points):
    f = open("data.txt", "w")
    number_of_coords = len(points)
    f.write(str(number_of_coords) +"\n")
    for i in range(0, number_of_coords):
        coord = points[i]
        f.write(str(coord[0]) +" "+ str(coord[1])+"\n")

#38
def forward(draw_length):
    glLineWidth(5)
    glColor(0, 1, 0, 1)
    current_pos = (0, 0)
    new_x = current_pos[0] + draw_length
    new_y = current_pos[1] + draw_length
    glBegin(GL_LINES)
    glVertex2f(current_pos[0], current_pos[1])
    glVertex2f(new_x, new_y)
    glEnd()

draw_length = 5
init_ortho()
done = False
points = [(3, 3), (4, 4), (5, 5), (6, 6)]
save_to_file(points)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # draw_triangle()
    forward(draw_length)
    # save_to_file(points)
    pygame.display.flip()
pygame.quit()