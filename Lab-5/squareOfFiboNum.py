def fibonacci(n):
    a, b = 0, 1
    fib_list = []
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

N = 10
fib_numbers = fibonacci(N)
squared_fib = list(map(lambda x: x ** 2, fib_numbers))
print(squared_fib)
