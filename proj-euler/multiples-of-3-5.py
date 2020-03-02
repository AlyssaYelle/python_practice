'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

import math

# method 1
def sum_multiples1(below_int):

    current_max_sum = 0

    current_int = 3

    while current_int < below_int:
        current_max_sum += current_int
        current_int += 3

    current_int = 5

    while current_int < below_int:
        if current_int % 3 != 0:
            current_max_sum += current_int

        current_int += 5

    return current_max_sum


# method 2
def sum_multiples2(below_int):
    print('we are here at sum_multiples2')
    '''
    will use SUM(k) k in (1, n) = (1/2)*n*(n+1)
    '''

    # first find out how many times 3, 5, and 15 (LCM of 3 & 5) fit into (below_int - 1)
    n3 = math.floor((below_int - 1)/3)
    n5 = math.floor((below_int - 1)/5)
    n15 = math.floor((below_int -1)/15)

    return (3 * summation(n3)) + (5 * summation(n5)) - (15 * summation(n15))


def summation(n):

    return int((1/2)*n*(n+1))


if __name__ == '__main__':
    my_sum1 = sum_multiples1(10) # -> 23
    print(my_sum1)

    my_sum2 = sum_multiples1(1000) # -> 233168
    print(my_sum2)

    my_sum3 = sum_multiples2(10)
    print(my_sum3)

    my_sum4 = sum_multiples2(1000)
    print(my_sum4)





