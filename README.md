# Lossless-Image-Compression
This project was done for the midterm exam of Digital Image Processing course. Three Lossless Compression algorithms were used in this project which are Huffman, RLE and LZW.

## Requirements
The only package required is `cv2`

## Implementation
### Algorithm Files
All the algorithms can be run by the same syntax:
```
python <folder of Algorithm>/main.py <image path>
```
**Example:**  
```
python RLE/main.py images/demi.jpg
```

### Other files
There are two other files were written to support this project:
* `compare.py`: Compare the images before and after compression.
```
python compare.py <path to input image> <path to output image>
```
**Example:**
```
python compare.py images/demi.jpg decompressed.bmp  
```
* `compare_ratio.py`: Run the selected algorithm on all the images file in the folder `images`.
```
python compare_ratio.py <code name>
```
**Example:**
```
python compare_ratio.py LZW/main
```
**NOTE:** The code name must NOT include `.py`, just the name of the code as `.py` has already been included in the code.  

Another thing is to run `compare_ratio.py` on RLE, these two lines in the file `main.py` in this folder must be removed or comment before running:
```
cv2.imshow('Original_img',encode.img)
cv2.imshow('Decompressed_img',decode.img)
```
Otherwise, the running process will stuck in showing the images.

## References
Source code:  
https://github.com/iamleevn/Lossless-Image-Compression  

*Two other sources will be provided soon..*
