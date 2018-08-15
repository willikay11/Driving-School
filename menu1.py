import pygame, sys, time, random, math
from pygame.locals import *
from math import pi

# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# set up the window
WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0,32)
pygame.display.set_caption('Table Theory')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255,255,255)
BGREEN = (0, 200, 0)
GREEN = (0, 160, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
LBLUE = (0, 200, 255)
LGREY = (75,75,75)
YELLOW = (255,255,0)

# set up variables
MOVESPEED = 50
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
option = [0,'Learn Module','Test Module','Settings','Instructions','Quit',0,'',0]# menu options
Texts = [0,'','','','','','']
curser = [40, 190, 50, 50]# Start position for the curser on the menu
curser2 = [40, 120, 50, 50]
fps = [0,60,10,60,0]# 0-On/Off, 1-Set Point, 2-Actual FPS, 3-Lowest Recorded, 4-Highest Recorded
gripImage = pygame.image.load('media/TableTheory.png').convert_alpha()
banner =[50,18]# Start point for banner text animation
position = [650,250]# Track start position
limit = [1,-1750+WINDOWWIDTH,-1950+WINDOWHEIGHT,1350,150,0,-5]
drawTrack = [3]#0-Track selector, 1-4 LapRecord file names
settings = [0,'Detail Level','Show FPS','Screen Size','Full Screen Mode','Exit',False]# Settings page options
LearnModule = [0, 'Select Module', 'Start', 'Exit', False]# Learning Page
LearnModule2 = [0, 'Selected Module', 'Options', 'Exit', False]# Learning Page
roundabt = [False]
FL1 = [False]
FL2 = [False]
FL3 = [False]
FL4 = [False]
Course = [0,1,2,3]
CourseName = [0,'Round About (4 Lane)','Round About (3 Lane)','Lanes']
Options = [0,1,2,3,5]
OptionName = [0,'Lane 1','Lane 2','Lane 3','Lane 4']
show = [0,2,True,True]# 0-Window / Fullscreen, 1-Display Resolution, 2-Gradient Sky, 3-Background
width = [640,800,1000,1024,1280,1280]# Screen widths
height = [480,600,600,768,720,768]# Screen heights
detail = [2] # LOD switch (0-3)
playerSettings = [WINDOWWIDTH/2-50,WINDOWHEIGHT/2,0]# 0-Player Horizontal, 1-Player Vertical
CourseImage = pygame.image.load('media/Four_lane_left_out.png').convert_alpha()


def setDisplay(w,h):
    playerSettings[0] = WINDOWWIDTH/2-50
    playerSettings[1] = WINDOWHEIGHT/2
    screen = pygame.display.set_mode((w, h),show[0],32)
    pygame.display.set_caption('Table Theory')

def framerate():
    mainClock.tick(fps[1])
    fps[2]=int(mainClock.get_fps())
    if fps[0]==1:
        text = smallFont.render('Set FPS - ' + str(fps[1]), True, WHITE,)
##        text = smallFont.render(str(playerImage), True, WHITE,)
        screen.blit(text, (10,WINDOWHEIGHT-60))
        text1 = smallFont.render('Current FPS - ' + str(fps[2]), True, WHITE,)
##        text1 = smallFont.render(str(lapRecord3), True, WHITE,)
        screen.blit(text1, (10,WINDOWHEIGHT-40))
        text2 = smallFont.render('Lowest FPS - ' + str(fps[3]), True, WHITE,)
##        text2 = smallFont.render(str(lapRecord4), True, WHITE,)
        screen.blit(text2, (10,WINDOWHEIGHT-20))
        if fps[2]<fps[3]:
            fps[3]=fps[2]
        if fps[2]>fps[4]:
            fps[4]=fps[2]
# set up the fonts
smallFont = pygame.font.SysFont(None, 20)
basicFont = pygame.font.SysFont(None, 24)
normalFont = pygame.font.SysFont(None, 30)
guessFont = pygame.font.SysFont(None, 36)

SLWP = pygame.image.load('media/servicelane_without_parking.png').convert_alpha()
Null = pygame.image.load('media/null.png').convert_alpha()
FLLO = pygame.image.load('media/Four_lane_left_out.png').convert_alpha()
FLRI = pygame.image.load('media/Four_lane_right_in.png').convert_alpha()
FLLI = pygame.image.load('media/Four_lane_left_in.png').convert_alpha()
FLRO = pygame.image.load('media/Four_lane_right_out.png').convert_alpha()
TLRO = pygame.image.load('media/Three_lane_right_out.png').convert_alpha()
TLRI = pygame.image.load('media/Three_lane_right_in.png').convert_alpha()
TLLI = pygame.image.load('media/Three_lane_left_in.png').convert_alpha()
TLLO = pygame.image.load('media/Three_lane_left_out.png').convert_alpha()
TLLCDI = pygame.image.load('media/three_lane_left_completely_dashed_in.png').convert_alpha()
TLLCDO = pygame.image.load('media/three_lane_left_completely_dashed_out.png').convert_alpha()
FQ = pygame.image.load('media/first_quadrant.png').convert_alpha()
SQ = pygame.image.load('media/second_quadrant.png').convert_alpha()
TQ = pygame.image.load('media/third_quadrant.png').convert_alpha()
FHQ = pygame.image.load('media/fourth_quadrant.png').convert_alpha()
FP = pygame.image.load('media/flush_parking.png').convert_alpha()
SWP = pygame.image.load('media/servicelane_with_parking.png').convert_alpha()
RNDABT = pygame.image.load('media/RoundAbout-1.png').convert_alpha()

def settingsScreen(WINDOWWIDTH,WINDOWHEIGHT):
    moveUp = False
    moveDown = False
    moveLeft = False
    moveRight = False
    WINDOWWIDTH = width[show[1]]
    WINDOWHEIGHT = height[show[1]]
    while settings[6]:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                    # change the keyboard variables
                    if event.key == K_UP or event.key == ord('w'):#Curser Up
                        moveDown = False
                        moveUp = True
                    if event.key == K_DOWN or event.key == ord('s'):#Curser Down
                        moveUp = False
                        moveDown = True
                    if event.key == K_RIGHT:#Select current option
                        if curser[1]==190:
                            detail[0] +=1
                            if detail[0] >3:
                                detail[0] = 1
                        if curser[1]==290:
                            show[1] +=1
                            if show[1] >5:
                                show[1] = 0
                            WINDOWWIDTH = width[show[1]]
                            WINDOWHEIGHT = height[show[1]]
                    if event.key == K_LEFT:#Select current option
                        if curser[1]==190:
                            detail[0] -=1
                            if detail[0] <1:
                                detail[0] = 3
                        if curser[1]==290:
                            show[1] -=1
                            if show[1] <0:
                                show[1] = 5
                            WINDOWWIDTH = width[show[1]]
                            WINDOWHEIGHT = height[show[1]]
                    if event.key == K_RETURN or event.key == K_SPACE:#
                        if curser[1] == 240:
                            if fps[0] == 1:
                                fps[0] = 0
                            else:
                                fps[0] = 1
                        if curser[1] == 290:
                            setDisplay(WINDOWWIDTH,WINDOWHEIGHT)
                        if curser[1] == 340:
                            if show[0]==0:
                                show[0]=FULLSCREEN
                                screentype = pygame.display.get_surface()
                                tmp = screentype.convert()
                                WINDOWWIDTH,WINDOWHEIGHT = screentype.get_width(),screentype.get_height()
                            else:
                                show[0]=0
                            setDisplay(WINDOWWIDTH,WINDOWHEIGHT)
                        if curser[1] == 390:
                            settings[6]=False
                            menu()

            # move the Curser
        if moveDown and curser[1] < 350:
                curser[1] += MOVESPEED
                moveDown = False
        if moveUp and curser[1] > 200:
                curser[1] -= MOVESPEED
                moveUp = False

        screen.fill(GREEN)
        moveTrack()
        drawBanner(gripImage)

        if curser[1]==190:
                curser[2]=len(settings[1]*17)
                option[7]='Press Left / Right to change track detail'
        if curser[1]==240:
                curser[2]=145
                option[7]='Press Enter to enable FPS display'
        if curser[1]==290:
                curser[2]=len(settings[1]*17)+len(str(width[show[1]])*17)+len(str(height[show[1]])*17)
                option[7]='Press Left / Right to adjust size - Enter Select'
        if curser[1]==340:
                curser[2]=235
                option[7]='Press Enter to enable fullscreen'
        if curser[1]==390:
                curser[2]=70
                option[7]='Exit Settings'

        # blit the options onto the screen
        text1s = guessFont.render(settings[1] + ' - ' + str(detail[0]), True, BLACK,)
        text1 = guessFont.render(settings[1] + ' - ' + str(detail[0]), True, WHITE,)
        text2s = guessFont.render(settings[2], True, BLACK,)
        text2 = guessFont.render(settings[2], True, WHITE,)
        text3s = guessFont.render(settings[3] + ' - ' + str(WINDOWWIDTH) + ' x ' + str(WINDOWHEIGHT), True, BLACK,)
        text3 = guessFont.render(settings[3] + ' - ' + str(WINDOWWIDTH) + ' x ' + str(WINDOWHEIGHT), True, WHITE,)
        text4s = guessFont.render(settings[4], True, BLACK,)
        text4 = guessFont.render(settings[4], True, WHITE,)
        text5s = guessFont.render(settings[5], True, BLACK,)
        text5 = guessFont.render(settings[5], True, WHITE,)
        text6s = basicFont.render(option[7], True, BLACK,)
        text6 = basicFont.render(option[7], True, WHITE,)
        screen.blit(text1s, (50,200))
        screen.blit(text1, (52,202))
        screen.blit(text2s, (50,250))
        screen.blit(text2, (52,252))
        screen.blit(text3s, (50,300))
        screen.blit(text3, (52,302))
        screen.blit(text4s, (50,350))
        screen.blit(text4, (52,352))
        screen.blit(text5s, (50,400))
        screen.blit(text5, (51,402))
        screen.blit(text6s, (50,450))
        screen.blit(text6, (51,451))

        # draw the curser onto the surface
        pygame.draw.rect(screen, BLACK, (curser[0],curser[1],curser[2],curser[3]),1)

        backgroundAnim()
        framerate()
        pygame.display.update()

#Learn Module
def LearnScreen(WINDOWWIDTH,WINDOWHEIGHT):
    global CourseImage
    moveUp = False
    moveDown = False
    moveLeft = False
    moveRight = False
    WINDOWWIDTH = width[show[1]]
    WINDOWHEIGHT = height[show[1]]
    while LearnModule[4]:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                    # change the keyboard variables
                    if event.key == K_UP or event.key == ord('w'):#Curser Up
                        moveDown = False
                        moveUp = True
                    if event.key == K_DOWN or event.key == ord('s'):#Curser Down
                        moveUp = False
                        moveDown = True
                    if event.key == K_RIGHT:#Select current option
                        if curser[1]==190:
                            print('Course_Right')
                            Course[0] +=1
                            if Course[0] > 3:
                                Course[0] = 1
                            CourseImage = CourseSelect(Course[0])
                    if event.key == K_LEFT:#Select current option
                        if curser[1]==190:
                            print('Course_Left')
                            Course[0] -=1
                            if Course[0] <1:
                                Course[0] = 3
                            CourseImage = CourseSelect(Course[0])
                    if event.key == K_RETURN or event.key == K_SPACE:#
                        if curser[1] == 240 and Course[0] == 1:
                            roundabt[0]=True
                            Roundabout_4(WINDOWWIDTH,WINDOWHEIGHT)
                        if curser[1]== 240 and Course[0] ==2:
                            roundabt[0]=True
                            Roundabout_3(WINDOWWIDTH,WINDOWHEIGHT)                            
                        if curser[1] == 290:
                            settings[6]=False
                            menu()

            # move the Curser
        if moveDown and curser[1] < 250:
                curser[1] += MOVESPEED
                moveDown = False
        if moveUp and curser[1] > 200:
                curser[1] -= MOVESPEED
                moveUp = False

        screen.fill(GREEN)
        moveTrack()
        drawBanner(gripImage)

        if curser[1]==190:
                curser[2]=len(LearnModule[1]*37)
                option[7]='Press Left / Right to change Learn Section'
        if curser[1]==240:
                curser[2]=len(LearnModule[1]*17)
                option[7]='Start the Tutorial'
        if curser[1]==290:
                curser[2]=70
                option[7]='Exit Learn Module'


        # blit the options onto the screen
        text1s = guessFont.render(LearnModule[1] + ' - ' + str(CourseName[Course[0]]), True, BLACK,)
        text1 = guessFont.render(LearnModule[1] + ' - ' + str(CourseName[Course[0]]), True, WHITE,)
        text2s = guessFont.render(LearnModule[2], True, BLACK,)
        text2 = guessFont.render(LearnModule[2], True, WHITE,)
        text3s = guessFont.render(LearnModule[3], True, BLACK,)
        text3 = guessFont.render(LearnModule[3], True, WHITE,)
        text6s = basicFont.render(option[7], True, BLACK,)
        text6 = basicFont.render(option[7], True, WHITE,)
        screen.blit(text1s, (50,200))
        screen.blit(text1, (52,202))
        screen.blit(text2s, (50,250))
        screen.blit(text2, (52,252))
        screen.blit(text3s, (50,300))
        screen.blit(text3, (52,302))
        screen.blit(text6s, (50,450))
        screen.blit(text6, (51,451))

        # draw the curser onto the surface
        pygame.draw.rect(screen, BLACK, (curser[0],curser[1],curser[2],curser[3]),1)

        screen.blit(CourseImage, (550,120))
        backgroundAnim()
        framerate()
        pygame.display.update()

def Roundabout_4(WINDOWWIDTH,WINDOWHEIGHT):
    moveUp = False
    moveDown = False
    moveLeft = False
    moveRight = False
    WINDOWWIDTH = width[show[1]]
    WINDOWHEIGHT = height[show[1]]
    while roundabt[0]:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                    # change the keyboard variables
                    if event.key == K_UP or event.key == ord('w'):#Curser Up
                        moveDown = False
                        moveUp = True
                    if event.key == K_DOWN or event.key == ord('s'):#Curser Down
                        moveUp = False
                        moveDown = True
                    if event.key == K_RIGHT:#Select current option
                        if curser2[1]==120:
                            Options[0] +=1
                            if Options[0] > 4:
                                Options[0] = 1
                    if event.key == K_LEFT:#Select current option
                        if curser2[1]==120:
                            Options[0] -=1
                            if Options[0] <1:
                                Options[0] = 4
                    if event.key == K_RETURN:#
                        if curser2[1] == 120 and Options[0] == 1:
                            print(Options[0])
                            Texts[1] = 'Lane One has only two Options'
                            Texts[2] = 'This is the First Option'
                            Texts[3] = 'This is the Second Option'
                            Texts[4] = 'Press Space-Bar to Exit'
                            text7 = basicFont.render(Texts[1], True, WHITE,)
                            text8 = basicFont.render(Texts[2], True, WHITE,)
                            text9 = basicFont.render(Texts[3], True, WHITE,)
                            text10 = basicFont.render(Texts[4], True, WHITE,)
                            screen.blit(text7, (51,200))
                            screen.blit(text8, (51,250))
                            screen.blit(text9, (51,300))
                            screen.blit(text10, (51,430))
                            #First Option
                            pygame.draw.circle(screen, RED,(280,255),5)
                            pygame.draw.circle(screen, RED,(290,255),5)
                            pygame.draw.circle(screen, RED,(300,255),5)
                            pygame.draw.circle(screen, RED,(310,255),5)
                            pygame.draw.circle(screen, RED,(320,255),5)
                            #Second Option
                            pygame.draw.circle(screen, YELLOW,(280,305),5)
                            pygame.draw.circle(screen, YELLOW,(290,305),5)
                            pygame.draw.circle(screen, YELLOW,(300,305),5)
                            pygame.draw.circle(screen, YELLOW,(310,305),5)
                            pygame.draw.circle(screen, YELLOW,(320,305),5)                            
                            FL1[0] = True
                            Four_Lane_1()
                        if curser2[1] == 120 and Options[0] == 2:
                            Texts[1] = 'Lane One has only one Options'
                            Texts[2] = 'This is the Option'
                            Texts[4] = 'Press Space-Bar to Exit'
                            text7 = basicFont.render(Texts[1], True, WHITE,)
                            text8 = basicFont.render(Texts[2], True, WHITE,)
                            text10 = basicFont.render(Texts[4], True, WHITE,)
                            screen.blit(text10, (51,430))
                            screen.blit(text8, (51,250))
                            screen.blit(text7, (51,200))
                            #First Option
                            pygame.draw.circle(screen, RED,(250,255),5)
                            pygame.draw.circle(screen, RED,(260,255),5)
                            pygame.draw.circle(screen, RED,(270,255),5)
                            pygame.draw.circle(screen, RED,(280,255),5)
                            pygame.draw.circle(screen, RED,(290,255),5)
                            FL2[0] = True
                            Four_Lane_2()
                        if curser2[1] == 120 and Options[0] == 3:
                            Texts[1] = 'Lane One has only two Options'
                            Texts[2] = 'This is the First Option'
                            Texts[3] = 'This is the Second Option'
                            Texts[4] = 'Press Space-Bar to Exit'
                            text7 = basicFont.render(Texts[1], True, WHITE,)
                            text8 = basicFont.render(Texts[2], True, WHITE,)
                            text9 = basicFont.render(Texts[3], True, WHITE,)
                            text10 = basicFont.render(Texts[4], True, WHITE,)
                            screen.blit(text7, (51,200))
                            screen.blit(text8, (51,250))
                            screen.blit(text9, (51,300))
                            screen.blit(text10, (51,430))
                            #First Option
                            pygame.draw.circle(screen, RED,(280,255),5)
                            pygame.draw.circle(screen, RED,(290,255),5)
                            pygame.draw.circle(screen, RED,(300,255),5)
                            pygame.draw.circle(screen, RED,(310,255),5)
                            pygame.draw.circle(screen, RED,(320,255),5)
                            #Second Option
                            pygame.draw.circle(screen, YELLOW,(280,305),5)
                            pygame.draw.circle(screen, YELLOW,(290,305),5)
                            pygame.draw.circle(screen, YELLOW,(300,305),5)
                            pygame.draw.circle(screen, YELLOW,(310,305),5)
                            pygame.draw.circle(screen, YELLOW,(320,305),5)
                            FL3[0] = True
                            Four_Lane_3()
                        if curser2[1] == 120 and Options[0] == 4:
                            Texts[1] = 'Lane One has only two Options'
                            Texts[2] = 'This is the First Option'
                            Texts[3] = 'This is the Second Option'
                            Texts[5] = 'This is the Third Option'
                            Texts[6] = 'This is the Fourth Option'
                            Texts[4] = 'Press Space-Bar to Exit'
                            text7 = basicFont.render(Texts[1], True, WHITE,)
                            text8 = basicFont.render(Texts[2], True, WHITE,)
                            text9 = basicFont.render(Texts[3], True, WHITE,)
                            text10 = basicFont.render(Texts[4], True, WHITE,)
                            text11 = basicFont.render(Texts[5], True, WHITE,)
                            text12 = basicFont.render(Texts[6], True, WHITE,)
                            screen.blit(text7, (51,200))
                            screen.blit(text8, (51,250))
                            screen.blit(text9, (51,300))
                            screen.blit(text10, (51,450))
                            screen.blit(text11, (51,350))
                            screen.blit(text12, (51,400))
                            #First Option
                            pygame.draw.circle(screen, RED,(280,255),5)
                            pygame.draw.circle(screen, RED,(290,255),5)
                            pygame.draw.circle(screen, RED,(300,255),5)
                            pygame.draw.circle(screen, RED,(310,255),5)
                            pygame.draw.circle(screen, RED,(320,255),5)
                            #Second Option
                            pygame.draw.circle(screen, YELLOW,(280,305),5)
                            pygame.draw.circle(screen, YELLOW,(290,305),5)
                            pygame.draw.circle(screen, YELLOW,(300,305),5)
                            pygame.draw.circle(screen, YELLOW,(310,305),5)
                            pygame.draw.circle(screen, YELLOW,(320,305),5)
                            #Third Option
                            pygame.draw.circle(screen, BLUE,(280,355),5)
                            pygame.draw.circle(screen, BLUE,(290,355),5)
                            pygame.draw.circle(screen, BLUE,(300,355),5)
                            pygame.draw.circle(screen, BLUE,(310,355),5)
                            pygame.draw.circle(screen, BLUE,(320,355),5)
                            #Fourth Option
                            pygame.draw.circle(screen, GREEN,(280,405),5)
                            pygame.draw.circle(screen, GREEN,(290,405),5)
                            pygame.draw.circle(screen, GREEN,(300,405),5)
                            pygame.draw.circle(screen, GREEN,(310,405),5)
                            pygame.draw.circle(screen, GREEN,(320,405),5)
                            FL4[0] = True
                            Four_Lane_4()                            
                        if curser2[1] == 490:
                            settings[6]=False
                            menu()
            # move the Curser
        if moveDown and curser2[1] < 360:
                curser2[1] += 370
                moveDown = False
        if moveUp and curser2[1] > 150:
                curser2[1] -= 370
                moveUp = False
        
        screen.fill(GREEN)
        
        if curser2[1]==120:
                curser2[2]=len(LearnModule2[1]*20)
                option[7]='Press Left / Right to change Lanes Then Press Enter'
        if curser2[1]==490:
                curser2[2]=70
                option[7]='Exit Learn Module'


        # blit the options onto the screen
        text1s = guessFont.render(LearnModule2[1] + ' - ' + str(CourseName[Course[0]]), True, BLACK,)
        text1 = guessFont.render(LearnModule2[1] + ' - ' + str(CourseName[Course[0]]), True, WHITE,)
        text2s = guessFont.render(LearnModule2[2] + ' - ' + str(OptionName[Options[0]]), True, BLACK,)
        text2 = guessFont.render(LearnModule2[2] + ' - ' + str(OptionName[Options[0]]), True, WHITE,)
        text3s = guessFont.render(LearnModule2[3], True, BLACK,)
        text3 = guessFont.render(LearnModule2[3], True, WHITE,)
        text6s = basicFont.render(option[7], True, BLACK,)
        text6 = basicFont.render(option[7], True, WHITE,)
        screen.blit(text1s, (50,80))
        screen.blit(text1, (52,82))
        screen.blit(text2s, (50,130))
        screen.blit(text2, (52,132))
        screen.blit(text3s, (50,500))
        screen.blit(text3, (52,502))
        screen.blit(text6s, (50,550))
        screen.blit(text6, (51,551))

        # draw the curser onto the surface
        pygame.draw.rect(screen, BLACK, (curser2[0],curser2[1],curser2[2],curser2[3]),1)
        pygame.draw.rect(screen, YELLOW, (40,180,400,300),1)

        screen.blit(RNDABT,(500,0))
        backgroundAnim()
        framerate()
        pygame.display.update()
#Round About Three Lane
def Roundabout_3(WINDOWWIDTH,WINDOWHEIGHT):
    moveUp = False
    moveDown = False
    moveLeft = False
    moveRight = False
    WINDOWWIDTH = width[show[1]]
    WINDOWHEIGHT = height[show[1]]
    while roundabt[0]:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                    # change the keyboard variables
                    if event.key == K_UP or event.key == ord('w'):#Curser Up
                        moveDown = False
                        moveUp = True
                    if event.key == K_DOWN or event.key == ord('s'):#Curser Down
                        moveUp = False
                        moveDown = True
                    if event.key == K_RIGHT:#Select current option
                        if curser2[1]==120:
                            Options[0] +=1
                            if Options[0] > 4:
                                Options[0] = 1
                    if event.key == K_LEFT:#Select current option
                        if curser2[1]==120:
                            Options[0] -=1
                            if Options[0] <1:
                                Options[0] = 4
                    if event.key == K_RETURN:#
                        if curser2[1] == 120 and Options[0] == 1:
                            print(Options[0])
                            Texts[1] = 'Lane One has only two Options'
                            Texts[2] = 'This is the First Option'
                            Texts[3] = 'This is the Second Option'
                            Texts[4] = 'Press Space-Bar to Exit'
                            text7 = basicFont.render(Texts[1], True, WHITE,)
                            text8 = basicFont.render(Texts[2], True, WHITE,)
                            text9 = basicFont.render(Texts[3], True, WHITE,)
                            text10 = basicFont.render(Texts[4], True, WHITE,)
                            screen.blit(text7, (51,200))
                            screen.blit(text8, (51,250))
                            screen.blit(text9, (51,300))
                            screen.blit(text10, (51,430))
                            #First Option
                            pygame.draw.circle(screen, RED,(280,255),5)
                            pygame.draw.circle(screen, RED,(290,255),5)
                            pygame.draw.circle(screen, RED,(300,255),5)
                            pygame.draw.circle(screen, RED,(310,255),5)
                            pygame.draw.circle(screen, RED,(320,255),5)
                            #Second Option
                            pygame.draw.circle(screen, YELLOW,(280,305),5)
                            pygame.draw.circle(screen, YELLOW,(290,305),5)
                            pygame.draw.circle(screen, YELLOW,(300,305),5)
                            pygame.draw.circle(screen, YELLOW,(310,305),5)
                            pygame.draw.circle(screen, YELLOW,(320,305),5)                            
                            FL1[0] = True
                            Three_Lane_1()
                        if curser2[1] == 120 and Options[0] == 2:
                            Texts[1] = 'Lane One has only one Options'
                            Texts[2] = 'This is the Option'
                            Texts[4] = 'Press Space-Bar to Exit'
                            text7 = basicFont.render(Texts[1], True, WHITE,)
                            text8 = basicFont.render(Texts[2], True, WHITE,)
                            text10 = basicFont.render(Texts[4], True, WHITE,)
                            screen.blit(text10, (51,430))
                            screen.blit(text8, (51,250))
                            screen.blit(text7, (51,200))
                            #First Option
                            pygame.draw.circle(screen, RED,(250,255),5)
                            pygame.draw.circle(screen, RED,(260,255),5)
                            pygame.draw.circle(screen, RED,(270,255),5)
                            pygame.draw.circle(screen, RED,(280,255),5)
                            pygame.draw.circle(screen, RED,(290,255),5)
                            FL2[0] = True
                            Three_Lane_2()
                        if curser2[1] == 120 and Options[0] == 3:
                            Texts[1] = 'Lane One has only two Options'
                            Texts[2] = 'This is the First Option'
                            Texts[3] = 'This is the Second Option'
                            Texts[4] = 'Press Space-Bar to Exit'
                            text7 = basicFont.render(Texts[1], True, WHITE,)
                            text8 = basicFont.render(Texts[2], True, WHITE,)
                            text9 = basicFont.render(Texts[3], True, WHITE,)
                            text10 = basicFont.render(Texts[4], True, WHITE,)
                            screen.blit(text7, (51,200))
                            screen.blit(text8, (51,250))
                            screen.blit(text9, (51,300))
                            screen.blit(text10, (51,430))
                            #First Option
                            pygame.draw.circle(screen, RED,(280,255),5)
                            pygame.draw.circle(screen, RED,(290,255),5)
                            pygame.draw.circle(screen, RED,(300,255),5)
                            pygame.draw.circle(screen, RED,(310,255),5)
                            pygame.draw.circle(screen, RED,(320,255),5)
                            #Second Option
                            pygame.draw.circle(screen, YELLOW,(280,305),5)
                            pygame.draw.circle(screen, YELLOW,(290,305),5)
                            pygame.draw.circle(screen, YELLOW,(300,305),5)
                            pygame.draw.circle(screen, YELLOW,(310,305),5)
                            pygame.draw.circle(screen, YELLOW,(320,305),5)
                            FL3[0] = True
                            Three_Lane_3()
                        if curser2[1] == 120 and Options[0] == 4:
                            Texts[1] = 'Lane One has only two Options'
                            Texts[2] = 'This is the First Option'
                            Texts[3] = 'This is the Second Option'
                            Texts[5] = 'This is the Third Option'
                            Texts[6] = 'This is the Fourth Option'
                            Texts[4] = 'Press Space-Bar to Exit'
                            text7 = basicFont.render(Texts[1], True, WHITE,)
                            text8 = basicFont.render(Texts[2], True, WHITE,)
                            text9 = basicFont.render(Texts[3], True, WHITE,)
                            text10 = basicFont.render(Texts[4], True, WHITE,)
                            text11 = basicFont.render(Texts[5], True, WHITE,)
                            text12 = basicFont.render(Texts[6], True, WHITE,)
                            screen.blit(text7, (51,200))
                            screen.blit(text8, (51,250))
                            screen.blit(text9, (51,300))
                            screen.blit(text10, (51,450))
                            screen.blit(text11, (51,350))
                            screen.blit(text12, (51,400))
                            #First Option
                            pygame.draw.circle(screen, RED,(280,255),5)
                            pygame.draw.circle(screen, RED,(290,255),5)
                            pygame.draw.circle(screen, RED,(300,255),5)
                            pygame.draw.circle(screen, RED,(310,255),5)
                            pygame.draw.circle(screen, RED,(320,255),5)
                            #Second Option
                            pygame.draw.circle(screen, YELLOW,(280,305),5)
                            pygame.draw.circle(screen, YELLOW,(290,305),5)
                            pygame.draw.circle(screen, YELLOW,(300,305),5)
                            pygame.draw.circle(screen, YELLOW,(310,305),5)
                            pygame.draw.circle(screen, YELLOW,(320,305),5)
                            #Third Option
                            pygame.draw.circle(screen, BLUE,(280,355),5)
                            pygame.draw.circle(screen, BLUE,(290,355),5)
                            pygame.draw.circle(screen, BLUE,(300,355),5)
                            pygame.draw.circle(screen, BLUE,(310,355),5)
                            pygame.draw.circle(screen, BLUE,(320,355),5)
                            #Fourth Option
                            pygame.draw.circle(screen, GREEN,(280,405),5)
                            pygame.draw.circle(screen, GREEN,(290,405),5)
                            pygame.draw.circle(screen, GREEN,(300,405),5)
                            pygame.draw.circle(screen, GREEN,(310,405),5)
                            pygame.draw.circle(screen, GREEN,(320,405),5)
                            FL4[0] = True
                            Four_Lane_4()                            
                        if curser2[1] == 490:
                            settings[6]=False
                            menu()
            # move the Curser
        if moveDown and curser2[1] < 360:
                curser2[1] += 370
                moveDown = False
        if moveUp and curser2[1] > 150:
                curser2[1] -= 370
                moveUp = False
        
        screen.fill(GREEN)
        
        if curser2[1]==120:
                curser2[2]=len(LearnModule2[1]*20)
                option[7]='Press Left / Right to change Lanes Then Press Enter'
        if curser2[1]==490:
                curser2[2]=70
                option[7]='Exit Learn Module'


        # blit the options onto the screen
        text1s = guessFont.render(LearnModule2[1] + ' - ' + str(CourseName[Course[0]]), True, BLACK,)
        text1 = guessFont.render(LearnModule2[1] + ' - ' + str(CourseName[Course[0]]), True, WHITE,)
        text2s = guessFont.render(LearnModule2[2] + ' - ' + str(OptionName[Options[0]]), True, BLACK,)
        text2 = guessFont.render(LearnModule2[2] + ' - ' + str(OptionName[Options[0]]), True, WHITE,)
        text3s = guessFont.render(LearnModule2[3], True, BLACK,)
        text3 = guessFont.render(LearnModule2[3], True, WHITE,)
        text6s = basicFont.render(option[7], True, BLACK,)
        text6 = basicFont.render(option[7], True, WHITE,)
        screen.blit(text1s, (50,80))
        screen.blit(text1, (52,82))
        screen.blit(text2s, (50,130))
        screen.blit(text2, (52,132))
        screen.blit(text3s, (50,500))
        screen.blit(text3, (52,502))
        screen.blit(text6s, (50,550))
        screen.blit(text6, (51,551))

        # draw the curser onto the surface
        pygame.draw.rect(screen, BLACK, (curser2[0],curser2[1],curser2[2],curser2[3]),1)
        pygame.draw.rect(screen, YELLOW, (40,180,400,300),1)

        screen.blit(RNDABT,(500,0))
        backgroundAnim()
        framerate()
        pygame.display.update()

##FOUR LANE STUFF
def Four_Lane_1():
    while FL1[0]:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    FL1[0] = False
        for y in range(700,590,-15):
            pygame.draw.circle(screen, RED,(720,int(y)),5)
            mainClock.tick(10)
            pygame.display.update()
        startX = 840
        startX =720 
        for y in range(600,200,-10):
            if(y<600 and y >=550):
                startX = startX - 7
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<550 and y>=500):
                startX = startX - 5
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<500 and y>=450):
                startX = startX - 3
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<450 and y>=400):
                startX = startX - 1
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<400 and y>=350):
                startX = startX + 1
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<350 and y>=300):
                startX = startX + 3
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<300 and y>=250):
                startX = startX + 5
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<250 and y>=200):
                startX = startX + 7
                pygame.draw.circle(screen, RED,(startX,y),5)
            mainClock.tick(10)
            pygame.display.update()
        for y in range(200,100,-15):
            pygame.draw.circle(screen, RED,(720,int(y)),5)
            mainClock.tick(10)
            pygame.display.update()
