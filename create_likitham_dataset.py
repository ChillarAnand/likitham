import os

from PIL import Image, ImageFont, ImageDraw


mode = 'RGB'
size = (100, 64)

im = Image.new(mode, size)
draw = ImageDraw.Draw(im)

fonts_dir = os.path.expanduser('~/.fonts/')

font_telugu = ImageFont.truetype(os.path.join(fonts_dir, "Vani.ttf"), 28)
text = "నిత్య"
w, h = draw.textsize(text)

# draw.text(((W-w)/2,(H-h)/2), msg, fill="black")
draw.text((10, 10), text, font=font_telugu)


im.show()
