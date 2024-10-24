a, b = map(int, input().split())
c = int(input())
d = c//60
e = c%60
h = a+d
m = b+e
if m >= 60:
    m -= 60
    h += 1
if h >= 24:
    h -=24
print(h, m)    