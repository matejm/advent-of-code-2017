a = 277
b = 349

c = 0
x = 256*256-1

for i in range(40000000):
    a *= 16807
    a %= 2147483647

    b *= 48271
    b %= 2147483647
    
    if a&x == b&x:
        c+= 1
        print(i, c)

print(c)

a = 277
b = 349
c2 = c
c = 0

for i in range(5000000):
    a *= 16807
    a %= 2147483647
    while a%4 != 0:
        a *= 16807
        a %= 2147483647
    
    b *= 48271
    b %= 2147483647
    while b%8 != 0:
        b *= 48271
        b %= 2147483647
    
    if a&x == b&x:
        c+= 1
        print(i, c)

print(c2, c)