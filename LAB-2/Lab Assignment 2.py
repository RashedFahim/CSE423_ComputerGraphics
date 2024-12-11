from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time
import math



spaceship_speed = 0.001
spaceship_x = 0
bullet_y = -205
enemy_x, enemy_y = random.randint(-150, 200), 300

bullet_speed = 3
score = 0
player_lives = 3


bullets = []
enemies = []


bullet_shot_flag = False
spaceship_left_flag = False 
spaceship_right_flag = False
game_over_flag = False
play_button_flag = False
cross_button_flag = False
restart_button_flag = False
heart1_flag = False
heart2_flag = False
heart3_flag = False




def drawpoints(x,y,size = 2):
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()




def FindZone(x0,y0,x1,y1):
    dx = x1-x0
    dy = y1-y0
    zone = -1

    if abs(dx)>abs(dy):
        if dx>0 and dy>0:
            zone = 0
        elif dx<0 and dy>0:
            zone=3
        elif dx<0 and dy<0:
            zone=4
        else:
            zone=7
    else:
        if dx>0 and dy>0:
            zone=1
        elif dx<0 and dy>0:
            zone=2
        elif dx<0 and dy<0:
            zone=5 
        else:
            zone=6
    return zone




def convert_to_zone0(original_zone,x,y) :


    if (original_zone == 0) :
        return x,y
    elif (original_zone == 1) :
        return y,x
    elif (original_zone == 2) :
        return -y,x
    elif (original_zone == 3) :
        return -x,y
    elif (original_zone == 4) :
        return -x,-y
    elif (original_zone == 5) :
        return -y,-x
    elif (original_zone == 6) :
        return -y,x
    elif (original_zone == 7) :
        return x,-y
    



def convert_to_originalzone(originalzone,x,y):
    if originalzone == 0:
        return x,y
    elif originalzone == 1:
        return y,x
    elif originalzone == 2:
        return -y,-x
    elif originalzone == 3:
        return -x,y
    elif originalzone == 4:
        return -x,-y
    elif originalzone == 5:
        return -y,-x
    elif originalzone == 6:
        return y,-x
    elif originalzone == 7:
        return x,-y




def MidpointLine(zone,x0,y0,x1,y1):
    dx = x1-x0
    dy = y1-y0
    d = 2*dy-dx
    E = 2*dy
    NE = 2*(dy-dx)
    x = x0
    y = y0
    while x<x1:
        original_x,original_y = convert_to_originalzone(zone,x,y)
        drawpoints(original_x,original_y)
        if d<=0:
            d = d+E
            x = x+1
        else:
            d = d+NE
            x = x+1
            y = y+1


def PlotCirclePoints(xc, yc, x, y):
    drawpoints(xc + x, yc + y)  
    drawpoints(xc - x, yc + y) 
    drawpoints(xc + x, yc - y)  
    drawpoints(xc - x, yc - y)  
    drawpoints(xc + y, yc + x)  
    drawpoints(xc - y, yc + x)  
    drawpoints(xc + y, yc - x)  
    drawpoints(xc - y, yc - x) 


def MidpointCircle(r,xc,yc):
    d = 1-r
    x = 0
    y = r
    PlotCirclePoints(xc,yc,x,y)
    while x<y:
        if d<0:
            d = d+2*x+3
        else:
            d = d+2*x-2*y+5
            y = int(y-1)
        x+=1
        PlotCirclePoints(xc,yc,int(x),int(y))



def Eight_way_symmetry(x0,y0,x1,y1):
    if x0==x1:
        for y in range(int(min(y0, y1)), int(max(y0, y1)) + 1):
            drawpoints(x0,y)
    elif y0==y1:
        for x in range(int(min(x0, x1)), int(max(x0, x1)) + 1):
            drawpoints(x,y0)
    else:
        zone = FindZone(x0,y0,x1,y1)
        coverted_x0,converted_y0 = convert_to_zone0(zone,x0,y0)
        coverted_x1,coverted_y1 = convert_to_zone0(zone,x1,y1)
        MidpointLine(zone,coverted_x0,converted_y0,coverted_x1,coverted_y1)


#End of the Algorithms


#Buttons

def draw_play_button():
    Eight_way_symmetry(-5, 240, 15, 230) 
    Eight_way_symmetry(-5, 240, -5, 220) 
    Eight_way_symmetry(-5, 220, 15, 230) 


