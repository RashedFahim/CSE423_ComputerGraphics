from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

rain_speed = 0.1
raindrop = []
direction = 0.0
r,g,b = 0.0,0.0,0.0

def createrain(x,y):
    global direction
    if r<=0.9 and g<=0.9 and b<=0.9:
        glColor3f(1,1,1)
    else:
        glColor3f(0,0,0)

    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex2d(x,y)
    glVertex2d(x+direction,y-20)
    glEnd()

def update_raindrops():
    global direction
    global rain_drop
    for i in range(0,len(raindrop)):
        x,y = raindrop[i]
        x1 = x
        y1 = y-rain_speed
        if y1<0:
            y1 = 500
        if 100<x1<400 and 100<y1<270:
            y1 = 500
        raindrop[i] = (x1,y1)


def specialKeyListener(key,x,y):
    global direction 
    global rain_speed
    if direction<15:
        if key==GLUT_KEY_RIGHT:
            direction +=0.5
            print('Right Key Pressed')
    if direction>-15:
        if key==GLUT_KEY_LEFT:
            direction -= 0.5
            print('Left key pressed')
    
    if key==GLUT_KEY_DOWN:
        if rain_speed>0.2:
            rain_speed-=0.1
            print("Speed Down")

    if rain_speed<5:
        if key==GLUT_KEY_UP:
            rain_speed+=0.1
            print("Speed Up")
    glutPostRedisplay()


def keyBoardListener(key, x, y):
    global r,g,b
    if key==b'd':
        r = min(1.0,r+0.1)
        g = min(1.0,g+0.1)
        b = min(1.0,b+0.1)
        glClearColor(r,g,b,1.0)
        print('Shifting to Day')
        print(f'{r},{g},{b}')
    if key==b'n':
        r = max(0.0,r-0.1)
        g = max(0.0,g-0.1)
        b = max(0.0,b-0.1)
        glClearColor(r,g,b,1.0)
        print('Shifting to Night')
        print(f'{r},{g},{b}')
    glutPostRedisplay()




def DrawHouse():
    if r<=0.9 and g<=0.9 and b<=0.9:
        glColor3f(1,1,1)
    else:
        glColor3f(0,0,0)

    # Creating the Roof
    glBegin(GL_TRIANGLES)
    glVertex2d(100,250)
    glVertex2d(250,350)
    glVertex2d(400,250)
    glEnd()

    # Creating the walls
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2d(100,100)
    glVertex2d(400,100)
    glVertex2d(100,100)
    glVertex2d(100,250)
    glVertex2d(400,100)
    glVertex2d(400,250)
    glEnd()

    #Creating Door
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2d(210,200)
    glVertex2d(270,200)
    glVertex2d(210,200)
    glVertex2d(210,100)
    glVertex2d(270,200)
    glVertex2d(270,100)
    glEnd()
    glPointSize(4)
    glBegin(GL_POINTS)
    glVertex2d(260,150)
    glEnd()



def animation():
    update_raindrops()
    glutPostRedisplay()




def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    DrawHouse()
    for i in raindrop:
        createrain(i[0],i[1])

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"House and Rain") #window name
glutDisplayFunc(showScreen)
glutIdleFunc(animation)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyBoardListener)
glClearColor(r,g,b,1.0)

for i in range(200):
    x1 = random.uniform(0,500)
    y1 = random.uniform(0,500)
    raindrop.append((x1,y1))


glutMainLoop()