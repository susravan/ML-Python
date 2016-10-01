# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/contests/real-data-contest-april-2016/challenges/segment-the-twitter-hashtags 


# Initialization of the dictionary of words
def getDict():
	dict = {}
	
	words_arr = []
	with open("google 20k word list.txt",'r') as f:
		for line in f:
			words_arr = line.split('|')
	
	for str in words_arr:
		dict[str] = 0
	return dict

# Check if the is present in the dictionary
def isValidWord(word, dict):
	if word in dict.keys():
		return True
	else:
		return False

# Splits the given string taking the entire word first and reducing from the right end by each character
def getSegmentedWordR2L(rword,dict):
	limit = len(rword) - 1
	start = 0
	valid_words = []
	while limit != start:
		# print rword[start:limit]
		if isValidWord(rword[start:limit],dict):
			valid_words.append(rword[start:limit])
			start = limit
			# print 'rword = ', rword, 'limit = ', limit
			limit = len(rword)
		else:
			limit = limit -1
	# print valid_words
	return valid_words

# Starts from left and goes right by each character and checks if that word is present in the dictionary of words
def getSegmentedWordL2R(rword,dict):
	limit = 2
	start = 0
	valid_words = []
	while limit <= len(rword):
		# print rword[start:limit]
		if isValidWord(rword[start:limit],dict):
			valid_words.append(rword[start:limit])
			start = limit
			# print 'rword = ', rword, 'limit = ', limit
			limit = limit + 2
		else:
			limit = limit + 1
			# print 'start = ', start, 'limit = ', limit
			# print rword[start:limit]
	return valid_words

#Gets the best possible match between the L2R and R2L parsing
def getSegmentedWord(rword,dict):
	# arr_L2R = getSegmentedWordL2R(rword,dict)
	arr_R2L = getSegmentedWordR2L(rword,dict)
	if len(''.join(arr_R2L)) == len(rword):
		return arr_R2L
	else:
		arr_L2R = getSegmentedWordL2R(rword,dict)
		# print len(arr_L2R)
		if len(arr_L2R) > len(arr_R2L):
			return arr_L2R
		else:
			return arr_R2L
	return [arr_L2R,arr_R2L]

# Main program starts from here

test_cases = int(raw_input())
dict = getDict()
while test_cases != 0:
	# print getSegmentedWord(str(raw_input().strip()),dict)
	print ' '.join(getSegmentedWord(str(raw_input().strip()),dict))
	# segmented_words = getSegmentedWord(str(raw_input().strip()),dict)
	# print 'L2R', segmented_words[0]
	# print 'R2L', segmented_words[1]
	test_cases = test_cases - 1
