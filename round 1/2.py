def wheel_moves(s):
    count, countList = 0, []
    startWithA = abs(ord('a') - ord(s[0]))
    if startWithA > 13:
        count = count + 26 - startWithA
    else:
        count = count + startWithA

    for i in range(len(s)):
        if s[i - 1] != s[i]:
            countList.append(s[i])

    for i in range(len(countList) - 1):
        num = abs(ord(countList[i]) - ord(countList[i + 1]))
        if num > 13:
            count = count + 26 - num
        else:
            count = count + num
    return count


if __name__ == '__main__':
    num = int(input())
    s = input()

    print(wheel_moves(s))