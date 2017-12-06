initial_state = '14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4'.split()
initial_state = list(map(int, initial_state))

state = initial_state[:]

states = set()
states.add(tuple(initial_state))

indices = dict()
indices[tuple(initial_state)] = 0

c = 0
while True:
	m = max(state)
	for i in range(len(state)):
		if state[i] == m:
			break
	state[i] = 0

	j = (i+1) % len(state)
	while m:
		state[j] += 1
		m -= 1
		j+=1
		j %= len(state)
	c += 1
	if tuple(state) in states:
		print(c - indices[tuple(state)])
		break
	states.add(tuple(state))
	indices[tuple(state)] = c
print(c)