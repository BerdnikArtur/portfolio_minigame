import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        
        super(Player, self).__init__()
        self.screen = screen
        self.animation = [pygame.image.load(f'assets/Spaceship-shooter-gamekit/spritesheets/ship/ship{i}.png') for i in range(1, 10)]
        self.image = self.animation[0]

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = self.screen_rect.centerx - 24
        self.rect.y = self.screen_rect.bottom - 72
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.bottom)
        self.movement1 = False
        self.movement2 = False
        self.movement3 = False
        self.movement4 = False

        self.frame = 0
        self.last_output = pygame.time.get_ticks()
        self.frame_rate = 200

    def output(self):
        now = pygame.time.get_ticks()
        if now - self.last_output > self.frame_rate:
            self.last_output = now
            self.frame += 1
            if self.frame == len(self.animation):
                self.frame = 0

            self.image = self.animation[self.frame]

        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.movement1 and self.rect.bottom > 32:
            self.y -= 3
        if self.movement2 and self.rect.right < 700:
            self.x += 3
        if self.movement3 and self.rect.bottom < 1000:
            self.y += 3
        if self.movement4 and self.rect.left > 0:
            self.x -= 3

        self.rect.centerx = self.x
        self.rect.bottom = self.y

