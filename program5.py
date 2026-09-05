def fibonacci(n):
    a, b = 0, 1
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print(f"Fibonacci sequence up to {n} term:")
        print(a)
    else:
        print(f"Fibonacci sequence up to {n} terms:")
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b  # Update a and b simultaneously
        print()
terms = int(input("How many terms? "))
fibonacci(terms)