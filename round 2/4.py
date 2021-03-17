import math

l = int(input())
k = int(input())
count = 0
for n in range(l, k+1):
    x = int(math.sqrt(n))
    y = n/x
    if y< x+1 and x<=y:
        count+=1
print(count)