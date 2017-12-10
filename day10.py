def reverse(i, ln, l):
	for j in range(ln // 2):
		l[(i + j) % len(l)], l[(i + ln - j - 1) % len(l)] = l[(i + ln - j - 1) % len(l)], l[(i + j) % len(l)]

with open('in') as f:
	twists = f.readline().rstrip()

twists = list(map(int, twists.split(',')))

l = [i for i in range(256)]

skip = 0
i = 0

for twist in twists:
	reverse(i, twist, l)
	i += twist + skip
	skip += 1

print(l[0] * l[1])


# Second star
with open('in') as f:
	twists = f.readline().rstrip()

twists = list(map(ord, twists))
twists += [17, 31, 73, 47, 23]

i = 0
skip = 0
l = [i for i in range(256)]

for j in range(64):
	for twist in twists:
		reverse(i, twist, l)
		i += twist + skip
		skip += 1

dense = []
for i in range(16):
	k = l[i * 16]
	for j in range(1, 16):
		k ^= l[i * 16 + j]
	dense.append(k)

out = ''.join('{:0>2x}'.format(i) for i in dense)
print(out)