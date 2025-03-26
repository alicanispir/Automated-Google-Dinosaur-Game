import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dinosaur Game")

dino_image = pygame.image.load("dino.png")
cactus_image = pygame.image.load("cactus.png")

dino_image = pygame.transform.scale(dino_image, (40, 60))
cactus_image = pygame.transform.scale(cactus_image, (40, 60))

class Dino:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT - 60
        self.width = 40
        self.height = 60
        self.jump = False
        self.jump_count = 20

    def update(self):
        if self.jump:
            self.y -= self.jump_count
            self.jump_count -= 1
            if self.jump_count < -20:
                self.jump = False
                self.jump_count = 20
        else:
            if self.y < HEIGHT - 60:
                self.y += self.jump_count
                self.jump_count = 20

    def draw(self):
        screen.blit(dino_image, (self.x, self.y))  # Draw dino image

class Cactus:
    def __init__(self, x_offset):
        self.x = WIDTH + x_offset
        self.y = HEIGHT - cactus_image.get_height()
        self.width = cactus_image.get_width()

    def move(self, speed):
        self.x -= speed

    def draw(self):
        screen.blit(cactus_image, (self.x, self.y))

    def is_off_screen(self):
        return self.x < -self.width

dino = Dino()
cactus_speed = 5
cactus_distance_min = 400
cactus_distance_max = 500
num_cacti = 3

cacti = []
start_x = WIDTH + 100
for _ in range(num_cacti):
    cacti.append(Cactus(start_x))
    start_x += random.randint(cactus_distance_min, cactus_distance_max)

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dino.jump = True

    dino.update()
    dino.draw()

    for cactus in cacti:
        cactus.move(cactus_speed)
        cactus.draw()

        if dino.x + dino.width > cactus.x and dino.x < cactus.x + cactus.width:
            if dino.y + dino.height > cactus.y:
                running = False

    for cactus in cacti:
        if cactus.is_off_screen():
            max_x = max(c.x for c in cacti)
            cactus.x = max_x + random.randint(cactus_distance_min, cactus_distance_max)

    pygame.display.update()
    clock.tick(30)

pygame.quit()