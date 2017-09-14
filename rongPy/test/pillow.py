from PIL import Image

img = Image.open("./img/zelda.jpg")
img1 = Image.open("./img/shield.jpg")

area = (50, 15, 125, 90)

cropped_img = img.crop(area)

area1 = (75, 75, 150, 150)
img1.paste(cropped_img, area1)

#img1.show()

#

are2 = (24, 13, 201, 213)

r, g, b = img.split()
r1, g1, b1 = img1.crop(are2).split()
new_img = Image.merge("RGB", (b, g, r))
new_img1 = Image.merge("RGB", (r1, g, b))
#new_img.show()
#new_img1.show()

#

img2 = Image.open("./img/mipha.png")
square_img2 = img2.resize((300, 300))
flip_img2 = img2.transpose(Image.FLIP_LEFT_RIGHT)
spin_img2 = img2.transpose(Image.ROTATE_90)

#square_img2.show()
#flip_img2.show()
#spin_img2.show()

#

from PIL import ImageFilter

bw_img2 = img2.convert("L")
blur = img2.filter(ImageFilter.BLUR)
detail = img2.filter(ImageFilter.DETAIL)
edges = img2.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()
