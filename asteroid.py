import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_angle = random.uniform(20,50)
        new_vector_1 = self.velocity.rotate(new_angle)
        new_vector_2 = -new_vector_1
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        child_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        child_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        child_asteroid_1.velocity = new_vector_1 * 1.2
        child_asteroid_2.velocity = new_vector_2 * 1.2
