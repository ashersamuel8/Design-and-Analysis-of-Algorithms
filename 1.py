import sys


def findIsolated(A, k):
    B = ['Y'] * len(A)

    dict = {}

    for i in range(0, len(A)):

        if A[i] in dict:

            if dict[A[i]] > i - k - 1:
                B[i] = 'N'

        dict[A[i]] = i

    return B


def sumLargestSmallest(A, k):
    # A = [10,6,15,3,12,7,50,1,8]
    # k = 2

    min = select(A, k )
    max = select(A, len(A) - k - 1)
    print(f"min: {min}, max: {max}")
    sum = 0

    for i in range(0, len(A)):
        if A[i] < min or A[i] > max:
            sum += A[i]
            # print(A[i])

    print(f"sum: {sum}")
    return sum


def select(A, k):
    if len(A) < 10:
        A.sort()
        return A[k]
    S = []
    lIndex = 0
    while lIndex + 5 < len(A) - 1:
        S.append(A[lIndex:lIndex + 5])
        lIndex += 5
    S.append(A[lIndex:])
    Meds = []
    for subAist in S:
        Meds.append(select(subAist, int((len(subAist) - 1) / 2)))
    med = select(Meds, int((len(Meds) - 1) / 2))
    A1 = []
    A2 = []
    A3 = []
    for i in A:
        if i < med:
            A1.append(i)
        elif i > med:
            A3.append(i)
        else:
            A2.append(i)
    if k < len(A1):
        return select(A1, k)
    elif k < len(A2) + len(A1):
        return A2[0]
    else:
        return select(A3, k - len(A1) - len(A2))


def partition_left(A, median):
    A1 = []

    for i in range(0, len(A)):
        if A[i] < median:
            A1.append(A[i])

    return A1


def partition_right(A, median):
    A1 = []

    for i in range(0, len(A)):
        if A[i] > median:
            A1.append(A[i])

    return A1


def partition(A, median):
    A1 = []
    A2 = []

    for i in range(0, len(A)):
        if A[i] < median:
            A1.append(A[i])
        if A[i] > median:
            A2.append(A[i])

    return A1 + A2


def thresholdLargestSmallest(A, T):
    # for i in range(0, len(A) // 2 + 1):
    #     if sumLargestSmallest(A, i) > T:
    #         return i

    if len(A) == 0:
        return -1

    median = select(A, len(A) // 2)
    print()
    print(median)

    A3 = partition(A, median)
    print(A3)

    if sum(A3) >= T:
        x = thresholdLargestSmallest(A3, T)

    else:
        print(len(A3) // 2 + 1)
        return len(A3) // 2 + 1

    return x


# A = [1,2,5,1,6,2,8,2,4]
#    0,1,2,3,4,5,6,7,8,9,1,1,1,1,1,1,1,1,1,1,2,2
#	                     0 1 2 3 4 5 6 7 8 9 0 1

# k = 3


# A = [50, 1, 15, 3, 12, 7, 10, 6, 8]
# k = 2
#
# sumLargestSmallest(A, k)

A = [10, 6, 15, 3, 12, 7, 50, 1, 8, 2]
print(select(A, 5))
B = [1, 2, 3, 6, 7, 8, 10, 12, 15, 50]
T = 80
x = thresholdLargestSmallest(A, T)
print(x)

# for k1 in range(0, len(A)):
#
# 	if A[k1] in dict:
# 		i1 = max(dict[A[k1]] + 1, i1)
# 		# i1 = dict[A[k1]] + 1
#
# 	dict[A[k1]] = k1
#
# 	if k1 - i1 > k2 - i2:
# 		i2 = i1
# 		k2 = k1
#
# 	print(f"i1: {i1}, k1: {k1}\ni2: {i2}, k2: {k2}\n")
#
# print(dict)
# print(f"i: {i2}, k: {k2}")
# print()
