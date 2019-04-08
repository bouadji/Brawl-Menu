#python3 BS.py

import pygame
import time
import random
import math


pygame.init()

standing = [pygame.image.load('stand0.png'),pygame.image.load('stand1.png'),pygame.image.load('stand2.png'),pygame.image.load('stand3.png')]
rightrun = [pygame.image.load('run0.png'),pygame.image.load('run1.png'),pygame.image.load('run2.png'),pygame.image.load('run3.png'),pygame.image.load('run4.png'),pygame.image.load('run5.png')]
leftrun = [pygame.image.load('runleft0.png'),pygame.image.load('runleft1.png'),pygame.image.load('runleft2.png'),pygame.image.load('runleft3.png'),pygame.image.load('runleft4.png'),pygame.image.load('runleft5.png')]
jump = [pygame.image.load('jump0.png'),pygame.image.load('jump1.png'),pygame.image.load('jump2.png'),pygame.image.load('jump3.png')]
fall = [pygame.image.load('fall0.png'),pygame.image.load('fall1.png')]
runpunch =  [pygame.image.load('runpunch0.png'),pygame.image.load('runpunch1.png'),pygame.image.load('runpunch2.png'),pygame.image.load('runpunch3.png'),pygame.image.load('runpunch4.png'),pygame.image.load('runpunch5.png'),pygame.image.load('runpunch6.png')]
crouch = [pygame.image.load('crouch0.png'),pygame.image.load('crouch1.png'),pygame.image.load('crouch2.png'),pygame.image.load('crouch3.png')]
kick = [pygame.image.load('kick0.png'),pygame.image.load('kick1.png'),pygame.image.load('kick2.png'),pygame.image.load('kick3.png'),pygame.image.load('kick4.png'),pygame.image.load('kick5.png'),pygame.image.load('kick6.png'),pygame.image.load('kick7.png')]


clock= pygame.time.Clock()
point=0
surfaceW = 500
surfaceH = 500
x=250
y=280
vel=1
LO=100
LA=74
left = False
right = False
fallz = False
punchrun = False
crouchman = False
kickme = False
jumpme = False
jumpcount = 10
walkcount=0
v = 8
m = 2
g = 9.81
a = 45


surface = pygame.display.set_mode((surfaceW,surfaceH))
pygame.display.set_caption("BRAWL")

dada = pygame.image.load('run0.png')
wallp1 = pygame.image.load('maplala.jpg')
stage1 = pygame.image.load('plat.png')
stage1 = pygame.transform.scale(stage1, (430, 70))
wallp1 = pygame.transform.scale(wallp1, (500, 500))








def dessiner():
	global walkcount
	surface.blit(wallp1,(0,0))
	surface.blit(stage1,(50,300))

	if walkcount + 1 >= 40:
		walkcount = 0
	elif right:
		surface.blit(rightrun[walkcount//10], (x,y))
		walkcount += 1
	elif left:
		surface.blit(leftrun[walkcount//10], (x,y+10))
		walkcount += 1
	elif fallz:
		surface.blit(fall[walkcount//20],(x,y))
		walkcount += 1
	elif punchrun:
		surface.blit(runpunch[walkcount//12],(x,y))
		walkcount += 1

	elif crouchman:
		surface.blit(crouch[walkcount//10],(x,y))
		walkcount += 1

	elif kickme:
		surface.blit(kick[walkcount//9],(x,y))
		walkcount += 1
	elif jumpme:
		surface.blit(jump[walkcount//10 ],(x,y))
		walkcount += 1

	else:
		surface.blit(standing[walkcount//10],(x,y))
		walkcount +=1


	pygame.display.update()


def commandepit():
	global x,y,vel,right,left,kickme,punchrun,fallz, crouchman, jumpme, jumpcount, v, m, g, a
	keys = pygame.key.get_pressed()

	if keys[pygame.K_SPACE]:
		jumpme = True
		kickme = False
		punchrun = False
		left = False
		right = False
		fallz = False
		crouchman = False




# Calculate force (F). F = 0.5 * mass * velocity^2.
		if y == 280:
		    F = -g/(2*v**2 * cos(a)**2) * x**2 + tan(a)*x
		else:
		    F = g/(2*v**2 * cos(a)**2) * x**2 + tan(a)*x

		# Change position
		y = y - F

		# Change velocity
		
		#if jumpcount >= -10:
			#neg = 1
			#if jumpcount < 0:
				#neg = -1
			#y -= (jumpcount**2)*0.3*neg
			#jumpcount-= 1
	#	else:
	#		jumpme = False
	#		jumpcount = 10

	if keys[pygame.K_2]:
		kickme = True
		punchrun = False
		left = False
		right = False
		fallz = False
		crouchman = False
		jumpme = False




	if keys[pygame.K_e] :
		x+=3
		punchrun = True
		left = False
		right = False
		fallz = False
		kickme = False
		crouchman = False
		jumpme = False



	if keys[pygame.K_q]:
		x-=3
		punchrun = False
		left = False
		right = False
		fallz = False
		kickme = False
		crouchman = False
		jumpme = False


	if keys[pygame.K_DOWN]:
		crouchman = True
		punchrun = False
		left = False
		right = False
		fallz = False
		kickme = False
		jumpme = False


	if keys[pygame.K_RIGHT] :
		x=x+vel
		right= True
		left = False
		punchrun = False
		kickme = False
		fallz = False
		crouchman = False
		jumpme = False


	if keys[pygame.K_RIGHT] == False:
		right= False
		left = False
		punchrun = False
		kickme = False
		fallz = False
		crouchman = False
		jumpme = False





	if x >430 :
		y=y+1
		fallz = True
		left = False
		right = False
		punchrun = False
		kickme = False
		crouchman = False
		jumpme = False


	if keys[pygame.K_LEFT] :
		x=x-vel
		left=True
		right = False
		punchrun = False
		kickme = False
		fallz = False
		crouchman = False
		jumpme = False


	if x <40:
		y=y+1
		fallz = True
		kickme = False
		crouchman = False
		right= True
		left = False
		punchrun = False
		jumpme = False


	if y> 280:
		y=y+1
		fallz = True
		left = False
		right = False
		kickme = False
		crouchman = False
		punchrun = False
		jumpme = False


	if y>500 and x<250:
		time.sleep(1.5)
		x=50
		y=280
		right= True
		fallz = False
		kickme = False
		crouchman = False
		left = False
		punchrun = False
		jumpme = False


	if y>500 and x>250:
		time.sleep(1.5)
		x=410
		y=280
		right= True
		fallz = False
		kickme = False
		crouchman = False
		left = False
		punchrun = False
		jumpme = False














run = True
while run:
	clock.tick(100)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False






	commandepit()


	dessiner()
pygame.quit()

