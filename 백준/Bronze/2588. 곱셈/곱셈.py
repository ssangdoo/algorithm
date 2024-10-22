n = 2
list1 = []
for i in range(n):
    list1.append(int(input()))

c = int(list1[0]*(list1[1]%10))
d = int(list1[0]*((list1[1]%100)//10))
e = int(list1[0]*(list1[1]//100))
print(c)
print(d)
print(e)
print(c+(10*d)+(100*e))