##    CenterX = 900
##    CenterY = 400
##    for angle in range(0,360,5):
##        radius = 90
##        x = radius*math.cos(angle)
##        y = radius*math.sin(angle)
##        x = x + CenterX
##        y = y + CenterY
##        print(int(x),int(y))
##        pygame.draw.circle(screen, RED,(int(x),int(y)),5)
##        mainClock.tick(10)
##        pygame.display.update()

def Four_Lane_2():
    while FL2[0]:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    FL2[0] = False
        for y in range(700,580,-15):
            pygame.draw.circle(screen, RED,(760,int(y)),5)
            mainClock.tick(10)
            pygame.display.update()
        startX = 765
        for y in range(600,200,-10):
            if(y<600 and y>=550):
                startX = startX - 7
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<550 and y>=500):
                startX = startX - 5
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<500 and y>=450):
                startX = startX - 3
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<450 and y>=400):
                startX = startX - 1
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<400 and y>=350):
                startX = startX + 1
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<350 and y>=300):
                startX = startX + 3
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<300 and y>=250):
                startX = startX + 5
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<250 and y>=200):
                startX = startX + 7
                pygame.draw.circle(screen, RED,(startX,y),5)
            mainClock.tick(10)
            pygame.display.update()
        for y in range(200,100,-15):
            pygame.draw.circle(screen, RED,(760,int(y)),5)
            mainClock.tick(10)
            pygame.display.update()
