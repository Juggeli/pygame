import sys, pygame
pygame.init();

size = width, height = 1152, 648

screen = pygame.display.set_mode(size)

background = pygame.image.load('bg.png').convert()
snowman = pygame.image.load('snowman.png').convert()
screen.blit(background, (0, 0))

pygame.display.update()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		