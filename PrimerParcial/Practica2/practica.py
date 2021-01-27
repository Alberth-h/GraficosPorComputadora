from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

def dibujarcielo():
    glBegin(GL_QUADS)
    glColor3f(0.0,0.8,1.0)
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(1.0,1.0,0.0)
    glColor3f(0.9,0.7,0.2)
    glVertex3f(1.0,-1.0,0.0)
    glVertex3f(-1.0,-1.0,0.0)
    glEnd()

def dibujartierra():
    glColor3f(0.8,0.4,0.1)
    glBegin(GL_QUADS)
    glVertex3f(-1.0,-0.7,0.0)
    glVertex3f(1.0,-0.7,0.0)
    glVertex3f(1.0,-1.0,0.0)
    glVertex3f(-1.0,-1.0,0.0)

    glColor3f(0.8,1.0,0.1)
    glVertex3f(-1.0,-0.7,0.0)
    glVertex3f(1.0,-0.7,0.0)
    glVertex3f(1.0,-0.9,0.0)
    glVertex3f(-1.0,-0.9,0.0)
    glEnd()

def dibujarsol():
    glColor3f(1.0,0.4,0.2)
    glBegin(GL_TRIANGLE_STRIP)
    for x in range(500):
        x = x + 1
        if x % 3 == 0:
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo) * 0.3 - 0.6,sin(angulo) * 0.3 - 0.4,0.0)
        else:
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo) * 0.15 - 0.6,sin(angulo) * 0.15 - 0.4,0.0)
    glEnd()

    glColor3f(1.0,0.8,0.2)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.15 - 0.6,sin(angulo) * 0.15 - 0.4,0.0)
    glEnd()

def dibujarnubes():
    glColor3f(1.0,1.0,1.0)

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.25 + 0.6,sin(angulo) * 0.1 + 0.4,0.0)
    glEnd()
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.25 + 0.4,sin(angulo) * 0.1 + 0.35,0.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.25 - 0.4,sin(angulo) * 0.1 + 0.2,0.0)
    glEnd()
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.25 - 0.6,sin(angulo) * 0.1 + 0.15,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.25 - 0.1,sin(angulo) * 0.1 + 0.5,0.0)
    glEnd()
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.25 - 0.3,sin(angulo) * 0.1 + 0.45,0.0)
    glEnd()

def dibujararbol():
    glColor3f(0.5,0.2,0.0)
    glBegin(GL_QUADS)
    glVertex3f(-0.1,-0.8,0.0)
    glVertex3f(-0.1,-0.6,0.0)
    glVertex3f(-0.05,-0.6,0.0)
    glVertex3f(-0.05,-0.8,0.0)
    glEnd()

    glColor3f(0.5,0.7,0.0)
    glBegin(GL_POLYGON)
    glVertex3f(-0.2,-0.7,0.0)
    glVertex3f(-0.25,-0.5,0.0)
    glVertex3f(-0.075,-0.2,0.0)
    glVertex3f(0.075,-0.5,0.0)
    glVertex3f(0.05,-0.7,0.0)
    glEnd()    

def dibujarcasa():
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex3f(0.4,-0.8,0.0)
    glVertex3f(0.4,-0.6,0.0)
    glVertex3f(0.51,-0.42,0.0)
    glVertex3f(0.64,-0.6,0.0)
    glVertex3f(0.9,-0.6,0.0)
    glVertex3f(0.9,-0.8,0.0)
    glEnd()

    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex3f(0.4,-0.6,0.0)
    glVertex3f(0.39,-0.6,0.0)
    glVertex3f(0.51,-0.41,0.0)
    glVertex3f(0.79,-0.41,0.0)
    glVertex3f(0.91,-0.6,0.0)
    glEnd()

    glColor3f(1.0,1.0,1.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(0.4,-0.6,0.0)
    glVertex3f(0.51,-0.42,0.0)
    glVertex3f(0.64,-0.6,0.0)
    glEnd() 

    glColor3f(0.5,1.0,1.0)
    glBegin(GL_QUADS)
    glVertex3f(0.47,-0.75,0.0)
    glVertex3f(0.47,-0.63,0.0)
    glVertex3f(0.57,-0.63,0.0)
    glVertex3f(0.57,-0.75,0.0)
    glEnd()

    glColor3f(1.0,0.9,0.8)
    glBegin(GL_QUADS)
    glVertex3f(0.73,-0.8,0.0)
    glVertex3f(0.73,-0.66,0.0)
    glVertex3f(0.81,-0.66,0.0)
    glVertex3f(0.81,-0.8,0.0)
    glEnd()

    glColor3f(0.0,0.0,0.0)
    glBegin(GL_QUADS)
    glVertex3f(0.79,-0.75,0.0)
    glVertex3f(0.79,-0.74,0.0)
    glVertex3f(0.81,-0.74,0.0)
    glVertex3f(0.81,-0.75,0.0)
    glEnd()


def dibujar():
    #rutinas de dibujo
    dibujarcielo()
    dibujarsol()
    dibujartierra()
    dibujarnubes()
    dibujararbol()
    dibujarcasa()

def main():
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

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,800,800)
        #Establece color de borrado
        glClearColor(0.0,0.0,0.0,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

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