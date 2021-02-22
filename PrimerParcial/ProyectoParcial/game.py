from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import math
import random
import sys
import playsound


#Jugador
psX_jugador = 0.0
psY_jugador = 0.0

#Policia
psY_Policia = -0.9
faro = 0

#Daño
Dano = 0

#Obstaculos
psX_Cono = random.uniform(0.0, 0.8)
psY_Cono = 4.0
psX_Barril = random.uniform(0.0, 0.8)
psY_Barril = 3.0
psX_PonLlan = random.uniform(0.0, 0.8)
psY_PonLlan = 2.0
psX_Barrera = random.uniform(0.0, 0.8)
psY_Barrera = 10.0 

#Tiempo y velocidades
tiempo = 0.0
tiempoAnterior = 0.0
velocidad = 1.0
velocidadCarretera = 2
condicionXP = False
condicionXN = False
condicionYP = False
condicionYN = False

#Carretera
psX_Tramo = 0.0
psY_Tramo = 0.0
psY_TramoAux = 2.0
psX_CalleTrans = 0.0
psY_CalleTrans = 6.11
psX_CaminoTrans = 0.0
psY_CaminoTrans = 20.0

#Vehiculos
psX_Carro1 = -0.5
psY_Carro1 = 5.0
psX_Carro2 = -0.1
psY_Carro2 = 8.0
psX_Carro3 = -0.3
psY_Carro3 = 14.0
psX_Carro4 = -0.7
psY_Carro4 = 18.0
psX_Carro5 = -1.0
psY_Carro5 = psY_CalleTrans + 0.8
psX_vaca = -1.0
psY_vaca = psY_CaminoTrans + 1.0

playsound.playsound('song.mp3', False)
playsound.playsound('siren.mp3', False)

#colisiones
gameOver = False

def colisiones():
    global psX_jugador
    global psY_jugador
    global psY_Policia
    global psX_Cono
    global psY_Cono
    global psX_Barril
    global psY_Barril
    global psX_PonLlan
    global psY_PonLlan
    global psX_Barrera
    global psY_Barrera
    global psX_Carro1
    global psY_Carro1
    global psX_Carro2
    global psY_Carro2
    global psX_Carro3
    global psY_Carro3
    global psX_Carro4
    global psY_Carro4
    global psX_Carro5
    global psY_Carro5
    global psX_vaca
    global psY_vaca
    global gameOver
    global Dano
    global condicionXP
    global condicionXN
    global condicionYP
    global condicionYN    
    global psY_Tramo
    global psY_TramoAux
    global psY_CalleTrans
    global psY_CaminoTrans

    if psY_jugador - 0.1 < psY_Policia + 0.1:
        gameOver = True
    elif psX_jugador - 0.05 < psX_Cono + 0.03 and psX_jugador + 0.05 > psX_Cono - 0.03 and psY_jugador - 0.1 < psY_Cono + 0.03 and psY_jugador + 0.1 > psY_Cono - 0.03:  
        Dano += 1
    elif psX_jugador - 0.05 < psX_Barril + 0.05 and psX_jugador + 0.05 > psX_Barril - 0.05 and psY_jugador - 0.1 < psY_Barril + 0.05 and psY_jugador + 0.1 > psY_Barril - 0.05:  
        Dano += 1
    elif psX_jugador - 0.05 < psX_PonLlan + 0.05 and psX_jugador + 0.05 > psX_PonLlan - 0.05 and psY_jugador - 0.1 < psY_PonLlan + 0.0125 and psY_jugador + 0.1 > psY_PonLlan - 0.0125:  
        Dano += 1
    elif psX_jugador - 0.05 < psX_Barrera + 0.1 and psX_jugador + 0.05 > psX_Barrera - 0.1 and psY_jugador - 0.1 < psY_Barrera + 0.05 and psY_jugador + 0.1 > psY_Barrera - 0.05:  
        Dano += 1
    elif psX_jugador - 0.05 < psX_Carro1 + 0.05 and psX_jugador + 0.05 > psX_Carro1 - 0.05 and psY_jugador - 0.1 < psY_Carro1 + 0.1 and psY_jugador + 0.1 > psY_Carro1 - 0.1:  
        Dano += 1
    elif psX_jugador - 0.05 < psX_Carro2 + 0.05 and psX_jugador + 0.05 > psX_Carro2 - 0.05 and psY_jugador - 0.1 < psY_Carro2 + 0.1 and psY_jugador + 0.1 > psY_Carro2 - 0.1:  
        Dano += 1
    elif psX_jugador - 0.05 < psX_Carro3 + 0.05 and psX_jugador + 0.05 > psX_Carro3 - 0.05 and psY_jugador - 0.1 < psY_Carro3 + 0.1 and psY_jugador + 0.1 > psY_Carro3 - 0.1:  
        Dano += 1
    elif psX_jugador - 0.05 < psX_Carro4 + 0.05 and psX_jugador + 0.05 > psX_Carro4 - 0.05 and psY_jugador - 0.1 < psY_Carro4 + 0.1 and psY_jugador + 0.1 > psY_Carro4 - 0.1:  
        Dano += 1
    elif psX_jugador - 0.05 < psX_Carro5 + 0.05 and psX_jugador + 0.05 > psX_Carro5 - 0.05 and psY_jugador - 0.1 < psY_Carro5 + 0.1 and psY_jugador + 0.1 > psY_Carro5 - 0.1:  
        Dano += 1
    elif psX_jugador - 0.05 < psX_vaca + 0.055 and psX_jugador + 0.05 > psX_vaca - 0.055 and psY_jugador - 0.1 < psY_vaca + 0.55 and psY_jugador + 0.1 > psY_vaca - 0.55:  
        Dano += 1
    else:
        gameOver = False
    
    if gameOver == True:
        print("Has sido arrestado!!!")
        print(("Has durado en la persecución por:"), tiempo, ("segundos"))
        sys.exit()

