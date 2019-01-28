import pygame


def draw():
    screen.fill(pygame.Color('white'))
    for i in range(height // (b_height + white_space) + 2):
        coef = 15 if i % 2 == 1 else 0
        for x in range(width // (b_width + white_space) + 2):
            pygame.draw.rect(screen, pygame.Color('red'), pygame.Rect(
                (b_width + white_space) * x - coef, (b_height + white_space) * i, b_width, b_height))


pygame.init()

size = width, height = 300, 200
brick_size = b_width, b_height = 30, 15
white_space = 2

screen = pygame.display.set_mode((width, height))
draw()
pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass