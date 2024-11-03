import random

from matplotlib import pyplot as plt
from PIL import Image, ImageDraw
from PIL.ImageFilter import (BLUR, CONTOUR, DETAIL, EDGE_ENHANCE,
                             EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SHARPEN,
                             SMOOTH, SMOOTH_MORE)


def image_read(file_name: str) -> None:
	"""
	Reads an image file and returns its properties.

	This function opens an image, retrieves pixel data, and displays the image.
	For the pixel at coordinates (1, 1), it prints the RGB values.

	Args:
	    file_name (str): The name of the image file to read.

	Returns:
	    dict: A dictionary containing image properties, including:
	        - 'image_file': The loaded image object.
	        - 'image_draw': An ImageDraw object for drawing on the image.
	        - 'image_width': The width of the image.
	        - 'image_height': The height of the image.
	        - 'image_pix': The pixel data of the image.
	"""
	image = Image.open(file_name)
	draw = ImageDraw.Draw(image)
	width = image.size[0]
	height = image.size[1]
	pix = image.load()
	print("START_im", "red=", pix[1, 1][0], "green=", pix[1, 1][1], "blue=", pix[1, 1][2])
	plt.imshow(image)
	plt.show()
	image_info = {"image_file": image, "image_draw": draw, "image_width": width,
				  "image_height": height, "image_pix": pix}

	return image_info


def shades_of_gray(file_name_start: str, file_name_stop: str) -> None:
	"""
	Converts an image to shades of gray and saves the result.

	This function reads an image from the specified file, converts it to grayscale
	by averaging the RGB values of each pixel, and saves the transformed image to
	a new file.

	Args:
	    file_name_start (str): The path to the input image file.
	    file_name_stop (str): The path where the output image will be saved.
	"""
	image_info = image_read(file_name_start)
	image = image_info["image_file"]
	draw = image_info["image_draw"]
	width = image_info["image_width"]
	height = image_info["image_height"]
	pix = image_info["image_pix"]

	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = (a + b + c) // 3
			draw.point((i, j), (S, S, S))

	plt.imshow(image)
	plt.show()
	print("STOP_im", "red=", pix[1, 1][0], "green=", pix[1, 1][1], "blue=", pix[1, 1][2])
	image.save(file_name_stop, "JPEG")
	del draw
	print(f'------- Transformation completed. Saved to file {file_name_stop} --------------')
	return


def serpia(file_name_start: str, file_name_stop: str) -> None:
	"""
    Applies a sepia tone effect to an image and saves the result.

    This function reads an image from the specified file, applies a sepia transformation
    based on a specified depth, and saves the transformed image to a new file.

    Args:
        file_name_start (str): The path to the input image file.
        file_name_stop (str): The path where the output image will be saved.
	"""
	image_info = image_read(file_name_start)
	image = image_info["image_file"]
	draw = image_info["image_draw"]
	width = image_info["image_width"]
	height = image_info["image_height"]
	pix = image_info["image_pix"]

	print('------- Enter sepia depth coefficient --------------')
	depth = int(input('depth:'))
	print('------- Transforming image to sepia --------------')
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = (a + b + c) // 3
			a = S + depth * 2
			b = S + depth
			c = S
			if (a > 255):
				a = 255
			if (b > 255):
				b = 255
			if (c > 255):
				c = 255
			draw.point((i, j), (a, b, c))

	plt.imshow(image)
	plt.show()
	print("STOP_im", "red=", pix[1, 1][0], "green=", pix[1, 1][1], "blue=", pix[1, 1][2])
	image.save(file_name_stop, "JPEG")
	del draw
	print(f'------- Transformation completed. Saved to file {file_name_stop} --------------')

	return


def negative(file_name_start: str, file_name_stop: str) -> None:
	"""
	Creates a negative of an image and saves the result.

	This function reads an image from the specified file, inverts the colors of each pixel,
	and saves the transformed image to a new file. The color inversion is done by subtracting
	each color channel value from 255.

	Args:
	    file_name_start (str): The path to the input image file.
	    file_name_stop (str): The path where the output image will be saved.
	"""
	image_info = image_read(file_name_start)
	image = image_info["image_file"]
	draw = image_info["image_draw"]
	width = image_info["image_width"]
	height = image_info["image_height"]
	pix = image_info["image_pix"]

	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			draw.point((i, j), (255 - a, 255 - b, 255 - c))

	plt.imshow(image)
	plt.show()
	print("STOP_im", "red=", pix[1, 1][0], "green=", pix[1, 1][1], "blue=", pix[1, 1][2])
	image.save(file_name_stop, "JPEG")
	del draw
	print(f'------- Transformation completed. Saved to file {file_name_stop} --------------')
	return


