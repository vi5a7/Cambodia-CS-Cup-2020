def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 3 == 0 or n % 2 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def palindrome(s):
    return s == s[::-1]


s = input()

if palindrome(s):
    print(len(s))
    if prime(len(s)):
        print("yes")
    else:
        print("no")
else:
    for i in range(len(s)):
        for j in range(i):
            if palindrome(s[j:len(s)-i+j]):
                x = len(s[j:len(s)-i+j])
                print(x)
                if prime(x):
                    print("yes")
                else:
                    print("no")
                break
        else:
            continue
        break