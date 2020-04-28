'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def get_largest_prime(large_int):
    
    my_num = large_int
    local_divisor = 2

    while my_num > local_divisor:
        if my_num % local_divisor == 0:
            my_num = my_num /local_divisor
        else:
            local_divisor = local_divisor +1

    return local_divisor




if __name__ == '__main__':


    print(get_largest_prime(600851475143))
