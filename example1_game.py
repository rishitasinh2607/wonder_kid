import pygame
pygame.init()


mode = pygame.display.set_mode((500,500))
pygame.display.set_caption("wonder kid")

Right = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
Left = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()#play the music

                                
x= 50;y=50;width=15;height=15
vel = 5
jump = False
count = 10


run = True #initiate running
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #close window
            run = False
    keys = pygame.key.get_pressed() #dict to use keys
    if keys[pygame.K_LEFT]and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT]and x<500 - vel - width:
        x += vel
    if not jump:
        if keys[pygame.K_UP] and y>vel:
           y -= vel
        if keys[pygame.K_DOWN]and y < 500 - height - vel:
           y += vel
        if keys[pygame.K_SPACE]:
           jump = True
    else:
        if count >= -10:
            y -= (count *abs(count))*0.5
            count -= 1
        else:
            count = 10
            jump = False

            
    mode.fill((0,0,0)) #to remove traces
    pygame.draw.rect(mode,(255,0,0),(x,y,width,height)) #display (255,0,0) rgb(x,y,width,height)
    pygame.display.update()
pygame.quit()#end


