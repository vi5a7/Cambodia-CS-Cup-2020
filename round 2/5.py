arr = [0, 0, 1]
m = (10**9)+7

for i in range(3, pow(10,4)+1):
    j = 2*arr[i-1] + 2*arr[i-2] + 3**(i-2)
    arr.append(j)

n = int(input())
all_strings = pow(3,n)
res = all_strings - arr[n]

print(res%m)