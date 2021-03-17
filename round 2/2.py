import math

l = int(input())
r = int(input())
count = 0
for i in range(l, r+1):
    if math.sqrt(i).is_integer():
        count += 1
print(count)