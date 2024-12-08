import pygame
import sys
import random
from constants import *
from player import *
from circleshape import *
from asteroid import *
from AsteroidField import *
from shot import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
rocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, rocks)
AsteroidField.containers = updatable
Shot.containers = (updatable, drawable, bullets)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for obj in updatable:
            obj.update(dt)
        for obj in rocks:
            if obj.collide(player):
                print("Game over!")
                sys.exit()
            for pew in bullets:
                if obj.collide(pew):
                    obj.split()
                    pew.kill()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

