from collections import defaultdict

def adj(tupl):
	x, y = tupl
	return [
		(x-1, y-1), (x-1, y), (x-1, y+1),
		(x, y-1), (x, y+1),
		(x+1, y-1), (x+1, y), (x+1, y+1)
	]


inp = 289326

c = 1
b = False
for i in range(1, 1000):
	for k in range(4):
		for j in range(i-1, 0, -1):
			c += 1
			if c == inp:
				print(i + j)
				b = True
				break			
		for j in range(0, i+1):
			c += 1
			if c == inp:
				print(i + j)
				b = True
				break
		if b:
			break
	if b:
		break

d = defaultdict(int)
c = 1
d[(0, 0)] = 1
l = [0, 0]

for i in range(1, 100, 2):
	for j in range(i):
		l[0] += 1
		d[tuple(l)] = sum(d[a] for a in adj(l))
		if d[tuple(l)] > inp:
			print(d[tuple(l)])
			exit()
	for j in range(i):
		l[1] += 1
		d[tuple(l)] = sum(d[a] for a in adj(l))
		if d[tuple(l)] > inp:
			print(d[tuple(l)])
			exit()
	for j in range(i+1):
		l[0] -= 1
		d[tuple(l)] = sum(d[a] for a in adj(l))
		if d[tuple(l)] > inp:
			print(d[tuple(l)])
			exit()
	for j in range(i+1):
		l[1] -= 1
		d[tuple(l)] = sum(d[a] for a in adj(l))
		if d[tuple(l)] > inp:
			print(d[tuple(l)])
			exit()
