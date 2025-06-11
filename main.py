import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from math import sin, cos, radians

Keys = {"Up": False, "Down": False, "Left": False, "Right": False, "W": False, "S": False}

PosicaoCamera = [0.0, 0.0, 40.0]
LookAtCamera  = [ 0.0, 0.0, 0.0]

def key_callback(window, key, scancode, action, mods):
    # atualiza o dicionário quando tecla é pressionada ou solta
    if key == glfw.KEY_UP:
        Keys["Up"] = (action == glfw.PRESS or action == glfw.REPEAT)
    elif key == glfw.KEY_DOWN:
        Keys["Down"] = (action == glfw.PRESS or action == glfw.REPEAT)
    elif key == glfw.KEY_LEFT:
        Keys["Left"] = (action == glfw.PRESS or action == glfw.REPEAT)
    elif key == glfw.KEY_RIGHT:
        Keys["Right"] = (action == glfw.PRESS or action == glfw.REPEAT)
    elif key == glfw.KEY_W:
        Keys["W"] = (action == glfw.PRESS or action == glfw.REPEAT)
    elif key == glfw.KEY_S:
        Keys["S"] = (action == glfw.PRESS or action == glfw.REPEAT)  

def init():
    glClearColor(0.4,0.4,1,1)
    glEnable(GL_DEPTH_TEST)

    # Projeção
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 1.0, 0.1, 500.0)
    glMatrixMode(GL_MODELVIEW)

def desenharCubo(cor):
    glBegin(GL_TRIANGLE_STRIP)
    glColor3fv(cor)
    glVertex3f(-0.5,-0.5,0)
    glVertex3f( 0.5,-0.5,0)
    glVertex3f(-0.5, 0.5,0)
    glVertex3f( 0.5, 0.5,0)
    glEnd()
    glBegin(GL_TRIANGLE_STRIP)
    glColor3fv(cor)
    glVertex3f(-0.5,-0.5,1)
    glVertex3f( 0.5,-0.5,1)
    glVertex3f(-0.5, 0.5,1)
    glVertex3f( 0.5, 0.5,1)
    glEnd()
    glBegin(GL_TRIANGLE_STRIP)
    glColor3fv(cor)
    glVertex3f(0.5, -0.5,0)
    glVertex3f(0.5, 0.5,0)
    glVertex3f(0.5, -0.5,1)
    glVertex3f(0.5, 0.5,1)
    glEnd()
    glBegin(GL_TRIANGLE_STRIP)
    glColor3fv(cor)
    glVertex3f(-0.5, -0.5,0)
    glVertex3f(-0.5, 0.5,0)
    glVertex3f(-0.5, -0.5,1)
    glVertex3f(-0.5, 0.5,1)
    glEnd()
    glBegin(GL_TRIANGLE_STRIP)
    glColor3fv(cor)
    glVertex3f(-0.5,  0.5,0)
    glVertex3f( 0.5,  0.5,0)
    glVertex3f(-0.5,  0.5,1)
    glVertex3f( 0.5,  0.5,1)
    glEnd()
    glBegin(GL_TRIANGLE_STRIP)
    glColor3fv(cor)
    glVertex3f(-0.5, -0.5,0)
    glVertex3f( 0.5, -0.5,0)
    glVertex3f(-0.5, -0.5,1)
    glVertex3f( 0.5, -0.5,1)
    glEnd()

def desenharLinha():
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex3f(-100,0,0)
    glVertex3f(100,0,0)
    glEnd()
    
    glBegin(GL_LINES)
    glColor3f(0,1,0)
    glVertex3f(0,-100,0)
    glVertex3f(0,100,0)
    glEnd()
    
    glBegin(GL_LINES)
    glColor3f(0,0,1)
    glVertex3f(0,0,-100)
    glVertex3f(0,0,100)
    glEnd()

