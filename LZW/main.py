from PIL import Image
from grayscale import GrayscaleImage
from io import StringIO
import numpy as np
import random
import sys,os
import re

N_ROWS = 1500
N_COLS = 1500


def compress(uncompressed):
    """
    Compress a string to a list of output symbols.
    :param uncompressed: str
    :return: list
    """
    # Build the dictionary.
    dict_size = 255
    dictionary = {chr(i): i for i in range(dict_size)}
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary.keys():
            w = wc
        else:
            result.append(dictionary[w])
            dict_size += 1
            dictionary[wc] = dict_size
            w = c
    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result


def decompress(compressed):
    """
    Decompress a list of output values to a string.
    :param compressed: list
    :return: str
    """
    # Build the dictionary.
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}
    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        w = entry
    return result.getvalue()

path = sys.argv[1]
im = Image.open(path)
# im1 = Image.new('L', im.size, 'black')
# im1.show()
width, height = im.size
img = GrayscaleImage(N_ROWS, N_COLS) #create 2D array with 1000 rows and 1000 column; 
pixels = ""
pixs = im.load() #load the pixel data
for i in range(width):
    for j in range(height):
        k = im.getpixel((i, j)) #return the pixel at (i, j)
        img.setitem(i, j, k) #set the item in the array at (i, j) is k
        pixs[i, j] = img.getitem(i, j) #print the k to pixs
for i in range(width):
    for j in range(height):
        if img.getitem(i, j):
            pixels += str(img.getitem(i, j)) + " " #if element at (i,j) exists, pixels += the content
        else:
            pixels += " "
    pixels += "\n"
compressed = []
overall = []
intt = []
decompress_ed = []
idk = compress(pixels)
decompress_ed =decompress(idk)

intt = re.findall('\d+', decompress_ed)
for i in range(len(intt)):
    intt[i]= int(intt[i])
# print(intt)
def divide_chunks(l, n): 
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
neww = list(divide_chunks(intt, 3))
# print(neww)
# make it to be tuples

for i in range(len(neww)):
    neww [i]=tuple(neww[i])
# print(neww)
new_img = Image.new("RGB", (width,height))

new_pixels = new_img.load()

for x in range(width):
    for y in range(height):
        new_pixels[x,y] = neww[height*x+y]

new_img.save('result.tiff')

# Decompress Info
print("Decompressed successfully")
origin_size = os.path.getsize(path)
decompress_size = os.path.getsize('result.tiff')
print("Original size: " + str(origin_size))
print("Decompressed size: " + str(decompress_size))
<<<<<<< HEAD:LZW/main.py
print('Compress Ratio: ', int(origin_size)/int(decompress_size))
=======
print("Compress ratio: " + str(origin_size/decompress_size))
>>>>>>> 9e131f11fa3598b3f0db0a976ac600dea673b56e:LZW/grayscale_test.py
