import pygame
from network import Network
from props import Ball
import pickle

width = 600
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def redrawWindow(win, player, player2, ball):
    win.fill((0, 0, 0))
    player.draw(win)
    player2.draw(win)
    ball.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()[0]
    b = Ball(300, 300, 5, velocity=(2, 0))

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2, ball = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win, p, p2, ball)


main()
