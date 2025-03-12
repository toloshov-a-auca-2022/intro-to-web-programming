# Part 1
def square(n):
    return n * n
print(square(5))

# Part 2
def sum_of_list(*list):
    sum = 0
    for x in list:
        sum += x
    return sum

print(sum_of_list(1, 2, 3, 4, 5))

# Part 3
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
print(fibonacci(7))

# Part 4
def prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print(prime_number(7))
print(prime_number(10))