##        CenterX = 900
##        CenterY = 400
##        for angle in range(0,360,5):
##            radius = 150
##            x = radius*math.cos(angle)
##            y = radius*math.sin(angle)
##            x = x + CenterX
##            y = y + CenterY
##            print(int(x),int(y))
##            pygame.draw.circle(screen, YELLOW,(int(x),int(y)),5)
##            mainClock.tick(10)
##            pygame.display.update()
            
def Four_Lane_3():
    while FL3[0]:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    FL3[0] = False
        for y in range(700,540,-15):
            pygame.draw.circle(screen, RED,(800,int(y)),5)
            mainClock.tick(10)
            pygame.display.update()
        startX = 800
        for y in range(550,250,-10):
            if(y<550 and y>=500):
                startX = startX - 5
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<500 and y>=450):
                startX = startX - 3
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<450 and y>=400):
                startX = startX - 1
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<400 and y>=350):
                startX = startX + 1
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<350 and y>=300):
                startX = startX + 3
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<300 and y>=250):
                startX = startX + 5
                pygame.draw.circle(screen, RED,(startX,y),5)
            mainClock.tick(10)
            pygame.display.update()
        for y in range(250,100,-15):
            pygame.draw.circle(screen, RED,(800,int(y)),5)
            mainClock.tick(10)
            pygame.display.update()
        startY = 370
        for x in range(770,1030,10):
            if(x>=770 and x<820):
                startY = startY - 16
                pygame.draw.circle(screen, YELLOW,(x,startY),5)
            if(x>=820 and x<850):
                startY = startY - 9
                pygame.draw.circle(screen, YELLOW,(x,startY),5)
            if(x>=850 and x<890):
                startY = startY - 4
                pygame.draw.circle(screen, YELLOW,(x,startY),5)
            if(x>=890 and x<920):
                startY = startY - 1
                pygame.draw.circle(screen, YELLOW,(x,int(startY)),5)
            if(x>=920 and x<950):
                startY = startY + 1
                pygame.draw.circle(screen, YELLOW,(x,int(startY)),5)
            if(x>=950 and x<980):
                startY = startY + 3
                pygame.draw.circle(screen, YELLOW,(x,int(startY)),5)
            if(x>=980 and x<1030):
                startY = startY + 4
                pygame.draw.circle(screen, YELLOW,(x,int(startY)),5)                
            mainClock.tick(10)
            pygame.display.update()
        for x in range(1030,1230,15):
            pygame.draw.circle(screen, YELLOW,(x,280),5)
            mainClock.tick(10)
            pygame.display.update()

