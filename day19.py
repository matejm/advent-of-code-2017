with open('in') as f:
	m = f.readlines()

x = m[0].index('|')
y = 0

d = 'down'

path = ''
step = 0

while True:
	step += 1
	if d == 'down' and m[y + 1][x] != ' ':
		y += 1
		if m[y][x].isalpha():
			path += m[y][x]
		elif m[y][x] == '+':
			if m[y][x + 1] != ' ':
				d = 'right'
			elif m[y][x - 1] != ' ':
				d = 'left'
			else:
				print(x, y, 'problem', d)
	elif d == 'up' and m[y - 1][x] != ' ':
		y -= 1
		if m[y][x].isalpha():
			path += m[y][x]
		elif m[y][x] == '+':
			if m[y][x + 1] != ' ':
				d = 'right'
			elif m[y][x - 1] != ' ':
				d = 'left'
			else:
				print(x, y, 'problem', d)
	elif d == 'right' and m[y][x + 1] != ' ':
		x += 1
		if m[y][x].isalpha():
			path += m[y][x]
		elif m[y][x] == '+':
			if m[y + 1][x] != ' ':
				d = 'down'
			elif m[y - 1][x] != ' ':
				d = 'up'
			else:
				print(x, y, 'problem', d)
	elif d == 'left' and m[y][x - 1] != ' ':
		x -= 1
		if m[y][x].isalpha():
			path += m[y][x]
		elif m[y][x] == '+':
			if m[y + 1][x] != ' ':
				d = 'down'
			elif m[y - 1][x] != ' ':
				d = 'up'
			else:
				print(x, y, 'problem', d)
	else:
		break

print(path)
print(step)
