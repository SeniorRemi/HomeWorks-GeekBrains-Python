import random

n = int(input("The amount of money "))

# Генерация списка монеток
mas = [random.randint(0, 1) for _ in range(n)]

print("Money on the table ", mas)

# Находим минимальное количество монеток для переворота
print(min(mas.count(0), mas.count(1)))
