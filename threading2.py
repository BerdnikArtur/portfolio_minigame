import controls
import time
import pygame

def timer_game(enemies, bullets_enemy, play, screen, player):
            if play == True:
                timer = 0
                time.sleep(1.5)
                pygame.mixer.music.load('assets/Spaceship-shooter-gamekit/music/spaceship_shooter.mp3')
                pygame.mixer.music.play(-1)

                while True:
                    controls.create_enemy(screen, timer, enemies, bullets_enemy, player)
                    time.sleep(1)
                    timer += 1