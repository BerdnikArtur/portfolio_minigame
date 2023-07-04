import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, unit, kind):
        super(Bullet, self).__init__()
        self.screen = screen
        self.animation = [pygame.image.load(f'assets/Spaceship-shooter-gamekit/spritesheets/lazer_and_power-up/laser-{kind}{i}.png') for i in range(1, 3)]
        self.image = self.animation[0]
        self.rect = self.image.get_rect()

        self.rect.x = unit.x
        self.rect.y = unit.y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.frame = 0
        self.last_output = pygame.time.get_ticks()
        self.frame_rate = 200

    def draw(self): 
        now = pygame.time.get_ticks()
        if now - self.last_output > self.frame_rate:
            self.last_output = now
            self.frame += 1
            if self.frame == len(self.animation):
                self.frame = 0

            self.image = self.animation[self.frame]

        self.screen.blit(self.image, self.rect)

class PlayerBullet(Bullet):
    def __init__(self, screen, player, type):
        super().__init__(screen, player, type)

        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        '''bullet's movement'''
        self.y -= 5
        self.rect.y = self.y

class EnemySmallBullet(Bullet):
    def __init__(self, screen, enemy, type):
        super().__init__(screen, enemy, type)

    def update(self):
        self.y += 5
        self.rect.y = self.y

class EnemyBigBullet(Bullet):
    def __init__(self, screen, enemy, type):
        super().__init__(screen, enemy, type)

        self.b = 0
        self.k = 0

    def self_homing(self, player):
        try :
            self.k = (self.y - player.y) / (self.x - player.x)
            self.b = player.y - self.k * player.x
        except ZeroDivisionError:
            self.k = (self.y - player.y) / (self.x - player.x) + 1 # +1 --- float division by zero
            self.b = player.y - self.k * player.x

    def update(self):
        self.y += 10
        self.rect.y = self.y

        self.x = (self.y - self.b) / self.k
        self.rect.x = self.x