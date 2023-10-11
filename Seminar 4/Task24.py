n = int(input("Введите количество кустов: "))
berries = list(map(int, input("Введите количество ягод на каждом кусте через пробел: ").split()))
berries += berries[:2]

max_berries = 0

for i in range(n):
    sum_berries = berries[i] + berries[i + 1] + berries[i + 2]
    max_berries = max(max_berries, sum_berries)

print(max_berries)
