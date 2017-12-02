with open('in') as f:
	data = f.readlines()

data = [list(map(int, i.split())) for i in data]

# FIRST STAR
s = sum(map(lambda x: max(x) - min(x), data))
print(s)

# SECOND STAR
s = 0
for row in data:
	for i in range(len(row)):
		for j in range(i + 1, len(row)):
			if row[i] % row[j] == 0 or row[j] % row[i] == 0:
				s += max(row[i] // row[j], row[j] // row[i])
				break
print(s)
