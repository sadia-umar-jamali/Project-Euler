# Find the sum of all the multiples of 3 or 5 below 1000.
from itertools import chain
import time


def sum_multiples_brute_force():
    # Brute force approach: Check each number from 1 to 999
    total = 0
    for num in range(1, 1000):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total


def sum_multiples_optimized():
    # Optimized approach using itertools and set operations
    # Generate multiples of 3 and 5 up to 999
    multiples_3 = range(0, 1000, 3)
    multiples_5 = range(0, 1000, 5)

    # Use set to remove duplicates (numbers divisible by both 3 and 5)
    # Chain combines both iterables efficiently
    unique_multiples = set(chain(multiples_3, multiples_5))

    return sum(unique_multiples)


if __name__ == "__main__":
    # Compare both solutions
    result_brute = sum_multiples_brute_force()
    result_optimized = sum_multiples_optimized()

    print(f"Brute force solution: {result_brute}")
    print(f"Optimized solution: {result_optimized}")
    assert (
        result_brute == result_optimized
    ), "Both solutions should yield the same result"
    # Measure and display runtime for both solutions

    # Measure brute force solution
    start_time = time.time()
    sum_multiples_brute_force()
    brute_force_time = time.time() - start_time

    # Measure optimized solution
    start_time = time.time()
    sum_multiples_optimized()
    optimized_time = time.time() - start_time

    print(f"Brute force solution runtime: {brute_force_time:.6f} seconds")
    print(f"Optimized solution runtime: {optimized_time:.6f} seconds")
    print(f"Optimization speedup: {brute_force_time / optimized_time:.2f}x")
