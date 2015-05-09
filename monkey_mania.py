import pygame, sys,os, time
from pygame.locals import *
import random
pygame.init()
max_x=300
max_y=300
window = pygame.display.set_mode((max_x, max_y))
pygame.display.set_caption('Monkey Mania')
screen = pygame.display.get_surface()

monkey = pygame.image.load("images/Chimp.ico")
monkey = pygame.transform.scale(monkey,(30,30))
monkey_rect = monkey.get_rect()

banana = pygame.image.load("images/banana.jpg").convert()
banana=pygame.transform.scale(banana,(20,20))
banana_rect = banana.get_rect()

gameover = pygame.image.load("images/gameover.jpg").convert()
gameover =pygame.transform.scale(gameover,(300,300))

orange = pygame.image.load("images/orange.png").convert()
orange =pygame.transform.scale(orange,(20,20))


#screen.blit(pygame.transform.scale(monkey,(30,30)), (0,0))

#screen.blit(banana, (5,5))
pygame.display.update()
x=0
y=20
score1=0

x1=270
y1=270
score2=0
banana_pos=[]
for i in range(10):
	bx=random.randrange(0,271,10)
	by=random.randrange(20,271,10)
	if (bx,by) not in banana_pos:
		banana_pos.append((bx,by))
	else:
		i-=1
#print banana_pos
orange_pos=[]
for i in range(10):
	o_x=random.randrange(0,271,10)
	o_y=random.randrange(20,271,10)
	if (o_x,o_y) not in banana_pos and (o_x,o_y) not in orange_pos:
		orange_pos.append((o_x,o_y))
	else:
		i-=1

print orange_pos

game=True
pygame.mixer.music.load('music/moonlight.wav')
pygame.mixer.music.play()
#sound
eat = pygame.mixer.Sound('music/eat.wav')
gameover_sound = pygame.mixer.Sound('music/gameover.wav')

while game:
	#events = pygame.event.get()
	for event in pygame.event.get():
		#pygame.mixer.music.play()
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit(0)
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				print 'r8'
				x+=10
			elif event.key == pygame.K_LEFT:
				x-=10
				print 'left'
			elif event.key == pygame.K_UP:
				y-=10
				print 'up'
			elif event.key == pygame.K_DOWN:
				y+=10
				print 'down'
			
			elif event.key == pygame.K_a:   #left
				x1-=10
			elif event.key == pygame.K_w:   #up     
				y1-=10
			elif event.key == pygame.K_s:    #down
				y1+=10
			elif event.key == pygame.K_d: #right
				x1+=10

	 	screen.fill((255,255,255))
	 	if x > 270:
	 		x= 270
	 	elif x < 0:
	 		x=0
	 	if y > 270:
	 		y=270
	 	elif y < 20:
	 		y=20

	 	if x1 > 270:
	 		x1= 270
	 	elif x1 < 0:
	 		x1=0
	 	if y1 > 270:
	 		y1=270
	 	elif y1 < 20:
	 		y1=20
	 	#print "PLAYER 1:"+str(x)+" PLAYER 2:"+str(y)
	 	pygame.font.init()
	 	font = pygame.font.Font(None, 24)
	 	text = font.render("PLAYER 1: "+str(score1)+"                     PLAYER 2: "+str(score2), True, (0,255,0))
	 	screen.blit(text, (0,0))

	 	if (x,y) in banana_pos:
	 		print 'banana'
	 		banana_pos.remove((x,y))
	 		score1+=10
	 		eat.play()
	 	if (x1,y1) in banana_pos:
	 		print 'banana2'
	 		banana_pos.remove((x1,y1))
	 		score2+=10
	 		eat.play()

	 	if (x,y) in orange_pos:
	 		print 'banana'
	 		orange_pos.remove((x,y))
	 		score1+=5
	 		eat.play()
	 	if (x1,y1) in orange_pos:
	 		print 'banana2'
	 		orange_pos.remove((x1,y1))
	 		score2+=5
	 		eat.play()


		screen.blit(monkey, (x,y))
		screen.blit(monkey,(x1,y1))
		#All bananas finished
		if not banana_pos and not orange_pos:
			print 'GAME OVER'
			font = pygame.font.Font(None, 50)
			gameover_sound.play()
			if score1 > score2:
				text = font.render("PLAYER1 WON", True, (255,0,0))
			elif score2 > score1:
				text = font.render("PLAYER2 WON ", True, (255,0,0))
			if score1 == score2:
				text = font.render("DRAW", True, (255,0,0))
			textRect = text.get_rect()
			textRect.centerx = screen.get_rect().centerx
			textRect.centery = screen.get_rect().centery+100
			screen.blit(gameover, (0,0))
			screen.blit(text, textRect)
		for b_x,b_y in banana_pos:
			screen.blit(banana,(b_x,b_y))
		for o_x,o_y in orange_pos:
			screen.blit(orange,(o_x,o_y));
		pygame.display.update()
# while 1:
# 	print "EMPTY"
# 	print "s1:"+str(score1)+" s2:"+str(score2)
# 	pygame.font.init()
# 	font = pygame.font.Font(None, 24)
# 	text = font.render("score: "+str(score1)+"%", True, (255,0,0))
# 	textRect = text.get_rect()
# 	textRect.centerx = screen.get_rect().centerx
# 	textRect.centery = screen.get_rect().centery+24
# 	#screen.blit(gameover, (0,0))
# 	screen.blit(text, textRect)
# 	pygame.display.update()