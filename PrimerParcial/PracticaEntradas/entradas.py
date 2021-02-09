from OpenGL.GL import *
from glew_wish import *
import glfw

posX_triangle = 0
posY_triangle = 0

tiempo = 0.0
tiempoAnterior = 0.0
velocidad = 1.0

def actualizar(window):
    global tiempo
    global tiempoAnterior
    global velocidad
    global posX_triangle
    global posY_triangle

    tiempo = glfw.get_time()
    deltatime = tiempo - tiempoAnterior
    movimiento = velocidad * deltatime

    estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)
    estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estado_tecla_abajo = glfw.get_key(window, glfw.KEY_DOWN)
    estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)

    if estado_tecla_izquierda == glfw.PRESS:
        posX_triangle = posX_triangle - movimiento
    if estado_tecla_derecha == glfw.PRESS:
        posX_triangle = posX_triangle + movimiento
    if estado_tecla_abajo == glfw.PRESS:
        posY_triangle = posY_triangle - movimiento
    if estado_tecla_arriba == glfw.PRESS:
        posY_triangle = posY_triangle + movimiento

    tiempoAnterior = tiempo

def dibujar():
    global posX_triangle
    global posY_triangle
    #rutinas de dibujo
    glPushMatrix()
    glTranslate(posX_triangle, posY_triangle, 0)
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLES)
    
    glVertex3f(0,0.1,0)
    glVertex3f(-0.1,-0.1,0)
    glVertex3f(0.1,-0.1,0)

    glEnd()
    glPopMatrix()

def key_callback(window, key, scancode, action, mods):
    #Press, release, repeat
    #if key == glfw.KEY_ESCAPE:
    #    if action == glfw.PRESS:
    #        print("Se detecto un press de la tecla escape")
    #    if action == glfw.RELEASE:
    #        print("Se detecto un release de la tecla escape")
    #    if action == glfw.REPEAT:
    #        print("Se detecto un repeatc de la tecla escape")
    global posX_triangle
    global posY_triangle
    
    #Escape
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, 1)
    
    if action == glfw.PRESS or action == glfw.REPEAT:
        #MovX
        if key == glfw.KEY_LEFT:
            posX_triangle = posX_triangle - 0.05
        if key == glfw.KEY_RIGHT:
            posX_triangle = posX_triangle + 0.05
    
        #MovY
        if key == glfw.KEY_UP:
            posY_triangle = posY_triangle + 0.05
        if key == glfw.KEY_DOWN:
            posY_triangle = posY_triangle - 0.05

def main():
    global tiempo
    global tiempoAnterior
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(800,800,"Mi ventana", None, None)

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
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    #Establecer callback de evento de teclado
    #glfw.set_key_callback(window, key_callback)
    tiempo = glfw.get_time()
    tiempoAnterior = glfw.get_time()
    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,800,800)
        #Establece color de borrado
        glClearColor(0.4,0.8,0.1,1)
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