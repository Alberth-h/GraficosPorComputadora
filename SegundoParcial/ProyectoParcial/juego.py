from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import math
import random
import sys
import playsound

from Jugador import *
from Policia import *

from Carretera import *
from Obstaculos import *
from Vehiculos import *

from Interfaz import *

#Jugador
jugador = Jugador()

#Policia
policia = Policia()

#Carretera
tramo = Tramo(0.0, 0.0)
tramoAux = Tramo(0.0, 2.0)
calleTrans = CalleTrans()
caminoTrans = CaminoTrans()

#Obstaculos
cono = Cono()
barril = Barril()
ponLlan = PonLlan()
barrera = Barrera()

#Vehiculos
carro1 = Carro1()
carro2 = Carro2()
carro3 = Carro3()
carro4 = Carro4()
carro5 = Carro5()
vaca = Vaca()

#Interfaz
interfaz = Interfaz()

#Tiempo y velocidades
tiempo = 0.0
tiempoAnterior = 0.0

#Musica y sonido
playsound.playsound('song.mp3', False)
playsound.playsound('siren.mp3', False)

def actualizar(window):
    global tiempo
    global tiempoAnterior
    global jugador
    global policia
    global tramo
    global tramoAux
    global calleTrans
    global caminoTrans
    global cono
    global barril
    global ponLlan
    global barrera
    global carro1 
    global carro2
    global carro3
    global carro4
    global carro5
    global vaca

    #Tiempo
    tiempo = glfw.get_time()
    deltatime = tiempo - tiempoAnterior

    #Jugador
    jugador.actualizar_movimiento(window, deltatime)
    jugador.actualizar_dano(deltatime, tiempo, policia, tramo, tramoAux, calleTrans, caminoTrans, cono, barril, ponLlan, barrera, carro5, vaca)
    jugador.colisiones(tiempo, policia, cono, barril, ponLlan, barrera, carro1, carro2, carro3, carro4, carro5, vaca)

    #Policia
    policia.actualizar_retroceso(deltatime, cono, barril, ponLlan, barrera, carro1, carro2, carro3, carro4, carro5, vaca, jugador)
    policia.actualizar_faro(deltatime)

    #Carretera
    tramo.actualizar(deltatime)
    tramoAux.actualizar(deltatime)
    calleTrans.actualizar(deltatime)
    caminoTrans.actualizar(deltatime)

    #Obstaculos
    cono.actualizar(deltatime)
    barril.actualizar(deltatime)
    ponLlan.actualizar(deltatime)
    barrera.actualizar(deltatime)

    #Vehiculos
    carro1.actualizar(deltatime)
    carro2.actualizar(deltatime)
    carro3.actualizar(deltatime)
    carro4.actualizar(deltatime)
    carro5.actualizar(deltatime, calleTrans)
    vaca.actualizar(deltatime, caminoTrans)

    tiempoAnterior = tiempo

def dibujar():
    global jugador
    global policia
    global tramo
    global tramoAux
    global calleTrans
    global caminoTrans
    global cono
    global barril
    global ponLlan
    global barrera
    global carro1 
    global carro2
    global carro3
    global carro4
    global carro5
    global vaca
    global interfaz
    #Carretera
    caminoTrans.dibujar()
    tramo.dibujar()
    tramoAux.dibujar()
    calleTrans.dibujar()

    #Obstaculos
    cono.dibujar()
    barril.dibujar()
    ponLlan.dibujar()
    barrera.dibujar()

    #Vehiculos
    carro1.dibujar()
    carro2.dibujar()
    carro3.dibujar()
    carro4.dibujar()
    carro5.dibujar()
    vaca.dibujar()

    #Policia
    policia.dibujar()

    #Jugador
    jugador.dibujar()

    #Interfaz
    interfaz.dibujar(jugador)

def main():
    global tiempo
    global tiempoAnterior
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