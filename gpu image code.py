# Import the Image class from the PIL (Pillow) library to handle image processing
from PIL import Image

# Open the image file named "finchfinal.png" and load it into a PIL Image object
image = Image.open("finchfinal.png")

# Load the pixel data from the image, allowing pixel access via coordinates (x, y)
pixels = image.load()

# Open (or create) a binary file named "image.bin" for writing binary data
out_file = open("image.bin", "wb")

# Loop over the vertical pixels (rows), assuming a height of 256 pixels
for y in range(256):
    # Loop over the horizontal pixels (columns), assuming a width of 128 pixels
    for x in range(128):
        try:
            # Attempt to write the pixel value at (x, y) to the binary file
            # Convert the pixel value to a character (assuming grayscale or single channel)
            out_file.write(chr(pixels[x, y]))
        except IndexError:
            # If (x, y) is out of bounds (e.g., image is smaller than 128x256), write a null byte
            out_file.write(chr(0))

