def fibonacci(n: int):
    """ The function returns the nth number in the Fibonacci sequence (1, 1, 2, 3, 5, 8 etc.); n > 0"""

    if n <= 2:
        # the first two are ones
        return 1

    # All other numbers equal the sum of the two preceding numbers in the sequence
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test that everything works
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"The {i}. number in the Fibonacci sequence is {fibonacci(i)}")