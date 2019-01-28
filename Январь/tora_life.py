import pygame as pg
import time
import random
from copy import deepcopy


class Board:
    def __init__(self, width, heigth):
        self.width = width
        self.height = heigth
        self.board = [[0] * self.width for _ in range(self.height)]
        self.left = 10
        self.top = 10
        self.cell_size = 10

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        t1 = time.time()
        for i in range(self.height):
            for j in range(self.width):
                color = 0 if self.board[i][j] else 1
                pg.draw.rect(screen, WHITE, [self.left + self.cell_size * j,
                                             self.top + self.cell_size * i, self.cell_size,
                                             self.cell_size], color)
        # print(time.time() - t1)

    def get_cell(self, mouse_pos):
        y_cell = (mouse_pos[1] - self.top) // self.cell_size
        x_cell = (mouse_pos[0] - self.left) // self.cell_size
        if 0 <= x_cell < self.width and 0 <= y_cell < self.height:
            return [y_cell, x_cell]
        return None

    def on_click(self, cell_coords):
        self.paint_one_cell(cell_coords)

    def get_click(self, mouse_pos):
        cell_pos = self.get_cell(mouse_pos)
        if cell_pos is not None:
            self.on_click(cell_pos)

    def paint_one_cell(self, cell_coords):
        act = 0 if self.board[cell_coords[0]][cell_coords[1]] else 1
        color = WHITE if act else BLACK
        self.board[cell_coords[0]][cell_coords[1]] = act
        pg.draw.rect(screen, color, [self.left + self.cell_size * cell_coords[1] + 1,
                                     self.top + self.cell_size * cell_coords[0] + 1,
                                     self.cell_size - 2, self.cell_size - 2])


class Life(Board):

    def next_move(self):
        skip = [[0, 0], [0, self.width + 1], [self.height + 1, 0], [self.height + 1, self.width + 1]]
        copy_board = deepcopy(self.board)
        copy_board.append([0] * self.width)
        copy_board.insert(0,  [0] * self.width)
        for i in range(len(copy_board)):
            copy_board[i].append(0)
            copy_board[i].insert(0, 0)
        print(copy_board, len(copy_board))
        for i in range(self.height + 2):
            for j in range(self.width + 2):
                if [i, j] in skip:
                    continue
                if i == 0 or i >= self.height or j == 0 or j >= self.width or self.board[i][j] == 0:
                    neighbors = 0
                    for x in [-1, 0, 1]:
                        for y in [-1, 0, 1]:
                            if x == y == 0:
                                continue
                            coord = [i + x, j + y]
                            if coord in skip:
                                continue
                            if coord[0] < 1:
                                coord[0] -= 0
                            elif coord[0] > self.height:
                                coord[0] = coord[0] - self.height
                            elif coord[1] < 1:
                                coord[1] -= 0
                            elif coord[1] > self.width:
                                coord[1] = coord[1] - self.width
                            #print(coord, [i, j])
                            if 0 <= coord[0] < self.height and 0 <= coord[1] < self.width:
                                if self.board[coord[0] - 1][coord[1] - 1]:
                                    neighbors += 1
                    if neighbors == 3:
                        copy_board[i][j] = 1
                    else:
                        copy_board[i][j] = 0
                elif self.board[i][j] == 1:
                    neighbors = 0
                    for x in [-1, 0, 1]:
                        for y in [-1, 0, 1]:
                            if x == y == 0:
                                continue
                            coord = [i + x, j + y]
                            if coord[0] < 1:
                                coord[0] -= 0
                            elif coord[0] > self.height:
                                coord[0] = coord[0] - self.height - 1
                            elif coord[1] < 1:
                                coord[1] -= 0
                            elif coord[1] > self.width:
                                coord[1] = coord[1] - self.width - 1
                            if self.board[coord[0] - 1][coord[1] - 1]:
                                neighbors += 1
                    if 1 < neighbors < 4:
                        copy_board[i][j] = 1
                    else:
                        copy_board[i][j] = 0
                if neighbors > 0:
                    print(neighbors, [i, j])

        for c_i, i in enumerate(copy_board):
            for c_j, j in enumerate(i):
                if j == 1:
                    if c_i == 0:
                        copy_board[-2][c_j] = 1
                    elif c_i == self.height - 1:
                        copy_board[1][c_j] = 1
                    elif c_j == 0:
                        copy_board[c_i][-2] = 1
                    elif c_j == self.width - 1:
                        copy_board[c_i][1] = 1
                    else:
                        continue
                    copy_board[c_i][c_j] = 0
        print(copy_board)
        self.board = copy_board


run = True
living = False

BLACK = pg.Color('black')
WHITE = pg.Color('white')

pg.init()
screen = pg.display.set_mode((500, 500))

MYEVENTTIMER = 19

screen.fill(BLACK)

speed = 1000
pg.time.set_timer(MYEVENTTIMER, speed)

board = Life(5, 5)
board.set_view(0, 0, 100)
board.render()

print(board.board)

while run:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.get_click(event.pos)
            elif event.button == 5:
                speed += 50
                pg.time.set_timer(MYEVENTTIMER, speed)
            elif event.button == 4:
                speed -= 50
                pg.time.set_timer(MYEVENTTIMER, speed)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                living = False if living else True

        if event.type == MYEVENTTIMER:
            if living:
                board.next_move()
                screen.fill(BLACK)
                board.render()
            pass
    pg.display.flip()
