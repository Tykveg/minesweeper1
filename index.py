import pygame
import random

k_mines = 99 #Количество мин/Amount of mines
map_size = (35,25) #Размер карты/Map size
sq_size = 30 #Размер одного квадрата в пикселях/Square size in px.







you_won_title='''
                                                                      
                                                                      
                                                                      
                    ____                  .   . ,   ,   ____    ,____ 
         /'    /  /'    )--/'    /        |   |/   /  /'    )--/'    )
       /'    /' /'    /' /'    /'         |  /|  /' /'    /' /'    /' 
      (___,/(__(___,/'  (___,/(__        _|/' |/(__(___,/' /'    /(__ 
         /'                                                           
 /     /'                                                             
(___,/'                                                               
'''



you_lose_title='''
                                                                    
                                              /'                    
                                            /'                      
                    ____                  /' ____     ____     ____ 
         /'    /  /'    )--/'    /      /' /'    )--/'    )--/'    )
       /'    /' /'    /' /'    /'     /' /'    /'  '---,   /(___,/' 
      (___,/(__(___,/'  (___,/(__    (__(___,/'  (___,/   (________ 
         /'                                                         
 /     /'                                                           
(___,/'                                                             
'''



def open_mines(screen, map, map_size):
	for y in range(map_size[1]):
		for x in range(map_size[0]):
			if map[x,y][0] == -1 and map[x,y][1] != -1:
				map[x,y][1] = -2
			if map[x,y][0] != -1 and map[x,y][1] == -1:
				map[x,y][1] = -3


def draw_grind(screen, map, map_size, sq_size, mine_img, numbs_img, colour=(255,255,255)):
	won = True
	for y in range(map_size[1]):
		for x in range(map_size[0]):
			if not (map[(x,y)][0] == -1 and map[(x,y)][1] == -1 or map[(x,y)][0] != -1 and map[(x,y)][1] == 1):
				won = False
			rect = pygame.Rect(x*(sq_size+1), y*(sq_size+1)+timer_width, sq_size, sq_size)
			color = (255, 255, 255)
			draw_i = False
			if map[(x,y)][1] == 0:
				color = (133, 133, 133)
			if map[(x,y)][1] == -1:
				color = (133, 133, 133)
				draw_i = flag_img
			if map[(x,y)][1] == 1:
				if map[(x,y)][0] == -1:
					draw_i = mine_img
				elif map[(x,y)][0] != 0:
					draw_i = numbs_img[map[(x,y)][0]-1]
			if map[(x,y)][1] == -2:
				color = (255,0,0)
				draw_i = mine_img
			if map[(x,y)][1] == -3:
				color = (255,0,0)
				draw_i = flag_img
			if colour == False:
				won = False
			pygame.draw.rect(screen, color, rect)
			if draw_i:
				screen.blit(draw_i, (x*(sq_size+1),y*(sq_size+1)+timer_width))
	return won

def check_grind(sq_xy, map, map_size):
	i = sq_xy[0]
	ii = sq_xy[1]
	map[sq_xy][1] = 1
	if map[sq_xy][0] != 0:
		return
	if ii-1>=0:
		if map[(i,ii-1)][0] == 0 and map[(i,ii-1)][1] != 1:
			check_grind((i,ii-1), map, map_size)
		elif map[(i,ii-1)][0] != -1 and map[(i,ii-1)][1] != -1:
			map[(i,ii-1)][1] = 1
		
	if ii-1>=0 and i+1<=map_size[0]:
		if map[(i+1,ii-1)][0] == 0 and map[(i+1,ii-1)][1] != 1:
			check_grind((i+1,ii-1), map, map_size)
		elif map[(i+1,ii-1)][0] != -1 and map[(i+1,ii-1)][1] != -1:
			map[(i+1,ii-1)][1] = 1

	if i+1<=map_size[0]:
		if map[(i+1,ii)][0] == 0 and map[(i+1,ii)][1] != 1:
			check_grind((i+1,ii), map, map_size)
		elif map[(i+1,ii)][0] != -1 and map[(i+1,ii)][1] != -1:
			map[(i+1,ii)][1] = 1

	if i+1<=map_size[0] and ii+1<=map_size[1]:
		if map[(i+1,ii+1)][0] == 0 and map[(i+1,ii+1)][1] != 1:
			check_grind((i+1,ii+1), map, map_size)
		elif map[(i+1,ii+1)][0] != -1 and map[(i+1,ii+1)][1] != -1:
			map[(i+1,ii+1)][1] = 1

	if ii+1<=map_size[1]:
		if map[(i,ii+1)][0] == 0 and map[(i,ii+1)][1] != 1:
			check_grind((i,ii+1), map, map_size)
		elif map[(i,ii+1)][0] != -1 and map[(i,ii+1)][1] != -1:
			map[(i,ii+1)][1] = 1

	if i-1>=0 and ii+1<=map_size[1]:
		if map[(i-1,ii+1)][0] == 0 and map[(i-1,ii+1)][1] != 1:
			check_grind((i-1,ii+1), map, map_size)
		elif map[(i-1,ii+1)][0] != -1 and map[(i-1,ii+1)][1] != -1:
			map[(i-1,ii+1)][1] = 1

	if i-1>=0:
		if map[(i-1,ii)][0] == 0 and map[(i-1,ii)][1] != 1:
			check_grind((i-1,ii), map, map_size)
		elif map[(i-1,ii)][0] != -1 and map[(i-1,ii)][1] != -1:
			map[(i-1,ii)][1] = 1

	if i-1>=0 and ii-1>=0:
		if map[(i-1,ii-1)][0] == 0 and map[(i-1,ii-1)][1] != 1:
			check_grind((i-1,ii-1), map, map_size)
		elif map[(i-1,ii-1)][0] != -1 and map[(i-1,ii-1)][1] != -1:
			map[(i-1,ii-1)][1] = 1

