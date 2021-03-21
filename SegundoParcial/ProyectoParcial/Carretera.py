from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import math

velocidad = 2.0

class Tramo:
    psX = 0.0
    psY = 0.0

    def __init__(self, x, y):
        self.psX = x
        self.psY = y

    def actualizar(self, deltatime):
        global velocidad
        movimiento = velocidad * deltatime
        self.psY = self.psY - movimiento

        if self.psY < -2.0:
            self.psY = 2.0

    def dibujar(self):
        #Carretera principal
        glPushMatrix()
        glTranslatef(self.psX, self.psY, 0.0)
        glScalef(1.0,1.1,1.1)
        glColor3f(0.1, 0.1, 0.1)
        glBegin(GL_QUADS)
        glVertex2f(-0.8, 1.0)
        glVertex2f(0.8, 1.0)
        glVertex2f(0.8, -1.0)
        glVertex2f(-0.8, -1.0)
        glEnd()

        glColor3f(0.3, 0.3, 0.3)
        glBegin(GL_QUADS)
        glVertex2f(-0.82, 1.0)
        glVertex2f(-0.8, 1.0)
        glVertex2f(-0.8, -1.0)
        glVertex2f(-0.82, -1.0)
        glEnd()

        glColor3f(0.3, 0.3, 0.3)
        glBegin(GL_QUADS)
        glVertex2f(-0.01, 1.0)
        glVertex2f(0.01, 1.0)
        glVertex2f(0.01, -1.01)
        glVertex2f(-0.01, -1.01)
        glEnd()

        glColor3f(0.3, 0.3, 0.3)
        glBegin(GL_QUADS)
        glVertex2f(0.82, 1.0)
        glVertex2f(0.8, 1.0)
        glVertex2f(0.8, -1.01)
        glVertex2f(0.82, -1.01)
        glEnd()
        glPopMatrix()

        #lineas carretera principal
        glPushMatrix()
        glTranslatef(self.psX, self.psY, 0.0)
        glScalef(1.0,1.0,1.1)
        glColor3f(0.4, 0.4, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(-0.41, 0.9)
        glVertex2f(-0.39, 0.9)
        glVertex2f(-0.39, 0.7)
        glVertex2f(-0.41, 0.7)
        glEnd()
        glColor3f(0.4, 0.4, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(-0.41, 0.5)
        glVertex2f(-0.39, 0.5)
        glVertex2f(-0.39, 0.3)
        glVertex2f(-0.41, 0.3)
        glEnd()
        glColor3f(0.4, 0.4, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(-0.41, 0.1)
        glVertex2f(-0.39, 0.1)
        glVertex2f(-0.39, -0.1)
        glVertex2f(-0.41, -0.1)
        glEnd()
        glColor3f(0.4, 0.4, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(-0.41, -0.3)
        glVertex2f(-0.39, -0.3)
        glVertex2f(-0.39, -0.5)
        glVertex2f(-0.41, -0.5)
        glEnd()
        glColor3f(0.4, 0.4, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(-0.41, -0.7)
        glVertex2f(-0.39, -0.7)
        glVertex2f(-0.39, -0.9)
        glVertex2f(-0.41, -0.9)
        glEnd()

        glColor3f(0.4, 0.4, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(0.41, 0.9)
        glVertex2f(0.39, 0.9)
        glVertex2f(0.39, 0.7)
        glVertex2f(0.41, 0.7)
        glEnd()
        glColor3f(0.4, 0.4, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(0.41, 0.5)
        glVertex2f(0.39, 0.5)
        glVertex2f(0.39, 0.3)
        glVertex2f(0.41, 0.3)
        glEnd()
        glColor3f(0.4, 0.4, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(0.41, 0.1)
        glVertex2f(0.39, 0.1)
        glVertex2f(0.39, -0.1)
        glVertex2f(0.41, -0.1)
        glEnd()
        glColor3f(0.4, 0.4, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(0.41, -0.3)
        glVertex2f(0.39, -0.3)
        glVertex2f(0.39, -0.5)
        glVertex2f(0.41, -0.5)
        glEnd()
        glColor3f(0.4, 0.4, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(0.41, -0.7)
        glVertex2f(0.39, -0.7)
        glVertex2f(0.39, -0.9)
        glVertex2f(0.41, -0.9)
        glEnd()
        glPopMatrix()

class CalleTrans:
    psX = 0.0
    psY = 6.11

    def actualizar(self, deltatime):
        global velocidad
        movimiento = velocidad * deltatime
        self.psY = self.psY - movimiento

        if self.psY < -2.0:
            self.psY = 6.11

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.psX, self.psY, 0.0)
        glRotate(60,0,0,1)
        glScalef(1.0,1.0,1.0)
        glColor3f(0.1, 0.1, 0.1)
        glBegin(GL_QUADS)
        glVertex2f(-0.2, 1.5)
        glVertex2f(0.2, 1.5)
        glVertex2f(0.2, -1.5)
        glVertex2f(-0.2, -1.5)
        glEnd()

        glColor3f(0.3, 0.3, 0.3)
        glBegin(GL_QUADS)
        glVertex2f(-0.22, 1.5)
        glVertex2f(-0.2, 1.5)
        glVertex2f(-0.2, 0.81)
        glVertex2f(-0.22, 0.81)
        glEnd()
        glColor3f(0.3, 0.3, 0.3)
        glBegin(GL_QUADS)
        glVertex2f(-0.22, -1.5)
        glVertex2f(-0.2, -1.5)
        glVertex2f(-0.2, -1.05)
        glVertex2f(-0.22, -1.05)
        glEnd()
        
        glColor3f(0.3, 0.3, 0.3)
        glBegin(GL_QUADS)
        glVertex2f(0.22, 1.5)
        glVertex2f(0.2, 1.5)
        glVertex2f(0.2, 1.05)
        glVertex2f(0.22, 1.05)
        glEnd()
        glColor3f(0.3, 0.3, 0.3)
        glBegin(GL_QUADS)
        glVertex2f(0.22, -1.5)
        glVertex2f(0.2, -1.5)
        glVertex2f(0.2, -0.81)
        glVertex2f(0.22, -0.81)
        glEnd()
        glPopMatrix()

class CaminoTrans:
    psX = 0.0
    psY = 20.0

    def actualizar(self, deltatime):
        global velocidad
        movimiento = velocidad * deltatime
        self.psY = self.psY - movimiento

        if self.psY < -3.0:
            self.psY = 20.0

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.psX, self.psY, 0.0)
        glRotate(50,0,0,1)
        glScalef(1.0,1.0,1.0)
        glColor3f(0.3, 0.2, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(-0.2, 2.5)
        glVertex2f(0.2, 2.5)
        glVertex2f(0.2, -2.5)
        glVertex2f(-0.2, -2.5)
        glEnd()
        glPopMatrix()