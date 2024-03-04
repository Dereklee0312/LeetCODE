def fibonacci(n):
    # Check if the input is a valid positive integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer.")

    # Base cases for Fibonacci sequence
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # Generate Fibonacci sequence
    fib_sequence = [0, 1]  # Initialize with the first two numbers
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence

# Example usage:
print(fibonacci(10))
