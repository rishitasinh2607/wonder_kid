import pygame
pygame.init()


mode = pygame.display.set_mode((500,500))
pygame.display.set_caption("Wonder Kid")

Right = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
Left = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()  #play the music


class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.jump = False
        self.left = False
        self.right = False
        self.walk = 0
        self.count = 10

    def draw(self,mode):
        if self.walk +1 >= 27: #27 units for each img 3units to capture
            self.walk = 0

        if self.left:
            mode.blit(Left[self.walk//3],(self.x,self.y))
            self.walk += 1

        elif self.right:
            mode.blit(Right[self.walk//3],(self.x,self.y))
            self.walk += 1
        else:
            mode.blit(char,(self.x,self.y))

def redrawGameWindow():
    mode.blit(bg,(0,0)) #background image
    p.draw(mode) #man character
    pygame.display.update()


#Create the instance for class
p = player(200,335,64,64)

run = True #initiate running
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #closing window
            run = False
    keys = pygame.key.get_pressed() #dict to use keys
    if keys[pygame.K_LEFT] and p.x > p.vel:
        p.x -= p.vel
        p.left = True
        p.right = False
    elif keys[pygame.K_RIGHT] and p.x<500 - p.vel - p.width:
        p.x += p.vel
        p.right = True
        p.left = False
    else:
        p.right = False
        p.left = False
        p.walk = 0
        
    if not p.jump:
        if keys[pygame.K_SPACE]:
            p.jump = True
            p.right = False
            p.left = False
            p.walk=0
    else:
        if p.count >= -10: #it will come to default position
            n = 1 #to fit up and down keys
            if p.count <0:
                n=-1
            p.y -= (p.count **2)*0.5*n
            p.count -= 1
        else:
            p.count =10
            p.jump = False
    redrawGameWindow()
        
pygame.quit() #ending
