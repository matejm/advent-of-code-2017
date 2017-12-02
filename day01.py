with open('in') as f:
	data = f.readline().rstrip()

l = list(map(int, data))

first_star = 0
second_star = 0
d = len(l) // 2
for i in range(len(l)):
	if l[i] == l[i - 1]:
		first_star += l[i]
	if l[i] == l[i - d]:
		second_star += l[i]

print(first_star, second_star)