def Four_Lane_4():
    while FL4[0]:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    FL4[0] = False
        # First Option
        for y in range(700,500,-15):
            pygame.draw.circle(screen, RED,(840,int(y)),5)
            mainClock.tick(10)
            pygame.display.update()
        startX = 840
        for y in range(500,300,-10):
            if(y<500 and y>=450):
                startX = startX - 3
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<450 and y>=400):
                startX = startX - 1
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<400 and y>=350):
                startX = startX + 1
                pygame.draw.circle(screen, RED,(startX,y),5)
            if(y<350 and y>=300):
                startX = startX + 3
                pygame.draw.circle(screen, RED,(startX,y),5)
            mainClock.tick(10)
            pygame.display.update()
        for y in range(300,100,-15):
            pygame.draw.circle(screen, RED,(840,int(y)),5)
            mainClock.tick(10)
            pygame.display.update()
        #Second Option
        startY = 370
        for x in range(830,980,10):
            if(x>=830 and x<860):
                startY = startY - 10
                pygame.draw.circle(screen, YELLOW,(x,startY),5)
            if(x>=860 and x<890):
                startY = startY - 7
                pygame.draw.circle(screen, YELLOW,(x,startY),5)
            if(x>=890 and x<920):
                startY = startY - 2.5
                pygame.draw.circle(screen, YELLOW,(x,int(startY)),5)
            if(x>=920 and x<950):
                startY = startY + 2
                pygame.draw.circle(screen, YELLOW,(x,int(startY)),5)
            if(x>=950 and x<980):
                startY = startY + 4
                pygame.draw.circle(screen, YELLOW,(x,int(startY)),5)
            mainClock.tick(10)
            pygame.display.update()
        for x in range(980,1250,15):
            pygame.draw.circle(screen, YELLOW,(x,int(330)),5)
            mainClock.tick(10)
            pygame.display.update()
        #Third Option
        startX = 960
        for y in range(330,500,10):
            if(y<500 and y>=475):
                startX = startX - 4
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            if(y<475 and y>=450):
                startX = startX - 4
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            if(y<450 and y>=425):
                startX = startX - 2
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            if(y<425 and y>=400):
                startX = startX - 1
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            if(y<400 and y>=375):
                startX = startX + 2
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            if(y<375 and y>=350):
                startX = startX + 4
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            if(y<350 and y>=325):
                startX = startX + 8
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            if(y<325 and y>=300):
                startX = startX + 10
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            mainClock.tick(10)
            pygame.display.update()
        for y in range(500,700,15):
            pygame.draw.circle(screen, BLUE,(965,y),5)
            mainClock.tick(10)
            pygame.display.update()
        #Fourth Option
        startY = 470
        for x in range(980,830,-10):
            if(x>=830 and x<860):
                startY = startY - 4
                pygame.draw.circle(screen, GREEN,(x,startY),5)
            if(x>=860 and x<890):
                startY = startY - 2
                pygame.draw.circle(screen, GREEN,(x,startY),5)
            if(x>=890 and x<920):
                startY = startY - 1
                pygame.draw.circle(screen, GREEN,(x,int(startY)),5)
            if(x>=920 and x<950):
                startY = startY + 2
                pygame.draw.circle(screen, GREEN,(x,int(startY)),5)
            if(x>=950 and x<980):
                startY = startY + 5
                pygame.draw.circle(screen, GREEN,(x,int(startY)),5)
            mainClock.tick(10)
            pygame.display.update()
        for x in range(830,600,-15):
            pygame.draw.circle(screen, GREEN,(x,470),5)
            mainClock.tick(10)
            pygame.display.update() 
