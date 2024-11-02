import pygame
import sys


class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		for i in range(10):
			self.sprites.append(pygame.image.load('img/attack_' + str(i+1) + '.png'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]
		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x, pos_y]

	def attack(self):
		self.attack_animation = True

	def update(self, speed):
		if self.attack_animation:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]

	def move(self, move_x, move_y):
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
player = Player(100, 0)
player2 = Player(100, 50)
player3 = Player(100, 100)
player4 = Player(100, 150)
player5 = Player(100, 200)
moving_sprites.add(player)
moving_sprites.add(player2)
moving_sprites.add(player3)
moving_sprites.add(player4)
moving_sprites.add(player5)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:
				player.attack()
			elif event.key == pygame.K_2:
				player2.attack()
			elif event.key == pygame.K_3:
				player3.attack()
			elif event.key == pygame.K_4:
				player4.attack()
			elif event.key == pygame.K_5:
				player5.attack()
			elif event.key == pygame.K_RIGHT:
				player.move(10, 0)
			elif event.key == pygame.K_LEFT:
				player.move(-10, 0)
			elif event.key == pygame.K_UP:
				player.move(0, -10)
			elif event.key == pygame.K_DOWN:
				player.move(0, 10)

	# Drawing
	screen.fill((0, 0, 0))
	moving_sprites.draw(screen)
	moving_sprites.update(0.25)
	pygame.display.flip()
	clock.tick(60)