def draw_pause_button():
    Eight_way_symmetry(-5, 240, -5, 220)
    Eight_way_symmetry(5, 240, 5, 220)


def draw_restart_button():
    Eight_way_symmetry(-240, 230, -210, 230)
    Eight_way_symmetry(-240, 230, -220, 240)
    Eight_way_symmetry(-240, 230, -220, 220)


def draw_cross_button():
    Eight_way_symmetry(240, 240, 220, 220)
    Eight_way_symmetry(220, 240, 240, 220)


def heart1():
    glColor3f(1.0, 0.0, 0.0)
    Eight_way_symmetry(220, 180, 232, 165) 
    Eight_way_symmetry(220, 180, 226, 187)
    Eight_way_symmetry(226, 187, 232, 180)
    Eight_way_symmetry(244, 180, 238, 187)
    Eight_way_symmetry(238, 187, 232, 180)
    Eight_way_symmetry(232, 165, 244, 180)
    Eight_way_symmetry(239, 187, 244, 180)

def heart2():
    glColor3f(1.0, 0.0, 0.0)
    Eight_way_symmetry(220, 140, 232, 125) 
    Eight_way_symmetry(220, 140, 226, 147)
    Eight_way_symmetry(226, 147, 232, 140)
    Eight_way_symmetry(244, 140, 238, 147)
    Eight_way_symmetry(238, 147, 232, 140)
    Eight_way_symmetry(232, 125, 244, 140)
    Eight_way_symmetry(239, 147, 244, 140)

def heart3():
    glColor3f(1.0, 0.0, 0.0)
    Eight_way_symmetry(220, 100, 232, 85) 
    Eight_way_symmetry(220, 100, 226, 107)
    Eight_way_symmetry(226, 107, 232, 100)
    Eight_way_symmetry(244, 100, 238, 107)
    Eight_way_symmetry(238, 107, 232, 100)
    Eight_way_symmetry(232, 85, 244, 100)
    Eight_way_symmetry(239, 107, 244, 100)

















def collision(bullet, enemy):
    bullet_x, bullet_y = bullet
    curr_enemy_radius, enemy_x, enemy_y, _, is_unique, _ = enemy
    distance_from_enemy = ((bullet_x - enemy_x) ** 2 + (bullet_y - enemy_y) ** 2)

    return math.sqrt(distance_from_enemy) < curr_enemy_radius


def bullets_fire():
    global bullets, enemies, score, player_lives, play_button_flag, game_over_flag,heart1_flag,heart2_flag,heart3_flag
    new_bullets = []
    for bullet in bullets:
        bullet_hit = False
        if bullet[1] < 290:
            if not play_button_flag:
                bullet[1] += bullet_speed

            for enemy in enemies:
                if collision(bullet, enemy):
                    if enemy[4]:  # Unique enemy
                        score += 5  # Award more points
                        print("Hit unique enemy! Extra points awarded.")
                    else:
                        score += 1
                    enemies.remove(enemy)
                    bullet_hit = True
                    print("Current Score:", score)
                    break

            if not bullet_hit:
                new_bullets.append(bullet)
                MidpointCircle(8, bullet[0], bullet[1])
        else:
            if not game_over_flag:
                player_lives -= 1
                print('Remaining Lives:', player_lives)
                if player_lives == 2:
                    heart3_flag = True
                elif player_lives == 1:
                    heart2_flag = True
                elif player_lives == 0:
                    heart1_flag = True
                    game_over_flag = True
                    print("Remaining Lives: 0.\nGAME OVER")
                    print('FINAL SCORE: ', score)
                    break
            continue

    bullets[:] = new_bullets

def spaceship_move():
    global spaceship_x, play_button_flag,spaceship_speed
    if not play_button_flag:
        if spaceship_left_flag:
            spaceship_x -= spaceship_speed
        
        if spaceship_right_flag:
            spaceship_x += spaceship_speed
    

        spaceship_x = max(-230, min(230, spaceship_x)) 



def keyBoardListerner(key,x,y):
    global spaceship_x, bullet_shot_flag, spaceship_left_flag, spaceship_right_flag, play_button_flag, game_over_flag, bullet_y
    
    if not game_over_flag:
       if key == b' ':
            if not play_button_flag:
                bullets.append([spaceship_x, bullet_y])
                bullet_shot_flag = True

    if not game_over_flag:
        if key == b'a':
                spaceship_left_flag = True
                
        elif key == b'd':
                spaceship_right_flag = True