def actualizar(window):
    global tiempo
    global tiempoAnterior
    global velocidad
    global velocidadCarretera
    global psX_jugador
    global psY_jugador
    global psY_Tramo
    global psY_TramoAux
    global psY_CalleTrans
    global psY_CaminoTrans
    global condicionXP
    global condicionXN
    global condicionYP
    global condicionYN
    global faro
    global psY_Policia
    global psX_Cono
    global psY_Cono
    global psX_Barril
    global psY_Barril
    global psX_PonLlan
    global psY_PonLlan
    global psX_Barrera
    global psY_Barrera
    global psX_Carro1
    global psY_Carro1
    global psX_Carro2
    global psY_Carro2
    global psX_Carro3
    global psY_Carro3
    global psX_Carro4
    global psY_Carro4
    global psX_Carro5
    global psY_Carro5
    global psX_vaca
    global psY_vaca
    global Dano

    tiempo = glfw.get_time()
    deltatime = tiempo - tiempoAnterior
    movimiento = velocidad * deltatime
    movimientoCarretera = velocidadCarretera * deltatime

    faro = faro + deltatime * 8

    if faro > 2.0:
        faro = 0.0
    
    estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)
    estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estado_tecla_abajo = glfw.get_key(window, glfw.KEY_DOWN)
    estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)

    psY_Tramo = psY_Tramo - movimientoCarretera
    psY_TramoAux = psY_TramoAux - movimientoCarretera
    psY_CalleTrans = psY_CalleTrans - movimientoCarretera
    psY_CaminoTrans = psY_CaminoTrans - movimientoCarretera

    psY_Cono = psY_Cono - movimientoCarretera
    psY_Barril = psY_Barril - movimientoCarretera
    psY_PonLlan = psY_PonLlan - movimientoCarretera
    psY_Barrera = psY_Barrera - movimientoCarretera

    psY_Carro1 = psY_Carro1 - movimientoCarretera * 1.5
    psY_Carro2 = psY_Carro2 - movimientoCarretera * 1.4
    psY_Carro3 = psY_Carro3 - movimientoCarretera * 1.2
    psY_Carro4 = psY_Carro4 - movimientoCarretera * 1.6

    psY_Carro5 = psY_Carro5 - movimientoCarretera
    psY_vaca = psY_vaca - movimientoCarretera

    if psY_Carro5 < 1.0:
        psY_Carro5 = psY_Carro5 - movimientoCarretera
        psX_Carro5 = psX_Carro5 + movimiento
    
    if psY_vaca < 1.0:
        psY_vaca = psY_vaca - movimientoCarretera
        psX_vaca = psX_vaca + movimiento

    if psY_Tramo < -2.0:
        psY_Tramo = 2.0
    elif psY_TramoAux < -2.0:
        psY_TramoAux = 2.0
    elif psY_CalleTrans < -2.0:
        psY_CalleTrans = 6.11
    elif psY_CaminoTrans < -3.0:
        psY_CaminoTrans = 20.0

    if psY_Cono < -1.01:
        psX_Cono = random.uniform(0.0,0.8)
        psY_Cono = 4.0
    if psY_Barril < -1.01:
        psX_Barril = random.uniform(0.0,0.8)
        psY_Barril = 3.0
    if psY_PonLlan < -1.01:
        psX_PonLlan = random.uniform(0.0,0.8)
        psY_PonLlan = 2.0
    if psY_Barrera < -1.01:
        psX_Barrera = random.uniform(0.0,0.8)
        psY_Barrera = 10.0

    if psY_Carro1 < -1.01:
        psX_Carro1 = random.uniform(-0.8,0.0)
        psY_Carro1 = 5.0
    if psY_Carro2 < -1.01:
        psX_Carro2 = random.uniform(-0.8,0.0)
        psY_Carro2 = 8.0
    if psY_Carro3 < -1.01:
        psX_Carro3 = random.uniform(-0.8,0.0)
        psY_Carro3 = 14.0
    if psY_Carro4 < -1.01:
        psX_Carro4 = random.uniform(-0.8,0.0)
        psY_Carro4 = 18.0
    if psY_Carro5 < -2.0:
        psX_Carro5 = -1.0
        psY_Carro5 = psY_CalleTrans + 0.8
    if psY_vaca < -2.0:
        psX_vaca = -1.0
        psY_vaca = psY_CaminoTrans + 1.0

    if psY_Policia + 0.1 > psY_Cono - 0.03 and psX_jugador + 0.05 > psX_Cono - 0.03 and psX_jugador - 0.05 <  psX_Cono - 0.03:
        psY_Policia = psY_Policia - movimientoCarretera
    elif psY_Policia + 0.1 > psY_Barril - 0.05 and psX_jugador + 0.05 > psX_Barril - 0.03 and psX_jugador - 0.05 <  psX_Barril - 0.03:
        psY_Policia = psY_Policia - movimientoCarretera
    elif psY_Policia + 0.1 > psY_PonLlan - 0.0125 and psX_jugador + 0.05 > psX_PonLlan - 0.05 and psX_jugador - 0.05 <  psX_PonLlan - 0.05:
        psY_Policia = psY_Policia - movimientoCarretera
    elif psY_Policia + 0.1 > psY_Barrera - 0.05 and psX_jugador + 0.05 > psX_Barrera - 0.1 and psX_jugador - 0.05 <  psX_Barrera - 0.1:
        psY_Policia = psY_Policia - movimientoCarretera
    elif psY_Policia + 0.1 > psY_Carro1 - 0.1 and psX_jugador + 0.05 > psX_Carro1 - 0.05 and psX_jugador - 0.05 <  psX_Carro1 - 0.05:
        psY_Policia = psY_Policia - movimientoCarretera
    elif psY_Policia + 0.1 > psY_Carro2 - 0.1 and psX_jugador + 0.05 > psX_Carro2 - 0.05 and psX_jugador - 0.05 <  psX_Carro2 - 0.05:
        psY_Policia = psY_Policia - movimientoCarretera
    elif psY_Policia + 0.1 > psY_Carro3 - 0.1 and psX_jugador + 0.05 > psX_Carro3 - 0.05 and psX_jugador - 0.05 <  psX_Carro3 - 0.05:
        psY_Policia = psY_Policia - movimientoCarretera
    elif psY_Policia + 0.1 > psY_Carro4 - 0.1 and psX_jugador + 0.05 > psX_Carro4 - 0.05 and psX_jugador - 0.05 <  psX_Carro4 - 0.05:
        psY_Policia = psY_Policia - movimientoCarretera
    elif psY_Policia + 0.1 > psY_Carro5 - 0.1 and psX_jugador + 0.05 > psX_Carro5 - 0.05 and psX_jugador - 0.05 <  psX_Carro5 - 0.05:
        psY_Policia = psY_Policia - movimientoCarretera
    elif psY_Policia + 0.1 > psY_vaca - 0.55 and psX_jugador + 0.05 > psX_vaca - 0.055 and psX_jugador - 0.05 <  psX_vaca - 0.055:
        psY_Policia = psY_Policia - movimientoCarretera

    if psY_Policia < -1.0:
        psY_Policia = -0.9

    if Dano < 120:
        if estado_tecla_izquierda == glfw.PRESS:
            condicionXP = False
            condicionXN = True
            condicionYP = False
            condicionYN = False
        if psX_jugador - 0.05 < -0.8:
            condicionXP = True
            condicionXN = False
            condicionYP = False
            condicionYN = False
        if estado_tecla_derecha == glfw.PRESS:
            condicionXP = True
            condicionXN = False
            condicionYP = False
            condicionYN = False
        if psX_jugador + 0.05 > 0.8:
            condicionXP = False
            condicionXN = True
            condicionYP = False
            condicionYN = False
        if estado_tecla_abajo == glfw.PRESS:
            condicionXP = False
            condicionXN = False
            condicionYP = False
            condicionYN = True
        if psY_jugador - 0.1 < -1.0:
            condicionXP = False
            condicionXN = False
            condicionYP = True
            condicionYN = False
        if estado_tecla_arriba == glfw.PRESS:
            condicionXP = False
            condicionXN = False
            condicionYP = True
            condicionYN = False
        if psY_jugador + 0.1 > 1.0:
            condicionXP = False
            condicionXN = False
            condicionYP = False
            condicionYN = True

        if condicionXP == True:
            psX_jugador = psX_jugador + movimiento
        if condicionXN == True:
            psX_jugador = psX_jugador - movimiento
        if condicionYP == True:
            psY_jugador = psY_jugador + movimiento
        if condicionYN == True:
            psY_jugador = psY_jugador - movimiento
    
    if Dano > 120:
        condicionXP = False
        condicionXN = False
        condicionYP = False
        condicionYN = False
        psY_Tramo = psY_Tramo + movimientoCarretera
        psY_TramoAux = psY_TramoAux + movimientoCarretera
        psY_CalleTrans = psY_CalleTrans + movimientoCarretera
        psY_CaminoTrans = psY_CaminoTrans + movimientoCarretera
        psY_Cono = psY_Cono + movimientoCarretera
        psY_Barril = psY_Barril + movimientoCarretera
        psY_PonLlan = psY_PonLlan + movimientoCarretera
        psY_Barrera = psY_Barrera + movimientoCarretera
        psY_Carro5 = psY_Carro5 + movimientoCarretera
        psX_Carro5 = psX_Carro5 - movimiento
        psY_vaca = psY_vaca + movimientoCarretera
        psX_vaca = psX_vaca - movimiento
        psY_Policia = psY_Policia + movimiento
        if psY_Policia + 0.1 > psY_jugador - 0.1:
            psY_Policia = psY_Policia + movimientoCarretera
            psY_Policia = psY_Policia - movimiento
            print("Has sido arrestado!!!")
            print(("Has durado en la persecución por:"), tiempo, ("segundos"))
            sys.exit()
    tiempoAnterior = tiempo
    colisiones()


