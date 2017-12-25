from collections import defaultdict

with open('in') as f:
	data = f.readlines()[3:]

rules = dict()

for s in 'ABCDEF':
	k = data[1:10]
	data = data[10:]

	a = k[1:4]
	b = k[5:8]

	vala = int(a[0].rstrip()[-2])
	nexta = 'right' in a[1]
	statea = a[2].rstrip()[-2]

	valb = int(b[0].rstrip()[-2])
	nextb = 'right' in b[1]
	stateb = b[2].rstrip()[-2]

	rules[s] = ((vala, nexta, statea), (valb, nextb, stateb))

tape = defaultdict(bool)
state = 'A'
loc = 0

for i in range(12399302):
	if tape[loc] == 1:
		tape[loc] = rules[state][1][0]
		loc += 1 if rules[state][1][1] else -1
		state = rules[state][1][2]

	else:
		tape[loc] = rules[state][0][0]
		loc += 1 if rules[state][0][1] else -1
		state = rules[state][0][2]

c = 0
for k in tape.keys():
	c += tape[k] 
print(c)