N = int(input())
abcd = list(map(int, input().split()))
v = int(input())
sum = 0
for i in range(N):
    if abcd[i] == v:
        sum += 1
print(sum)