import pygame

class Stats():

    def __init__(self, screen):
        self.screen = screen
        self.exp = 0
        self.health = 3
        self.pixel_font = pygame.font.Font('assets/Spaceship-shooter-gamekit/Fonts/upheavtt.ttf', 50)

        self.font_rect = self.pixel_font.render(self.crutch(), True, (255, 255, 255))
        self.rect = self.font_rect.get_rect()
        self.rect.x = 500
        self.rect.y = 10

        self.hp_rect = self.pixel_font.render('hp ' + str(self.health), True, (255, 255, 255))
        self.rect_hp = self.hp_rect.get_rect()
        self.rect_hp.x = 20
        self.rect_hp.y = 10

    def dead(self, player):
        self.health -= 1
        if self.health <= 0:
            self.exp = 0
            self.font_rect = self.pixel_font.render(self.crutch(), True, (255, 255, 255))
            self.health = 3

        player.x = player.screen_rect.centerx
        player.y = player.screen_rect.bottom
        self.hp_rect = self.pixel_font.render('hp ' + str(self.health), True, (255, 255, 255))


    def plus_score(self, kind_of_enemy):
        match kind_of_enemy:
            case 'small':
                self.exp += 100
            case 'medium':
                self.exp += 300
            case 'big':
                self.exp += 500

        self.font_rect = self.pixel_font.render(self.crutch(), True, (255, 255, 255))

    def crutch(self):
        n = len(str(self.exp))
        if n < 7:
            i = 6 - n
            return i * '0' + str(self.exp)
        else:
            self.exp = 0
            return '000000'

    def draw(self):
        self.screen.blit(self.font_rect, self.rect)

    def draw1(self):
        self.screen.blit(self.hp_rect, self.rect_hp)
        

class Background():

    def __init__(self, screen, y):
        self.screen = screen
        self.image = pygame.image.load('assets/Spaceship-shooter-gamekit/Desert/backgrounds/SpaceShooterAssetPack_BackGrounds2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update_background(self):
        self.y += 0.5
        self.rect.y = self.y

        if self.y >= 1000:
            self.y = -1000
