from os import remove

cities = ["Москва", "Тверь", "Вологда"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "wd", True, 8.5]
print(cities[0])
print(numbers[-1])
#print(cities[10])
a = numbers[1] = 10
print(numbers)
b = mixed[-1] = "Python"
print(mixed)
print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(sorted(numbers))
w = [1, 2, 3]
t = [4, 5]
z = w + t
print(z)
za = ["Python", "is", "awesome"]
print(za*3)
print(3 in numbers)
print("Москва" in cities)
print([1, 2] in mixed)
del cities[2]
print(cities)
b = "Python"
ds = list(b)
print(ds)
print(ds.index(min(ds)))
print(ds.index(max(ds)))
#zc = sum(ds)