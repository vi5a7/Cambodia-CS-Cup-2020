if __name__ == '__main__':
    N = int(input())
    list_of_num, count, ano_count , index = [], 0, 0, 0

    for i in range(N):
        n = int(input())
        list_of_num.append(n)
    X = int(input())

    list_of_num.sort()
    ano_index = N-1

    while index < ano_index:
        Y = list_of_num[index] + list_of_num[ano_index]
        if Y < X:
            index += 1
        elif Y > X:
            ano_index -= 1
        else:
            count+=1
            if list_of_num[index] + list_of_num[ano_index-1] == X:
                ano_index -= 1
                ano_count += 1
            elif list_of_num[index+1] + list_of_num[ano_index] == X:
                index += 1
                ano_index += 1+ano_count
                sub_count = 0
            else:
                index +=1
    print(count)