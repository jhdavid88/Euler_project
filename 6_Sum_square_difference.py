k = 0
l = 0
o = 0
for i in range(1,101):
    k = k + i**2
    l = l + i
    o = l**2

print("*"*100)
print(k)
print(o)
print(o-k)