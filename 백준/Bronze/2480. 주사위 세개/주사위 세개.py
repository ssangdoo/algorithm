a, b, c = map(int, input().split())

if a==b==c:
    prize = 10000 + a*1000
elif a==b:
    prize = 1000 + a*100
elif b==c:
    prize = 1000 + b*100
elif a==c:
    prize = 1000 + c*100
elif a!=b and b!=c and a!=c:
    if a>b and a>c:
        prize = a*100
    elif b>a and b>c:
        prize = b*100
    elif c>a and c>b:
        prize = c*100
print(prize)