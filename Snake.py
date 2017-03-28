#Snake Game

#our game imports
import pygame, sys, random, time

#check for initialzing erros
check_errors = pygame.init()
if check_errors[1] > 0: 
    print("(!) Had {0} initializing errors, exiting".format(check_errors[1]))
    sys.exit(-1)
else: 
    print("(+) PyGame successfully initialized!")

#play surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption("Snake Game!")

#colors	
red = pygame.Color(255, 0, 0)			#game over
green = pygame.Color(0, 255, 0)			#snake
black = pygame.Color(0, 0, 0)			#score
white = pygame.Color(255, 255, 255)		#background
brown = pygame.Color(165, 42, 42)		#food

# FPS controller
fpsController = pygame.time.Clock()

#Important variables
snakePosition = [100, 50]
snakeBody = [[100,50], [90,50], [80,50]]

foodPosition = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]		#randrange(x, y)
foodSpawn = True

direction = 'RIGHT'
changeTo = direction

score = 0

#Game over function
def gameOver(): 
    myFont = pygame.font.SysFont('monaco', 72)
    gameOverSurface = myFont.render('Game Over!', True, red)
    gameOverRectangle = gameOverSurface.get_rect()
    gameOverRectangle.midtop = (360, 15)
    playSurface.blit(gameOverSurface, gameOverRectangle)
    pygame.display.flip()
    myScore(0)
    time.sleep(4)
    pygame.quit()		#pygame exit
    sys.exit()			#console

def myScore(choice = 1):
    scoreFont = pygame.font.SysFont('monaco', 24)
    scoreSurface = scoreFont.render('Score: {0}'.format(score), True, black)
    scoreRectangle = scoreSurface.get_rect()
    if choice == 1:
        scoreRectangle.midtop = (80, 10)
    else:
        scoreRectangle.midtop = (360, 120)
    playSurface.blit(scoreSurface, scoreRectangle)
    pygame.display.flip()
    
#Main Logic of game
while True:
    for event in pygame.event.get():
	    if event.type == pygame.QUIT:
		    pygame.quit()
		    sys.exit()
	    elif event.type == pygame.KEYDOWN: 
		    if event.key == pygame.K_RIGHT or event.key == ord('d'): 
			    changeTo = 'RIGHT'
		    if event.key == pygame.K_LEFT or event.key == ord('a'): 
			    changeTo = 'LEFT'
		    if event.key == pygame.K_UP or event.key == ord('w'): 
			    changeTo = 'UP'
		    if event.key == pygame.K_DOWN or event.key == ord('s'): 
			    changeTo = 'DOWN'
		    if event.key == pygame.K_ESCAPE: 
			    pygame.event.post(pygame.event.Event(QUIT))

    #validation of direction
    if changeTo == 'RIGHT' and not direction == 'LEFT': 
	    direction = 'RIGHT'
    if changeTo == 'LEFT' and not direction == 'LEFT': 
	    direction = 'LEFT'
    if changeTo == 'UP' and not direction == 'DOWN': 
	    direction = 'UP'
    if changeTo == 'DOWN' and not direction == 'UP': 
	    direction = 'DOWN'

    #update snake position [x,y]	
    if direction == 'RIGHT': 
	    snakePosition[0] += 10
    if direction == 'LEFT': 
	    snakePosition[0] -= 10
    if direction == 'UP': 
	    snakePosition[1] -= 10
    if direction == 'DOWN': 
	    snakePosition[1] += 10

    #snake body mechanism
    snakeBody.insert(0, list(snakePosition))
    if snakePosition[0] == foodPosition[0] and snakePosition[1] == foodPosition[1]:
        score += 1
        foodSpawn = False
    else: 
    	snakeBody.pop()

    #Food Spawn	
    if foodSpawn == False: 
    	foodPosition = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
    foodSpawn = True

    playSurface.fill(white)

    #Draw Snake
    for position in snakeBody:
            pygame.draw.rect(playSurface, green, pygame.Rect(position[0], position[1], 10, 10))
	
    #Draw Food	
    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPosition[0], foodPosition[1], 10, 10))

    #Boundary check
    if snakePosition[0] > 710 or snakePosition[0] < 0:
        gameOver()
    if snakePosition[1] > 450 or snakePosition[1] < 0:
        gameOver()

    for block in snakeBody[1:]:
        if snakePosition[0] == block[0] and snakePosition[1] == block[1]:
            gameOver()
    
    pygame.display.update()
    myScore()
    fpsController.tick(25)



























    




