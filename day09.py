with open('in') as f:
	l = f.readline().rstrip()

n = 0
garbage = False
ignore = False

s = 0
c = 0

for j, i in enumerate(l):
	if ignore:
		ignore = False
		continue

	if i == '!':
		ignore = True
		continue
	
	if garbage:
		if i == '>':
			garbage = False
		else:
			c += 1
		continue

	if i == '<':
		garbage = True
	elif i == '{':
		n += 1
	elif i == '}':
		s += n
		n -= 1

print(s, c)