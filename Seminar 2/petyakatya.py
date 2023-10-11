def find_numbers(S, P):
    for x in range(1, 1001):
        for y in range(1, 1001):
            if x + y == S and x * y == P:
                return x, y
    return None

# Sample usage
S = int(input("Enter the sum of numbers S: "))
P = int(input("Enter the product of numbers P: "))

result = find_numbers(S, P)
if result:
    print(f"Numbers thought of by Petya: {result[0]} and {result[1]}")
else:
    print("Unable to find such numbers")
