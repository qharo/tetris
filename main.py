import pygame
from game import Game
from drawer import UI

COLOR = {"RED": (255, 0, 0)}


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((1080,720))
    pygame.display.set_caption("Tetris!")
    clock = pygame.time.Clock()
    done = False

    testGame = Game(20, 10)
    testUi = UI(screen)


    margin = 5

    count = 1

    while not done:
        clock.tick(10)
        screen.fill((0,0,0))
        dir = 3

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                dir = 4
            if keys[pygame.K_RIGHT]:
                print(f"right pressed at {count}")
                dir = 2
            if keys[pygame.K_r]:
                print(f"pressed at {count}")
                dir = 5
            if event.type == pygame.QUIT:
                done = True
        
        testGame.update(dir)
        testUi.drawMatrix(testGame.matrix, (40, 100), 3, 27)

        count += 1
        pygame.display.update()

