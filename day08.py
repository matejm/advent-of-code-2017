from collections import defaultdict

with open('in') as f:
	data = f.readlines()

global_vars = defaultdict(int)
m = -1000000

for line in data:
	var, what, amount, __, *when = line.split()
	when = ''.join(when)
	amount = int(amount)

	if eval(when, None, global_vars):
		global_vars[var] += amount * (-1 if what == 'dec' else 1)
		m = max(max(global_vars.values()), m)

print(max(global_vars.values()), m)