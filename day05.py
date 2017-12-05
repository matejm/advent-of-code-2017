with open('in') as f:
	l = f.readlines()

l = list(map(int, l))

i = 0
c = 0
while i < len(l) and i >= 0:
	t = l[i]
	if l[i] >= 3:
		l[i] -= 1
	else:
		l[i] += 1
	i += t
	c += 1
print(c)