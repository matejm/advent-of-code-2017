with open('in') as f:
	data = f.readlines()

l = list(map(lambda x: x.split(), data))


# First star
print(sum(len(i) == len(set(i)) for i in l))

# Second star
print(sum(len(i) == len(set(map(lambda x: tuple(sorted(x)), i))) for i in l))

