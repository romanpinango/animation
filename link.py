import pygame
import sys


def get_sprite(sheet, x, y, width, height):
    # Create a new surface for the sprite
    sprite = pygame.Surface((width, height), pygame.SRCALPHA)
    # Blit the sprite from the sheet onto this surface
    sprite.blit(sheet, (0, 0), (x, y, width, height))
    return sprite


class Link(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.sprites_down = []
		self.sprites_up = []
		self.sprites_right = []
		self.sprites_left = []
		self.is_moving = False
		sprite_sheet = pygame.image.load("img/links.gif").convert_alpha()
		sprite_width = 100  # Set the width of each sprite
		sprite_height = 100  # Set the height of each sprite
		sheet_height = 100
		sheet_width = 3200

		for row in range(sheet_height // sprite_height):
			for col in range(sheet_width // sprite_width):
				x = col * sprite_width
				y = row * sprite_height
				sprite = get_sprite(sprite_sheet, x, y, sprite_width, sprite_height)
				if col < 8:
					self.sprites_right.append(sprite)
				elif col < 16:
					self.sprites_down.append(sprite)
				elif col < 24:
					self.sprites_left.append(sprite)
				else:
					self.sprites_up.append(sprite)
		self.current_sprite = 0
		self.direction = "DOWN"
		self.image = self.sprites_down[self.current_sprite]
		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x, pos_y]
		self.link_speed = 2

	def start(self):
		self.is_moving = True

	def stop(self):
		self.is_moving = False

	def update(self, speed):
		if self.is_moving:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites_up):
				self.current_sprite = 0

		if self.direction == "DOWN":
			self.image = self.sprites_down[int(self.current_sprite)]
		if self.direction == "UP":
			self.image = self.sprites_up[int(self.current_sprite)]
		if self.direction == "RIGHT":
			self.image = self.sprites_right[int(self.current_sprite)]
		if self.direction == "LEFT":
			self.image = self.sprites_left[int(self.current_sprite)]

	def move(self, direction):
		move_x = 0
		move_y = 0
		self.direction = direction
		if self.direction == "DOWN":
			move_y = self.link_speed
		if self.direction == "UP":
			move_y = self.link_speed * -1
		if self.direction == "RIGHT":
			move_x = self.link_speed
		if self.direction == "LEFT":
			move_x = self.link_speed * -1
		self.rect.topleft = [self.rect.x + move_x, self.rect.y + move_y]


# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Link(100, 0)
moving_sprites.add(player)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			player.start()
		elif event.type == pygame.KEYUP:
			player.stop()

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		player.move("LEFT")
	if keys[pygame.K_RIGHT]:
		player.move("RIGHT")
	if keys[pygame.K_UP]:
		player.move("UP")
	if keys[pygame.K_DOWN]:
		player.move("DOWN")

	# Drawing
	screen.fill((0, 0, 0))
	moving_sprites.draw(screen)
	moving_sprites.update(0.25)
	pygame.display.flip()
	clock.tick(60)

