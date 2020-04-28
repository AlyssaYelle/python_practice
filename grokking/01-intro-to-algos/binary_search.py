
import math

def binary_search(ordered_list, item):
    '''
    searches ordered list for item
    returns idx of item
    or None if item not found
    '''

    # initialize hi & lo values
    lo = 0
    hi = len(ordered_list) - 1

    # stop searching when lo is greater than hi
    while lo <= hi:

        # find the mid point and grab its value
        mid_idx = (lo + hi) // 2
        mid_value = ordered_list[mid_idx]

        # return idx if value matches the item we are searching for
        if mid_value == item:
            return mid_idx
        # if value is less than our item, reset lo to be mid point + 1
        elif mid_value < item:
            lo = mid_idx + 1
        # if value is greater than our item, reset hi to be mid point - 1
        elif mid_value > item:
            hi = mid_idx - 1

    return None


if __name__ == "__main__":
    ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    item = 1

    print(binary_search(ordered_list, item))

    print(math.log(128, 2))
    print(math.log(246, 2))