def dibujarObstaculos():
    global psX_Cono
    global psY_Cono
    global psX_Barril
    global psY_Barril
    global psX_PonLlan
    global psY_PonLlan
    global psX_Barrera
    global psY_Barrera

    #cono
    glPushMatrix()
    glTranslatef(psX_Cono,psY_Cono,0)
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

    #barril
    glPushMatrix()
    glTranslatef(psX_Barril,psY_Barril,0)
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

    #Ponchallantas
    glPushMatrix()
    glTranslatef(psX_PonLlan,psY_PonLlan,0)
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

    #barrera
    glPushMatrix()
    glTranslatef(psX_Barrera,psY_Barrera,0)
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

def dibujarCarros():
    global psX_Carro1
    global psY_Carro1
    global psX_Carro2
    global psY_Carro2
    global psX_Carro3
    global psY_Carro3
    global psX_Carro4
    global psY_Carro4
    global psX_Carro5
    global psY_Carro5
    global psX_vaca
    global psY_vaca

    #carro1
    glPushMatrix()
    glTranslatef(psX_Carro1,psY_Carro1,0)
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

    #carro2
    glPushMatrix()
    glTranslatef(psX_Carro2,psY_Carro2,0)
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

    #carro3
    glPushMatrix()
    glTranslatef(psX_Carro3,psY_Carro3,0)
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

    #carro4
    glPushMatrix()
    glTranslatef(psX_Carro4,psY_Carro4,0)
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

    #carro5
    glPushMatrix()
    glTranslatef(psX_Carro5,psY_Carro5,0)
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

    #vaca
    glPushMatrix()
    glTranslatef(psX_vaca,psY_vaca,0)
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

