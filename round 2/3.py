k = int(input())
n = int(input())
total = k**n
m = 1000000007

if n%2 == 0:
    palindrome = pow(k,n//2)
else:
    palindrome = pow(k,(n//2)+1)

print((total - palindrome)%m)