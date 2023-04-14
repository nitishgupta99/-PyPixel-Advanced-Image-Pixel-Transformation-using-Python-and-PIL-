# Mountain Climbers
# Nitish Gupta
# Python RGB Image Processor

import time

t7 = time.time()
t0 = time.time()
from PIL import Image

t1 = time.time()
print(t1 - t0)


# Define is_red function
def is_red(r, g, b):
	return (0 <= r <= 70 and 20 <= g <= 190 and 169 <= b <= 300)


# Load image
t3 = time.time()
image_mountain = Image.open("Mountain.jpeg").load()
image_ballon = Image.open("ballon.jpeg").load()
#print(image_ballon[0,0])

r = image_ballon[0, 0][0]
g = image_ballon[0, 0][1]
b = image_ballon[0, 0][2]
t4 = time.time()
#print(is_red(r,g,b))

# Create output canvas
image_output = Image.open("ballon.jpg")

# Get width and height of image
width = image_output.width
height = image_output.height
#print(width,height)
t5 = time.time()
for i in range(width):
	for j in range(height):
		r = image_ballon[i, j][0]
		g = image_ballon[i, j][1]
		b = image_ballon[i, j][2]
		if is_red(r, g, b):
			xy = (i, j)
			color = image_mountain[i, j]
			image_output.putpixel(xy, color)
image_output.save("Result.png", "png")
t6 = time.time()
t8 = time.time()
print("It took " + str(t1 - t0) + " seconds for import")
print("It took " + str(t4 - t3) + " seconds for image load")
print("It took " + str(t6 - t5) + " seconds for the loop ")
print("It took " + str(t8 - t7) + " seconds total")

print("Checkout the output in the file named: " + "Result.png")
