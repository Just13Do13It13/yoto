#1. Создание и копирование списков
from os import replace

cities = ['Москва', 'Санкт-Петербург', 'Казань', 'Нижний Новгород', 'Екатеринбург']
cities_copy = cities[:]
print(cities_copy)
print(cities)
print(id(cities))
print(id(cities_copy))
#2. Извлечение элементов с помощью срезов
print(cities_copy[1:3])
print(cities_copy[2::])
print(cities_copy[0:3])
print(cities_copy)
print(cities_copy[-2:])
print(cities_copy[0:5:2])
b = cities[1:3] = "Волгоград", "Омск"
print(b)
s = [1, 2, 3]
g = [4, 5, 6]
l = s+g
print(l)
f = ["Python", "rocks"]
print(f*2)
y = [1, 2, 3]
i = [1, 2, 3]
print(y == i)
d = [10, 5, 3] > [5, 10, 3]
print(d)
gg = [1, 2, 3] == [1, 2, "abc"]
print(gg)
chars = list("Python")
print(max(chars))
print(min(chars))
ds = sum(chars)
print(ds)