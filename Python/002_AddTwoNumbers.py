l1 = [9, 9, 9, 9, 9, 9, 9]      # Test cases: [2, 4, 3], [0], [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]      # Test cases: [5, 6, 4], [0], [9, 9, 9, 9]

stored = 0
output = []

for i in zip(l1, l2):

    print(i)             #Prints (2, 4), (4, 6), (3, 4)
    print(i[0] + i[1])   #Prints 7, 10, 7 as ints
    """
    sum = (i[0] + i[1]) + stored
    if sum >= 10:
        if stored != 1:
            print(stored)
            stored += 1
            print(stored)
            output.append(sum - 10)
    else:
        stored = 0
        output.append(sum)

print(output)
"""