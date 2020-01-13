#Abu Hasnat Hasib
#CIS 1051

def beer(start):

	for n in range(start):
		print(start-n, "bottles of beer on the wall",start-n," bottles of beer.")
		print("Take one down, pass it around",start-n-1, "bottles of beer on the wall")
		
beer(10)
