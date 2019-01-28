from PIL import Image
img = Image.open('image.bmp')
pixels = img.load()
x, y = img.size
step = 0.25 * x
print(step)
for i in range(4):
    for j in range(4):
        if i == 3 and j == 3:
            break
        ist = i * step
        jst = j * step
        img.crop([jst, ist, jst + step, ist + step]).save('image{}{}.bmp'.format(i + 1, j + 1))
