from collections import defaultdict

def get_weight(node):
	if not g[node]:
		return weight[node]
	w = []
	for i in g[node]:
		w.append(get_weight(i))

	if min(w) == max(w):
		return w[0] * len(w) + weight[node]

	w1, w2 = set(w)
	if w.count(w1) < w.count(w2):
		w1, w2 = w2, w1

	child = g[node][w.index(w2)]
	print(weight[child] + w1 - w2)
	exit()
	# return w1 * len(w)	


with open('in') as f:
	l = f.readlines()

all_programs = set()
children = set()

g = defaultdict(list)

weight = {}

for i in l:
	a = i.replace(',', '').split()

	all_programs.add(a[0])
	weight[a[0]] = int(a[1][1:-1])

	if '->' in i:
		childr = a[3:]
		for c in childr:
			g[a[0]].append(c)
			children.add(c)

root = list(all_programs - children)[0]

print(root)

get_weight(root)