def dibujarCarretera():
    global psX_Tramo
    global psY_Tramo
    global psY_TramoAux
    global psX_CalleTrans
    global psY_CalleTrans
    global psX_CaminoTrans
    global psY_CaminoTrans

    #Camino transversal
    glPushMatrix()
    glTranslatef(psX_CaminoTrans,psY_CaminoTrans,0.0)
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

    #Carretera principal
    glPushMatrix()
    glTranslatef(psX_Tramo,psY_Tramo,0.0)
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
    glTranslatef(psX_Tramo,psY_Tramo,0.0)
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

    #Carretera principal auxiliar
    glPushMatrix()
    glTranslatef(psX_Tramo,psY_TramoAux,0.0)
    glScalef(1.0,1.1,1.1)
    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_QUADS)
    glVertex2f(-0.8, 1.0)
    glVertex2f(0.8, 1.0)
    glVertex2f(0.8, -1.01)
    glVertex2f(-0.8, -1.01)
    glEnd()

    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_QUADS)
    glVertex2f(-0.82, 1.0)
    glVertex2f(-0.8, 1.0)
    glVertex2f(-0.8, -1.01)
    glVertex2f(-0.82, -1.01)
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

    #Carretera principal auxiliar lineas
    glPushMatrix()
    glTranslatef(psX_Tramo,psY_TramoAux,0.0)
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

    #Calle transversal
    glPushMatrix()
    glTranslatef(psX_CalleTrans,psY_CalleTrans,0.0)
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

