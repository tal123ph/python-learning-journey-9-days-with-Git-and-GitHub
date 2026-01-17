# 03_break_continue.py
# Topic: Break and continue statements
# This program demonstrates how to control loop execution flow using break and continue.

def main():
    print("--- Continue Statement Example ---")
    print("Printing only odd numbers from 1 to 10:")
    for i in range(1, 11):
        if i % 2 == 0:
            continue  # Skip the rest of the code inside the loop for even numbers
        print(i, end=" ")
    print("\n")

    print("\n--- Break Statement Example ---")
    print("Looking for the first number divisible by 7 in a list:")
    numbers = [10, 23, 45, 14, 9, 21]
    
    for num in numbers:
        print(f"Checking {num}...")
        if num % 7 == 0:
            print(f"Found it! {num} is divisible by 7.")
            break  # Exit the loop immediately
    else:
        # This else block executes if the loop completes normally (without break)
        print("No number divisible by 7 found.")

if __name__ == "__main__":
    main()
