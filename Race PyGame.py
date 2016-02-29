import pygame
import time
from pygame.locals import *
from random import randrange
from timeit import default_timer
pygame.init()

horse =  pygame.image.load("horse.png")

pygame.display.set_caption("Race Game")

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

players = 10
raceLength = 10
waitTime = 0.1

Width = 25*(raceLength)
Height = 25*(players)

screen = pygame.display.set_mode((Width,Height))
back = pygame.Surface((Width,Height))
background = back.convert()
background.fill(white)
screen.blit(background,(0,0))

font = pygame.font.Font(None, 24)
text = font.render("1", 1, white)
textpos = text.get_rect()
textpos.centerx = 0
textpos.centery = 0
screen.blit(text, textpos)

positions = []

def printPos():
	global raceLength
	global positions
	global players
	for x in range(players):
		toPrint = ""
		for y in range(positions[x]):
			toPrint = toPrint + "*"
		for z in range(len(toPrint)):
			#pygame.draw.rect(screen, black, (z*25,x*25,25,25), 0)
			pass
		for y in range(raceLength-len(toPrint)-1):
			toPrint = toPrint + "_"
		
		text = font.render(str(x+1), 1, red)
		textpos.centerx = z*25+8
		textpos.centery = x*25+13
		screen.blit(text, textpos)
		screen.blit(horse,(z*25+25, x*25))

		#print "Player " + str(x+1) + ": " + toPrint

for x in range(players):
	positions.append(1)

while not raceLength-1 in positions:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == KEYDOWN:
			if event.key == K_q:
				exit()
	pygame.display.update()
	randomNumber = randrange(0, players)
	positions[randomNumber] += 1
	screen.blit(background,(0,0))
	printPos()
	print ""
	time.sleep(waitTime)

screen.blit(background,(0,0))
printPos()
pygame.display.update()
time.sleep(2)