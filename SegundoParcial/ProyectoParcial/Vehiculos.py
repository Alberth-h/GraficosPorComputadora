from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import math
import random

from Carretera import velocidad as velocidadCarretera

class Carro1:
    psX = random.uniform(-0.8,0.0)
    psY = 5.0

    velocidad = 1.5

    def actualizar(self, deltatime):
        global velocidadCarretera

        movimiento = self.velocidad * velocidadCarretera * deltatime

        self.psY = self.psY - movimiento

        if self.psY < -1.01:
            self.psX = random.uniform(-0.8,0.0)
            self.psY = 5.0

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.psX, self.psY, 0)
        glRotate(180,0,0,1)
        glScalef(0.1,0.1,0.0)
        #carroceria
        glColor3f(0.0, 0.0, 0.7)
        glBegin(GL_QUADS)
        glVertex3f(-0.5, 0.3, 0.0)
        glVertex3f(-0.5, -0.4, 0.0)
        glVertex3f(0.5, -0.4, 0.0)
        glVertex3f(0.5, 0.3, 0.0)
        glEnd()
        glColor3f(0.0, 0.0, 0.6)
        glBegin(GL_QUADS)
        glVertex3f(-0.5, 0.3, 0.0)
        glVertex3f(-0.45, 1.0, 0.0)
        glVertex3f(0.45, 1.0, 0.0)
        glVertex3f(0.5, 0.3, 0.0)
        glEnd()
        glColor3f(0.0, 0.0, 0.6)
        glBegin(GL_QUADS)
        glVertex3f(-0.5, -0.4, 0.0)
        glVertex3f(-0.45, -1.0, 0.0)
        glVertex3f(0.45, -1.0, 0.0)
        glVertex3f(0.5, -0.4, 0.0)
        glEnd()
        #ventana
        glBegin(GL_QUADS)
        glColor3f(.0, 0.5, 0.5)
        glVertex3f(-.4, 0.0, 0.0)
        glVertex3f(-.5, 0.3, 0.0)
        glVertex3f(.5, 0.3, 0.0)
        glVertex3f(.4, 0.0, 0.0)
        glEnd()
        glPopMatrix()

class Carro2:
    psX = random.uniform(-0.8,0.0)
    psY = 8.0

    velocidad = 1.4

    def actualizar(self, deltatime):
        global velocidadCarretera

        movimiento = self.velocidad * velocidadCarretera * deltatime

        self.psY = self.psY - movimiento

        if self.psY < -1.01:
            self.psX = random.uniform(-0.8,0.0)
            self.psY = 8.0

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.psX, self.psY, 0)
        glRotate(180,0,0,1)
        glScalef(0.1,0.1,0.1)
        #carroceria
        glColor3f(0.7, 0.2, 0.0)
        glBegin(GL_QUADS)
        glVertex3f(-0.5, 0.3, 0.0)
        glVertex3f(-0.5, -0.4, 0.0)
        glVertex3f(0.5, -0.4, 0.0)
        glVertex3f(0.5, 0.3, 0.0)
        glEnd()
        glColor3f(0.6, 0.1, 0.0)
        glBegin(GL_QUADS)
        glVertex3f(-0.5, 0.3, 0.0)
        glVertex3f(-0.45, 1.0, 0.0)
        glVertex3f(0.45, 1.0, 0.0)
        glVertex3f(0.5, 0.3, 0.0)
        glEnd()
        glColor3f(0.6, 0.1, 0.0)
        glBegin(GL_QUADS)
        glVertex3f(-0.5, -0.4, 0.0)
        glVertex3f(-0.45, -1.0, 0.0)
        glVertex3f(0.45, -1.0, 0.0)
        glVertex3f(0.5, -0.4, 0.0)
        glEnd()
        #ventana
        glBegin(GL_QUADS)
        glColor3f(.0, 0.5, 0.5)
        glVertex3f(-.4, 0.0, 0.0)
        glVertex3f(-.5, 0.3, 0.0)
        glVertex3f(.5, 0.3, 0.0)
        glVertex3f(.4, 0.0, 0.0)
        glEnd()
        glPopMatrix()

