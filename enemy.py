import pygame
import math
import random

class Unit(pygame.sprite.Sprite):
    def __init__(self, screen, kind):
        super(Unit, self).__init__()
        self.screen = screen
        self.kind = kind
        self.animation = [pygame.image.load(f'assets/Spaceship-shooter-gamekit/spritesheets/enemy/enemy-{kind}{i}.png') for i in range(1, 3)]
        self.image = self.animation[0]
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(100, 600) 
        self.rect.y = random.randint(-300, -200) 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.frame = 0
        self.last_output = pygame.time.get_ticks()
        self.frame_rate = 100

    def draw(self):
        now = pygame.time.get_ticks()
        if now - self.last_output > self.frame_rate:
            self.last_output = now
            self.frame += 1
            if self.frame == len(self.animation):
                self.frame = 0

            self.image = self.animation[self.frame]

        self.screen.blit(self.image, self.rect)

class EnemySmall(Unit):
    def __init__(self, screen):
        super().__init__(screen, 'small')

    def update(self):
        self.y += 1.0
        self.rect.y = self.y

class EnemyMedium(Unit):
    def __init__(self, screen):
        super().__init__(screen, 'medium')

        self.rand = random.randint(100, 600)
        self.rand1 = random.randint(10, 30)
        self.rand2 = random.randint(40, 60)

    def update(self):
        self.y += 1.0
        self.rect.y = self.y

        self.x = (self.rand2 * math.sin(self.y / self.rand1)) + self.rand
        self.rect.x = self.x

class EnemyBig(Unit):
    def __init__(self, screen):
        super().__init__(screen, 'big')

        self.speed = random.uniform(4, 6)
        self.big_pause = pygame.time.get_ticks()

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

        now = pygame.time.get_ticks()
        if now - self.big_pause > 10000:
            self.speed *= 1.01
        else:
            self.speed /= 1.01

class Explosion(pygame.sprite.Sprite):

    def __init__(self, screen, x, y):
        super(Explosion, self).__init__()
        self.screen = screen
        self.animation = [pygame.image.load(f'assets/Spaceship-shooter-gamekit/spritesheets/explosion/explosion{i}.png') for i in range(1, 6)]
        self.image = self.animation[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.frame = 0
        self.last_output = pygame.time.get_ticks()
        self.frame_rate = 100

    def draw(self):
        now = pygame.time.get_ticks()

        if now - self.last_output > self.frame_rate:
            self.last_output = now
            self.frame += 1
            if self.frame == len(self.animation):
                self.kill()
                return False

            self.image = self.animation[self.frame]

        self.screen.blit(self.image, self.rect)

