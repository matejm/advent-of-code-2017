def dance(l):
	for command in data:
		c, *x = command
		x = ''.join(x)

		if c == 's':
			l =  l[-int(x):] + l[:-int(x)]
		elif c == 'x':
			a = x[:x.find('/')]
			b = x[x.find('/')+1:]

			l[int(a)], l[int(b)] = l[int(b)], l[int(a)]
		elif c == 'p':
			a = x[:x.find('/')]
			b = x[x.find('/')+1:]

			ai = l.index(a)
			bi = l.index(b)
			l[ai] = b
			l[bi] = a
	return l

with open('in') as f:
	data = f.readline()
data = data.split(',')

starting = list('abcdefghijklmnop')
l = starting[:]

l = dance(l)

print(''.join(l))

s = set()
n = -1
for i in range(2, 200):
	l = dance(l)

	if tuple(l) in s:
		n = i
		break

	s.add(tuple(l))

if n == -1:
	print('Problem')
else:
	k = 10**9 % n

	for i in range(k): l = dance(l)
	print(''.join(l))