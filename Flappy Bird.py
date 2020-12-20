import pygame, sys, random

def draw_floor():
	screen.blit(floor_serface, (floor_x_pos, 620))
	screen.blit(floor_serface, (floor_x_pos + 403, 620))

def create_pipe():
	random_pipe_pos = random.choice(pipr_height)
	bottom_pipe = pipe_surface.get_rect(midtop = (500, random_pipe_pos))
	top_pipe = pipe_surface.get_rect(midtop = (500, random_pipe_pos - 640))
	return top_pipe, bottom_pipe

def move_pipe(pipes):
	for pipe in pipes:
		pipe.centerx -=5
	return pipes

def draw_pipes(pipes):
	for pipe in pipes:
		if pipe.bottom >= 716:
			screen.blit(pipe_surface, pipe)
		else:
			flip_pipe = pygame.transform.flip(pipe_surface, False, True)
			screen.blit(flip_pipe, pipe)

def check_col(pipes):
	for pipe in pipes:
		if bird_rect.colliderect(pipe):
			return False

	if bird_rect.top <= -150 or bird_rect.bottom >= 620:
		return False

	return True



pygame.init()
screen = pygame.display.set_mode((403, 716))
clock = pygame.time.Clock()

#Game physics
gravity = 0.25
bird_move = 0
game_active = True

back_ground = pygame.image.load('assets/background-day.png').convert()
back_ground = pygame.transform.scale(back_ground, (403, 716))

floor_serface = pygame.image.load('assets/base.png').convert()
floor_serface = pygame.transform.scale(floor_serface, (470, 156))
floor_x_pos = 0

bird_surf = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_surf = pygame.transform.scale(bird_surf, (48, 34))
bird_rect = bird_surf.get_rect(center = (70, 358))

pipe_surface = pygame.image.load('assets/pipe-green.png')
pipe_surface = pygame.transform.scale(pipe_surface, (72, 420))
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipr_height = [330, 400, 500, 570]

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type ==pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and game_active == True:
				bird_move = 0
				bird_move -= 9
			if event.key == pygame.K_SPACE and game_active == False:
				game_active = True
				pipe_list.clear()
				bird_rect.center = (70, 358)
				bird_move = 0

		if event.type ==SPAWNPIPE:
			pipe_list.extend(create_pipe())

	screen.blit(back_ground,(0, 0))
	if game_active:
		#bird
		bird_move += gravity
		bird_rect.centery += bird_move
		screen.blit(bird_surf, bird_rect)
		game_active = check_col(pipe_list)

		#pipes
		pipe_list = move_pipe(pipe_list)
		draw_pipes(pipe_list)


	#floor
	floor_x_pos -= 1
	draw_floor()
	if floor_x_pos <= -403:
		floor_x_pos = 0


	pygame.display.update()
	clock.tick(60)
