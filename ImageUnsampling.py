# https://www.hackerrank.com/contests/real-data-contest-april-2016/challenges/image-upsampling

"""
Problem Description

To reduce the size of a 2-dimensional image, I, containing R rows and C columns of pixels, the image is downsampled using a crude algorithm.

The downsampling algorithm begins sampling from the top-left pixel position, (0,0), of the original image and then proceeds to retain only those pixels which are located in those positions where both the row number and the column number are either 0, or integer multiples of some integer. The downsampled image only contains r rows and c columns where these values correspond to (1+floor((R-1)/N) and (1+floor((C1)/N)

Let's assume for a moment that the original image is as follows (where each character indicates a pixel):

ABCDEFG
HIJKLMN
OPQRSTU
VWXYZab
cdefghi
jklmnop

This image has 6 rows and 7 columns.
Assume that the pixel A is the one positioned at row=0, column=0.
If we downsample this image using N=2, we only retain those pixels located in positions where both the row and column numbers are even. This means the downsampled image will be:

ACEG
OQSU
cegi

Observe that when N=2, the downsampled image retains over a quarter of the pixels.

Now, if we downsample this image using N=3, we only retain those pixels located in positions where both the row and column numbers are multiples of 3. This means the downsampled image will be:

ADG
VYb

Observe that when N=3, the downsampled image retains only 6 pixels.

Sample Input

3 3 2
6 6
0,0,200 0,0,10 10,0,0
90,90,50 90,90,10 255,255,255
100,100,88 80,80,80 15,75,255

Sample Output

0,0,200 100,100,100 0,0,10 5,5,5 10,0,0 50,50,50
90,90,50 90,90,50 90,90,10 90,90,10 255,255,255 0,0,10
100,100,88 100,100,88 80,80,80 80,80,80 15,75,255 15,75,255
100,100,88 100,100,88 80,80,80 80,80,80 15,75,255 15,75,255
100,100,88 100,100,88 80,80,80 80,80,80 15,75,255 15,75,255
90,90,50 90,90,50 90,90,10 90,90,10 255,255,255 0,0,10

"""

from __future__ import print_function

import numpy as np
import scipy.ndimage

procRow, procCol, N = map(int, raw_input().split())
origRow, origCol = map(int, raw_input().split())
raw_matrix = procRow * [procCol * [0]]  # np.zeros(shape=(procCol,procRow),dtype=np.int)
# print raw_matrix
row = 0
arr = []
while row != procRow:
    # np.append(raw_matrix,raw_input().split())
    # arr.append(raw_input().strip().split())
    raw_matrix[row] = raw_input().strip().split()
    row = row + 1


# Decoding the image
def decode(rMatrix):
    # Don't use the commented one  as a list is mutable
    # Refer - http://stackoverflow.com/questions/21036140/python-two-dimensional-array-changing-an-element
    matrixB = [[None] * (len(rMatrix[0])) for _ in range(len(rMatrix))]  # len(rMatrix)*[len(rMatrix[0])*[0]]
    matrixG = [[None] * (len(rMatrix[0])) for _ in range(len(rMatrix))]  # len(rMatrix)*[len(rMatrix[0])*[0]]
    matrixR = [[None] * (len(rMatrix[0])) for _ in range(len(rMatrix))]  # len(rMatrix)*[len(rMatrix[0])*[0]]
    row = 0
    while row < len(rMatrix):
        col = 0
        while col < len(rMatrix[0]):
            arr = rMatrix[row][col].split(',')
            matrixB[row][col], matrixG[row][col], matrixR[row][col] = map(int, rMatrix[row][col].split(','))
            col = col + 1
        row = row + 1
    return map(np.asmatrix, [matrixB, matrixG, matrixR])

matrixGBR = decode(raw_matrix)

# Encoding the image
def encode(matrices, origRow, origCol):
    encoded_matrix = [[None] * origCol for _ in range(origRow)]
    row = 0
    while row < origRow:
        col = 0
        while col < origCol:
            encoded_matrix[row][col] = [matrices[0][row][col], matrices[1][row][col], matrices[2][row][col]]
            col = col + 1
        row = row + 1
    return encoded_matrix

# Display the output
def showOutput(final_matrix):
    for row in final_matrix:
        # print 'row = ', row
        for col in row:
            # print col,
            print(str.replace(str.replace(str.replace(str(col), ' ', ''), '[', ''), ']', ''), end=" ")
        print("\n", end="")


order = 1
matrixGBR[0] = scipy.ndimage.zoom(matrixGBR[0], N, order=order)
matrixGBR[1] = scipy.ndimage.zoom(matrixGBR[1], N, order=order)
matrixGBR[2] = scipy.ndimage.zoom(matrixGBR[2], N, order=order)
showOutput(encode(matrixGBR, origRow, origCol))
