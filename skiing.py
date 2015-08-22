import pygame, sys, time, random
from pygame.locals import *

pygame.init()

fpsClock = pygame.time.Clock()


playSurface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Bob the Block goes Skiing')

redColour = pygame.Color(252, 0, 6)

blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150, 150, 150)
bobPosition = [300,70]
direction = 'right'
changeDirection = direction
pygame.draw.rect(playSurface,redColour,Rect(bobPosition[0], bobPosition[1], 40, 40))
pygame.display.flip()

length = 100
obstPosition = [100,475]

score = 0
speed = 10
displayText = 0

def gameOver():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 72)
    gameOverSurf = gameOverFont.render('Game Over', True, greyColour)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 10)
    playSurface.fill(blackColour)
    gameOverScoreFont = pygame.font.Font('freesansbold.ttf', 64)
    gameOverScoreSurf = gameOverFont.render('Score %s' % score, True, greyColour)
    gameOverScoreRect = gameOverScoreSurf.get_rect()
    gameOverScoreRect.midtop = (320, 150)
    
    playSurface.blit(gameOverScoreSurf, gameOverScoreRect)
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    print score
    time.sleep(3)
    pygame.quit()
    sys.exit()

while True:
    if displayText == 0:
    	gameOverFont = pygame.font.Font('freesansbold.ttf', 80)

    	gameOverSurf = gameOverFont.render('3', True, greyColour)
    	gameOverRect = gameOverSurf.get_rect()
    	gameOverRect.midtop = (320, 175)

	playSurface.fill(blackColour)
    	playSurface.blit(gameOverSurf, gameOverRect)
	pygame.display.flip()
	time.sleep(1)
    	gameOverSurf = gameOverFont.render('2', True, greyColour)
    	gameOverRect = gameOverSurf.get_rect()
    	gameOverRect.midtop = (320, 175)
	time.sleep(1)
	playSurface.fill(blackColour)
    	playSurface.blit(gameOverSurf, gameOverRect)
	pygame.display.flip()
    	gameOverSurf = gameOverFont.render('1', True, greyColour)
    	gameOverRect = gameOverSurf.get_rect()
    	gameOverRect.midtop = (320, 175)
	time.sleep(1)
	playSurface.fill(blackColour)
    	playSurface.blit(gameOverSurf, gameOverRect)
	pygame.display.flip()
	time.sleep(1)
	displayText = 1

    if obstPosition[1] < 25:
    	x = random.randint(10,505)
    	obstPosition = [x,475]
    	length += random.randint(1,5)
	score += 1
	speed += 0.1
	pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == ord('d'):
                changeDirection = 'right'
            if event.key == K_LEFT or event.key == ord('a'):
                changeDirection = 'left'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
	direction = changeDirection
    if direction == 'right':
        bobPosition[0] += 20
    if direction == 'left':
        bobPosition[0] -= 20
    playSurface.fill(blackColour)
    a = ['one','two','three']
    pygame.draw.rect(playSurface,whiteColour,Rect(obstPosition[0], obstPosition[1], length, 20))
    obstPosition[1] -= speed
    pygame.draw.rect(playSurface,redColour,Rect(bobPosition[0], bobPosition[1], 25, 25))
    pygame.display.flip()
    if bobPosition[0] > 620 or bobPosition[0] < 0:
        gameOver()
    if bobPosition[1] > 460 or bobPosition[1] < 0:
        gameOver()
    rect1 = Rect(bobPosition[0],bobPosition[1],25,25)
    rect2 = Rect(obstPosition[0],obstPosition[1],length,20)

    collideTest = rect1.colliderect(rect2)
    if collideTest == True:
	gameOver()
    fpsClock.tick(19)

