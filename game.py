import pygame
import random


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


# serzhana300: verified


class Block(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()

        self.image = pygame.Surface([20, 15])
        self.image.fill(color)

        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)

        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 3


pygame.init()
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
for i in range(50):
    block = Block(BLUE)
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(350)
    block_list.add(block)
    all_sprites_list.add(block)
player = Player()
all_sprites_list.add(player)
done = False
clock = pygame.time.Clock()
score = 0
player.rect.y = 370
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet()
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
    all_sprites_list.update()

    for i in range(10000):
        screen.fill(pygame.Color(WHITE),
                    (random.random() * screen_width,
                     random.random() * screen_height, 1, 1))
    for bullet in bullet_list:

        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()