def countdig(m):
    if (m == 0):
        return 0
    else:
        return 1 + countdig(m // 10)

def countSteps(x):
    c = 0
    last = x
    while (last):
        digits = countdig(last)

        digits -= 1

        divisor = pow(10, digits)

        first = last // divisor

        lastnumber = first * divisor

        skipped = (last - lastnumber) // first

        skipped += 1
        c += skipped

        last = last - (first * skipped)
    return c

n = 14
print(countSteps(n))