class Carro3:
    psX = random.uniform(-0.8,0.0)
    psY = 14.0

    velocidad = 1.2

    def actualizar(self, deltatime):
        global velocidadCarretera

        movimiento = self.velocidad * velocidadCarretera * deltatime

        self.psY = self.psY - movimiento

        if self.psY < -1.01:
            self.psX = random.uniform(-0.8,0.0)
            self.psY = 14.0

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.psX, self.psY, 0)
        glRotate(180,0,0,1)
        glScalef(0.1,0.1,0.0)
        #carroceria
        glColor3f(0.5, 0.0, 0.0)
        glBegin(GL_QUADS)
        glVertex3f(-0.5, 0.3, 0.0)
        glVertex3f(-0.5, -1, 0.0)
        glVertex3f(0.5, -1, 0.0)
        glVertex3f(0.5, 0.3, 0.0)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(0.4, 0.0, 0.0)
        for x in range(181):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.5,sin(angulo)*0.3+0.7,0.0)
        glEnd()
        glColor3f(0.4, 0.0, 0.0)
        glBegin(GL_QUADS)
        glVertex3f(-0.5, 0.3, 0.0)
        glVertex3f(-0.5, 0.7, 0.0)
        glVertex3f(0.5, 0.7, 0.0)
        glVertex3f(0.5, 0.3, 0.0)
        glEnd()
        glColor3f(0.3, 0.0, 0.0)
        glBegin(GL_QUADS)
        glVertex3f(-0.05, 0.3, 0.0)
        glVertex3f(-0.05, -1, 0.0)
        glVertex3f(0.05, -1, 0.0)
        glVertex3f(0.05, 0.3, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glVertex3f(-0.15, 0.3, 0.0)
        glVertex3f(-0.15, -1, 0.0)
        glVertex3f(-0.25, -1, 0.0)
        glVertex3f(-0.25, 0.3, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glVertex3f(0.15, 0.3, 0.0)
        glVertex3f(0.15, -1, 0.0)
        glVertex3f(0.25, -1, 0.0)
        glVertex3f(0.25, 0.3, 0.0)
        glEnd()
        #ventana
        glBegin(GL_QUADS)
        glColor3f(.0, 0.5, 0.5)
        glVertex3f(-.4, 0.0, 0.0)
        glVertex3f(-.5, 0.3, 0.0)
        glVertex3f(.5, 0.3, 0.0)
        glVertex3f(.4, 0.0, 0.0)
        glEnd()
        glPopMatrix()

class Carro4:
    psX = random.uniform(-0.8,0.0)
    psY = 18.0

    velocidad = 1.6

    def actualizar(self, deltatime):
        global velocidadCarretera

        movimiento = self.velocidad * velocidadCarretera * deltatime

        self.psY = self.psY - movimiento

        if self.psY < -1.01:
            self.psX = random.uniform(-0.8,0.0)
            self.psY = 18.0

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.psX, self.psY, 0)
        glRotate(180,0,0,1)
        glScalef(0.1,0.1,0.0)
        #carroceria
        glColor3f(0.5, 0.5, 0.0)
        glBegin(GL_QUADS)
        glVertex3f(-0.5, 0.7, 0.0)
        glVertex3f(-0.5, -1, 0.0)
        glVertex3f(0.5, -1, 0.0)
        glVertex3f(0.5, 0.7, 0.0)
        glEnd()
        glColor3f(0.4, 0.4, 0.0)
        glBegin(GL_QUADS)
        glVertex3f(-0.5, 0.7, 0.0)
        glVertex3f(-0.5, 1, 0.0)
        glVertex3f(0.5, 1, 0.0)
        glVertex3f(0.5, 0.7, 0.0)
        glEnd()
        glColor3f(0.3, 0.3, 0.0)
        glBegin(GL_QUADS)
        glVertex3f(-0.05, 0.5, 0.0)
        glVertex3f(-0.05, -1, 0.0)
        glVertex3f(0.05, -1, 0.0)
        glVertex3f(0.05, 0.5, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glVertex3f(-0.15, 0.5, 0.0)
        glVertex3f(-0.15, -1, 0.0)
        glVertex3f(-0.25, -1, 0.0)
        glVertex3f(-0.25, 0.5, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glVertex3f(0.15, 0.5, 0.0)
        glVertex3f(0.15, -1, 0.0)
        glVertex3f(0.25, -1, 0.0)
        glVertex3f(0.25, 0.5, 0.0)
        glEnd()

        glColor3f(0.0, 0.5, 0.6)
        glBegin(GL_QUADS)
        glVertex3f(-0.3, 0.2, 0.0)
        glVertex3f(-0.3, -0.1, 0.0)
        glVertex3f(0.3, -0.1, 0.0)
        glVertex3f(0.3, 0.2, 0.0)
        glEnd()

        glColor3f(0.0, 0.5, 0.6)
        glBegin(GL_QUADS)
        glVertex3f(-0.3, -0.4, 0.0)
        glVertex3f(-0.3, -0.7, 0.0)
        glVertex3f(0.3, -0.7, 0.0)
        glVertex3f(0.3, -0.4, 0.0)
        glEnd()
        #ventana
        glBegin(GL_QUADS)
        glColor3f(.0, 0.5, 0.5)
        glVertex3f(-.4, 0.5, 0.0)
        glVertex3f(-.45, 0.7, 0.0)
        glVertex3f(.45, 0.7, 0.0)
        glVertex3f(.4, 0.5, 0.0)
        glEnd()
        glPopMatrix()

class Carro5:
    psX = -1.0
    psY = 6.91

    velocidad = 1.0

    def actualizar(self, deltatime, calleTrans):
        global velocidadCarretera

        movimientoCarretera = velocidadCarretera * deltatime
        movimiento = self.velocidad * deltatime

        self.psY = self.psY - movimientoCarretera

        if self.psY < 1.0:
            self.psY = self.psY - movimientoCarretera
            self.psX = self.psX + movimiento

        if self.psY < -2.0:
            self.psX = -1.0
            self.psY = calleTrans.psY + 0.8

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.psX, self.psY, 0)
        glScalef(0.1,0.1,0.1)
        glRotate(240,0,0,1)
        #carroceria
        glColor3f(0.7, 0.7, 0.7)
        glBegin(GL_QUADS)
        glVertex3f(-0.5, 0.5, 0.0)
        glVertex3f(-0.5, 0.0, 0.0)
        glVertex3f(0.5, 0.0, 0.0)
        glVertex3f(0.5, 0.5, 0.0)
        glEnd()

        glColor3f(0.6, 0.6, 0.6)
        glBegin(GL_QUADS)
        glVertex3f(-0.5, 0.5, 0.0)
        glVertex3f(-0.45, 1.0, 0.0)
        glVertex3f(0.45, 1.0, 0.0)
        glVertex3f(0.5, 0.5, 0.0)
        glEnd()

        glColor3f(0.6, 0.6, 0.6)
        glBegin(GL_QUADS)
        glVertex3f(-0.5, 0.0, 0.0)
        glVertex3f(-0.5, -1.0, 0.0)
        glVertex3f(0.5, -1.0, 0.0)
        glVertex3f(0.5, 0.0, 0.0)
        glEnd()

        glColor3f(0.4, 0.4, 0.4)
        glBegin(GL_QUADS)
        glVertex3f(-0.45, -0.05, 0.0)
        glVertex3f(-0.45, -0.95, 0.0)
        glVertex3f(0.45, -0.95, 0.0)
        glVertex3f(0.45, -0.05, 0.0)
        glEnd()
        #ventana
        glBegin(GL_QUADS)
        glColor3f(.0, 0.5, 0.5)
        glVertex3f(-.4, 0.2, 0.0)
        glVertex3f(-.45, 0.5, 0.0)
        glVertex3f(.45, 0.5, 0.0)
        glVertex3f(.4, 0.2, 0.0)
        glEnd()
        glPopMatrix()

class Vaca:
    psX = -1.0
    psY = 21

    velocidad = 1.0

    def actualizar(self, deltatime, caminoTrans):
        global velocidadCarretera

        movimientoCarretera = velocidadCarretera * deltatime
        movimiento = self.velocidad * deltatime

        self.psY = self.psY - movimientoCarretera

        if self.psY < 1.0:
            self.psY = self.psY - movimientoCarretera
            self.psX = self.psX + movimiento

        if self.psY < -2.0:
            self.psX = -1.0
            self.psY = caminoTrans.psY + 1.0

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.psX, self.psY, 0)
        glScalef(0.055,0.055,0.0)
        glColor3f(0.9, 0.9, 0.9)
        glBegin(GL_QUADS)
        glVertex3f(-1.0, -0.6, 0.5)
        glVertex3f(0.5, -0.6, 0.0)
        glVertex3f(0.5, 0.3, 0.0)
        glVertex3f(-1.0, 0.3, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glVertex3f(1.0, 0.3, 0.5)

        glVertex3f(0.5, 0.7, 0.0)
        glVertex3f(0.0, 0.3, 0.0)
        glVertex3f(0.7, 0.0, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glVertex3f(-1.0, -1.0, 0.5)
        glVertex3f(-0.8, -1.0, 0.0)
        glVertex3f(-0.8, 0.0, 0.0)
        glVertex3f(-1.0, 0.0, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glVertex3f(0.3, -1.0, 0.5)
        glVertex3f(0.5, -1.0, 0.0)
        glVertex3f(0.5, 0.0, 0.0)
        glVertex3f(0.3, 0.0, 0.0)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.0, 0.0)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.3-0.6,sin(angulo)*0.2-0.3,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.0, 0.0)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.3-0.4,sin(angulo)*0.2-0.2,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.25+0.1,sin(angulo)*0.15+0.1,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.15+0.6,sin(angulo)*0.05+0.2,0.0)
        glEnd()
        glPopMatrix()