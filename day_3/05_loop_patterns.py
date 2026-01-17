# 05_loop_patterns.py
# Topic: Loop patterns (counting, accumulating)
# This program demonstrates common loop patterns used in programming.

def main():
    numbers = [5, 12, 8, 20, 7, 12, 5, 12]

    print(f"List of numbers: {numbers}")

    print("\n--- Pattern 1: Accumulating (Summing) ---")
    total = 0
    for num in numbers:
        total = total + num
    print(f"The sum of the numbers is: {total}")

    print("\n--- Pattern 2: Counting ---")
    target = 12
    count = 0
    for num in numbers:
        if num == target:
            count += 1
    print(f"The number {target} appears {count} times in the list.")

    print("\n--- Pattern 3: Finding Maximum (Manual) ---")
    # Assuming list is not empty
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    print(f"The maximum value in the list is: {max_val}")

if __name__ == "__main__":
    main()
