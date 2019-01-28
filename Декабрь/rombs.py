import pygame


def romb(x, y, diag):
    return [(x + diag // 2, y), (x + diag, y + diag // 2),
            (x + diag // 2, y + diag), (x, y + diag // 2)]


def draw():
    screen.fill(pygame.Color('yellow'))
    for i in range(height // N):
        for x in range(width // N):
            pygame.draw.polygon(screen, pygame.Color('orange'), romb(N * x, N * i, N))


pygame.init()

size = width, height = 155, 155
N = int(input())

screen = pygame.display.set_mode((width, height))
draw()
pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass