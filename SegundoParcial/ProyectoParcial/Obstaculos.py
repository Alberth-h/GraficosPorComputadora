from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import math
import random

from Carretera import velocidad as velocidadCarretera

class Cono:
    psX = random.uniform(0.0, 0.8)
    psY = 4.0

    def actualizar(self, deltatime):
        global velocidadCarretera

        movimientoCarretera = velocidadCarretera * deltatime
        self.psY = self.psY - movimientoCarretera

        if self.psY < -1.01:
            self.psX = random.uniform(0.0,0.8)
            self.psY = 4.0

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.psX, self.psY,0)
        glScalef(0.03,0.03,0.03)
        glBegin(GL_TRIANGLES)
        glColor3f(1, 0.6, 0.0)
        glVertex3f(-.5, -.75, 0.0)
        glVertex3f(0.5, -.75, 0.0)
        glVertex3f(0, 1.0, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(1, .7, 0.0)
        glVertex3f(-.85, -.85, 0.0)
        glVertex3f(0.85, -.85, 0.0)
        glVertex3f(0.85, -1.0, 0.0)
        glVertex3f(-.85, -1.0, 0.0)
        glEnd()
        glPopMatrix()

class Barril:
    psX = random.uniform(0.0, 0.8)
    psY = 3.0

    def actualizar(self, deltatime):
        global velocidadCarretera

        movimientoCarretera = velocidadCarretera * deltatime
        self.psY = self.psY - movimientoCarretera

        if self.psY < -1.01:
            self.psX = random.uniform(0.0,0.8)
            self.psY = 3.0

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.psX, self.psY,0)
        glScalef(0.05,0.05,0.05)
        glBegin(GL_QUADS)
        glColor3f(.65, .7, 0)
        glVertex3f(-0.65, -0.9, 0.0)
        glVertex3f(-0.65, 0.9, 0.0)
        glVertex3f(0.65, 0.9, 0.0)
        glVertex3f(0.65, -0.9, 0.0)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(.65, .7, 0)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos (angulo) * 0.65 ,sin (angulo) * 0.1 + 0.9 ,0.0)
        glEnd()  
        glBegin(GL_POLYGON)
        glColor3f(.0, 1, 0)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos (angulo) * 0.6 ,sin (angulo) * 0.1 + 0.85 ,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(.65, .7, 0)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos (angulo) * 0.65 ,sin (angulo) * 0.1 - 0.9 ,0.0)
        glEnd()
        glColor3f(0, 0, 0)
        glBegin(GL_POLYGON)
        glColor3f(.0, .0, 0)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos (angulo) * 0.75 ,sin (angulo) * 0.1 ,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(.65, .7, 0)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos (angulo) * 0.65 ,sin (angulo) * 0.1 + 0.06,0.0)
        glEnd() 
        glPopMatrix()

class PonLlan:
    psX = random.uniform(0.0, 0.8)
    psY = 2.0

    def actualizar(self, deltatime):
        global velocidadCarretera

        movimientoCarretera = velocidadCarretera * deltatime
        self.psY = self.psY - movimientoCarretera

        if self.psY < -1.01:
            self.psX = random.uniform(0.0,0.8)
            self.psY = 2.0

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.psX, self.psY,0)
        glScalef(0.05,0.05,0.05)
        glBegin(GL_QUADS)
        glColor3f(0.35, .35, .35)
        glVertex3f(-1, -.3, 0.0)
        glVertex3f(1, -.3, 0.0)
        glVertex3f(1, -.35, 0.0)
        glVertex3f(-1, -.35, 0.0)
        glEnd()
        glBegin(GL_TRIANGLES)
        glColor3f(0.4, .4, .4)
        glVertex3f(-1, -.3, 0.0)
        glVertex3f(-.9, .3, 0.0)
        glVertex3f(-0.8, -.3, 0.0)
        glVertex3f(-0.8, -.3, 0.0)
        glVertex3f(-.7, .3, 0.0)
        glVertex3f(-.6, -.3, 0.0)
        glVertex3f(-.6, -.3, 0.0)
        glVertex3f(-.5, .3, 0.0)
        glVertex3f(-.4, -.3, 0.0)
        glVertex3f(-.4, -.3, 0.0)
        glVertex3f(-.3, .3, 0.0)
        glVertex3f(-.2, -.3, 0.0)
        glVertex3f(-.2, -.3, 0.0)
        glVertex3f(-.1, .3, 0.0)
        glVertex3f(0.0, -.3, 0.0)
        glVertex3f(0.0, -.3, 0.0)
        glVertex3f(.2, -.3, 0.0)
        glVertex3f(.1, .3, 0.0)
        glVertex3f(1, -.3, 0.0)
        glVertex3f(.9, .3, 0.0)
        glVertex3f(0.8, -.3, 0.0)
        glVertex3f(0.8, -.3, 0.0)
        glVertex3f(.7, .3, 0.0)
        glVertex3f(.6, -.3, 0.0)
        glVertex3f(.6, -.3, 0.0)
        glVertex3f(.5, .3, 0.0)
        glVertex3f(.4, -.3, 0.0)
        glVertex3f(.4, -.3, 0.0)
        glVertex3f(.3, .3, 0.0)
        glVertex3f(.2, -.3, 0.0)
        glEnd()
        glPopMatrix()

class Barrera:
    psX = random.uniform(0.0, 0.8)
    psY = 10.0

    def actualizar(self, deltatime):
        global velocidadCarretera

        movimientoCarretera = velocidadCarretera * deltatime
        self.psY = self.psY - movimientoCarretera

        if self.psY < -1.01:
            self.psX = random.uniform(0.0,0.8)
            self.psY = 10.0

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.psX, self.psY,0)
        glScalef(0.1,0.1,0.1)
        glBegin(GL_QUADS)
        glColor3f(0.4, .4, .4)
        glVertex3f(-1, .025, 0.0)
        glVertex3f(1, .025, 0.0)
        glVertex3f(1, -.025, 0.0)
        glVertex3f(-1, -.025, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(0.4, .4, .4)
        glVertex3f(-1, .05, 0.0)
        glVertex3f(1, .05, 0.0)
        glVertex3f(1, .1, 0.0)
        glVertex3f(-1, .1, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(0.4, .4, .4)
        glVertex3f(-1, .125, 0.0)
        glVertex3f(1, .125, 0.0)
        glVertex3f(1, .175, 0.0)
        glVertex3f(-1, .175, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(0.4, .4, .4)
        glVertex3f(-1, .2, 0.0)
        glVertex3f(1, .2, 0.0)
        glVertex3f(1, .25, 0.0)
        glVertex3f(-1, .25, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(0.4, .4, .4)
        glVertex3f(-1, -.05, 0.0)
        glVertex3f(1, -.05, 0.0)
        glVertex3f(1, -.1, 0.0)
        glVertex3f(-1, -.1, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(0.4, .4, .4)
        glVertex3f(-1, -.125, 0.0)
        glVertex3f(1, -.125, 0.0)
        glVertex3f(1, -.175, 0.0)
        glVertex3f(-1, -.175, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(0.4, .4, .4)
        glVertex3f(-1, -.2, 0.0)
        glVertex3f(1, -.2, 0.0)
        glVertex3f(1, -.25, 0.0)
        glVertex3f(-1, -.25, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(0.4, .1, 0)
        glVertex3f(-1, -0.3, 0.0)
        glVertex3f(-.95, -0.3, 0.0)
        glVertex3f(-0.95, .3, 0.0)
        glVertex3f(-1, .3, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(0.4, .1, 0)
        glVertex3f(1, -0.3, 0.0)
        glVertex3f(.95, -.3, 0.0)
        glVertex3f(0.95, .3, 0.0)
        glVertex3f(1, .3, 0.0)
        glEnd()
        glPopMatrix() 