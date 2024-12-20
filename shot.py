import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, vector, velocity):
        super().__init__(0, 0, SHOT_RADIUS)
        self.position = vector
        self.velocity = velocity
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
