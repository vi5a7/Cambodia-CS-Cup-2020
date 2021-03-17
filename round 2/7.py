n = int(input())
m = int(input())
lst_of_puzzle, len_count, sum_of_num = [], 0, 0
for i in range(m):
    x = input()
    len_count += len(x)
    x = int(x)
    sum_of_num += x
    lst_of_puzzle.append(x)

if m > 1:
    x = n-len_count
    y = (x-m+1) * '9'
    if y == '':
        y = 9
    else:
        y = int(y)
    sum_of_num += y
    print(y)

if m > 2:
    for i in range(m-2):
        sum_of_num += 9
        print(9)

largest = 9 - (sum([int(x) for x in str(sum_of_num)]) % 9)
print(largest)