def spaceship_key_released(key, x, y):
    global bullet_shot_flag, spaceship_left_flag, spaceship_right_flag

    if key == b'a':
        spaceship_left_flag = False
    
    if key == b'd':
        spaceship_right_flag = False






def enemy():
    global enemies, play_button_flag, player_lives, game_over_flag, heart1_flag, heart2_flag, heart3_flag

    new_enemies = []
    for enemy in enemies:
        if not play_button_flag and not game_over_flag:
            enemy[2] -= enemy[3]  

            
            if enemy[4]:  
                if enemy[5] == "expand":
                    enemy[0] += 0.5  
                    if enemy[0] >= 30:  
                        enemy[5] = "shrink"
                elif enemy[5] == "shrink":
                    enemy[0] -= 0.5  
                    if enemy[0] <= 10: 
                        enemy[5] = "expand"

           
            if enemy[2] < -220:
                player_lives -= 1
                print(f"Remaining Lives: {player_lives}")
                if player_lives == 2:
                    heart3_flag = True
                elif player_lives == 1:
                    heart2_flag = True
                elif player_lives == 0:
                    heart1_flag = True
                    game_over_flag = True
                    print("Game Over!!")
                    print('FINAL SCORE: ', score)
                continue
            distance_to_spaceship = math.sqrt((spaceship_x - enemy[1])**2 + (-230 - enemy[2])**2)
            if distance_to_spaceship < enemy[0]:  
                heart1_flag = True
                heart2_flag = True
                heart3_flag = True
                game_over_flag = True
                print("Game Over!! Enemy hit the spaceship.")
                print('FINAL SCORE: ', score)
                return  
        # Draw enemy
        if enemy[2] > -220 and not game_over_flag:
            glColor3f(1, 0.5, 0) if enemy[4] else glColor3f(1, 1, 1)  
            MidpointCircle(enemy[0], enemy[1], enemy[2])
            new_enemies.append(enemy)

    enemies[:] = new_enemies

    if not play_button_flag:
        if random.randint(0, 90) == 0:
            new_enemy_position = random.randint(-230, 230)
            new_enemy_radius = random.randint(20, 25)
            falling_speed = random.uniform(0.5, 2.0)

            
            if random.randint(1, 10) == 1:
                enemies.append([new_enemy_radius, new_enemy_position, 300, falling_speed, True, "expand"])
            else:
                enemies.append([new_enemy_radius, new_enemy_position, 300, falling_speed, False, None])

def MouseListerner(button,state,x,y):

    global restart_button_flag, cross_button_flag, play_button_flag

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        clicked_x = x - 250
        clicked_y = 250 - y
        print(f"Mouse clicked at OpenGL coordinates: ({clicked_x}, {clicked_y})")

        if (-240 <= clicked_x <= -210) and (220 <= clicked_y <= 240):
            restart_button_flag = True
        elif (220 <= clicked_x <= 240) and (220 <= clicked_y <= 240):
            cross_button_flag = True
        elif (-5 <= clicked_x <= 15) and (220 <= clicked_y <= 240):
            play_button_flag = not play_button_flag



def GameOver():
    # G
    Eight_way_symmetry(-120, 50, -90, 50)  
    Eight_way_symmetry(-120, 50, -120, 10)  
    Eight_way_symmetry(-120, 10, -90, 10)  
    Eight_way_symmetry(-90, 10, -90, 30)  
    Eight_way_symmetry(-100, 30, -90, 30)  

    # A
    Eight_way_symmetry(-80, 10, -70, 50)  
    Eight_way_symmetry(-70, 50, -60, 10)  
    Eight_way_symmetry(-75, 30, -65, 30)  

    # M
    Eight_way_symmetry(-50, 10, -50, 50)  
    Eight_way_symmetry(-50, 50, -40, 30)  
    Eight_way_symmetry(-40, 30, -30, 50)  
    Eight_way_symmetry(-30, 50, -30, 10)  

    # E
    Eight_way_symmetry(-20, 10, -20, 50)  
    Eight_way_symmetry(-20, 50, -10, 50)  
    Eight_way_symmetry(-20, 30, -10, 30) 
    Eight_way_symmetry(-20, 10, -10, 10)  



    # O
    Eight_way_symmetry(0, 10, 0, 50)  
    Eight_way_symmetry(20, 10, 20, 50)  
    Eight_way_symmetry(0, 50, 20, 50)  
    Eight_way_symmetry(0, 10, 20, 10)  

    # V
    Eight_way_symmetry(30, 50, 40, 10)  
    Eight_way_symmetry(40, 10, 50, 50)  

    # E
    Eight_way_symmetry(60, 10, 60, 50)  
    Eight_way_symmetry(60, 50, 70, 50)  
    Eight_way_symmetry(60, 30, 70, 30)  
    Eight_way_symmetry(60, 10, 70, 10)  

    # R
    Eight_way_symmetry(80, 10, 80, 50)  
    Eight_way_symmetry(80, 50, 90, 50)  
    Eight_way_symmetry(90, 50, 90, 30)  
    Eight_way_symmetry(80, 30, 90, 30)  
    Eight_way_symmetry(80, 30, 91, 10)  



