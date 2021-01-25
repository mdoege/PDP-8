#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont

w, h, s = 1300, 562, 60

fnt = ImageFont.truetype('fonts/generic-Medium.otf', 30)

im = Image.open("panel_top.png")

d = ImageDraw.Draw(im)

d.text((575, h - 200 + s), "ACCUMULATOR", font = fnt, fill = (255,255,255,255), align = "center")

d.text((10, h - 200 + s), "LINK", font = fnt, fill = (255,255,255,255), align = "center")

d.text((530, h - 400 + s), "PROGRAM COUNTER", font = fnt, fill = (255,255,255,255), align = "center")

for i in range(5):
    x = 300 * i + 95
    y = h - 100
    d.rectangle([x, y, x + 5, y + 100] , (255,255,255,255) )
    y = h - 300
    d.rectangle([x, y, x + 5, y + 100] , (255,255,255,255) )

im.save("panel.png")

