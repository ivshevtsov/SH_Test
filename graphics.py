from PIL import Image, ImageDraw


# Пустой желтый фон.
im = Image.new('RGB', (11111, 11111), 'white')
draw = ImageDraw.Draw(im)

r=50
pitch=180
delta=100
x=0
y=0
for y in range(61):
    for x in range(61):
        draw.ellipse((x*pitch+delta, y*pitch+delta, x*pitch+r+delta, y*pitch+r+delta), 'red')

im.show()
