from PIL import Image, ImageDraw


# Пустой желтый фон.
im = Image.new('RGB', (500, 300), 'white')
draw = ImageDraw.Draw(im)

r=10
x=0
y=0
draw.ellipse((x-r, y-r, x+r, y+r), outline=0)



im.show()
