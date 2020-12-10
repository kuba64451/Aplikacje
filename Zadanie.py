def Fibonacci(n):
    fib1, fib2 = 2, 3
    for i in range(n+1):
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2

print(list(Fibonacci(3)))