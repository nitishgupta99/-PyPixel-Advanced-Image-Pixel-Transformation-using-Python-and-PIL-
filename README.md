
# PyPixel: Advanced Image Pixel Transformation using Python and PIL
This project is a Python program that transforms an image by modifying its pixel values. The program uses the Image module from the PIL (Python Imaging Library) package to load and manipulate images.

## Usage
Before running the program, download the '**ballon.jpeg**' and '**mountain.jpeg**' files and place them in the same directory as the Python script.

To run the program, simply execute the Python script. The script will load the # ballon.jpeg image and compare the pixel values with the mountain.jpeg image. If the pixel in the ballon.jpeg image is red, it will replace that pixel with the corresponding pixel from the mountain.jpeg image. The resulting image will be saved as '**Result.png**' in the same directory.

## Example
Here is an example of running the program:
```Python
python PyPixel.py
This will output the following:

```
```Python
It took 0.0 seconds for import
It took 0.0 seconds for image load
It took 0.28122425079345703 seconds for the loop
It took 0.28192663192749023 seconds total
Checkout the output in the file named: Result.png

```
## Requirements
The program requires Python 3 and the PIL package. The PIL package can be installed using pip:
```Python
pip install Pillow
```

## Contributor
**Nitish Gupta**

## Disclaimer
This program is for educational purposes only. Please ensure that you have the legal right to use the images before running the program.
