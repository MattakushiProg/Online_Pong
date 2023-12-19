import pygame

class Ball:
    def __init__(self, start_x, start_y, radius, color=(255, 255, 255), velocity=(0, 0)):
        self.cords = start_x, start_y
        self.radius = radius
        self.color = color
        self.velocity = velocity

    def draw(self, window):
        pygame.draw.circle(window, color=self.color, center=self.cords, radius=self.radius)
        print(self.cords)

    def deflect(self, surf, prop=None):
        if surf == "x":
            self.velocity = self.velocity[0], -self.velocity[1]
        elif surf == "y":
            self.velocity = -self.velocity[0], self.velocity[1]
        if prop is not None:
            self.velocity = self.velocity[0], self.velocity[1] + 1 * prop.vel

    def check_collision(self, prop):
        if prop.x <= self.cords[0] <= prop.x + prop.width and prop.y <= self.cords[1] <= prop.y + prop.height:
            return True
        return False

    def move_forward(self):
        self.cords = self.cords[0] + self.velocity[0], self.cords[1] + self.velocity[1]

    def move(self, game_props):
        for prop in game_props:
            if self.check_collision(prop):
                self.deflect("y", prop)

        if not 0 < self.cords[0] < 600:
            self.deflect("y")
        if not 0 < self.cords[1] < 600:
            self.deflect("x")
        self.move_forward()

    def serialize(self) -> str:
        return f"|{self.cords}:{self.velocity}"
