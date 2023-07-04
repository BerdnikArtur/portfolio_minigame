import pygame, sys
import threading
import controls
from menu import Menu
from player import Player
from pygame.sprite import Group
from stats import Stats , Background
from threading2 import timer_game

def exit():
    pygame.quit()
    sys.exit()

def main_menu(past_bg=0, past_bg1=-1000):
    pygame.init()
    screen = pygame.display.set_mode((700, 1000))
    pygame.display.set_icon(pygame.image.load("assets/Spaceship-shooter-gamekit/spritesheets/ship/ship_icon.png"))
    pygame.display.set_caption('qwerty')
    FPS = 60
    clock = pygame.time.Clock()

    background =  Background(screen, past_bg)
    background1 =  Background(screen, past_bg1)

    menu = Menu()
    menu.append_option('Start', lambda: start(screen, background.y, background1.y, main_menu))
    menu.append_option('Quit', exit)
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    menu.switch(-1)
                elif event.key == pygame.K_DOWN:
                    menu.switch(1)
                elif event.key == pygame.K_SPACE:
                    menu.select()

        screen.fill((0,0,0))

        controls.update_background(background, background1)
        background.draw()
        background1.draw()

        menu.draw(screen, 150, 300, 75)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

def start(screen, past_bg, past_bg1, main_menu):

    play = True
    FPS = 60

    player1 = Player(screen)
    bullets = Group()
    bullets_enemy = Group()
    enemies = Group()
    explosions = Group()
    stats = Stats(screen)
    clock = pygame.time.Clock() 

    background =  Background(screen, past_bg)
    background1 =  Background(screen, past_bg1)
                
    threading.Thread(target=timer_game, args=(enemies, bullets_enemy, play, screen, player1), daemon=True).start()

    while play:  
        controls.events(screen, player1, bullets, main_menu, background, background1)
        player1.update()
        controls.update_background(background, background1)
        controls.update(screen, FPS, player1, enemies, bullets, bullets_enemy, clock, background, background1, explosions, stats)
        controls.update_bullets(bullets, screen, stats, explosions, enemies=enemies)
        controls.update_bullets(bullets_enemy, screen, stats, explosions, player=player1)
        controls.update_enemies(screen, stats, enemies, player1, explosions)

if __name__ == "__main__":
    main_menu()