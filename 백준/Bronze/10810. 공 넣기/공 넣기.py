N, M = map(int, input().split())
arr = list()

for a in range(N):
    arr.append(0)

for a in range(M):
    i, j, k = map(int, input().split())
    while j-i >= 0:
            arr[i-1] = k
            i += 1

for a in range(N):
    print(arr[a], end=' ')