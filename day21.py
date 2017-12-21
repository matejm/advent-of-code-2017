from collections import defaultdict

def rotations(m):
    down = m[::-1]

    left = [[] for i in range(len(m))]
    right = [[] for i in range(len(m))]

    for line in m:
        for i, j in enumerate(line):
            left[i].append(j)
            right[-i -1].append(j)

    l = [m, down, right, left]

    # mirror
    m = [i[::-1] for i in m]

    down = m[::-1]

    left = [[] for i in range(len(m))]
    right = [[] for i in range(len(m))]

    for line in reversed(m):
        for i, j in enumerate(line):
            left[i].append(j)
            right[-i-1].append(j)

    l += [m, down, right, left]
    return l


with open('in') as f:
    rules = [i.replace(' ', '').split('=>') for i in  f.readlines()]

d = defaultdict(list)

for match, replace in rules:
    d[tuple(match.split('/'))] = tuple(replace.split('/'))


grid = ['.#.', '..#', '###']

for __ in range(18):
    if len(grid) % 2 == 0:
        m = [['' for i in range(len(grid) // 2 * 3)] for j in range(len(grid) // 2 * 3)]

        for i in range(0, len(grid), 2):
            for j in range(0, len(grid), 2):
                m2 = [k[j : j+2] for k in grid[i: i+2]]

                m3 = []
                for r in rotations(m2):
                    if d[tuple([''.join(q) for q in r])]:
                        m3 = d[tuple(''.join(q) for q in r)]
                        break

                for a in range(3):
                    for b in range(3):
                        m[i // 2 * 3 + a][j // 2 * 3 + b] = m3[a][b]
    else:
        m = [['' for i in range(len(grid) // 3 * 4)] for j in range(len(grid) // 3 * 4)]

        for i in range(0, len(grid), 3):
            for j in range(0, len(grid), 3):
                m2 = [k[j : j+3] for k in grid[i: i+3]]

                m3 = []

                for r in rotations(m2):
                    if d[tuple([''.join(q) for q in r])]:
                        m3 = d[tuple(''.join(q) for q in r)]
                        break

                for a in range(4):
                    for b in range(4):
                        m[i // 3 * 4 + a][j // 3 * 4 + b] = m3[a][b]
    grid = m

print(sum(i.count('#') for i in grid))