from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import math
import random
import sys

from Carretera import velocidad as velocidadCarretera

class Policia:
    psX = 0.0
    psY = -0.9

    faro = 0

    def actualizar_retroceso(self, deltatime, cono, barril, ponLlan, barrera, carro1, carro2, carro3, carro4, carro5, vaca, jugador):
        global velocidadCarretera

        movimientoCarretera = velocidadCarretera * deltatime
        self.psX = jugador.psX

        if jugador.dano < 120:  
            if self.psY + 0.1 > cono.psY - 0.03 and self.psX + 0.05 > cono.psX - 0.03 and self.psX - 0.05 < cono.psX - 0.03:
                self.psY = self.psY - movimientoCarretera
            elif self.psY + 0.1 > barril.psY - 0.05 and self.psX + 0.05 > barril.psX - 0.03 and self.psX - 0.05 < barril.psX - 0.03:
                self.psY = self.psY - movimientoCarretera
            elif self.psY + 0.1 > ponLlan.psY - 0.0125 and self.psX + 0.05 > ponLlan.psX - 0.05 and self.psX - 0.05 < ponLlan.psX - 0.05:
                self.psY = self.psY - movimientoCarretera
            elif self.psY + 0.1 > barrera.psY - 0.05 and self.psX + 0.05 > barrera.psX - 0.1 and self.psX - 0.05 < barrera.psX - 0.1:
                self.psY = self.psY - movimientoCarretera
            elif self.psY + 0.1 > carro1.psY - 0.1 and self.psX + 0.05 > carro1.psX - 0.05 and self.psX - 0.05 < carro1.psX - 0.05:
                self.psY = self.psY - movimientoCarretera
            elif self.psY + 0.1 > carro2.psY - 0.1 and self.psX + 0.05 > carro2.psX - 0.05 and self.psX - 0.05 < carro2.psX - 0.05:
                self.psY = self.psY - movimientoCarretera
            elif self.psY + 0.1 > carro3.psY - 0.1 and self.psX + 0.05 > carro3.psX - 0.05 and self.psX - 0.05 < carro3.psX - 0.05:
                self.psY = self.psY - movimientoCarretera
            elif self.psY + 0.1 > carro4.psY - 0.1 and self.psX + 0.05 > carro4.psX - 0.05 and self.psX - 0.05 < carro4.psX - 0.05:
                self.psY = self.psY - movimientoCarretera
            elif self.psY + 0.1 > carro5.psY - 0.1 and self.psX + 0.05 > carro5.psX - 0.05 and self.psX - 0.05 < carro5.psX - 0.05:
                self.psY = self.psY - movimientoCarretera
            elif self.psY + 0.1 > vaca.psY - 0.55 and self.psX + 0.05 > vaca.psX - 0.055 and self.psX - 0.05 < vaca.psX - 0.055:
                self.psY = self.psY - movimientoCarretera

        if self.psY < -1.0:
            self.psY = -0.9

    def actualizar_faro(self, deltatime):
        self.faro = self.faro + deltatime * 8
        if self.faro > 2.0:
            self.faro = 0.0

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.psX, self.psY, 0)
        glScalef(0.1,0.1,0.0)
        #carroceria
        glColor3f(0.6, 0.6, 0.6)
        glBegin(GL_QUADS)
        glVertex3f(-0.5, 0.4, 0.0)
        glVertex3f(-0.5, -0.4, 0.0)
        glVertex3f(0.5, -0.4, 0.0)
        glVertex3f(0.5, 0.4, 0.0)
        glEnd()
        glColor3f(.0, 0, .0)
        glBegin(GL_QUADS)
        glVertex3f(-0.5, 0.4, 0.0)
        glVertex3f(-0.45, 1.1, 0.0)
        glVertex3f(0.45, 1.1, 0.0)
        glVertex3f(0.5, 0.4, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(.0, 0, .0)
        glVertex3f(-0.5, -0.4, 0.0)
        glVertex3f(-0.45, -1.0, 0.0)
        glVertex3f(0.45, -1.0, 0.0)
        glVertex3f(0.5, -0.4, 0.0)
        glEnd()
        #ventana
        glBegin(GL_QUADS)
        glColor3f(.0, 0.5, 0.5)
        glVertex3f(-.4, 0.1, 0.0)
        glVertex3f(-.5, 0.4, 0.0)
        glVertex3f(.5, 0.4, 0.0)
        glVertex3f(.4, 0.1, 0.0)
        glEnd()

        #faros
        if self.faro < 1.3:
            glBegin(GL_TRIANGLE_FAN)
            glColor3f(0.0,0.0,1.0)
            glVertex3f(-0.25,-0.15,0.0)
            for x in range(361):
                angulo = x * 3.14159 / 180.0
                glColor3f(0.0,0.0,0.3)
                glVertex3f(cos(angulo)*0.4-0.25,sin(angulo)*0.4-0.15,0.0)
            glEnd()
        if self.faro > 1 and self.faro < 2:
            glBegin(GL_TRIANGLE_FAN)
            glColor3f(1.0,0.0,0.0)
            glVertex3f(0.25,-0.15,0.0)
            for x in range(361):
                angulo = x * 3.14159 / 180.0
                glColor3f(0.3,0.0,0.0)
                glVertex3f(cos(angulo)*0.4+0.25,sin(angulo)*0.4-0.15,0.0)
            glEnd()
        glPopMatrix()