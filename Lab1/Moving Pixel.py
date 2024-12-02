from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

W_Width, W_Height = 500, 500
speed = 1
ball_size = 5  
create_pixels = [] 
freeze =  False 
freeze_count = []




def draw_points(x, y, s, r=1.0, g=1.0, b=1.0):
    glPointSize(s)  
    glBegin(GL_POINTS)
    glColor3f(r, g, b)
    glVertex2f(x, y)  
    glEnd()


def mouseListener(button, state, x, y):
    global create_pixels
    global freeze
    if freeze==False:
        if button == GLUT_RIGHT_BUTTON:
            if state == GLUT_DOWN:
            
                x1 = (x / W_Width) * 2 - 1   
                y1 = -((y / W_Height) * 2 - 1)  

                dx = random.choice([-0.001,0.001])
                dy = random.choice([-0.001,0.001])

                r = random.random()
                g = random.random()
                b = random.random()

                
                create_pixels.append([x1, y1,dx,dy, r, g, b])
                print(f"Created pixel at ({x1:.2f}, {y1:.2f}) with color ({r:.2f}, {g:.2f}, {b:.2f})")

        if button == GLUT_LEFT_BUTTON:
            if state == GLUT_DOWN: 
                glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
                glClearColor(0,0,0,0)
                glutSwapBuffers()
                time.sleep(0.1)
                print('Blinked!!')

    glutPostRedisplay()



def keyboardListener(key,x,y):
    global freeze
    global freeze_count
    if key == b' ':
        freeze_count.append('freeze!!')

    if len(freeze_count) == 1:
        print("Freeze!!")
        freeze = True
    else:
        print('Unfreeze!!')
        freeze = False
        freeze_count.clear()
    




def specialKeyListener(key,x,y):
    global speed
    global freeze

    if freeze==False:
        if speed<10:
            if key == GLUT_KEY_UP:
                speed += 0.3
                print('Speed Up!!')
        if speed>1:
            if key == GLUT_KEY_DOWN:
                speed -= 0.3
                print('Speed Down!!')
    else:
        pass
    glutPostRedisplay()



def update_points():
    global create_pixels,speed
    global freeze

    for pixel in create_pixels:
        if freeze == False:
            pixel[0] += pixel[2]*speed
            pixel[1] += pixel[3]*speed

            if pixel[0]>=1 or pixel[0]<=-1:
                pixel[2] *= -1
            if pixel[1]>=1 or pixel[1]<=-1:
                pixel[3] *=-1
        else:
            pass
    glutPostRedisplay()


def showScreen():
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)  
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    
    for x, y,dx,dy, r, g, b in create_pixels:
        draw_points(x, y, ball_size, r, g, b)

    glutSwapBuffers()


def init():
    
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1) 

def animation():
    update_points()
    glutPostRedisplay()


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)

# Create the window
glutCreateWindow(b"Moving points")
init()

# Register the callback functions
glutDisplayFunc(showScreen)
glutIdleFunc(update_points)
glutMouseFunc(mouseListener)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)
glutIdleFunc(animation)
# Start the main loop
glutMainLoop()
