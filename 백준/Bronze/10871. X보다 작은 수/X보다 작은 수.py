N, X = map(int, input().split())
arr = list(map(int, input().split()))
while max(arr) >= X:
    del arr[arr.index(max(arr))]
print(*arr)