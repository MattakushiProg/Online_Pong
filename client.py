import pygame

width = 600
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(self, x = 10, y = 10, width = 10, height = 70, color = (255, 255, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 5
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
    
    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        
        if keys[pygame.K_UP]:
            self.y -= self.vel
            
        if keys[pygame.K_DOWN]:
            self.y += self.vel
            
        self.rect = (self.x, self.y, self.width, self.height)
            

def redrawWindow(win, player):
    win.fill((0, 0, 0))
    player.draw(win)
    pygame.display.update()
    

def main():
    run = True
    p = Player()
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win, p)
        
main()