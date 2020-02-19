#
# Complete the 'getMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def getMin(s):
    open_parens = 0
    close_parens = 0
    changes_required = 0

    for token in s:
        if token == '(':
            open_parens += 1
        if token == ')':
            close_parens += 1
            if close_parens > open_parens:
                changes_required += 1
                open_parens += 1

    if open_parens > close_parens:
        changes_required += (open_parens - close_parens)

    return changes_required

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getMin(s)

    fptr.write(str(result) + '\n')

    fptr.close()



#
# Complete the 'countPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. INTEGER k
#

def countPairs(numbers, k):
    print(len(numbers))
    # sort the list of numbers
    numbers.sort()

    # initialize set to store pairs
    pairs = set()

    i = 0

    prev_i = None

    for i in range(0, len(numbers) - 1):

        if numbers[i] == prev_i:
            continue
        else: 
            prev_i = numbers[i]

        prev_j = None

        for j in range (i + 1, len(numbers)):

            if numbers[j] == prev_j:
                continue
            else:
                prev_j = numbers[j]
            print(numbers[i], numbers[j])

            if numbers[j] - numbers[i] == k:
                pair = (numbers[i], numbers[j])

                if pair not in pairs:
                    pairs.add(pair)
            if numbers[j] - numbers[i] > k:
                break


    return len(pairs)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    k = int(input().strip())

    result = countPairs(numbers, k)

    fptr.write(str(result) + '\n')

    fptr.close()




# Complete the function below.

def superStack(operations):
    
    the_stack = [None] * len(operations)
    top_idx = -1

    for op in operations:
        op = op.split()

        if op[0] == 'pop':
            the_stack[top_idx] = None
            top_idx -= 1
        elif op[0] == 'push':
            the_stack[top_idx + 1] = int(op[1])
            top_idx += 1
        elif op[0] == 'inc':
            idx = int(op[1])
            added = int(op[2])
            for i in range(0, idx):
                the_stack[i] += added
        
        if top_idx == -1:
            print('EMPTY')
        else:
            print(the_stack[top_idx])


if __name__ == "__main__":
    operations_cnt = 0
    operations_cnt = int(input())
    operations_i = 0
    operations = []
    while operations_i < operations_cnt:
        try:
            operations_item = str(input())
        except:
            operations_item = None
        operations.append(operations_item)
        operations_i += 1


    res = superStack(operations);
    
