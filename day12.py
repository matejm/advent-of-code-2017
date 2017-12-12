from collections import deque

with open('in') as f:
	data = f.readlines()

g = [[] for i in range(len(data))]

for line in data:
	line = line.replace(',', '')
	a, __, *b = line.split()
	a = int(a)
	for i in b:
		g[a].append(int(i))

visited = [False for i in range(len(data))]

first = True
groups = 0

for i in range(len(data)):
	if visited[i]: continue

	q = deque()
	q.append(i)
	visited[i] = True
	c = 1
	groups += 1

	while q:
		a = q.popleft()
		for b in g[a]:
			if not visited[b]:
				visited[b] = True
				q.append(b)
				c += 1

	if first:
		first = False
		print(c)

print(groups)