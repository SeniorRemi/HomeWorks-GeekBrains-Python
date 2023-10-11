def print_powers_of_two(N):
    power = 1
    while power <= N:
        print(power)
        power *= 2
N = int(input("Enter number2 N: "))
print_powers_of_two(N)