def update(window):
    if Keys["Up"]:
        PosicaoCamera[0] += 0.2
        LookAtCamera[0] += 0.2
        
    if Keys["Down"]:
        PosicaoCamera[0] -= 0.2
        LookAtCamera[0] -= 0.2
        
    if Keys["Right"]:
        PosicaoCamera[1] += 0.2
        LookAtCamera[1] += 0.2
        
    if Keys["Left"]:
        PosicaoCamera[1] -= 0.2
        LookAtCamera[1] -= 0.2
        
    if Keys["W"]:
        PosicaoCamera[2] += 0.2
        LookAtCamera[2] += 0.2
        
    if Keys["S"]:
        PosicaoCamera[2] -= 0.2
        LookAtCamera[2] -= 0.2
        
def mesa():
    #centro do centro da mesa
    glPushMatrix()
    glTranslate(0,6,1.5)
    glRotate(90,1,0,0)
    glScale(0.5,0.5,12)
    desenharCubo([0,0,0])
    glPopMatrix()
    
    #centro do centro do centro da mesa mais a esquerda
    glPushMatrix()
    glTranslate(0,-6,1.5)
    glRotate(-90,0,1,0)
    glScale(0.5,0.5,5)
    desenharCubo([0,0,0])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(0,-6,1.5)
    glRotate(-90,0,1,0)
    glScale(0.5,0.5,-5)
    desenharCubo([0,0,0])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(0,-2,1.5)
    glRotate(-90,0,1,0)
    glScale(0.5,0.5,5)
    desenharCubo([0,0,0])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(0,-2,1.5)
    glRotate(-90,0,1,0)
    glScale(0.5,0.5,-5)
    desenharCubo([0,0,0])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(0,2,1.5)
    glRotate(-90,0,1,0)
    glScale(0.5,0.5,5)
    desenharCubo([0,0,0])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(0,2,1.5)
    glRotate(-90,0,1,0)
    glScale(0.5,0.5,-5)
    desenharCubo([0,0,0])
    glPopMatrix()
    #bancos
    
    glPushMatrix()
    glTranslate(0,6,1.5)
    glRotate(-90,0,1,0)
    glScale(0.5,0.5,5)
    desenharCubo([0,0,0])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(0,6,1.5)
    glRotate(-90,0,1,0)
    glScale(0.5,0.5,-5)
    desenharCubo([0,0,0])
    glPopMatrix()
    
    #apoios da mesa
    glPushMatrix()
    glTranslate(0,-6,1.5)
    glScale(0.5,0.5,3)
    desenharCubo([0,0,0])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(0,-2,1.5)
    glScale(0.5,0.5,3)
    desenharCubo([0,0,0])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(0,2,1.5)
    glScale(0.5,0.5,3)
    desenharCubo([0,0,0])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(0,6,1.5)
    glScale(0.5,0.5,3)
    desenharCubo([0,0,0])
    glPopMatrix()
    
    #apoios dos acentos
    glPushMatrix()
    glTranslate(-4.75,6,0)
    glScale(0.5,0.5,2.25)
    desenharCubo([0,0,0])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(-4.75,-6,0)
    glScale(0.5,0.5,2.25)
    desenharCubo([0,0,0])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(-4.75,-2,0)
    glScale(0.5,0.5,2.25)
    desenharCubo([0,0,0])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(-4.75,2,0)
    glScale(0.5,0.5,2.25)
    desenharCubo([0,0,0])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(4.75,6,0)
    glScale(0.5,0.5,2.25)
    desenharCubo([0,0,0])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(4.75,-6,0)
    glScale(0.5,0.5,2.25)
    desenharCubo([0,0,0])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(4.75,-2,0)
    glScale(0.5,0.5,2.25)
    desenharCubo([0,0,0])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(4.75,2,0)
    glScale(0.5,0.5,2.25)
    desenharCubo([0,0,0])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(4.75,2,2.25)
    glScale(2,2,0.25)
    desenharCubo([0.7,0.7,0.7])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(4.75,-2,2.25)
    glScale(2,2,0.25)
    desenharCubo([0.7,0.7,0.7])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(4.75,6,2.25)
    glScale(2,2,0.25)
    desenharCubo([0.7,0.7,0.7])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(4.75,-6,2.25)
    glScale(2,2,0.25)
    desenharCubo([0.7,0.7,0.7])
    glPopMatrix()

    glPushMatrix()
    glTranslate(-4.75,2,2.25)
    glScale(2,2,0.25)
    desenharCubo([0.7,0.7,0.7])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(-4.75,-2,2.25)
    glScale(2,2,0.25)
    desenharCubo([0.7,0.7,0.7])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(-4.75,6,2.25)
    glScale(2,2,0.25)
    desenharCubo([0.7,0.7,0.7])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(-4.75,-6,2.25)
    glScale(2,2,0.25)
    desenharCubo([0.7,0.7,0.7])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(0,0,4.5)
    glScale(8,16,0.25)
    desenharCubo([0.7,0.7,0.7])
    glPopMatrix()

