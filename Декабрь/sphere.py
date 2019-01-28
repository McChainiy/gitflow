import pygame


def draw():
    global cur_height, cur_width
    for i in range(0, N):
        pygame.draw.ellipse(screen, pygame.Color(255, 255, 255), pygame.Rect(
            delta * i / 1, 0, cur_width, 300), 1)
        pygame.draw.ellipse(screen, pygame.Color(255, 255, 255), pygame.Rect(
            0, delta * i / 1, 300, cur_height), 1)
        cur_height -= (delta * 2)
        cur_width -= (delta * 2)


pygame.init()

size = width, height = 300, 300
N = int(input())
cur_width = width
cur_height = height
delta = (300 / N / 2)

screen = pygame.display.set_mode((width, height))
draw()
pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass