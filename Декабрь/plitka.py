side = int(input())
x = int(input())
y = int(input())
width = int(input())
height = int(input())

left = x // side + 1
right = (x + width - 1) // side + 1

down = y // side + 1
up = (y + height - 1) // side + 1

abs_width = right - left + 1
abs_height = up - down + 1

print(abs_width * abs_height)