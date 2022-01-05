import pygame
import random
import sqlite3
import time

ColorXButton = (235, 85, 85)
ColorXbutton2 = (250, 105, 105)
ColorYButton = (225, 225, 0)
ColorYButton2 = (240, 240, 4)
ColorButton3 = (119, 221, 119)
ColorButtons3 = (109, 211, 109)
ColorFon = (0, 100, 210)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLLOW = (255, 255, 0)
GREY = (128, 128, 128)
game_state = "True"
running = True
changed_results_lvl_1 = True
changed_results_lvl_2 = True
pygame.init()
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
last_lvl_1 = 0
last_lvl_2 = 0
login = ""
time_lvl_1 = 0
time_lvl_2 = 0
id_player = 0
con = sqlite3.connect('users.db')
cur = con.cursor()
cur.execute(f'SELECT * FROM logins')
value = cur.fetchall()
if value:
    n = value[-1]
    id_player = int(n[0]) + 1
    cur.close()
    con.close()
else:
    pass


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
        # if outline:
        # pygame.draw.rect(drawing, outline, (248, self.y - 2, self.width + 4, self.height + 4), 2)

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
        global login, last_lvl_1, last_lvl_2, id_player
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
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        cur.execute(f'SELECT * FROM logins WHERE login = "{login}" ')
        value = cur.fetchall()
        if value:
            id_player = value[0][0]
            login = value[0][1]
            if value[0][2] is None:
                last_lvl_1 = 0
            else:
                last_lvl_1 = value[0][2]
            if value[0][3] is None:
                last_lvl_2 = 0
            else:
                last_lvl_2 = value[0][3]
        else:
            pass
        return login

    font = pygame.font.SysFont('Times New Roman', 75)
    textbox(font)


rules = Button(ColorButtons3, 240, 300, 240, 75, 50, "Rules")
First = Button(ColorXbutton2, 100, 200, 220, 75, 50, "Start")
Second = Button(ColorYButton2, 400, 200, 220, 75, 50, "Quit")
Continue = Button(ColorXbutton2, 250, 100, 200, 75, 25, "Continue?")
Quit = Button(ColorXButton, 250, 200, 200, 75, 25, "Quit")
Quit_for_rules = Button(ColorXButton, 250, 300, 200, 75, 25, "Quit")
Fin = Button(ColorXButton, 250, 100, 200, 75, 25, 'Finality!')
Starting_text = Button(ColorXButton, 250, 25, 200, 75, 50, f'Hello {login}')
Quit_fin = Button(ColorXButton, 250, 200, 200, 75, 25, "Quit")
last_result_lvl_1 = Button(ColorXButton, 250, 275, 200, 75, 20, f'Last 1 lvl was completed: {last_lvl_1}')
last_result_lvl_2 = Button(ColorXButton, 250, 300, 200, 75, 20, f'Last 2 lvl was completed: {last_lvl_2}')
result_lvl_1 = Button(ColorXButton, 250, 325, 200, 75, 20, f'1 lvl was completed: {time_lvl_1}')
result_lvl_2 = Button(ColorXButton, 250, 350, 200, 75, 20, f'2 lvl was completed: {time_lvl_2}')
result_better = Button(ColorXButton, 250, 250, 200, 75, 20, 'You results better than last!')


def Menu():
    drawing.fill((0, 100, 210))
    Starting_text.write()
    First.draw(drawing, (0, 0, 0))
    Second.draw(drawing, (0, 0, 0))
    rules.draw(drawing, (0, 0, 0))
    pygame.draw.rect(screen, GREY,
                     (240, 300, 240, 75), 4)
    pygame.draw.rect(screen, GREY,
                     (100, 200, 220, 75), 4)
    pygame.draw.rect(screen, GREY,
                     (400, 200, 220, 75), 4)


def Menu2():
    drawing.fill((0, 100, 210))
    Continue.draw(drawing, (0, 0, 0))
    Quit.draw(drawing, (0, 0, 0))


def Rules():  # делала Лиза
    global game_state

    drawing.fill((0, 100, 210))
    WHITE = [255, 255, 255]
    Quit_for_rules.draw(drawing, (0, 0, 0))
    SIZE = [700, 400]
    done = False
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Rules")

    cash = []

    for i in range(50):
        x = random.randrange(0, 700)
        y = random.randrange(0, 400)
        cash.append([x, y])

    clock = pygame.time.Clock()

    while not done:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if game_state == 'rules':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Quit_for_rules.positions(pos):
                        game_state = 'True'
                        done = True
            if event.type == pygame.QUIT:
                done = True

        drawing.fill((0, 100, 210))
        for i in range(len(cash)):

            pygame.draw.circle(screen, WHITE, cash[i], 4)

            cash[i][1] += 1

            if cash[i][1] > 400:
                y = random.randrange(-50, -10)
                cash[i][1] = y
                x = random.randrange(0, 700)
                cash[i][0] = x
        f1 = pygame.font.SysFont('Times New Roman',
                                 35)
        text1 = f1.render('Стрелять на левую кнопку мыши',
                          1,
                          (0, 0, 0))
        text2 = f1.render('Двигаться с помощью компьютерной мыши',
                          1,
                          (0, 0, 0))
        text3 = f1.render('Желаем удачи !',
                          1,
                          (0, 0, 0))
        Quit_for_rules.draw(drawing, (0, 0, 0))

        screen.blit(text1, (10, 50))
        screen.blit(text2, (10, 90))
        screen.blit(text3, (10, 130))
        pygame.draw.rect(screen, GREY,
                         (250, 300, 200, 75), 4)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(20)
    game_state = 'True'