def dibujarJugador():
    global psX_jugador
    global psY_jugador
    global Dano

    glPushMatrix()
    glTranslatef(psX_jugador,psY_jugador,0)
    glScalef(0.1,0.1,0.0)
    #carroceria
    if Dano > 60 and Dano < 100:
        glColor3f(.55, 0, .0)
    elif Dano > 99:
        glColor3f(.25, 0, .0)
    else:
        glColor3f(.7, 0, .0)
    glBegin(GL_QUADS)
    glVertex3f(-0.5, 0.2, 0.0)
    glVertex3f(-0.5, -0.6, 0.0)
    glVertex3f(0.5, -0.6, 0.0)
    glVertex3f(0.5, 0.2, 0.0)
    glEnd()
    if Dano > 60 and Dano < 100:
        glColor3f(.45, 0, .0)
    elif Dano > 99:
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
    if Dano > 60 and Dano < 100:
        glColor3f(.45, 0, .0)
    elif Dano > 99:
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
    if Dano < 60:
        glBegin(GL_QUADS)
        glColor3f(.0, 0.5, 0.5)
        glVertex3f(-.4, 0.0, 0.0)
        glVertex3f(-.5, 0.2, 0.0)
        glVertex3f(.5, 0.2, 0.0)
        glVertex3f(.4, 0.0, 0.0)
        glEnd()
    if Dano > 60:
        glBegin(GL_QUADS)
        glColor3f(.2, 0.0, 0.0)
        glVertex3f(-.4, 0.0, 0.0)
        glVertex3f(-.5, 0.2, 0.0)
        glVertex3f(.5, 0.2, 0.0)
        glVertex3f(.4, 0.0, 0.0)
        glEnd()

    #aleron
    if Dano > 60 and Dano < 100:
        glColor3f(0.5,  0.17, .075)
    elif Dano > 99:
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

