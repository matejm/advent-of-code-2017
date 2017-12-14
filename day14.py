from collections import deque

def reverse(i, ln, l):
	for j in range(ln // 2):
		l[(i + j) % len(l)], l[(i + ln - j - 1) % len(l)] = l[(i + ln - j - 1) % len(l)], l[(i + j) % len(l)]

def knot(twists):
    twists = list(map(ord, twists))
    twists += [17, 31, 73, 47, 23]

    i = 0
    skip = 0
    l = [i for i in range(256)]

    for j in range(64):
	       for twist in twists:
	           reverse(i, twist, l)
	           i += twist + skip
	           skip += 1

    dense = []
    for i in range(16):
        k = l[i * 16]
        for j in range(1, 16):
            k ^= l[i * 16 + j]
        dense.append(k)

    return ''.join('{:0>8b}'.format(i) for i in dense)

s = 0
m = []
for i in range(128):
    m.append(knot('ugkiagan-' + str(i)))
    s+= m[-1].count('1')
print(s)

vis = [[False]*128 for i in range(128)]
g = 0
for i in range(128):
    for j in range(128):
        if vis[i][j]: continue
        if m[i][j] == '0': continue
        
        q = deque()
        g += 1
        q.append((i,j))
        vis[i][j] = 1
        
        while q:
            x,y = q.popleft()
            if x<0:
                print(x)
            
            d = ((1,0),(0,1),(-1,0),(0,-1))
            for a,b in d:
                if x+a < 0 or x+a >= 128:
                    continue
                if y+b < 0 or y+b >= 128:
                    continue
                if (not vis[x+a][y+b]) and m[x+a][y+b] == '1':
                    q.append((x+a,y+b))
                    vis[x+a][y+b] = True

print(g)
