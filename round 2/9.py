N = int(input())
Arr =list(map(int, input().split()))
count = 0
for i in Arr:
    bin_i = bin(i)[2:]
    if bin_i.count("1")==1:
        count+=1

print(count)
