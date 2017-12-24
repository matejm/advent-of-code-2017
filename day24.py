with open('in') as f:
	components = f.readlines()

components = [tuple(sorted(map(int, i.split('/')))) for i in components]
components.sort()


def get_score(used, wanted, second_star=False):
	m = (0, 0)
	for i in range(zeros, len(components)):
		if i in used: continue

		next_wanted = 0
		if wanted == components[i][0]:
			next_wanted = components[i][1]
		elif wanted == components[i][1]:
			next_wanted = components[i][0]

		if next_wanted:
			used.add(i)
			
			recurs_score = list(get_score(used, next_wanted, second_star=second_star))
			recurs_score[0] += 1
			recurs_score[1] += component_score(i)

			if second_star:
				m = max(m, tuple(recurs_score))
			else:
				m = max(m, recurs_score, key=lambda x: x[1])

			used.remove(i)

	return m

def component_score(c):
	return sum(components[c])

strongest = -1
zeros = sum(components[i][0] == 0 for i in range(len(components)))

for starting in range(zeros):
	strongest = max(strongest, 
					get_score(set([starting]), components[starting][1])[1] + component_score(starting)
					)

print(strongest)

strongest = (-1, 0)

for starting in range(zeros):
	score = list(get_score(set([starting]), components[starting][1], second_star=True))
	score[1] += component_score(starting)
	strongest = max(strongest, tuple(score))

print(strongest[1])