from collections import defaultdict, deque

with open('in') as f:
	data = [i.split() for i in f.readlines()]

i = 0
var = defaultdict(int)
c = 0

var['a'] = 1


while i < len(data):
	if i == 23: print(var)
	command = data[i]

	if command[0] == 'set':
		x, y = command[1:]

		if y[0].isalpha():
			var[x] = var[y]
		else:
			var[x] = int(y)

	elif command[0] == 'sub':
		x, y = command[1:]

		if y[0].isalpha():
			var[x] -= var[y]
		else:
			var[x] -= int(y)

	elif command[0] == 'mul':
		x, y = command[1:]

		if y[0].isalpha():
			var[x] *= var[y]
		else:
			var[x] *= int(y)
		c += 1

	elif command[0] == 'jnz':
		x, y = command[1:]

		if x[0].isalpha() and var[x] != 0 or x[0].isdigit() and int(x) != 0:
			if y[0].isalpha():
				i += var[y]
			else:
				i += int(y)
			continue

	else:
		pass

	i += 1

print(var['h'])

# Second star solved in mathematica
# idea was to find count number of non primes two large numbers
# Count[Range[108100, 108100 + 17000, 17], _? CompositeQ]