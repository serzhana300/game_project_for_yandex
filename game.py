import pygame
import random

ColorXButton = (250, 105, 105)
ColorXbutton2 = (171, 168, 9)
ColorYButton = (200, 80, 51)
ColorYButton2 = (240, 240, 4)
ColorFon = (0, 100, 210)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLLOW = (255, 255, 0)
game_state = "True"
running = True
pygame.init()
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
login = ""

class Button():
    def __init__(self, color, x, y, width, height, size_test, text=''):
        global drawing
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.size = size_test
        pygame.init()
        drawing = pygame.display.set_mode((700, 400))
        drawing.fill(ColorFon)


    def draw(self, drawing, outline=None):
        #if outline:
            #pygame.draw.rect(drawing, outline, (248, self.y - 2, self.width + 4, self.height + 4), 2)

        pygame.draw.rect(drawing, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('Times New Roman', self.size)
            text = font.render(self.text, 1, (0, 0, 0))
            drawing.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def write(self):
        font = pygame.font.SysFont('Times New Roman', self.size)
        text = font.render(self.text, 1, (0, 0, 0))
        drawing.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def positions(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False

    def textbox(font30):
        global login
        f1 = pygame.font.SysFont('Times New Roman', 50)
        f2 = pygame.font.SysFont('Times New Roman', 20)
        screen.fill((0, 100, 210))
        text1 = f1.render('\_ Введите имя игрока _/', 20, (0, 0, 0))
        info = f2.render('*логин должен состоять из 10 или менее символов!', 10, (0, 0, 0))
        screen.blit(info, (130, 350))
        screen.blit(text1, (90, 50))
        input = pygame.Rect(100, 150, 800, 100)
        color_inactive = YELLLOW
        color_active = BLUE
        color = color_inactive
        running = False
        done = False
        font = font30
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if input.collidepoint(event.pos):
                        running = True
                    else:
                        running = False
                    color = color_active if running else color_inactive
                elif event.type == pygame.KEYDOWN:
                    if running:
                        if len(login) >= 11:
                            if event.key == pygame.K_BACKSPACE:
                                login = login[:-1]
                            else:
                                continue
                        if event.key == pygame.K_RETURN:
                            print(login)
                            done = True
                        elif event.key == pygame.K_BACKSPACE:
                            login = login[:-1]
                        else:
                            login += event.unicode

                        print("DEBUG: text is now [%s]" % (login))
                        pygame.display.flip()
            text_surface = font.render(login, True, BLACK)
            width = max(500, text_surface.get_width() + 10)
            input.w = width
            pygame.draw.rect(screen, color, input, 2)
            screen.blit(text_surface, (input.x + 5, input.y + 5))
            pygame.display.flip()

        return login

    font = pygame.font.SysFont('Times New Roman', 75)
    textbox(font)


First = Button(ColorXbutton2, 100, 200, 220, 75, 50, "Start")
Second = Button(ColorXButton, 400, 200, 220, 75, 50, "Quit")
Continue = Button(ColorXbutton2, 250, 100, 200, 75, 25, "Continue?")
Quit = Button(ColorXButton, 250, 200, 200, 75, 25, "Quit")
Fin = Button(ColorXButton, 250, 100, 200, 75, 25, 'Finality!')
Starting_text = Button(ColorXButton, 250, 25, 200, 75, 50, f'Hello {login}')
Quit_fin = Button(ColorXButton, 250, 200, 200, 75, 25, "Quit")


def Menu():
    drawing.fill((0, 100, 210))
    Starting_text.write()
    First.draw(drawing, (0, 0, 0))
    Second.draw(drawing, (0, 0, 0))


def Menu2():
    drawing.fill((0, 100, 210))
    Continue.draw(drawing, (0, 0, 0))
    Quit.draw(drawing, (0, 0, 0))


def Finallity():
    drawing.fill((0, 100, 210))
    Fin.write()
    Quit_fin.draw(drawing, (0, 0, 0))


def Game_lvl1():
    global game_state, login

    class Block(pygame.sprite.Sprite):
        def __init__(self, color):
            super().__init__()

            self.image = pygame.Surface([20, 20])
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
            self.image = pygame.Surface([4, 4])
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

    for i in range(75):
        block = Block(BLUE)
        block.rect.x = random.randrange(0, 670)
        block.rect.y = random.randrange(25, 350)
        block_list.add(block)
        all_sprites_list.add(block)

    player = Player()
    all_sprites_list.add(player)
    runnning = False
    clock = pygame.time.Clock()
    score = 0
    f2 = pygame.font.SysFont('serif', 35)
    text2 = f2.render(f"Score:{score}..............Player:{login}", True,
                      (250, 200, 0))
    screen.blit(text2, (0, 0))
    player.rect.y = 370

    while not runnning:
        if score == 75:
            runnning = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runnning = True
                pygame.quit()
                quit()
            # add god_mode (for skip test)
            elif event.type == pygame.K_5:
                runnning = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                bullet = Bullet()
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
        all_sprites_list.update()
        drawing.fill(WHITE)
        for bullet in bullet_list:

            block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
            for block in block_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                score += 1
                pygame.mixer.music.load('Kik.wav')
                pygame.mixer.music.play()
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
        key = pygame.key.get_pressed()
        # god mod (for creator testing)
        if key[pygame.K_5]:
            runnning = True
        f2 = pygame.font.SysFont('serif', 30)
        text2 = f2.render(f"Score: {score} .............. Player: {login}", False,
                          (0, 0, 0))
        screen.blit(text2, (0, 0))
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    game_state = 'continue'


def Game_lvl2():
    global game_state, login
    class Block(pygame.sprite.Sprite):
        def __init__(self, color):
            super().__init__()

            self.image = pygame.Surface([20, 20])
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
            self.image = pygame.Surface([4, 4])
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
        block.rect.x = random.randrange(0, 670)
        block.rect.y = random.randrange(25, 350)
        block_list.add(block)
        all_sprites_list.add(block)

    player = Player()
    all_sprites_list.add(player)
    runnning = False
    clock = pygame.time.Clock()
    score = 0
    f2 = pygame.font.SysFont('serif', 35)
    text2 = f2.render(f"Score: {score} .............. Player: {login}", False,
                      (250, 200, 0))
    screen.blit(text2, (0, 0))
    player.rect.y = 370

    while not runnning:
        if score == 50:
            runnning = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    event.type == pygame.KEYUP and \
                    event.type == pygame.K_ESCAPE:
                runnning = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                bullet = Bullet()
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
        all_sprites_list.update()
        drawing.fill(WHITE)
        for bullet in bullet_list:

            block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
            for block in block_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                score += 1
                pygame.mixer.music.load('Kik.wav')
                pygame.mixer.music.play()
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
        key = pygame.key.get_pressed()
        # god mod (for creator testing)
        if key[pygame.K_5]:
            runnning = True
        f2 = pygame.font.SysFont('serif', 30)
        text2 = f2.render(f"Score: {score}.............. Player: {login}", False,
                          (0, 0, 0))
        screen.blit(text2, (0, 0))
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    game_state = 'final'


while running:
    if game_state == "True":
        Menu()
    elif game_state == "game_1":
        Game_lvl1()
    elif game_state == 'continue':
        Menu2()
    elif game_state == 'game_2':
        Game_lvl2()
    elif game_state == 'final':
        Finallity()
    pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if game_state == 'continue':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Continue.positions(pos):
                    game_state = 'game_2'
                if Quit.positions(pos):
                    run = False
                    pygame.quit()
                    quit()
        if game_state == "True":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if First.positions(pos):
                    game_state = "game_1"
                if Second.positions(pos):
                    run = False
                    pygame.quit()
                    quit()
        if game_state == 'final':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Quit.positions(pos):
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
