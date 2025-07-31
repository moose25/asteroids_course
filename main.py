import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = updatable, drawable
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000  # Limit to 60 FPS and calculate delta time

        updatable.update(dt)  # Update all updatable objects

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return

            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()  # Remove the shot
                    asteroid.split()  # Split the asteroid

        screen.fill((0, 0, 0))  # Fill the screen with black
        for obj in drawable:  # Draw all drawable objects
            obj.draw(screen)

        pygame.display.flip()  # Refresh the screen


if __name__ == "__main__":
    main()
