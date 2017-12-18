from collections import defaultdict, deque

with open('in') as f:
	data = [i.split() for i in f.readlines()]

i = 0
var = defaultdict(int)
latest = 0

while True:
	command = data[i]

	if command[0] == 'set':
		x, y = command[1:]

		if y[0].isalpha():
			var[x] = var[y]
		else:
			var[x] = int(y)

	elif command[0] == 'snd':
		latest = var[command[1]]

	elif command[0] == 'add':
		x, y = command[1:]

		if y[0].isalpha():
			var[x] += var[y]
		else:
			var[x] += int(y)

	elif command[0] == 'mul':
		x, y = command[1:]

		if y[0].isalpha():
			var[x] *= var[y]
		else:
			var[x] *= int(y)

	elif command[0] == 'mod':
		x, y = command[1:]

		if y[0].isalpha():
			var[x] %= var[y]
		else:
			var[x] %= int(y)

	elif command[0] == 'rcv':
		if var[command[1]] != 0:
			var[command[1]] = latest
			print(latest)
			break

	elif command[0] == 'jgz':
		x, y = command[1:]

		if x[0].isalpha() and var[x] > 0 or x[0].isdigit() and int(x) > 0:
			if y[0].isalpha():
				i += var[y]
			else:
				i += int(y)
			continue
	else:
		print('Wrong command')

	i += 1


# second star:

i = 0
j = 0
vari = defaultdict(int)
varj = defaultdict(int)

queuei = deque()
queuej = deque()

vari['p'] = 0
varj['p'] = 1

c = 0


def execute(program):
	global i, j, vari, varj, queuei, queuej, c
	if program == 0:
		k = i
		var = vari
	else:
		k = j
		var = varj

	command = data[k]

	if command[0] == 'set':
		x, y = command[1:]

		if y[0].isalpha():
			var[x] = var[y]
		else:
			var[x] = int(y)

	elif command[0] == 'snd':
		if program == 0:
			queuej.append(var[command[1]])
		else: 
			queuei.append(var[command[1]])
			c += 1

	elif command[0] == 'add':
		x, y = command[1:]

		if y[0].isalpha():
			var[x] += var[y]
		else:
			var[x] += int(y)

	elif command[0] == 'mul':
		x, y = command[1:]

		if y[0].isalpha():
			var[x] *= var[y]
		else:
			var[x] *= int(y)

	elif command[0] == 'mod':
		x, y = command[1:]

		if y[0].isalpha():
			var[x] %= var[y]
		else:
			var[x] %= int(y)

	elif command[0] == 'rcv':
		if program == 0:
			if not len(queuei):
				return k
			var[command[1]] = queuei.popleft()
		else: 
			if not len(queuej):
				return k
			var[command[1]] = queuej.popleft()

	elif command[0] == 'jgz':
		x, y = command[1:]

		if x[0].isalpha() and var[x] > 0 or x[0].isdigit() and int(x) > 0:
			if y[0].isalpha():
				k += var[y]
			else:
				k += int(y)
			return k
	else:
		print('Wrong command')

	return k + 1

for __ in range(1000000):
	i = execute(0)
	j = execute(1)

print(c)