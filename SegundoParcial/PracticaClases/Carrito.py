from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
from Bala import *

bala = Bala()

class Carrito:
    posx = 0.0
    posy = -0.8
    angulo = 0
    desfase = 90
    velocidad = 1
    velocidad_angular = 180
    disparando = False
    colisionando = False

    def dibujar(self):
        global bala
        glPushMatrix()
        glTranslate(self.posx, self.posy, 0.0)
        glRotate(self.angulo, 0.0, 0.0, 1.0)
        glBegin(GL_TRIANGLES)
        if self.colisionando == True:
            glColor3f(1.0, 1.0, 1.0)
        else:
            glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.0, 0.05, 0.0)
        glVertex3f(-0.05, -0.05, 0.0)
        glVertex3f(0.05, -0.05, 0.0)
        glEnd()
        glPopMatrix()

        if self.disparando:
            bala.dibujar()

    def actualizar(self, window, tiempo_delta):
        global bala
        estadoIzquierda = glfw.get_key(window, glfw.KEY_LEFT)
        estadoDerecha = glfw.get_key(window, glfw.KEY_RIGHT)
        estadoAbajo = glfw.get_key(window, glfw.KEY_DOWN)
        estadoArriba = glfw.get_key(window, glfw.KEY_UP)

        if estadoIzquierda == glfw.PRESS:
            self.angulo = self.angulo + (self.velocidad_angular * tiempo_delta)
            if self.angulo > 360:
                self.angulo = 0
        if estadoDerecha == glfw.PRESS:
            self.angulo = self.angulo - (self.velocidad_angular * tiempo_delta)
            if self.angulo < 0:
                self.angulo = 360

        if estadoArriba == glfw.PRESS:
            self.posy = self.posy + \
                (sin((self.angulo + self.desfase) * 3.14159 / 180) * self.velocidad * tiempo_delta)
            self.posx = self.posx + \
                (cos((self.angulo + self.desfase) * 3.14159 / 180) * self.velocidad * tiempo_delta)
        
        if self.disparando:
            if bala.posx >= 1:
                self.disparando = False
            elif bala.posx <= -1:
                self.disparando = False
            elif bala.posy >= 1:
                self.disparando = False
            elif bala.posy <= -1:
                self.disparando = False

        if self.disparando:
            bala.actualizar(tiempo_delta)
   
    def checar_colision(self, obstaculo):
        global bala
        # Si extremaDerechaCarrito > extremaIzquierdaObstaculo
        # Y extremaIzquierdaCarrito < extremaDerechaObstaculo
        # Y extremoSuperiorCarrito > extremoInferiorObstaculo
        # Y extremoInferiorCarrito < extremoSuperiorObstaculo
        if self.posx + 0.05 > obstaculo.posx - 0.15 and self.posx - 0.05 < obstaculo.posx + 0.15 and self.posy + 0.05 > obstaculo.posy - 0.15 and self.posy - 0.05 < obstaculo.posy + 0.15:
            self.colisionando = True
        else:
            self.colisionando = False

        if self.disparando and obstaculo.vivo and bala.posx + 0.01 > obstaculo.posx - 0.15 and bala.posx - 0.01 < obstaculo.posx + 0.15 and bala.posy + 0.01 > obstaculo.posy - 0.15 and bala.posy - 0.01 < obstaculo.posy + 0.15:
            obstaculo.vivo = False
            self.disparando = False

    def disparar(self):
        global bala
        self.disparando = True
        bala.posx = self.posx
        bala.posy = self.posy
        bala.angulo = self.angulo