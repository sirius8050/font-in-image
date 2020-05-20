#!/usr/bin/python
import numpy as np
from PIL import Image, ImageFont, ImageDraw
import matplotlib.pyplot as plt


path = './bin/img.jpg'
fontfile = 'C:\Windows\Fonts\simhei.ttf'
text = '朱先志'
init = 15


img = Image.open(path)
# img = np.array(img)
data = np.array(img)
# print(data.shape)
space = Image.new(mode = 'RGB', size = (data.shape[1], data.shape[0]), color=(255, 255, 255))


W = data.shape[1]
H = data.shape[0]
font =  ImageFont.truetype(fontfile,init, 0)
width, height = font.getsize(text)

draw = ImageDraw.Draw(space)
for row in range(int(H / (height + 1))):
    for i in range(int(W / init)):
        data_i = data[row*height:(row+1)*height, i*init: (i+1)* init, :]
        # color = [np.mean(np.mean(data_i, axis=0), axis=0)]
        color = [np.mean(data_i[:, :, i]) for i in range(3)]
        color = [int(color[i]) for i in range(len(color))]

        print(tuple(color))
        draw.text((i*init, row*height), text[i%len(text)], font = font, fill = tuple(color))
        # for j in range(3):
        #     for k in range(3):
        #         draw.text((i*init*3 + k, row*height*3 + j), text[i%len(text)], font = font, fill = tuple(color))
            # draw.text((i*init*3, row*height), text[i%len(text)], font = font, fill = tuple(color))
            # draw.text((i*init*3, row*height), text[i%len(text)], font = font, fill = tuple(color))
        # draw.text((-100, 0), text[i%len(text)], font = font, fill = tuple(color))
space.show()
space.save('./mysmile.jpg')

# space = np.array(space)
# import cv2
# img = cv2.imshow(space)
# img.save('NB.jpg')
# font =  ImageFont.truetype(fontfile,150, 0)
# text = '潘豪的小清清'
# width, height = font.getsize(text)
# print(width, height)

# draw = ImageDraw.Draw(img,)
# draw.text((500,100), 'smile', fill = (255, 0 ,0))
# img.show()




# print(img.shape)