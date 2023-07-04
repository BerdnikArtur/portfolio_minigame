import pygame

class Menu:

    def __init__(self):
        self.option_surfaces = []
        self.callback = []
        self.current_index = 0
        self.color = (255, 255, 255)
        self.pixel_font = pygame.font.Font('assets/Spaceship-shooter-gamekit/Fonts/upheavtt.ttf', 50)

    def append_option(self, option, callback):
        self.option_surfaces.append(self.pixel_font.render(option, True, self.color))
        self.callback.append(callback)

    def switch(self, direction):
        self.current_index = max(0, min(self.current_index + direction, len(self.option_surfaces) - 1))

    def select(self):
        self.callback[self.current_index]()

    def draw(self, screen, x, y, option_y_padding):
        for i, option in enumerate(self.option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self.current_index:
                pygame.draw.rect(screen, (20, 20, 20), option_rect)
            screen.blit(option, option_rect)