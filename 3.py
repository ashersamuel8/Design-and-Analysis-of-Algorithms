# #problem 2
#
# A = [13, 7, 10, 8, 3, 1, 20, 4, 9, 2]
#
# dict = {}
#
# max = -1
#
# for i in range(0, len(A)):
#
# 	if (A[i] - 1) not in dict:
# 		dict[A[i]] = 1
# 	else:
# 		x = dict.pop(A[i] - 1)
# 		dict[A[i]] = x + 1
#
# 		if(x + 1 > max):
# 			max = x + 1
#
#
# print(dict)
# print(max)
#

#problem 3

# A = [3,4,5,6,2,1,9,7,3,9,3,5,7,5,2,7,3,5,8,2,2,7]
#    0,1,2,3,4,5,6,7,8,9,1,1,1,1,1,1,1,1,1,1,2,2
#	                     0 1 2 3 4 5 6 7 8 9 0 1

A = [3,2,7,3,5,3,9,3,5,7,5,8,2,2,7]
#    0,1,2,3,4,5,6,7,8,9,1,1,1,1,1,1,1,1,1,1,2,2
#	                     0 1 2 3 4 5 6 7 8 9 0 1


dict = {}

i1 = 0
i2 = 0
j2 = 0

for j1 in range(0, len(A)):

	if A[j1] in dict:
		i1 = max(dict[A[j1]] + 1, i1)
		# i1 = dict[A[j1]] + 1

	dict[A[j1]] = j1

	if j1 - i1 > j2 - i2:
		i2 = i1
		j2 = j1

	print(f"i1: {i1}, j1: {j1}\ni2: {i2}, j2: {j2}\n")

print(dict)
print(f"i: {i2}, j: {j2}")
print()


def find_median(A):
	A.sort()
	return A[len(A)/2]
#
#
# def FindSpecial(A, offset):
#
# 	m = find_median(A)
#
# 	if -m = len(A)/2:
#
# 	elif m < offset
#
# 	elif m > offset





#problem 5

def square(x):
	return x*x

def mult(x, y):

	avg = (x + y)/ 2

	return square(avg) - square(avg - x)

print(mult(9,12))


#problem6

mutuals = []
p1
p2

for i in range (0, len(P)):

	for j in range (i+1, len(P)):

		p1 = i
		p2 = j

		for k in range(0, len(P[i])):

			for q in range(0, len(P[j])):

				if P[i][k] == P[j][q]
					mutuals.append(P[i][k])
				if len(mutuals) == 2
					 break

if len(mutuals) < 2:
	return 'no solution'

else:
	return p1, p2, mutuals[0], mutuals[1]