def draw_spaceship(x, y):
    glColor3f(0.0, 1.0, 1.0)  
    Eight_way_symmetry(x, y + 40, x - 20, y)  
    Eight_way_symmetry(x, y + 40, x + 20, y)
    

    glColor3f(1.0, 1.0, 1.0)  
    Eight_way_symmetry(x - 10, y + 35, x + 10, y + 35)
    Eight_way_symmetry(x - 10, y + 35, x - 10, y + 25)
    Eight_way_symmetry(x + 10, y + 35, x + 10, y + 25)
    Eight_way_symmetry(x - 10, y + 25, x + 10, y + 25)

    glColor3f(1.0, 0.0, 0.0)  
    Eight_way_symmetry(x - 10, y - 10, x - 5, y - 25)  
    Eight_way_symmetry(x + 10, y - 10, x + 5, y - 25)




def draw_score(score):
   
    glColor3f(0.0, 1.0, 0.0) 
    glRasterPos2f(100, 230) 
    
    score_str = f"Score: {score}"
    for char in score_str:
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(char))  





def timer(value):
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)
   



def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()




def ShowScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    
    global spaceship_x, bullet_y, enemy_x, enemy_y, bullet_speed, bullet_shot_flag, spaceship_left_flag, spaceship_right_flag, score, player_lives, bullets, enemies, restart_button_flag, play_button_flag, cross_button_flag, game_over_flag,heart1_flag,heart2_flag,heart3_flag

    # Reset Button Start
    glColor3f(0.03, 0.96, 0.95)
    draw_restart_button()
    if restart_button_flag:
        print("Start Over")
        spaceship_x = 0
        bullet_y = -205
        enemy_x, enemy_y = random.randint(-150, 200), 300
        bullet_speed = 3
        bullet_shot_flag = False
        spaceship_left_flag = spaceship_right_flag = False
        score = 0
        player_lives = 3
        game_over_flag = False
        restart_button_flag = False
        play_button_flag = False
        cross_button_flag = False
        heart1_flag =  False
        heart2_flag = False
        heart3_flag = False
        bullets = []
        enemies = []

        glColor3f(0.0, 1.0, 1.0)
        # MidpointCircle(18, spaceship_x, -230)
        draw_spaceship(spaceship_x,-230)

        if bullet_shot_flag:
            bullets_fire()
        enemy()

    # Close Button Start
    glColor3f(1, 0, 0)
    draw_cross_button()
    draw_score(score)
    # Close Button End

    # Play & Pause Button Start
    if play_button_flag:
        glColor3f(0.95, 0.96, 0.03)
        draw_play_button()
    else:
        glColor3f(0.95, 0.96, 0.03)
        draw_pause_button()
    # Play & Pause Button End

    if cross_button_flag:
        draw_cross_button()
        print("GOODBYE..")
        glutLeaveMainLoop()

    # Color of circles
    glColor3f(0.96, 1, 0)
    draw_spaceship(spaceship_x,-230)
    if bullet_shot_flag:
        bullets_fire()
    enemy()
    
    
    if heart1_flag==False:
        heart1()
    if heart2_flag==False:
        heart2()
    if heart3_flag==False:
        heart3()

    if game_over_flag==True:
        glColor3f(1,0,0)
        GameOver()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)

glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)

window = glutCreateWindow(b"Shoot The Circles")
glutTimerFunc(0, timer, 0)
glutDisplayFunc(ShowScreen)
glutIdleFunc(spaceship_move)
glutKeyboardFunc(keyBoardListerner)
glutKeyboardUpFunc(spaceship_key_released)
glutMouseFunc(MouseListerner)
glutMainLoop()
