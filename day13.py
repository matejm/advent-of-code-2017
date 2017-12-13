with open('in') as f:
    l = f.readlines()
l = [list(map(int,i.split(': '))) for i in l]

for c in range(10000000):
    s = 0
    for i in l:
        a, b = i
        if (c + a) % (b+b-2) == 0:
            if c == 0:
                s += a * b
            else:
                break
    else:
        if c == 0:
            print(s)
        else:
            print(c)
            break


