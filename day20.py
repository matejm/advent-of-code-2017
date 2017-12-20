with open('in') as f:
	data = f.readlines()

p = []
v = []
a = []

for line in data:
	line = line.replace('<', '').replace(' ', '').replace('>', '').replace('=', '').replace('a', '').replace('p', '').replace('v', '')
	p1, p2, p3, v1, v2, v3, a1, a2, a3 = map(int, line.split(','))
	
	p.append([p1, p2, p3])
	v.append([v1, v2, v3])
	a.append([a1, a2, a3])

print(min(enumerate(a), key=lambda c: c[1][0]**2 + c[1][1]**2 + c[1][2]**2)[0])

for __ in range(1000):
	s = set()
	d = {}

	for i in range(len(p)):
		if not p[i]: continue

		for j in range(3):
			v[i][j] += a[i][j]
			p[i][j] += v[i][j]

		t = tuple(p[i])
		if t in s:
			p[d[t]] = []
			p[i] = []
		else:		
			s.add(t)
			d[t] = i

print(sum(1 for i in p if i))