############END OF FOUR LANE STUFF

#######THREE LANE STUFF
def Three_Lane_1():
    while FL1[0]:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    FL1[0] = False
##        mouse = pygame.mouse.get_pos()
##        print(mouse)
        for x in range(600,700,15):
            pygame.draw.circle(screen, RED,(x,235),5)
            mainClock.tick(10)
            pygame.display.update()
        startY = 235 
        for x in range(700,1120,10):
            if(x<1120 and x >=1050):
                startY = startY + 7
                pygame.draw.circle(screen, RED,(x,startY),5)
            if(x<1050 and x>=1000):
                startY = startY + 5
                pygame.draw.circle(screen, RED,(x,startY),5)
            if(x<1000 and x>=950):
                startY = startY + 3
                pygame.draw.circle(screen, RED,(x,startY),5)
            if(x<950 and x>=930):
                startY = startY + 2
                pygame.draw.circle(screen, RED,(x,startY),5)
            if(x<930 and x>=900):
                startY = startY + 1
                pygame.draw.circle(screen, RED,(x,startY),5)
            if(x<900 and x>=870):
                startY = startY - 1
                pygame.draw.circle(screen, RED,(x,startY),5)
            if(x<870 and x>=850):
                startY = startY - 2
                pygame.draw.circle(screen, RED,(x,startY),5)
            if(x<850 and x>=800):
                startY = startY - 4
                pygame.draw.circle(screen, RED,(x,startY),5)
            if(x<800 and x>=750):
                startY = startY - 6
                pygame.draw.circle(screen, RED,(x,startY),5)
            if(x<750 and x>=700):
                startY = startY - 8
                pygame.draw.circle(screen, RED,(x,startY),5)
            mainClock.tick(10)
            pygame.display.update()
        for x in range(1120,1200,15):
            pygame.draw.circle(screen, RED,(x,235),5)
            mainClock.tick(10)
            pygame.display.update()