pygame.init()
pygame.font.init()

font = pygame.font.SysFont('Comic Sans MS', 30)
mines_counter = font.render(str(k_mines), False, (255,255,255))
k_flags = k_mines

timer_width = 75


mine_img = pygame.transform.scale(pygame.image.load('img/mine.png'), (sq_size, sq_size))
flag_img = pygame.transform.scale(pygame.image.load('img/flag.png'), (sq_size, sq_size))
numbs_img = []
for i in range(1, 8+1):
	numbs_img.append(pygame.transform.scale(pygame.image.load('img/'+str(i)+'.png'),(sq_size, sq_size)))



screen = pygame.display.set_mode((map_size[0]*sq_size+map_size[0],map_size[1]*sq_size+map_size[1]+timer_width))

pygame.display.set_caption("Just a minesweeper")
screen.fill((0,0,0))
pygame.display.flip()

clock = pygame.time.Clock()

screen.blit(mines_counter,(0,0))

map = {}
for i in range(map_size[0]+1):
	for ii in range(map_size[1]+1):
		map[(i,ii)] = [0,0]

for i in range(k_mines):
	yes = True
	while yes:
		x = random.randint(0, map_size[0]-1)
		y = random.randint(0, map_size[1]-1)
		if map[(x,y)][0] == 0:
			map[(x,y)][0] = -1
			yes = False

for i in range(map_size[0]+1):
	for ii in range(map_size[1]+1):
		if map[(i,ii)][0] != -1:
			if ii-1>=0 and map[(i,ii-1)][0] == -1:
				map[(i,ii)][0] += 1
			if ii-1>=0 and i+1<=map_size[0] and map[(i+1,ii-1)][0] == -1:
				map[(i,ii)][0] += 1
			if i+1<=map_size[0] and map[(i+1,ii)][0] == -1:
				map[(i,ii)][0] += 1
			if i+1<=map_size[0] and ii+1<=map_size[1] and map[(i+1,ii+1)][0] == -1:
				map[(i,ii)][0] += 1
			if ii+1<=map_size[1] and map[(i,ii+1)][0] == -1:
				map[(i,ii)][0] += 1
			if i-1>=0 and ii+1<=map_size[1] and map[(i-1,ii+1)][0] == -1:
				map[(i,ii)][0] += 1
			if i-1>=0 and map[(i-1,ii)][0] == -1:
				map[(i,ii)][0] += 1
			if i-1>=0 and ii-1>=0 and map[(i-1,ii-1)][0] == -1:
				map[(i,ii)][0] += 1


running = True
while running:
	clock.tick(60)
	screen.fill((0,0,0))
	if draw_grind(screen, map, map_size, sq_size, mine_img, numbs_img):
		running = False
		print(you_won_title)
		open_mines(screen, map, map_size)
		draw_grind(screen, map, map_size, sq_size, mine_img, numbs_img, colour=False)
		while True:
			pygame.display.update()
			clock.tick(15)
		break
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			#print(pygame.mouse.get_pos())
			sq_x = pygame.mouse.get_pos()[0]//sq_size
			sq_x = (pygame.mouse.get_pos()[0]-sq_x)//sq_size
			sq_y = (pygame.mouse.get_pos()[1]-timer_width)//sq_size
			sq_y = (pygame.mouse.get_pos()[1]-timer_width-sq_y)//sq_size
			sq_xy = (sq_x, sq_y)
			#print(sq_xy)
			#print()
			if sq_x >= 0 and sq_y >= 0:
				if map[sq_xy][1] != 1:
					if event.button == 1:
						if map[sq_xy][1] == -1:
							k_flags += 1
							mines_counter = font.render(str(k_flags), False, (255,255,255))
							map[sq_xy][1] += 1
						else:
							if map[sq_xy][0] == -1:
								running = False
								print(you_lose_title)
								open_mines(screen, map, map_size)
								draw_grind(screen, map, map_size, sq_size, mine_img, numbs_img)
								while True:
									pygame.display.update()
									clock.tick(15)
								break
							check_grind(sq_xy, map, map_size)
					if event.button == 3:
						if map[sq_xy][1] == -1:
							k_flags += 1
							mines_counter = font.render(str(k_flags), False, (255,255,255))
							map[sq_xy][1] += 1
						else:
							k_flags -= 1
							mines_counter = font.render(str(k_flags), False, (255,255,255))
							map[sq_xy][1] -= 1
	screen.blit(mines_counter,(0,0))		
	pygame.display.flip()
pygame.quit()
input()