import pygame
import math

#declarations
wScreen = 1200
hScreen = 500

#game variables
win = pygame.display.set_mode((wScreen, hScreen))


def redrawWindow():
    win.fill((64,64,64))
    golfBall.draw(win)
    pygame.draw.line(win, (255,255,255), line[0], line[1])
    pygame.display.update()

class ball(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, (0,0,0), (self.x, self.y), self.radius)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius-1)

    @staticmethod
    def ballPath(startx, starty, power, ang, time):
        pass

def findAngle(pos):
    sX = golfBall.x 
    sY = golfBall.y 

    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0])) 
    except:
        angle = math.pi / 2
        
    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle) 
    elif pos[1] < sY and pos0] < sX:
        angle = math.pi - angle 
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle) 
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi * 2) - angle
        
    return angle

golfBall = ball(300, 494, 5, (255,255,255))

x = 0
y = 0
time = 0
power = 0
angle = 0
shoot = False

run = True
while run:
    if shoot:
        if golfBall.y < 500 - golfBall.radius:
            time += 0.05
            po = ball.ballPath(x, y)
    
    pos = pygame.mouse.get_pos()
    line = [(golfBall.x, golfBall.y), pos]

    redrawWindow()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if shoot == False:
                shoot = True
                x = golfBall.x
                y = golfBall.y
                time = 0
                power = math.sqrt((line[1][1] - line[0][1])**2 + (line[1][0] - line[0][0])**2)/8
                angle = findAngle(pos)

pygame.quit()
