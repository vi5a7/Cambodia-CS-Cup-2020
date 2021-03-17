import math

if __name__ == '__main__':
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())

    C = C - D
    R = B**2-4*A*C
    if A == 0:
        if B == 0:
            print("Empty")
        else:
            X = -C/B
            if X.is_integer():
                print(int(X))
    else:
        if R < 0:
            print("Empty")
        elif R == 0:
            X = -B/(2*A)
            if X.is_integer():
                print(int(X))
        else:
            X1 = (-B - math.sqrt(R))/(2*A)
            X2 = (-B + math.sqrt(R))/(2*A)
            if X1.is_integer():
                print(int(X1))
            if X2.is_integer():
                print(int(X2))
            else:
                print("Empty")