n = int(input())
f = int(input())
cities = []
att_values = {}

for i  in range(n):
    c = int(input("Which city?"))
    cities.append(c)
    a = int(input("Attraction value: "))
    att_values.update({c:a})

cities.sort()
sorted(att_values.items(), key=lambda x: x[1])




"""
print(n)
print(f)
print(cities)
print(att_values)
"""