def noise(file_name_start: str, file_name_stop: str) -> None:
	"""
	Adds random noise to an image and saves the result.

	This function reads an image from the specified file, applies random noise
	to each pixel based on a specified noise factor, and saves the transformed
	image to a new file. The noise is added to each color channel, and the
	resulting pixel values are clamped to the range [0, 255].

	Args:
	    file_name_start (str): The path to the input image file.
	    file_name_stop (str): The path where the output image will be saved.
	"""
	image_info = image_read(file_name_start)
	image = image_info["image_file"]
	draw = image_info["image_draw"]
	width = image_info["image_width"]
	height = image_info["image_height"]
	pix = image_info["image_pix"]

	print('------- Enter noise factor --------------')
	factor = int(input('factor:'))
	print('------- Transforming image with noise --------------')
	for i in range(width):
		for j in range(height):
			rand = random.randint(-factor, factor)
			a = pix[i, j][0] + rand  # додавання рандомного числа
			b = pix[i, j][1] + rand
			c = pix[i, j][2] + rand
			if (a < 0):
				a = 0
			if (b < 0):
				b = 0
			if (c < 0):
				c = 0
			if (a > 255):
				a = 255
			if (b > 255):
				b = 255
			if (c > 255):
				c = 255
			draw.point((i, j), (a, b, c))

	plt.imshow(image)
	plt.show()
	print("STOP_im", "red=", pix[1, 1][0], "green=", pix[1, 1][1], "blue=", pix[1, 1][2])
	image.save(file_name_stop, "JPEG")
	del draw
	print(f'------- Transformation completed. Saved to file {file_name_stop} --------------')

	return


def brightness_change(file_name_start: str, file_name_stop: str) -> None:
	"""
	Adjusts the brightness of an image and saves the result.

	This function reads an image from the specified file, modifies the brightness
	of each pixel by a specified factor, and saves the transformed image to a new file.
	The brightness factor can range from -100 to +100, where negative values darken
	the image and positive values brighten it. Pixel values are clamped to the range [0, 255].

	Args:
	    file_name_start (str): The path to the input image file.
	    file_name_stop (str): The path where the output image will be saved.
	"""
	image_info = image_read(file_name_start)
	image = image_info["image_file"]
	draw = image_info["image_draw"]
	width = image_info["image_width"]
	height = image_info["image_height"]
	pix = image_info["image_pix"]

	print('Enter brightness change factor: -100 to +100')
	factor = int(input('factor:'))  # наприклад в діапазоні +100, -100
	print('------- Transforming image brightness --------------')
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0] + factor  # одавання яскравості
			b = pix[i, j][1] + factor
			c = pix[i, j][2] + factor
			if (a < 0):
				a = 0
			if (b < 0):
				b = 0
			if (c < 0):
				c = 0
			if (a > 255):
				a = 255
			if (b > 255):
				b = 255
			if (c > 255):
				c = 255
			draw.point((i, j), (a, b, c))

	plt.imshow(image)
	plt.show()
	print("STOP_im", "red=", pix[1, 1][0], "green=", pix[1, 1][1], "blue=", pix[1, 1][2])
	image.save(file_name_stop, "JPEG")
	del draw
	print(f'------- Transformation completed. Saved to file {file_name_stop} --------------')

	return


def monochrome(file_name_start: str, file_name_stop: str) -> None:
	"""
	Converts an image to a monochrome (black and white) representation.

	This function reads an image from the specified file, converts it to monochrome based
	on a specified threshold factor, and saves the transformed image to a new file. The
	conversion uses the sum of the RGB values to determine whether each pixel should be
	set to black or white. The threshold is influenced by the provided factor, which
	should be in the range of 50 to 100.

	Args:
	    file_name_start (str): The path to the input image file.
	    file_name_stop (str): The path where the output image will be saved.
	"""
	image_info = image_read(file_name_start)
	image = image_info["image_file"]
	draw = image_info["image_draw"]
	width = image_info["image_width"]
	height = image_info["image_height"]
	pix = image_info["image_pix"]

	print('------ Enter a threshold factor for monochrome conversion (range: 50-100) ----------')
	factor = int(input('factor:'))
	print('------- Transforming image to monochrome --------------')
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = a + b + c
			if (S > (((255 + factor) // 2) * 3)):  # рішення до якого з 2 кольорів поточне значення кольору ближче
				a, b, c = 255, 255, 255
			else:
				a, b, c = 0, 0, 0
			draw.point((i, j), (a, b, c))

	plt.imshow(image)
	plt.show()
	print("STOP_im", "red=", pix[1, 1][0], "green=", pix[1, 1][1], "blue=", pix[1, 1][2])
	image.save(file_name_stop, "JPEG")
	del draw
	print(f'------- Transformation completed. Saved to file {file_name_stop} --------------')

	return


def contour_im(file_name_start: str, file_name_stop: str) -> None:
	"""
	Applies contour and blur filters to an image and saves the result.

	This function reads an image from the specified file, applies a series of filters
	(contour, blur, and detail) to create a stylized effect, and saves the transformed
	image to a new file. The resulting image highlights edges and enhances details.

	Args:
	    file_name_start (str): The path to the input image file.
	    file_name_stop (str): The path where the output image will be saved.
	"""
	image_info = image_read(file_name_start)
	image = image_info["image_file"]
	draw = image_info["image_draw"]
	width = image_info["image_width"]
	height = image_info["image_height"]
	pix = image_info["image_pix"]

	image_filter = image.filter(CONTOUR)
	image_filter = image.filter(BLUR)
	image_filter = image.filter(DETAIL)

	plt.imshow(image_filter)
	plt.show()
	pix = image_filter.load()  # отримання значень пікселей для картинки
	print("STOP_im", "red=", pix[1, 1][0], "green=", pix[1, 1][1], "blue=", pix[1, 1][2])
	image_filter.save(file_name_stop, "JPEG")
	del draw
	print(f'------- Transformation completed. Saved to file {file_name_stop} --------------')

	return