def Finallity():
    drawing.fill((0, 100, 210))
    Quit_fin.draw(drawing, (0, 0, 0))
    Fin.write()

    if True:
        if not changed_results_lvl_1 and not changed_results_lvl_2:
            result_better.write()
            result_lvl_1.write()
            result_lvl_2.write()
            # Подключение к БД
            con = sqlite3.connect("users.db")

            # Создание курсора
            cur = con.cursor()

            # Выполнение запроса и получение всех результатов
            cur.execute(f"""INSERT OR REPLACE INTO logins (id, login, lvl_1, lvl_2) 
                            VALUES ('{id_player}', '{login}', '{time_lvl_1}', '{time_lvl_2}')""")

            con.commit()
            cur.close()
            con.close()
        if changed_results_lvl_1 and changed_results_lvl_2:
            result_lvl_1.write()
            result_lvl_2.write()
            last_result_lvl_1.write()
            last_result_lvl_2.write()
    print(time_lvl_1)
    print(time_lvl_2)


def Game_lvl1():
    global game_state, login, time_lvl_1, changed_results_lvl_1

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
    text2 = f2.render(f"Score:{score}..............Player:{login}",
                      True,
                      (250, 200, 0))
    screen.blit(text2, (0, 0))
    player.rect.y = 370
    tic = time.perf_counter()
    while not runnning:
        if score == 75:
            toc = time.perf_counter()
            time_lvl_1 = toc - tic
            runnning = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runnning = True
                pygame.quit()
                quit()
            # add god_mode (for skip test)
            elif event.type == pygame.K_5:
                toc = time.perf_counter()
                time_lvl_1 = toc - tic
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
            toc = time.perf_counter()
            time_lvl_1 = toc - tic
            runnning = True
        f2 = pygame.font.SysFont('serif', 30)
        text2 = f2.render(f"Score: {score} .............. Player: {login}", False,
                          (0, 0, 0))
        screen.blit(text2, (0, 0))
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    if float(last_lvl_1) > float(time_lvl_1):
        # Подключение к БД
        con = sqlite3.connect("users.db")

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        cur.execute(f"""INSERT OR REPLACE INTO logins (id, login, lvl_1, lvl_2) 
                            VALUES ('{id_player}', '{login}', '{time_lvl_1}', '{time_lvl_2}')""")

        con.commit()
        cur.close()
        con.close()
        changed_results_lvl_1 = False
    elif last_lvl_1 == 0 and time_lvl_1 != 0:
        con = sqlite3.connect("users.db")

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        cur.execute(f"""INSERT OR REPLACE INTO logins (id, login, lvl_1, lvl_2) 
                                    VALUES ('{id_player}', '{login}', '{time_lvl_1}', '{time_lvl_2}')""")

        con.commit()
        cur.close()
        con.close()
        changed_results_lvl_1 = False
    else:
        pass
    game_state = 'continue'


def Game_lvl2():
    global game_state, login, time_lvl_2, changed_results_lvl_2

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
    tic = time.perf_counter()

    while not runnning:
        if score == 50:
            toc = time.perf_counter()
            time_lvl_2 = toc - tic
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
            toc = time.perf_counter()
            time_lvl_2 = toc - tic
            runnning = True

        f2 = pygame.font.SysFont('serif', 30)
        text2 = f2.render(f"Score: {score}.............. Player: {login}", False,
                          (0, 0, 0))
        screen.blit(text2, (0, 0))
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    if float(last_lvl_2) > float(time_lvl_2):
        # Подключение к БД
        con = sqlite3.connect("users.db")

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        cur.execute(f"""INSERT OR REPLACE INTO logins (id, login, lvl_1, lvl_2) 
                                VALUES ('{id_player}', '{login}', '{time_lvl_1}', '{time_lvl_2}')""")

        con.commit()
        cur.close()
        con.close()
        changed_results_lvl_2 = False
    elif last_lvl_2 == 0 and float(time_lvl_2) != 0:
        # Подключение к БД
        con = sqlite3.connect("users.db")

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        cur.execute(f"""INSERT OR REPLACE INTO logins (id, login, lvl_1, lvl_2) 
                                        VALUES ('{id_player}', '{login}', '{time_lvl_1}', '{time_lvl_2}')""")

        con.commit()
        cur.close()
        con.close()
        changed_results_lvl_2 = False
    else:
        pass
    game_state = 'final'


while running:
    if game_state == "True":
        Menu()
    elif game_state == "game_1":
        Game_lvl1()
    elif game_state == 'rules':
        Rules()
    elif game_state == 'continue':
        Menu2()
        pygame.draw.rect(screen, GREY,
                         (250, 200, 200, 75), 4)
        pygame.draw.rect(screen, GREY,
                         (250, 100, 200, 75), 4)
    elif game_state == 'game_2':
        Game_lvl2()
    elif game_state == 'final':
        Finallity()
        pygame.draw.rect(screen, GREY,
                         (250, 200, 200, 75), 4)
    pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if game_state == 'rules':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Quit_for_rules.positions(pos):
                    game_state = 'True'
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
                if rules.positions(pos):
                    game_state = 'rules'
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

        if event.type == pygame.MOUSEMOTION:
            if First.positions(pos):
                First.color = ColorXButton
            else:
                First.color = ColorXbutton2
            if Second.positions(pos):
                Second.color = ColorYButton
            else:
                Second.color = ColorYButton2
            if rules.positions(pos):
                rules.color = ColorButtons3
            else:
                rules.color = ColorButton3
print(time_lvl_1)
print(time_lvl_2)