def Three_Lane_2():
    while FL2[0]:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    FL2[0] = False
##        mouse = pygame.mouse.get_pos()
##        print(mouse)
        for x in range(600,700,15):
            pygame.draw.circle(screen, RED,(x,280),5)
            mainClock.tick(10)
            pygame.display.update()
        startY = 280
        for x in range(700,1100,010):
            if(x<1100 and x>=1050):
                startY = startY + 7
                pygame.draw.circle(screen, RED,(x,startY),5)
            if(x<1050 and x>=1000):
                startY = startY + 5
                pygame.draw.circle(screen, RED,(x,startY),5)
            if(x<1000 and x>=950):
                startY = startY + 3
                pygame.draw.circle(screen, RED,(x,startY),5)
            if(x<950 and x>=900):
                startY = startY + 1
                pygame.draw.circle(screen, RED,(x,startY),5)
            if(x<900 and x>=850):
                startY = startY - 1
                pygame.draw.circle(screen, RED,(x,startY),5)
            if(x<850 and x>=800):
                startY = startY - 3
                pygame.draw.circle(screen, RED,(x,startY),5)
            if(x<800 and x>=750):
                startY = startY - 5
                pygame.draw.circle(screen, RED,(x,startY),5)
            if(x<750 and x>=700):
                startY = startY - 7
                pygame.draw.circle(screen, RED,(x,startY),5)
            mainClock.tick(10)
            pygame.display.update()
        for x in range(1100,1200,15):
            pygame.draw.circle(screen, RED,(x,280),5)
            mainClock.tick(10)
            pygame.display.update()

