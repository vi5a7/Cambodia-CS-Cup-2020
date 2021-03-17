n = int(input())
k = int(input())
s = int(input())
ls, st_coro_ls, flag = [], set(), True
st_coro_ls.add(s)
all_participants = list(range(1, n+1))

for i in range(k):
    j = [int(j) for j in input().split()]
    ls.append(j)

while True:
    flag = False
    for i in ls:
        if i[0] in st_coro_ls or i[1] in st_coro_ls:
            st_coro_ls.add(i[0])
            st_coro_ls.add(i[1])
            ls.remove(i)
            flag = True
    if not flag:
        break

res = len(set(all_participants) - st_coro_ls)

if res > 0:
    print("Will be")
else:
    print("Coronavirus")