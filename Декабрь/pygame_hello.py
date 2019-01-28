import pygame

clrs = [pygame.Color(0, 0, 255), pygame.Color(255, 0, 0), pygame.Color(0, 255, 0)]


def draw():
    global cur_radius
    cur_clr = N % 3
    print(cur_clr)
    if cur_clr == 0:
        cur_clr = 0
    elif cur_clr == 1:
        print('glak')
        cur_clr = -2
    else:
        cur_clr = -1
    for i in range(N):
        pygame.draw.circle(screen, clrs[cur_clr], center, cur_radius)
        cur_radius -= radius
        cur_clr -= 1
        if cur_clr == -4:
            cur_clr = -1


pygame.init()

size = radius, N = int(input()), int(input())

cur_radius = N * radius
center = (cur_radius, cur_radius)
screen = pygame.display.set_mode((cur_radius * 2, cur_radius * 2))
draw()
pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass