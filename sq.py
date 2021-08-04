#light back ground dark fonts
import PIL
import textwrap
from PIL import Image,ImageFont,ImageDraw
import os
import random
def draw_on_img(image,text,font,tcolor,text_height):
	draw = ImageDraw.Draw(image)
	image_width,image_height = image.size
	y_text = text_height
	#lines = textwrap.dedent(text)
	lines = textwrap.wrap(text,width=30)
	#print(lines)
	#lines = textwrap.shorten(text,width=40)
	for line in lines:
		line_width,line_height = font.getsize(line)
		draw.text(((image_width-line_width)/2,y_text),line,font=font,fill=tcolor)
		y_text += line_height

	return image

def image_create(path):
	#c1 = random.randrange(0,255)
	#c2 = random.randrange(0,255)
	#c3 = random.randrange(0,255)
	img_list = os.listdir(path)
	i = random.choice(img_list)
	image = Image.open(path+i)

	return image

with open('random_3.txt','r') as f:
	textchars = f.read()

paths = './back/'


text_height = 60
fonted = os.listdir('./fonts/')

list_text = list(textchars.split(" "))
words = [10,15,25,35,30]
colors =[(0,0,0),(128,0,0),(178,34,34),(255,69,0),(255,0,0),(0,100,0),(34,139,34),(25,25,112),(75,0,130),(139,69,19),(160,82,45),(0,128,128)]
for i in range(10):
	tcolor = random.choice(colors)
	w = random.choice(words)
	text1 = ' '.join(random.choice(list_text) for k in range(w))
	font_path = './fonts/'+random.choice(fonted)
	font = ImageFont.truetype(font_path,size=50)
	img = image_create(paths)
	im = draw_on_img(img,text1,font,tcolor,text_height)
	#im = im.resize((1000,700),Image.ANTIALIAS)
	im.save('./sample_res/'+str(i)+'.png')
