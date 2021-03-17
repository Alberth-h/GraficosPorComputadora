from OpenGL.GL import *
from glew_wish import *
import glfw

class Obstaculo:
    posx = 0.0
    posy = 0.6
    vivo = True

    def __init__(self, x, y):
        self.posx = x
        self.posy = y

    def dibujar(self):
        if self.vivo:
            glPushMatrix()
            glTranslate(self.posx, self.posy, 0.0)
            glBegin(GL_QUADS)
            glColor3f(0.0, 0.0, 1.0)
            glVertex(-0.15, 0.15, 0.0)
            glVertex(0.15, 0.15, 0.0)
            glVertex(0.15, -0.15, 0.0)
            glVertex(-0.15, -0.15, 0.0)
            glEnd()
            glPopMatrix()