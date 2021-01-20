from OpenGL.GL import *
from glew_wish import *
import glfw
from random import random

def main():
    #Inicia glfw
    if not glfw.init():
        return

    #Crea la ventana, independiente de SO que usemos
    window = glfw.create_window(800, 600, "ventana", None, None)
    
    #Configuramos OpenGl
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return

    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activar la validacion de funciones modernas de OpenGl
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y SHaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version)

    while not glfw.window_should_close(window):
        #Establece region de dibujo
        glViewport(0,0,800,600)
        #Establece color de borrado
        #glClearColor(1,0,0,1)
        red = random()
        green = random()
        blue = random()

        color = glClearColor(red,green,blue,1)

        #Borra el contenido de la venta
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #DIbujar

        #Preguntar si hubo entradas de perofericos
        #(Teclado, mous, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inicio glfw.init
    glfw.terminate()

#emular el main de c++
if __name__ == "__main__":
    main()