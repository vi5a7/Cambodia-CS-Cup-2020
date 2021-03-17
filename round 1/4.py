def divide_treasure(listOfItem):
    firstFriend, secondFriend, count, k = 0, 0, 1, 0

    # First Friend takes the most valueable item, and sorts the item from highest to the lowest
    firstFriend = max(listOfItem)
    listOfItem.remove(firstFriend)
    listOfItem.sort(reverse=True)

    # Sum the values of remaining items
    for i in range(len(listOfItem)):
        secondFriend += listOfItem[i]

    # First Friend's sum of values must be higher than Second Friend's sum of values
    while (firstFriend <= secondFriend):
        count += 1
        firstFriend += listOfItem[k]
        secondFriend -= listOfItem[k]
        k += 1

    return count


if __name__ == '__main__':
    N = int(input())
    listOfItem = []
    for i in range(N):
        item = int(input())
        listOfItem.append(item)

    print(divide_treasure(listOfItem))