
# Author: Samuel Kappala
# sk2175, 195007762

def squareroot(low, high, x):
    if x == 0 or x == 1:
        return x

    if low > high:
        return "no solution"

    if ((low + high) // 2) ** 2 == x:
        return (low + high) // 2
    elif ((low + high) // 2) ** 2 > x:
        return squareroot(low, (low + high) // 2 - 1, x)
    elif ((low + high) // 2) ** 2 < x:
        return squareroot((low + high) // 2 + 1, high, x)


def max_prod_crossing(A, low, mid, high):
    left_prod = 0
    prod = 1
    max_left = None
    for i in range(mid, low - 1, -1):
        prod = prod * A[i]
        if prod > left_prod:
            left_prod = prod
            max_left = i

    right_prod = 0
    prod = 1
    max_right = None
    for j in range(mid + 1, high + 1):
        prod = prod * A[j]
        if prod > right_prod:
            right_prod = prod
            max_right = j

    return max_left, max_right, left_prod * right_prod


def max_prod(A, low, high):
    if low == high:
        return low, high, A[low]
    else:
        mid = (low + high) // 2

        left_low, left_high, left_prod = max_prod(A, low, mid)

        right_low, right_high, right_prod = max_prod(A, mid + 1, high)

        cross_low, cross_high, cross_prod = max_prod_crossing(A, low, mid, high)


        # left_prod = 0
        # prod = 1
        # cross_low = None
        # for i in range(mid, low + 1, -1):
        #     prod = prod * A[i]
        #     if prod > left_prod:
        #         left_prod = prod
        #         cross_low = i
        #
        # right_prod = 0
        # prod = 1
        # cross_high = None
        # for j in range(mid+1, high + 1):
        #     prod = prod * A[j]
        #     if prod > right_prod:
        #         right_prod = prod
        #         cross_high = j
        #
        # cross_prod = left_prod *
        print(f"low, mid, high: {low, mid, high}")
        print(f"left low, high, prod: {left_low, left_high, left_prod}")
        print(f"right low, high, prod: {right_low, right_high, right_prod}")
        print(f"cross low, high, prod: {cross_low, cross_high, cross_prod}")
        print()

        if left_prod >= right_prod and left_prod >= cross_prod:
            return left_low, left_high, left_prod
        elif right_prod >= left_prod and right_prod >= cross_prod:
            return right_low, right_high, right_prod
        else:
            return cross_low, cross_high, cross_prod

def count(A, low, high, obj):

    count = 0
    for i in range(low, high + 1):
        if A[i] == obj:
            count = count + 1

    return count

    # if count >= 2*len(A)//3:
    #     return True
    # else:
    #     return False


def find_majority(A, low, high):

    if low == high:
        return A[low]

    mid = (low + high)//2

    left_majority_obj = find_majority(A, low, mid)
    right_majority_obj = find_majority(A, mid + 1, high)

    # if left_majority_obj == right_majority_obj:
    #     return left_majority_obj

    left_count = count(A, low, high, left_majority_obj)
    right_count = count(A, low, high, right_majority_obj)

    print(f"left count: {left_count}, left obj: {left_majority_obj}")
    print(f"right count: {right_count}, right obj: {right_majority_obj}")
    for i in range(low, high+1):
        print(A[i], end = ' ')
    print()
    print(2*len(A)//3)

    if left_count >= (2*(high-low))/3:
        print("returning left majority")
        print("\n")
        return left_majority_obj
    elif right_count >= (2*(high-low))/3:
        print("returning right majority")
        print("\n")
        return right_majority_obj
    else:
        print("returning -1")
        print("\n")
        return -1

def majority(A, x):

    count = 0
    majority_element = 0

    for i in range(0, x):
        if count <= 0:
            majority_element = A[i]
        if A[i] == majority_element:
            count = count + 1
        else:
            count = count - 2

        print(f"count: {round(count,2)},\t majority candidate: {majority_element}")

    if count >= 0:
        count = 0
        for i in range(x):
            if A[i] == majority_element:
                count+=1

        if count >= 2*len(A)/3:
            print(f"count: {count}")
            return majority_element
        else:
            return -1
        # return majority_element
    else:
        return -1


def main():
    print("Testing squareroot() for the squares of first 100 numbers")
    for x in range(1, 100):
        if not x == squareroot(0, x**2//2, x**2):
            print(f"{x}: failed")
        else:
            print("passed")
    print()

    array1 = [3, .2, 4, .5, 1, 4, .3, 2]
    print("maximum product subarray is", max_prod(array1, 0, len(array1) - 1))

    print()

    array2 = [3,3,3,3,1,3,3,5,3,2,3,3,4,3,1,8,3,3]
    # # print("majority element is ", find_majority(array2, 0, len(array2) - 1))
    print("majority element is ", majority(array2, len(array2)))



if __name__ == "__main__":
    main()
