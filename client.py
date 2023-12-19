import pygame
from network import Network
from props import Ball

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
    b = Ball(300, 300, 5, velocity=(3, 0))
    n = Network()
    p = n.getP()
    
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        p2, ball = n.send([p, b])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        b.move([p, p2])
        redrawWindow(win, p, p2, b)
        
main()