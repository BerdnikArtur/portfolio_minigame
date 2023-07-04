import pygame, sys
from bullet import EnemySmallBullet, EnemyBigBullet, PlayerBullet
from enemy import Explosion, EnemySmall, EnemyMedium, EnemyBig
import random

def events(screen, player1, bullets, main_menu, past_bg, past_bg1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1.movement1 = True
            elif event.key == pygame.K_RIGHT:
                player1.movement2 = True
            elif event.key == pygame.K_DOWN:
                player1.movement3 = True
            elif event.key == pygame.K_LEFT:
                player1.movement4 = True
            elif event.key == pygame.K_SPACE:
                new_bullet = PlayerBullet(screen, player1, 'bolts')
                bullets.add(new_bullet)
            elif event.key == pygame.K_ESCAPE:
                pygame.mixer.music.stop()
                main_menu(past_bg.y, past_bg1.y)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player1.movement1 = False
            if event.key == pygame.K_RIGHT:
                player1.movement2 = False
            if event.key == pygame.K_DOWN:
                player1.movement3 = False
            if event.key == pygame.K_LEFT:
                player1.movement4 = False

def update(screen, FPS, player1, enemies, bullets, bullets_enemy, clock, background, background1, explosions, stats):
    screen.fill((0, 0, 0))
    background.draw()
    background1.draw()
    player1.output()
    for bullet in bullets.sprites():
        bullet.draw()
    for enemy in enemies.sprites():
        enemy.draw()
    for explosion in explosions.sprites():
        explosion.draw()
    for bullet in bullets_enemy.sprites():
        bullet.draw()
    stats.draw()
    stats.draw1()

    pygame.display.flip()
    clock.tick(FPS)

def update_enemies(screen, stats, enemies, player, explosions):
    enemies.update()

    collisions = pygame.sprite.spritecollideany(player, enemies)
    if collisions:
        enemies.remove(collisions)
        exp = Explosion(screen, collisions.x, collisions.y)
        explosions.add(exp)
        death(screen, stats, player, explosions)

    for enemy in enemies.copy():
        if enemy.rect.y >= 1000:
            enemies.remove(enemy)

def death(screen, stats, player, explosions):
    exp = Explosion(screen, player.x - 32, player.y - 72)
    explosions.add(exp)
    stats.dead(player)

def create_enemy(screen, timer, enemies, bullets_enemy, player):
    if timer == 0 or timer % 2 == 0:
        kinds = [EnemySmall, EnemyMedium, EnemyBig]
        if timer > 120:
            for i in range(5):
                enemy = kinds[random.randint(0, 2)](screen)
                enemies.add(enemy)
        elif timer > 60:
            for i in range(3):
                enemy = kinds[random.randint(0, 1)](screen)
                enemies.add(enemy)
        else:
            enemy = EnemySmall(screen)
            enemies.add(enemy)
        for enemy in enemies.sprites():
            if random.randint(0, 3) == 0 and enemy.kind == 'small':
                bullet = EnemySmallBullet(screen, enemy, 'ball')
                bullets_enemy.add(bullet)
            if random.randint(0, 3) == 0 and enemy.kind == 'big':
                bullet = EnemyBigBullet(screen, enemy, 'ball')
                bullets_enemy.add(bullet)
                bullet.self_homing(player)

def update_bullets(bullets, screen, stats, explosions, enemies=None, player=None):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= -500 or bullet.rect.bottom >= 1000:
            bullets.remove(bullet)
        elif bullet.rect.centerx <= 0 or bullet.rect.centerx >= 700:
            bullets.remove(bullet)    

    if enemies:
        collisions = pygame.sprite.groupcollide(enemies, bullets, True, True)
        if collisions:
            enemy = list(collisions.keys())[0]
            exp = Explosion(screen, enemy.x, enemy.y)
            explosions.add(exp)
            stats.plus_score(enemy.kind)
    elif player:
        collisions = pygame.sprite.spritecollideany(player, bullets)
        if collisions:
            bullets.remove(collisions)
            death(screen, stats, player, explosions)


def update_background(background, background1):
    background.update_background()
    background1.update_background()