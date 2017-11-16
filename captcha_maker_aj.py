"""
Project : Captcha maker
Author : Ajeet
Date : 16/11/2017
"""
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageFilter

#Generating Captcha

def gen_captcha(text, font, font_size, file_name, FORMAT='JPEG'):
	"""Generate a captcha image"""
	# randomly select the foreground color
	fgcolor = random.randint(0,0xffff00)
	
	# make the background color the opposite of fgcolor
	bgcolor = fgcolor ^ 0xffffff
	
	# create a font object 
	font1 = ImageFont.truetype(font,font_size)
	
	# determine dimensions of the text
	dim = font1.getsize(text)
	
	# create a new image slightly larger that the text
	im = Image.new('RGB', (dim[0]+5,dim[1]+5), bgcolor)
	d = ImageDraw.Draw(im)
	x, y = im.size
	r = random.randint
	
	# draw 100 random colored boxes on the background
	for num in range(100):
		d.rectangle((r(0,x),r(0,y),r(0,x),r(0,y)),fill=r(0,0xffffff))
		
	# add the text to the image
	d.text((3,3), text, font=font1, fill=fgcolor)
	im = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
	
	# save the image to a file
	im.save(file_name, format=FORMAT)


#Generating random words everytime
def gen_random_word(wordLen=6):
        allowedChars = "0123456789abcdefghijklmnopqrstuvwzyzABCDEFGHIJKLMNOPQRSTUVWZYZ"
        word = ""
        for i in range(0, wordLen):
                word = word + allowedChars[random.randint(0,0xffffff) % len(allowedChars)]

        return word
        



"""Example: This grabs a random word and generates a jpeg image named 'test1.jpg' using
the truetype font 'arial.ttf' with a font size of 70.
"""
word = gen_random_word()
gen_captcha(word.strip(), 'arial.ttf', 70, "test1.jpg")