def Three_Lane_3():
    while FL3[0]:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    FL3[0] = False
        mouse = pygame.mouse.get_pos()
        print(mouse)
        for x in range(570,750,15):
            pygame.draw.circle(screen, YELLOW,(x,330),5)
            mainClock.tick(10)
            pygame.display.update()
        startY = 330
        for x in range(750,1050,10):
            if(x<1050 and x>=1000):
                startY = startY + 10
                pygame.draw.circle(screen, YELLOW,(x,startY),5)
            if(x<1000 and x>=950):
                startY = startY + 4
                pygame.draw.circle(screen, YELLOW,(x,startY),5)
            if(x<950 and x>=900):
                startY = startY + 1
                pygame.draw.circle(screen, YELLOW,(x,startY),5)
            if(x<900 and x>=850):
                startY = startY - 3
                pygame.draw.circle(screen, YELLOW,(x,startY),5)
            if(x<850 and x>=800):
                startY = startY - 6
                pygame.draw.circle(screen, YELLOW,(x,startY),5)
            if(x<800 and x>=750):
                startY = startY - 8
                pygame.draw.circle(screen, YELLOW,(x,startY),5)
            mainClock.tick(10)
            pygame.display.update()
        for x in range(1050,1200,15):
            pygame.draw.circle(screen, YELLOW,(x,330),5)
            mainClock.tick(10)
            pygame.display.update()

        startX = 990
        for y in range(280,550,10):
            if(y<600 and y>=550):
                startX = startX - 7
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            if(y<550 and y>=500):
                startX = startX - 5
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            if(y<500 and y>=450):
                startX = startX - 3
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            if(y<450 and y>=400):
                startX = startX - 1
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            if(y<400 and y>=350):
                startX = startX + 2
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            if(y<350 and y>=300):
                startX = startX + 5
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            if(y<300 and y>=250):
                startX = startX + 10
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            mainClock.tick(10)
            pygame.display.update()
        for y in range(550,700,15):
            pygame.draw.circle(screen, BLUE,(1000,y),5)
            mainClock.tick(10)
            pygame.display.update()
        startY = 540
        for x in range(1000,750,-10):
            if(x<1000 and x>=965):
                startY = startY + 6
                pygame.draw.circle(screen, GREEN,(x,startY),5)
            if(x<965 and x>=940):
                startY = startY + 4
                pygame.draw.circle(screen, GREEN,(x,startY),5)
            if(x<940 and x>=915):
                startY = startY + 2
                pygame.draw.circle(screen, GREEN,(x,startY),5)
            if(x<915 and x>=890):
                startY = startY + 1
                pygame.draw.circle(screen, GREEN,(x,startY),5)
            if(x<890 and x>=865):
                startY = startY - 1
                pygame.draw.circle(screen, GREEN,(x,startY),5)
            if(x<865 and x>=840):
                startY = startY - 2
                pygame.draw.circle(screen, GREEN,(x,startY),5)
            if(x<840 and x>=815):
                startY = startY - 4
                pygame.draw.circle(screen, GREEN,(x,startY),5)
            if(x<815 and x>=750):
                startY = startY - 6
                pygame.draw.circle(screen, GREEN,(x,startY),5)
            mainClock.tick(10)
            pygame.display.update()
        for x in range(750,570,-15):
            pygame.draw.circle(screen, GREEN,(x,520),5)
            mainClock.tick(10)
            pygame.display.update()
        startX = 800
        for y in range(550,250,-10):
            if(y<550 and y>=500):
                startX = startX - 5
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            if(y<500 and y>=450):
                startX = startX - 3
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            if(y<450 and y>=400):
                startX = startX - 1
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            if(y<400 and y>=350):
                startX = startX + 1
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            if(y<350 and y>=300):
                startX = startX + 3
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            if(y<300 and y>=250):
                startX = startX + 5
                pygame.draw.circle(screen, BLUE,(startX,y),5)
            mainClock.tick(10)
            pygame.display.update()
############END OF THREE LANE STUFF
            
#Course Select
def CourseSelect(Course):
    if Course == 1:
        CourseImage = pygame.image.load('media/Four_lane_left_out.png').convert_alpha()
    elif Course == 2:
        CourseImage = pygame.image.load('media/left_four_laneCompletelyDashed.png').convert_alpha()
    elif Course == 3:
        CourseImage = pygame.image.load('media/three_lane_left_completely_dashed_out.png').convert_alpha()
    elif Course == 4:
        CourseImage = pygame.image.load('media/servicelane_with_parking.png').convert_alpha()
    return CourseImage
        
# Opening menu
def menu():
    # run the menu loop
    moveUp = False
    moveDown = False
    moveLeft = False
    moveRight = False
    global lapRecord
    global lapRecord2
    global lapRecord3
    global lapRecord4
    global lapRecord5
    global position
    global timer
    global lapTimes
    global cheatCheck
    global lap
    global originalLapRecord
    global newLapRecord
    global limit
    global bikeImage
    global playerImage
    global menuImage1
    while option[6]==0:# Option [6] is the selection output bit
        # check for events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                    # change the keyboard variables
                    if event.key == K_UP or event.key == ord('w'):#Curser Up
                        moveDown = False
                        moveUp = True
                    if event.key == K_DOWN or event.key == ord('s'):#Curser Down
                        moveUp = False
                        moveDown = True
                    if event.key == K_9:#Show FPS
                        if fps[0] == 1:
                            fps[0] = 0
                        else:
                            fps[0] = 1
                    if event.key == K_EQUALS:#Increase max FPS
                        show[1] += 5
                    if event.key == K_MINUS:#Decrease max FPS
                        show[1] -= 5
                    if event.key == K_RETURN or event.key == K_SPACE:#Select current option
                        if curser[1]==240:#Start game
                            #position = [(WINDOWWIDTH/2)+50,(WINDOWHEIGHT/2)-50]
                            print(LearnModule[4])
                            LearnModule[4]=True
                            LearnScreen(WINDOWWIDTH,WINDOWHEIGHT)
                        if curser[1]==290:#Go to settings page
                            print(settings[6])
                            settings[6]=True
                            settingsScreen(WINDOWWIDTH,WINDOWHEIGHT)
                        if curser[1]==340:#Go to instructions page
                            option[8]=600
                            print(option[8])
                            #about()
                        if curser[1]==390:#Quit game
                            pygame.quit()
                            sys.exit()
                    if event.key == K_RIGHT:#Change bike selected
                        if curser[1]==190:
                            print('Change car')                       
##                            bikeSelect[0] +=1
##                            if bikeSelect[0] >4:
##                                bikeSelect[0] = 1
##                            playerImage, bikeImage = playerGraphics(bikeSelect[0])
                        if curser[1]==240:#Change track selected
                            print('Change Track')
##                            drawTrack[0] +=1
##                            if drawTrack[0] >9:
##                                drawTrack[0] = 1
##                            lapRecord, lapRecord2, lapRecord3, lapRecord4, lapRecord5 = loadRecords(drawTrack)
                            position,limit = scrollLimits(drawTrack)
                    if event.key == K_LEFT:#Change bike selected
                        if curser[1]==190:
                            print('Change car selected left')
