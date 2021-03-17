def find_the_position(G):
    positions = []
    for i in range(len(G)):
        if G[i] == '1':
            positions.append(i + 1)

    for position in positions:
        print(position)


if __name__ == '__main__':
    A = int(input())

    # conversion of decimal to binary number
    G = bin(A).replace("0b", "")

    find_the_position(G)

