if __name__ == '__main__':
    N = int(input())
    num, dn = set(), 0
    for i in range(N):
        n = int(input())
        if n not in num:
            dn+=1
        num.add(n)
        print(dn)