def blocoDaJanela():
    glPushMatrix()
    glTranslate(0,-5.80,0)
    glScale(0.2,0.4,4)
    desenharCubo([0.6,0.6,0.6])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(0,6,0)
    glRotate(90,1,0,0)
    glScale(0.2,0.4,12)
    desenharCubo([0.6,0.6,0.6])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(0,5.80,0)
    glScale(0.2,0.4,4)
    desenharCubo([0.6,0.6,0.6])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(0,6,4)
    glRotate(90,1,0,0)
    glScale(0.2,0.4,12)
    desenharCubo([0.6,0.6,0.6])
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(0.1,6,-0.3)
    glRotate(90,1,0,0)
    glScale(0.1,0.5,12)
    desenharCubo([0.57,0.57,0.57])
    glPopMatrix()

def linhaDaJanela(jan1 = False, jan2 = False, jan3 = False):
    glPushMatrix()
    glTranslate(0,-6.3,-0.5)
    glScale(0.2,0.6,4.7)
    desenharCubo([0.57,0.57,0.57])
    glPopMatrix()
    
    if jan1:
        glPushMatrix()
        glTranslate(0.5,0,0.25)
        glRotate(-25,0,1,0)
        blocoDaJanela()
        glPopMatrix()
    else:
        glPushMatrix()
        blocoDaJanela()
        glPopMatrix()
    
    glPushMatrix()
    glTranslate(0,6.2,-0.5)
    glScale(0.2,0.6,4.7)
    desenharCubo([0.57,0.57,0.57])
    glPopMatrix()
    
    if jan2:
        glPushMatrix()
        glTranslate(0.5,12.5,0.25)
        glRotate(-25,0,1,0)
        blocoDaJanela()
        glPopMatrix()
    else:
        glPushMatrix()
        glTranslate(0,12.5,0)
        blocoDaJanela()
        glPopMatrix()
    
    glPushMatrix()
    glTranslate(0,18.7,-0.5)
    glScale(0.2,0.6,4.7)
    desenharCubo([0.57,0.57,0.57])
    glPopMatrix()
    
    if jan3:
        glPushMatrix()
        glTranslate(0.5,25,0.25)
        glRotate(-25,0,1,0)
        blocoDaJanela()
        glPopMatrix()
    else:
        glPushMatrix()
        glTranslate(0,25,0)
        blocoDaJanela()
        glPopMatrix()
        
    glPushMatrix()
    glTranslate(0,31.2,-0.5)
    glScale(0.2,0.6,4.7)
    desenharCubo([0.57,0.57,0.57])
    glPopMatrix()
    
def janela():
    glPushMatrix()
    glTranslatef(0,12.5,-0.5)
    glScalef(0.2,37.5,0.6)
    desenharCubo([0.57,0.57,0.57])
    glPopMatrix()
    glPushMatrix()
    linhaDaJanela(0,0,0)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0,0,4.5)
    linhaDaJanela(1,1,1)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0,0,9)
    linhaDaJanela(1,1,1)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0,0,13.5)
    linhaDaJanela(1,1,1)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0,0,18)
    linhaDaJanela(1,1,1)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0,0,22.5)
    linhaDaJanela(0,0,0)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0,12.4,26.7)
    glScalef(0.2,38.1,0.6)
    desenharCubo([0.57,0.57,0.57])
    glPopMatrix()
  
