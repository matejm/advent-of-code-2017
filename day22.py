from collections import defaultdict

with open('in') as f:
	field = f.readlines()

d = defaultdict(bool)

for i in range(len(field)):
	for j in range(len(field[i])):
		d[(i, j)] = field[i][j] == '#'

p = len(field) // 2, len(field[0].rstrip()) // 2
direction = 'up'

c = 0

for ___ in range(10000):
	# print(p, direction, d[p])
	# for i in range(-1, 5):
	# 	print(''.join('#' if d[(i, j)] else '.' for j in  range(-1, 5)))


	if direction == 'up':
		direction = 'left' if not d[p] else 'right'
	elif direction == 'down':
		direction = 'left' if d[p] else 'right'
	elif direction == 'left':
		direction = 'down' if not d[p] else 'up'
	elif direction == 'right':
		direction = 'down' if d[p] else 'up'

	d[p] = not d[p] 
	c += d[p]

	if direction == 'left':
		p = p[0], p[1] - 1
	elif direction == 'right':
		p = p[0], p[1] + 1
	elif direction == 'up':
		p = p[0] - 1, p[1]
	elif direction == 'down':
		p = p[0] + 1, p[1]

print(c)

for i in range(-10, 10):
	print(''.join('#' if d[(i, j)] else '.' for j in  range(-10, 10)))



# SECOND STAR

d = defaultdict(int)

for i in range(len(field)):
	for j in range(len(field[i])):
		d[(i, j)] = 2 if field[i][j] == '#' else 0

p = len(field) // 2, len(field[0].rstrip()) // 2
direction = 'up'

c = 0

for ___ in range(10**7):
	# print(p, direction, d[p])
	# for i in range(-1, 5):
	# 	print(''.join('#' if d[(i, j)] else '.' for j in  range(-1, 5)))


	if direction == 'up':
		if d[p] == 0:
			direction = 'left'
		elif d[p] == 1:
			direction = 'up'
		elif d[p] == 2:
			direction = 'right'
		elif d[p] == 3:
			direction = 'down'
	elif direction == 'down':
		if d[p] == 0:
			direction = 'right'
		elif d[p] == 1:
			direction = 'down'
		elif d[p] == 2:
			direction = 'left'
		else:
			direction = 'up'
	elif direction == 'left':
		if d[p] == 0:
			direction = 'down'
		elif d[p] == 1:
			direction = 'left'
		elif d[p] == 2:
			direction = 'up'
		else:
			direction = 'right'
	elif direction == 'right':
		if d[p] == 0:
			direction = 'up'
		elif d[p] == 1:
			direction = 'right'
		elif d[p] == 2:
			direction = 'down'
		else:
			direction = 'left'

	d[p] += 1
	d[p] %= 4 
	if d[p] == 2:
		c += 1

	if direction == 'left':
		p = p[0], p[1] - 1
	elif direction == 'right':
		p = p[0], p[1] + 1
	elif direction == 'up':
		p = p[0] - 1, p[1]
	elif direction == 'down':
		p = p[0] + 1, p[1]

print(c)
