from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import math

class Interfaz:
    def dibujar(self, jugador):
        #H
        glPushMatrix()
        glTranslatef(0.87,0.2,0.0)
        glScalef(0.03,0.05,0.0)
        glColor3f(1.0,1.0,1.0)
        glBegin(GL_QUADS)
        glVertex2f(-1,1)
        glVertex2f(-0.8,1)
        glVertex2f(-0.8,-1)
        glVertex2f(-1,-1)
        glVertex2f(0.8,1)
        glVertex2f(1,1)
        glVertex2f(1,-1)
        glVertex2f(0.8,-1)
        glVertex2f(-1,0.1)
        glVertex2f(1,0.1)
        glVertex2f(1,-0.1)
        glVertex2f(-1,-0.1)
        glEnd()
        glPopMatrix()
        
        #P
        glPushMatrix()
        glTranslatef(0.95,0.2,0.0)
        glScalef(0.03,0.05,0.0)
        glColor3f(1.0,1.0,1.0)
        glBegin(GL_QUADS)
        glVertex2f(-1,1)
        glVertex2f(-0.8,1)
        glVertex2f(-0.8,-1)
        glVertex2f(-1,-1)
        glVertex2f(0.8,1)
        glVertex2f(1,1)
        glVertex2f(1,0)
        glVertex2f(0.8,0)
        glVertex2f(-1,0.1)
        glVertex2f(1,0.1)
        glVertex2f(1,-0.1)
        glVertex2f(-1,-0.1)
        glVertex2f(-1,1)
        glVertex2f(1,1)
        glVertex2f(1, 0.8)
        glVertex2f(-1,0.8)
        glEnd()
        glPopMatrix()

        #cuadro salud
        glPushMatrix()
        glTranslatef(0.91,0.05,0.0)
        glScalef(0.05,0.05,0.0)
        if jugador.dano > -1 and jugador.dano < 10:
            glColor3f(0.0,1.0,0.0)
        if jugador.dano > 9 and jugador.dano < 20:
            glColor3f(0.4,1.0,0.0)
        if jugador.dano > 19 and jugador.dano < 30:
            glColor3f(0.6,1.0,0.0)
        
        if jugador.dano > 29 and jugador.dano < 40:
            glColor3f(0.8,1.0,0.0)
        if jugador.dano > 39 and jugador.dano < 50:
            glColor3f(1.0,1.0,0.0)
        if jugador.dano > 49 and jugador.dano < 60:
            glColor3f(1.0,0.8,0.0)

        if jugador.dano > 59 and jugador.dano < 70:
            glColor3f(1.0,0.6,0.0)
        if jugador.dano > 69 and jugador.dano < 80:
            glColor3f(1.0,0.4,0.0)
        if jugador.dano > 79 and jugador.dano < 90:
            glColor3f(1.0,0.2,0.0)

        if jugador.dano > 89 and jugador.dano < 100:
            glColor3f(1.0,0.0,0.0)
        if jugador.dano > 99 and jugador.dano < 110:
            glColor3f(0.6,0.0,0.0)
        if jugador.dano > 109 and jugador.dano < 120:
            glColor3f(0.3,0.0,0.0)

        if jugador.dano >= 120:
            glColor3f(0.0,0.0,0.0)

        glBegin(GL_QUADS)
        glVertex2f(-1,1)
        glVertex2f(1,1)
        glVertex2f(1,-1)
        glVertex2f(-1,-1)
        glEnd()
        glPopMatrix()