def mureta():
    glPushMatrix()
    glScalef(1,15,3)
    desenharCubo([0.9,0.9,0.9])
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0,0,3)
    glScalef(2,15,0.25)
    desenharCubo([0.2,0.2,0.2])
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0,7.7,3)
    glScalef(2,0.5,0.25)
    desenharCubo([0.2,0.2,0.2])
    glPopMatrix()
  
def piso():
    glColor3fv([0.3,0.3,0.3])
    glBegin(GL_TRIANGLE_FAN)
    glVertex(0.5,0.5,0)
    glVertex(0.5,-0.5,0)
    glVertex(-0.5,-0.5,0)
    glVertex(-0.5,0.5,0)
    glEnd()
    
    glColor3fv([1,1,1])
    glLineWidth(2.0)
    glBegin(GL_LINE_LOOP)
    glVertex(0.5,0.5,0)
    glVertex(0.5,-0.5,0)
    glVertex(-0.5,-0.5,0)
    glVertex(-0.5,0.5,0)
    glEnd()
    
def paredeLateral():
      
    glPushMatrix()
    glScale(2.5,5,37.5)
    desenharCubo([1,1,1])
    glPopMatrix()
    glPushMatrix()
    glTranslate(0,17.5,0)
    glScale(2.5,31,11.75)
    desenharCubo([1,1,1])
    glPopMatrix()
    glPushMatrix()
    glTranslate(0,35.5,0)
    glScale(2.5,5,37.5)
    desenharCubo([1,1,1])
    glPopMatrix()
    glPushMatrix()
    glTranslate(0,17.5,34.08)
    glScalef(2.5,31,3.42)
    desenharCubo([1,1,1])
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0,7.8,12.24)
    glScalef(0.8,0.8,0.8)
    janela()
    glPopMatrix()
  
def render():
    global PosicaoCamera, LookAtCamera
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(PosicaoCamera[0], PosicaoCamera[1], PosicaoCamera[2],
              LookAtCamera[0], LookAtCamera[1], LookAtCamera[2],
              1, 0, 0)
    
    glPushMatrix()
    desenharLinha()
    glPopMatrix()
    
    x = 9
    y = 3
    for i in range(20):
        glPushMatrix()
        glTranslate(x,y,0)
        glScale(10,10,1)
        piso()
        glPopMatrix()
        
        if x % 19 != 0:
            x+=10
        else:
            x = 9
            y += 10
    # glPushMatrix()
    # glTranslate(9,3,0)
    # glScale(10,10,1)
    # piso()
    # glPopMatrix()
    
    # glPushMatrix()
    # glTranslate(19,3,0)
    # glScale(10,10,1)
    # piso()
    # glPopMatrix()
    
    # glPushMatrix()
    # glTranslate(7,16,0)
    # glScale(12,12,1)
    # piso()
    # glPopMatrix()
    
    # glPushMatrix()
    # glTranslate(16,1,0)
    # glScale(6,6,1)
    # piso()
    # glPopMatrix()
    # glPushMatrix()
    # glTranslate(4,7,0)
    # glScale(6,6,1)
    # piso()
    # glPopMatrix()
    
    # glPushMatrix()
    # glTranslate(35,0,0)
    # mesa()
    # glPopMatrix()
    
    glPushMatrix()
    glScale(0.8,0.8,0.8)
    paredeLateral()
    glPopMatrix()
    
    # glPushMatrix()
    # glTranslatef(-15,0,0)
    # glScale(1,1,3)
    # mureta()
    # glPopMatrix()
    
    
def main():
    glfw.init()
    jan = glfw.create_window(700,700,"Câmera",None,None)
    glfw.make_context_current(jan)
    
    glfw.set_key_callback(jan, key_callback)
    init()

    while not glfw.window_should_close(jan):
        glfw.poll_events()
        
        update(jan)
        
        render()
        glfw.swap_buffers(jan)

    glfw.terminate()

if __name__ == "__main__":
    main()
