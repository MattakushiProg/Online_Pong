import pygame

class Player():
    def __init__(self, x = 10, y = 10, width = 10, height = 70, color = (255, 255, 255)):
        """
        Basic characteristics of class Player
        :param x: x-coordinate of player object
        :type x: int
        :param y: y-coordinate of player object
        :type y: int
        :param width: width of rectangle, which is described in class Player
        :type width: int
        :param height: height of rectangle, which is described in class Player
        :type height: int
        :param color: color of rectangle, which is described in class Player. Includes intensity values for red, green and blue component of pixel
        :type color: typle
        :param rect: coordinates and size of rectangle, which is described in class Player
        :type rect: typle
        :param vel: speed of moving rectangle. Literally the distance, which rectangle is passing during time of one frame
        :type vel: int
        :param yFac: direction of player moving
        :type yFac: int
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 5
        self.yFac = 0 # 1 - вверх (-1) - вниз
        
    def draw(self, win): #Отрисовка ишрока в окне
        """
        Draws rectangle in the window, according on rectangle's characteristics
        """
        pygame.draw.rect(win, self.color, self.rect) # Принимает окно(встроенный объект пайгейма), цвет, координаты, ширина, высота
    
    def move(self):
        """
        Changes coordinates of player object depending on the button which is pushed right now
        :param keys: Button, which is being pushed at the moment
        :type keys:
        """
        keys = pygame.key.get_pressed() # Переменная кей запоминает, какая клавиша нажата
        
        self.yFac = 0
        
        if keys[pygame.K_UP]:
            self.y -= self.vel #Если нажато вверх то уменьшить игрек на фикс длину (1 кадр)
            self.yFac = 1
            
        if keys[pygame.K_DOWN]:
            self.y += self.vel
            self.yFac = -1
            
        if  self.y >= 600 - self.height:
            self.y = 600 - self.height
        if self.y <= 0:
            self.y = 0
        
        self.update()   # Переписать переменную rect 
            
            
    def update(self):
        """
        Updates characteristics of object through changing rect-tuple
        """
        self.rect = (self.x, self.y, self.width, self.height)
