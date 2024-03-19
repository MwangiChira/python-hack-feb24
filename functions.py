def fibonacci(n):
    if n <= 1:
        return [0] if n == 1 else []
    else:
        a, b = 0, 1
        fibonacci_sequence = [a, b]
        for _ in range(2, n):
            c = a + b
            fibonacci_sequence.append(c)
            a, b = b, c  # Update values of a and b for next iteration
        return fibonacci_sequence

num_terms = int(input("Enter the number of terms: "))
fibonacci_sequence = fibonacci(num_terms)
print(f"Fibonacci sequence up to {num_terms}:")
print(fibonacci_sequence)
