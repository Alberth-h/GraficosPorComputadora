from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

class Bala:
    posx = 0.0
    posy = 0.0
    velocidad = 1.5
    desfase = 90
    angulo = 0.0

    def actualizar(self, tiempo_delta):
        #global obstaculo

        self.posy = self.posy + \
            (sin((self.angulo + self.desfase) * 3.14159 / 180) * self.velocidad * tiempo_delta)
        self.posx = self.posx + \
            (cos((self.angulo + self.desfase) * 3.14159 / 180) * self.velocidad * tiempo_delta)
        # checar colision con obstaculo si sigue "vivo"
        #if obstaculo.vivo and xBala + 0.01 > obstaculo.posx - 0.15 and xBala - 0.01 < obstaculo.posx + 0.15 and yBala + 0.01 > obstaculo.posy - 0.15 and yBala - 0.01 < obstaculo.posy + 0.15:
        #    obstaculo.vivo = False
        #    carrito.disparando = False

    def dibujar(self):
        glPushMatrix()
        glTranslate(self.posx, self.posy, 0.0)
        glRotate(self.angulo, 0.0, 0.0, 1.0)
        glBegin(GL_QUADS)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f(-0.01, 0.01, 0.0)
        glVertex3f(0.01, 0.01, 0.0)
        glVertex3f(0.01, -0.01, 0.0)
        glVertex3f(-0.01, -0.01, 0.0)
        glEnd()
        glPopMatrix()