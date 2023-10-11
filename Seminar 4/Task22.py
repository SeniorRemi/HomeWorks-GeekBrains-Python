n = int(input('Введите количество элементов 1 набора '))
list_1 = [int(i) for i in input('Введите элементы: ').split()[:n]]
m = int(input('Введите количество элементов 2 набора '))
list_2 = [int(i) for i in input('Введите элементы: ').split()[:m]]

print(*[i for i in list_1 if i not in list_2])
