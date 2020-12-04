def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)


n = int(input())
f = int(input())
cities = []
att_values = {}
max = 0
max_list = []

for i in range(n):
    c = int(input("Which city?"))
    cities.append(c)
    a = int(input("Attraction value: "))
    att_values.update({c:a})

cities.sort()
sorted(att_values.items(), key=lambda x: x[1])

for i in range(len(cities)):
    


"""
print(n)
print(f)
print(cities)
print(att_values)
"""