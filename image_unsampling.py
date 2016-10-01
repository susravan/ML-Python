# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/contests/real-data-contest-april-2016/challenges/image-upsampling 

from __future__ import print_function
import numpy as np
import scipy.ndimage

procRow,procCol,N = map(int, raw_input().split())
origRow,origCol = map(int, raw_input().split())
raw_matrix = procRow*[procCol*[0]]		# np.zeros(shape=(procCol,procRow),dtype=np.int)
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
	matrixB = [[None]*(len(rMatrix[0])) for _ in range(len(rMatrix))] # len(rMatrix)*[len(rMatrix[0])*[0]]
	matrixG = [[None]*(len(rMatrix[0])) for _ in range(len(rMatrix))] # len(rMatrix)*[len(rMatrix[0])*[0]]
	matrixR = [[None]*(len(rMatrix[0])) for _ in range(len(rMatrix))] # len(rMatrix)*[len(rMatrix[0])*[0]]
	row = 0
	while row < len(rMatrix):
		col = 0
		while col < len(rMatrix[0]):
			arr = rMatrix[row][col].split(',')
			matrixB[row][col], matrixG[row][col], matrixR[row][col] = map(int,rMatrix[row][col].split(','))
			col = col + 1
		row = row + 1
	return map(np.asmatrix,[matrixB,matrixG,matrixR])

matrixGBR = decode(raw_matrix)

# Encoding the image
def encode(matrices,origRow,origCol):
	encoded_matrix = [[None]*origCol for _ in range(origRow)]
	row = 0
	while row < origRow:
		col = 0
		while col < origCol:
			encoded_matrix[row][col] = [matrices[0][row][col],matrices[1][row][col],matrices[2][row][col]]
			col = col + 1
		row = row + 1
	# return np.asmatrix(encoded_matrix)
	return encoded_matrix

def showOutput(final_matrix):
	for row in final_matrix:
		# print 'row = ', row
		for col in row:
			# print col,
			print(str.replace(str.replace(str.replace(str(col),' ',''),'[',''),']',''),end=" ")
		print("\n",end="")
		
order = 1
matrixGBR[0] = scipy.ndimage.zoom(matrixGBR[0],N,order=order)
matrixGBR[1] = scipy.ndimage.zoom(matrixGBR[1],N,order=order)
matrixGBR[2] = scipy.ndimage.zoom(matrixGBR[2],N,order=order)
showOutput(encode(matrixGBR,origRow,origCol))
