import pygame
import sys
import random
pygame.init() # Pygameの初期化

FPS = 30
SCREEN_W, SCREEN_H = (600, 800)
BLOCK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
# screen 設定
SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))
SCREEN.fill(BLOCK)
pygame.display.set_caption("Sprite base")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 60))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_W/2, SCREEN_H/2)
        self.speed = 20

    def update(self):
        # key
        keyslist = pygame.key.get_pressed()
        if keyslist[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if keyslist[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keyslist[pygame.K_UP]:
            self.rect.move_ip(0, -self.speed)
        if keyslist[pygame.K_DOWN]:
            self.rect.move_ip(0, self.speed)

        # 壁に触れたら
        if self.rect.right > SCREEN_W:
            self.rect.right = SCREEN_W
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_H:
            self.rect.bottom = SCREEN_H

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery)
        all_group.add(bullet)
        bullet_group.add(bullet)

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 60))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, SCREEN_W - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randint(2, 10)
        self.speed_x = random.randrange(-3, 3)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        # 石頭到底部的話讓石頭重新回到頂部
        if self.rect.top > SCREEN_H:
          self.rect.x = random.randrange(0, SCREEN_W - self.rect.width)
          self.rect.y = random.randrange(-100, -40)
          self.speed_y = random.randint(2, 10)
          self.speed_x = random.randrange(-3, 3)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 30))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()


player = Player()
# Sprite group 作成
all_group = pygame.sprite.RenderUpdates()
# Sprite 追加
all_group.add(player)

rock_group = pygame.sprite.RenderUpdates()
bullet_group = pygame.sprite.RenderUpdates()

for i in range(8):
    rock = Rock()
    all_group.add(rock)
    rock_group.add(rock)

GAME_FLAG = True
while GAME_FLAG :  # game loop
    SCREEN.fill(BLOCK)
    # Sprite groupを更新
    all_group.update()
    #pygame.sprite.groupcollide(rock_group, bullet_group, True, True)

    hits = pygame.sprite.groupcollide(rock_group, bullet_group, True, True)
    for hit in hits:
        r = Rock()
        all_group.add(r)
        rock_group.add(r)

    hits = pygame.sprite.spritecollide(player, rock_group, False)
    if hits:
        GAME_FLAG = False

    # Spriteを描画
    all_group.draw(SCREEN)

    # screenを更新
    pygame.display.update()
    # pygame.time.wait(30)
    clock.tick(FPS)  # screen(30fps)
    # イベント 処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:    # 閉じるボタンが押されたとき
            GAME_FLAG = False
        if event.type == pygame.KEYDOWN: # キーを押したとき
            if event.key == pygame.K_SPACE:
                player.shoot()
else:
     pygame.quit()                # Pygameの終了(画面閉じられる)
     sys.exit()