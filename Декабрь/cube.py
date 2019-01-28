import pygame, colorsys


def hsv2rgb(h, s, v):
    return colorsys.hsv_to_rgb(h, s / 100, v / 100)

def draw():
    color = pygame.Color(0, 0, 0)
    color.hsva = (hue, 100, 75)
    pygame.draw.rect(screen, color,
                     pygame.Rect(coord_x, coord_y, side, side))
    color.hsva = (hue, 100, 100)
    pygame.draw.polygon(screen, color, [(coord_x, coord_y),
                    (side + coord_x, coord_y), (side + coord_x + side / 2, coord_y - side / 2),
                                                        (coord_x + side / 2, coord_y - side / 2)])
    color.hsva = (hue, 100, 50)
    pygame.draw.polygon(screen, color, [(side + coord_x, coord_y),
        (side + coord_x + side / 2, coord_y - side / 2),
        (side + coord_x + side / 2, coord_y - side / 2 + side), (coord_x + side, coord_y + side)])


pygame.init()

size = width, height = 300, 300
side = int(input())
coord_x, coord_y = (width - (side + side / 2)) / 2, (height - side) / 2
hue = int(input())

screen = pygame.display.set_mode((width, height))
draw()
pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass