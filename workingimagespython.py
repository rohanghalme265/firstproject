from PIL import Image

mac = Image.open('example.jpg')
print(type(mac))                  #<class 'PIL.JpegImagePlugin.JpegImageFile'>
# # mac.show()
print(mac.size)                   #(1500, 1099)
print(mac.filename)               #example.jpg
print(mac.format_description)     #JPEG (ISO 10918)
# mac.crop((0,0,1000,1000)).show()

#
pencil = Image.open('pencil.jpg.jpeg')
print(type(pencil))
# pencil.show()
print(pencil.size)

x1 = 0
y1 = 0
w1 = 3000 / 2
h1 = 2827 / 10
# pencil.crop((x,y,w,h)).show()

print(mac.size)
halfway = 1500/2

x = halfway - 200
w = halfway + 200
y = 800
h = 1099
# mac.crop((x,y,w,h)).show()

#
computer = mac.crop((x,y,w,h))
mac.paste(im=computer,box=(100,0))
# mac.show()

# mac.resize((2000,2000)).show()
# mac.rotate(90).show()

red = Image.open('red.jpg')
# red.show()

blue = Image.open('blue.png')
# blue.show()
# blue.putalpha(0)
blue.putalpha(128)
# blue.show()

red.putalpha(128)
# red.show()

#
blue.paste(im=red,box=(0,0),mask=red)
# blue.show()

blue.save("purple.png")
purple = Image.open("purple.png")
# purple.show()


############################################
# IMAGE EXERCISE:-

from PIL import Image
word = Image.open('word_matrix.png')
mask = Image.open('mask.png')




























































































































































































































