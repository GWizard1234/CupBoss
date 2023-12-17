import time
import pygame
import random
pygame.init()
background_image = pygame.image.load('fon.png')


back = (200, 255, 255)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()
start_time = time.time()
dx = 3
dy = 3

# генерація списку для координатів монет
list1 = []
a = 120
b = 210
while a <= b:
    list1.append(a)
    a += 1
a = 290
b = 380
while a <= b:
    list1.append(a)
    a += 1

platform_x = 10
platform_y = 330
move_right = False
move_left = False
move_up = False
move_down = False
game_over = False
boss_x = 10
boss_y = 90
bullets_color = (255,0,0)

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)      
    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))





platform = Picture('platform.png', platform_x, platform_y, 30, 50)
boss = Picture("boss.png", boss_x, boss_y, 100,30)
start_x = 5
start_y = 5
count = 9
start_time = time.time()





coin = 0 # змінна для збереження кількості зібраних монет
coins = []
bullets = []
game_over = False
while not game_over:  
    platform.fill()
    boss.fill()

    for d in bullets:
        if platform.rect.colliderect(d):
            game_over = True
    
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_w:
                move_up = True
            if event.key == pygame.K_s:
                move_down = True         
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_w:
                move_up = False
            if event.key == pygame.K_s:
                move_down = False
        
    if move_right:
        platform.rect.x +=3
    if move_left:
        platform.rect.x -=3
    if move_up:
        platform.rect.y -=3
    if move_down:
        platform.rect.y +=3

    # генерація монет
    if len(coins) < 4:
        x = random.choice(list1)
        y = random.choice(list1)
        coins.append(pygame.Rect(x,y,10,10))

    # генерація пуль боса
    if len(bullets) < 40:
        if random.randint(0,100) < 10:
            x = 252
            y = 220
            bullets.append(pygame.Rect(x,y,20,20))

        
    for d in bullets:
        if platform.rect.colliderect(d):
            game = True

    for c in coins:
        if platform.rect.colliderect(c):
            coin += 1
            c.x = random.randint(120,380)
            c.y = random.randint(120,380)
        
    
    
    for d in bullets:
        if d == bullets[0]:
            d.x +=2
            d.y +=2
        elif d == bullets[1]:
            d.y +=2
        elif d == bullets[2]:
            d.y +=2
            d.x -=2
        elif d == bullets[3]:
            d.x -=2
        elif d == bullets[4]:
            d.x -=2
            d.y -=2
        elif d == bullets[5]:
            d.y -=2
        elif d == bullets[6]:
            d.x -=2
            d.y -=2
        elif d == bullets[7]:
            d.x +=2
            d.x +=2
        elif d == bullets[8]:
            d.x +=2
            d.y +=2
            d.y -=2
        elif d == bullets[9]:
            d.y +=2
            d.x -=2
            d.y +=2
            d.x +=2
            d.x -=2
        elif d == bullets[10]:
            d.y +=2
            d.y +=2
            d.y +=2
        elif d == bullets[11]:
            d.y +=2
        elif d == bullets[12]:
            d.y +=2
            d.x -=2
        elif d == bullets[13]:
            d.x -=2
        elif d == bullets[14]:
            d.x -=2
            d.y -=2
        elif d == bullets[15]:
            d.y -=2
        elif d == bullets[16]:
            d.x -=2
            d.y -=2
        elif d == bullets[17]:
            d.x +=2
            d.x +=2
        elif d == bullets[18]:
            d.x +=2
            d.y +=2
            d.y -=2
        elif d == bullets[19]:
            d.y +=2
            d.x -=2
            d.y +=2
            d.x +=2
            d.x -=2
        elif d == bullets[20]:
            d.y +=2
            d.y +=2
            d.y +=2
        
        if d.x > 700 or d.x < -700 or d.y > 700 or d.y < -700:
            d.x = 252
            d.y = 220

        
            
    
    mw.blit(background_image, (0, 0))
    boss.draw()
    platform.draw()
    for b in bullets:
        pygame.draw.rect(mw,bullets_color,b)
    
    for c in coins:
        pygame.draw.rect(mw,(255, 255, 0),c)
    

    t = int(time.time() - start_time)
    f = pygame.font.Font(None,30)
    time_text = f.render(f'Час {t} секунд', True, (255,255,255))
    mw.blit(time_text,(10,10))

    coin_text = f.render(f'Монети: {coin}', True, (255,255,255))
    mw.blit(coin_text,(10,40))

    

   
    pygame.display.update()
    clock.tick(100)