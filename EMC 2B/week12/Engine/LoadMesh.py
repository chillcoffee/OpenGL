from Mesh import *
from OpenGL.GL import *
import pygame

class LoadMesh(Mesh):
    def __init__(self, filename, draw_type):
        self.vertices = []
        self.triangles = []
        self.draw_type = draw_type
        self.filename = filename
        self.load_drawing()

    def load_drawing(self):
        #read the file, if v add to vertex, f add triangle
        with open(self.filename) as fp:
            line = fp.readline()
            while line:
                if line[:2] == 'v ':
                    vx, vy, vz = [float(value) for value in line[2:].split()]
                    self.vertices.append((vx, vy, vz))
                #f 49/51/49 48/50/48 69/72/69
                if line[:2] == 'f ':
                    t1, t2, t3 = [value for value in line[2:].split()]
                    self.triangles.append([int(value) for value in t1.split('/')][0]-1)
                    self.triangles.append([int(value) for value in t2.split('/')][0] - 1)
                    self.triangles.append([int(value) for value in t3.split('/')][0] - 1)
                line = fp.readline()




















