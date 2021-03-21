from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import math
import random
import sys

from Carretera import velocidad as velocidadCarretera

class Jugador:
    psX = 0.0
    psY = 0.0

    velocidad = 1.0

    condicionXP = False
    condicionXN = False
    condicionYP = False
    condicionYN = False

    dano = 0
    gameOver = False

    def actualizar_movimiento(self, window, deltatime):
        movimiento = self.velocidad * deltatime

        estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)
        estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
        estado_tecla_abajo = glfw.get_key(window, glfw.KEY_DOWN)
        estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)

        if self.dano < 120:
            if estado_tecla_izquierda == glfw.PRESS:
                self.condicionXP = False
                self.condicionXN = True
                self.condicionYP = False
                self.condicionYN = False
            if self.psX - 0.05 < -0.8:
                self.condicionXP = True
                self.condicionXN = False
                self.condicionYP = False
                self.condicionYN = False
            if estado_tecla_derecha == glfw.PRESS:
                self.condicionXP = True
                self.condicionXN = False
                self.condicionYP = False
                self.condicionYN = False
            if self.psX + 0.05 > 0.8:
                self.condicionXP = False
                self.condicionXN = True
                self.condicionYP = False
                self.condicionYN = False
            if estado_tecla_abajo == glfw.PRESS:
                self.condicionXP = False
                self.condicionXN = False
                self.condicionYP = False
                self.condicionYN = True
            if self.psY - 0.1 < -1.0:
                self.condicionXP = False
                self.condicionXN = False
                self.condicionYP = True
                self.condicionYN = False
            if estado_tecla_arriba == glfw.PRESS:
                self.condicionXP = False
                self.condicionXN = False
                self.condicionYP = True
                self.condicionYN = False
            if self.psY + 0.1 > 1.0:
                self.condicionXP = False
                self.condicionXN = False
                self.condicionYP = False
                self.condicionYN = True

            if self.condicionXP == True:
                self.psX = self.psX + movimiento
            if self.condicionXN == True:
                self.psX = self.psX - movimiento
            if self.condicionYP == True:
                self.psY = self.psY + movimiento
            if self.condicionYN == True:
                self.psY = self.psY - movimiento

    def actualizar_dano(self, deltatime, tiempo, policia, tramo, tramoAux, calleTrans, caminoTrans, cono, barril, ponLLan, barrera, carro5, vaca):
        global velocidadCarretera

        movimiento = self.velocidad * deltatime
        movimientoCarretera = velocidadCarretera * deltatime
        if self.dano >= 120:
            self.condicionXP = False
            self.condicionXN = False
            self.condicionYP = False
            self.condicionYN = False
            tramo.psY = tramo.psY + movimientoCarretera
            tramoAux.psY = tramoAux.psY + movimientoCarretera
            calleTrans.psY = calleTrans.psY + movimientoCarretera
            caminoTrans.psY = caminoTrans.psY + movimientoCarretera
            cono.psY = cono.psY + movimientoCarretera
            barril.psY = barril.psY + movimientoCarretera
            ponLLan.psY = ponLLan.psY + movimientoCarretera
            barrera.psY = barrera.psY + movimientoCarretera
            carro5.psY = carro5.psY + movimientoCarretera
            carro5.psX = carro5.psX - movimiento
            vaca.psY = vaca.psY + movimientoCarretera
            vaca.psX = vaca.psX - movimiento
            policia.psY  = policia.psY + movimiento
            if policia.psY + 0.1 > self.psY - 0.1:
                print("Has sido arrestado!!!")
                print(("Has durado en la persecución por:"), tiempo, ("segundos"))
                sys.exit()

    def colisiones(self, tiempo, policia, cono, barril, ponLlan, barrera, carro1, carro2, carro3, carro4, carro5, vaca):
        if self.psY - 0.1 < policia.psY + 0.1:
            self.gameOver = True
        elif self.psX - 0.05 < cono.psX + 0.03 and self.psX + 0.05 > cono.psX - 0.03 and self.psY - 0.1 < cono.psY + 0.03 and self.psY + 0.1 > cono.psY - 0.03:  
            self.dano += 1
        elif self.psX - 0.05 < barril.psX + 0.05 and self.psX + 0.05 > barril.psX - 0.05 and self.psY - 0.1 < barril.psY + 0.05 and self.psY + 0.1 > barril.psY - 0.05:  
            self.dano += 1
        elif self.psX - 0.05 < ponLlan.psX + 0.05 and self.psX + 0.05 > ponLlan.psX - 0.05 and self.psY - 0.1 < ponLlan.psY + 0.0125 and self.psY + 0.1 > ponLlan.psY - 0.0125:  
            self.dano += 1
        elif self.psX - 0.05 < barrera.psX + 0.1 and self.psX + 0.05 > barrera.psX - 0.1 and self.psY - 0.1 < barrera.psY + 0.05 and self.psY + 0.1 > barrera.psY - 0.05:  
            self.dano += 1
        elif self.psX - 0.05 < carro1.psX + 0.05 and self.psX + 0.05 > carro1.psX - 0.05 and self.psY - 0.1 < carro1.psY + 0.1 and self.psY + 0.1 > carro1.psY - 0.1:  
            self.dano += 1
        elif self.psX - 0.05 < carro2.psX + 0.05 and self.psX + 0.05 > carro2.psX - 0.05 and self.psY - 0.1 < carro2.psY + 0.1 and self.psY + 0.1 > carro2.psY - 0.1:  
            self.dano += 1
        elif self.psX - 0.05 < carro3.psX + 0.05 and self.psX + 0.05 > carro3.psX - 0.05 and self.psY - 0.1 < carro3.psY + 0.1 and self.psY + 0.1 > carro3.psY - 0.1:  
            self.dano += 1
        elif self.psX - 0.05 < carro4.psX + 0.05 and self.psX + 0.05 > carro4.psX - 0.05 and self.psY - 0.1 < carro4.psY + 0.1 and self.psY + 0.1 > carro4.psY - 0.1:  
            self.dano += 1
        elif self.psX - 0.05 < carro5.psX + 0.05 and self.psX + 0.05 > carro5.psX - 0.05 and self.psY - 0.1 < carro5.psY + 0.1 and self.psY + 0.1 > carro5.psY - 0.1:  
            self.dano += 1
        elif self.psX - 0.05 < vaca.psX + 0.055 and self.psX + 0.05 > vaca.psX - 0.055 and self.psY - 0.1 < vaca.psY + 0.55 and self.psY + 0.1 > vaca.psY - 0.55:  
            self.dano += 1
        else:
            self.gameOver = False
        
        if self.gameOver == True:
            print("Has sido arrestado!!!")
            print(("Has durado en la persecución por:"), tiempo, ("segundos"))
            sys.exit()

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.psX, self.psY, 0)
        glScalef(0.1,0.1,0.0)
        #carroceria
        if self.dano > 60 and self.dano < 100:
            glColor3f(.55, 0, .0)
        elif self.dano > 99:
            glColor3f(.35, 0, .0)
        else:
            glColor3f(.7, 0, .0)
        glBegin(GL_QUADS)
        glVertex3f(-0.5, 0.2, 0.0)
        glVertex3f(-0.5, -0.6, 0.0)
        glVertex3f(0.5, -0.6, 0.0)
        glVertex3f(0.5, 0.2, 0.0)
        glEnd()
        if self.dano > 60 and self.dano < 100:
            glColor3f(.45, 0, .0)
        elif self.dano > 99:
            glColor3f(.25, 0, .0)
        else:
            glColor3f(.6, 0, .0)
        glBegin(GL_QUADS)
        glVertex3f(-0.5, 0.2, 0.0)
        glVertex3f(-0.45, 1.0, 0.0)
        glVertex3f(0.45, 1.0, 0.0)
        glVertex3f(0.5, 0.2, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        if self.dano > 60 and self.dano < 100:
            glColor3f(.45, 0, .0)
        elif self.dano > 99:
            glColor3f(.25, 0, .0)
        else:
            glColor3f(.6, 0, .0)
        glVertex3f(-0.5, -0.6, 0.0)
        glVertex3f(-0.45, -1.0, 0.0)
        glVertex3f(0.45, -1.0, 0.0)
        glVertex3f(0.5, -0.6, 0.0)
        glEnd()

        #rayas
        glBegin(GL_QUADS)
        glColor3f(0, .0, .0)
        glVertex3f(0.1, -1, 0.0)
        glVertex3f(0.05, -1, 0.0)
        glVertex3f(0.05, 1, 0.0)
        glVertex3f(0.1, 1, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(0, .0, .0)
        glVertex3f(-0.1, -1, 0.0)
        glVertex3f(-0.05, -1, 0.0)
        glVertex3f(-0.05, 1, 0.0)
        glVertex3f(-0.1, 1, 0.0)
        glEnd()
        
        #ventana
        if self.dano <= 60:
            glBegin(GL_QUADS)
            glColor3f(0.0, 0.5, 0.5)
            glVertex3f(-.4, 0.0, 0.0)
            glVertex3f(-.5, 0.2, 0.0)
            glVertex3f(.5, 0.2, 0.0)
            glVertex3f(.4, 0.0, 0.0)
            glEnd()
        if self.dano > 60:
            glBegin(GL_QUADS)
            glColor3f(0.15, 0.0, 0.0)
            glVertex3f(-.4, 0.0, 0.0)
            glVertex3f(-.5, 0.2, 0.0)
            glVertex3f(.5, 0.2, 0.0)
            glVertex3f(.4, 0.0, 0.0)
            glEnd()

        #aleron
        if self.dano > 60 and self.dano < 100:
            glColor3f(0.5,  0.17, .075)
        elif self.dano > 99:
            glColor3f(0.3,  0.1, .05)
        else:
            glColor3f(0.7,  0.25, .1)
        glBegin(GL_QUADS)
        glVertex3f(-.6, -.85, 0.0)
        glVertex3f(-.6, -.95, 0.0)
        glVertex3f(.6, -.95, 0.0)
        glVertex3f(.6, -.85, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(.0,  0, .0)
        glVertex3f(-.6, -.9, 0.0)
        glVertex3f(-.6, -.925, 0.0)
        glVertex3f(.6, -.925, 0.0)
        glVertex3f(.6, -.9, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(.0,  0, .0)
        glVertex3f(-.6, -.87, 0.0)
        glVertex3f(-.6, -.895, 0.0)
        glVertex3f(.6, -.895, 0.0)
        glVertex3f(.6, -.87, 0.0)
        glEnd()
        glPopMatrix()