##                            bikeSelect[0] -=1
##                            if bikeSelect[0] <1:
##                                bikeSelect[0] = 4
##                            playerImage, bikeImage = playerGraphics(bikeSelect[0])
                        if curser[1]==240:#Change track selected
                            print('Change track select right')
                            drawTrack[0] -=1
##                            if drawTrack[0] <1:
##                                drawTrack[0] = 9
##                            lapRecord, lapRecord2, lapRecord3, lapRecord4, lapRecord5 = loadRecords(drawTrack)
                            position,limit = scrollLimits(drawTrack)
            if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_UP or event.key == ord('w'):
                        moveUp = False
                    if event.key == K_DOWN or event.key == ord('s'):
                        moveDown = False

        # move the Curser
        if moveDown and curser[1] < 350:
            curser[1] += MOVESPEED
            moveDown = False
        if moveUp and curser[1] > 200:
            curser[1] -= MOVESPEED
            moveUp = False

        # draw the background onto the surface & draw the banner
        screen.fill(GREEN)
        moveTrack()
        drawBanner(gripImage)

        # Output the current curser position
        if curser[1]==190:
            curser[2]=265
            option[7]='Press Left / Right to select your motorbike'
        if curser[1]==240:
            curser[2]=320
            option[7]='Left / Right to select Track - Enter Start'
        if curser[1]==290:
            curser[2]=130
            option[7]='Adjust settings'
        if curser[1]==340:
            curser[2]=175
            option[7]='How to play GRIP'
        if curser[1]==390:
            curser[2]=75
            option[7]='Quit Game'

        # draw the curser onto the surface
        pygame.draw.rect(screen, BLACK, (curser[0],curser[1],curser[2],curser[3]),1)

        # draw the options onto the surface
        text1s = guessFont.render(option[1], True, BLACK,)
        text1 = guessFont.render(option[1], True, WHITE,)
        text2s = guessFont.render(option[2], True, BLACK,)
        text2 = guessFont.render(option[2], True, WHITE,)
        text3s = guessFont.render(option[3], True, BLACK,)
        text3 = guessFont.render(option[3], True, WHITE,)
        text4s = guessFont.render(option[4], True, BLACK,)
        text4 = guessFont.render(option[4], True, WHITE,)
        text5s = guessFont.render(option[5], True, BLACK,)
        text5 = guessFont.render(option[5], True, WHITE,)
        text6s = basicFont.render(option[7], True, BLACK,)
        text6 = basicFont.render(option[7], True, WHITE,)
        screen.blit(text1s, (50,200))
        screen.blit(text1, (52,202))
        screen.blit(text2s, (50,250))
        screen.blit(text2, (52,252))
        screen.blit(text3s, (50,300))
        screen.blit(text3, (52,302))
        screen.blit(text4s, (50,350))
        screen.blit(text4, (52,352))
        screen.blit(text5s, (50,400))
        screen.blit(text5, (51,402))
        screen.blit(text6s, (50,450))
        screen.blit(text6, (51,451))

        #windowSurface.blit(previewImage[drawTrack[0]], (400,350))


        #windowSurface.blit(bikeImage, (400,120))

        #bikeStats(bikeSelect)
        backgroundAnim()
        framerate()
        # draw the window onto the screen
        pygame.display.update()
def drawBanner(gripImage):
    screen.blit(gripImage, (banner[0],banner[1]))

def backgroundAnim():
        if banner[0]<=WINDOWWIDTH:# Animate the banner text and background
            banner[0]+=1
        if banner[0]>WINDOWWIDTH:
            banner[0]=-340
        position[limit[5]] = int(position[limit[5]])
        if position[limit[5]] == limit[limit[0]]:
            limit[0] += 1
            if limit[0] > 4:
                limit[0]=1
            if limit[5] == 1:
                limit[5]=0
            else:
                limit[5]=1
            if limit[0] == 1:
                limit[6]=-5
            elif limit[0] == 2:
                limit[6]=-5
            elif limit[0] == 3:
                limit[6]=5
            else:
                limit[6]=5
        else:
            position[limit[5]] += limit[6]

def scrollLimits(drawTrack):
    position = [(WINDOWWIDTH/2)+50,(WINDOWHEIGHT/2)-50]
    print(drawTrack[0])
    if drawTrack[0] == 1:
        limit = [1,-1950+WINDOWWIDTH,-1450+WINDOWHEIGHT,1750,1350,0,-5]
    elif drawTrack[0] == 2:
        limit = [1,-1300+WINDOWWIDTH,-1450+WINDOWHEIGHT,1850,1350,0,-5]
    elif drawTrack[0] == 3:
        limit = [1,-1750+WINDOWWIDTH,-1950+WINDOWHEIGHT,1350,150,0,-5]
    elif drawTrack[0] == 4:
        limit = [1,-3350+WINDOWWIDTH,-2350+WINDOWHEIGHT,750,150,0,-5]
    elif drawTrack[0] == 5:
        limit = [1,-1950+WINDOWWIDTH,-2350+WINDOWHEIGHT,1350,150,0,-5]
    elif drawTrack[0] == 6:
        limit = [1,-1500+WINDOWWIDTH,-2850+WINDOWHEIGHT,1850,150,0,-5]
    elif drawTrack[0] == 7:
        limit = [1,-2250+WINDOWWIDTH,-1550+WINDOWHEIGHT,1550,1450,0,-5]
    elif drawTrack[0] == 8:
        limit = [1,-4150+WINDOWWIDTH,-2150+WINDOWHEIGHT,1250,900,0,-5]
    else:
        limit = [1,-1800+WINDOWWIDTH,-3150+WINDOWHEIGHT,1250,600,0,-5]
    return position, limit
    
def moveTrack():
    if drawTrack[0] == 3:
        screen.blit(SLWP,(position[0]-1050,position[1]-100))
        screen.blit(Null,(position[0]-600,position[1]-100))
        screen.blit(Null,(position[0]-150,position[1]-100))
        screen.blit(FLLO,(position[0]+300,position[1]-100))
        screen.blit(FLRI,(position[0]+750,position[1]-100))
        screen.blit(Null,(position[0]+1200,position[1]-100))
        #END OF FIRST ROW
        screen.blit(TLRI,(position[0]+1200,position[1]+350))
        screen.blit(SQ,(position[0]+750,position[1]+350))
        screen.blit(FQ,(position[0]+300,position[1]+350))
        screen.blit(TLLI,(position[0]-150,position[1]+350))
        screen.blit(TLLCDI,(position[0]-600,position[1]+350))
        screen.blit(SLWP,(position[0]-1050,position[1]+350))
        #END OF SECOND ROW
        screen.blit(TLRO,(position[0]+1200,position[1]+800))
        screen.blit(TQ,(position[0]+750,position[1]+800))
        screen.blit(FHQ,(position[0]+300,position[1]+800))
        screen.blit(TLLO,(position[0]-150,position[1]+800))
        screen.blit(TLLCDO,(position[0]-600,position[1]+800))
        screen.blit(SLWP,(position[0]-1050,position[1]+800))
        #END OF THIRD ROW
        screen.blit(Null,(position[0]+1200,position[1]+1250))
        screen.blit(FLRO,(position[0]+750,position[1]+1250))
        screen.blit(FLLI,(position[0]+300,position[1]+1250))
        screen.blit(FP,(position[0]-150,position[1]+1250))
        screen.blit(Null,(position[0]-600,position[1]+1250))
        screen.blit(SWP,(position[0]-1050,position[1]+1250))
        #END OF FOURTH ROW
menu()
