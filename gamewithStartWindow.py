import pygame
import random

ColorXButton = (250, 105, 105)
ColorXbutton2 = (171, 168, 9);
ColorYButton = (200, 80, 51)
ColorYButton2 = (240, 240, 4)
ColorFon = (0, 100, 210)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

game_state = "True"
running = True


class Button():
    def __init__(self, color, x, y, width, height, text=''):
        global drawing
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        pygame.init()
        drawing = pygame.display.set_mode((800, 600))
        drawing.fill(ColorFon)

    def draw(self, drawing, outline=None):
        if outline:
            pygame.draw.rect(drawing, outline, (278, self.y - 2, self.width + 4, self.height + 4), 2)

        pygame.draw.rect(drawing, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('Times New Roman', 80)
            text = font.render(self.text, 1, (0, 0, 0))
            drawing.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def positions(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


First = Button(ColorXbutton2, 280, 190, 250, 100, "Start")
Second = Button(ColorXButton, 280, 310, 250, 100, "Quit")


def Menu():
    drawing.fill((0, 100, 210))
    First.draw(drawing, (0, 0, 0))
    Second.draw(drawing, (0, 0, 0))


def Game():
    drawing.fill((0, 0, 0))

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
    runnning = False
    clock = pygame.time.Clock()
    score = 0
    player.rect.y = 370

    while not runnning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runnning = True

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
                f2 = pygame.font.SysFont('serif', 90)
                text2 = f2.render("Score!", False,
                                  (250, 200, 0))
                screen.blit(text2, (200, 200))
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


while running:
    if game_state == "True":
        Menu()
    elif game_state == "game":
        Game()
    pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if game_state == "True":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if First.positions(pos):
                    game_state = "game"
                if Second.positions(pos):
                    run = False
                    pygame.quit()
                    quit()

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

            if event.type == pygame.MOUSEMOTION:
                if First.positions(pos):
                    First.color = ColorXButton
                else:
                    First.color = ColorYButton
                if Second.positions(pos):
                    Second.color = ColorYButton
                else:
                    Second.color = ColorYButton2