def dibujarPolicia():
    global psX_jugador
    global psY_Policia
    global faro
    
    glPushMatrix()
    glTranslatef(psX_jugador,psY_Policia,0)
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
    if faro < 1.3:
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.0,0.0,1.0)
        glVertex3f(-0.25,-0.15,0.0)
        for x in range(361):
            angulo = x * 3.14159 / 180.0
            glColor3f(0.0,0.0,0.3)
            glVertex3f(cos(angulo)*0.4-0.25,sin(angulo)*0.4-0.15,0.0)
        glEnd()
    if faro > 1 and faro < 2:
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1.0,0.0,0.0)
        glVertex3f(0.25,-0.15,0.0)
        for x in range(361):
            angulo = x * 3.14159 / 180.0
            glColor3f(0.3,0.0,0.0)
            glVertex3f(cos(angulo)*0.4+0.25,sin(angulo)*0.4-0.15,0.0)
        glEnd()
    glPopMatrix()

def dibujarInterfazDano():
    global Dano
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
    if Dano > -1 and Dano < 10:
        glColor3f(0.0,1.0,0.0)
    if Dano > 9 and Dano < 20:
        glColor3f(0.4,1.0,0.0)
    if Dano > 19 and Dano < 30:
        glColor3f(0.6,1.0,0.0)
    
    if Dano > 29 and Dano < 40:
        glColor3f(0.8,1.0,0.0)
    if Dano > 39 and Dano < 50:
        glColor3f(1.0,1.0,0.0)
    if Dano > 49 and Dano < 60:
        glColor3f(1.0,0.8,0.0)

    if Dano > 59 and Dano < 70:
        glColor3f(1.0,0.6,0.0)
    if Dano > 69 and Dano < 80:
        glColor3f(1.0,0.4,0.0)
    if Dano > 79 and Dano < 90:
        glColor3f(1.0,0.2,0.0)

    if Dano > 89 and Dano < 100:
        glColor3f(1.0,0.0,0.0)
    if Dano > 99 and Dano < 110:
        glColor3f(0.6,0.0,0.0)
    if Dano > 109 and Dano < 120:
        glColor3f(0.3,0.0,0.0)

    if Dano >= 120:
        glColor3f(0.0,0.0,0.0)


    glBegin(GL_QUADS)
    glVertex2f(-1,1)
    glVertex2f(1,1)
    glVertex2f(1,-1)
    glVertex2f(-1,-1)
    glEnd()
    glPopMatrix()

def dibujar():
    dibujarCarretera()
    dibujarObstaculos()
    dibujarCarros()
    dibujarPolicia()
    dibujarJugador()
    dibujarInterfazDano()

def key_callback(window, key, scancode, action, mods):
    global psX_jugador
    global psY_jugador
    
    #Escape
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, 1)
    
    if action == glfw.PRESS or action == glfw.REPEAT:
        #MovX
        if key == glfw.KEY_LEFT:
            psX_jugador = psX_jugador - 0.05
        if key == glfw.KEY_RIGHT:
            psX_jugador = psX_jugador + 0.05
    
        #MovY
        if key == glfw.KEY_UP:
            psY_jugador = psY_jugador + 0.05
        if key == glfw.KEY_DOWN:
            psY_jugador = psY_jugador - 0.05

def main():
    global tiempo
    global tiempoAnterior
    global gameOver
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(1000,1000,"Policia Escape Carro Choques Persecucion Juego", None, None)
    glfw.set_window_pos(window,450,35)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)

    #Establecer callback de evento de teclado
    #glfw.set_key_callback(window, key_callback)
    tiempo = glfw.get_time()
    tiempoAnterior = glfw.get_time()
    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,1000,1000)
        #Establece color de borrado
        glClearColor(0.05,0.2,0.1,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Actualizar valores de la app
        actualizar(window)
        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()