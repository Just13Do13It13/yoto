# 1. Напишите декоратор uppercase_decorator, который делает результат выполнения функции прописными буквами.
# Пример вызова:
# @uppercase_decorator
# def say_hello():
#     return "hello, world!"
# print(say_hello())  # "HELLO, WORLD!"
# def lower_decorator(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res.lower()
#     return wrapper
#
# @lower_decorator
# def lowercase(text):
#     return text.lower()
# print(lowercase("Ну чоА ЛЫСАЯ БашКвинция"))
# 2. Создайте декоратор repeat(n), который выполняет функцию n раз.
# Пример вызова:
# @repeat(3)
# def hello():
#     print("Hello!")
# hello()
# Вывод:
# Hello!
# Hello!
# Hello!
# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @repeat(5)
# def hello():
#     print('hello')
# hello()
# 3. Создайте декоратор cache, который кэширует результаты выполнения функции.
# Если функция вызывается с теми же аргументами – возвращать сохраненный результат вместо нового вычисления.
# Пример вызова:
# @cache
# def slow_add(a, b):
#     print(f"Вычисляю {a} + {b}...")
#     return a + b
# print(slow_add(2, 3))  # "Вычисляю 2 + 3..." 5
# print(slow_add(2, 3))  # 5 (результат взят из кэша)
# def cache(func):
#     cache_dict = {}
#     def wrapper(*args, **kwargs):
#         key = (args, frozenset(kwargs.items()))
#         if key in cache_dict:
#             return cache_dict[key]
#         result = func(*args, **kwargs)
#         cache_dict[key] = result
#         return result
#     return wrapper
#
# @cache
# def slow_add(a, b):
#     print(f"Вычисляю {a} + {b}...")
#     return a + b
#
# print(slow_add(2, 3))
# print(slow_add(2, 3))
# 4. Создайте декоратор с таймером timer(repeat), который выполняет функцию repeat раз и выводит среднее время выполнения.
# Пример вызова:
# @timer(3)
# def slow_function():
#     time.sleep(1)
# slow_function()  # Среднее время выполнения: 1.0002 сек
import time
import time

def timer(repeat):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total = 0
            result = None

            for _ in range(repeat):
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                total += (end - start)

            average = total / repeat
            print(f"Среднее время выполнения: {average:.5f} сек")
            return result
        return wrapper
    return decorator

@timer(3)
def slow_function():
    time.sleep(1)

slow_function()