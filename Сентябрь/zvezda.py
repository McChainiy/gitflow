from PIL import Image
img = Image.open('image.png')
pixels = img.load()
x, y = img.size
area = [x - 1, y - 1, 0, 0]
main_color = pixels[0, 0]
for i in range(x):
    for j in range(y):
        if pixels[i, j] != main_color:
            if i < area[0]:
                area[0] = i
            if j < area[1]:
                area[1] = j
            if i > area[2]:
                area[2] = i
            if j > area[3]:
                area[3] = j
area[2] += 1
area[3] += 1
cropped_img = img.crop(tuple(area))
cropped_img.save('res.png')