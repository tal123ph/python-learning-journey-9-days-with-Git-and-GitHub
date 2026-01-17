# 01_for_loops_range.py
# Topic: For loops and Range function
# This program demonstrates the usage of for loops with the range() function.

def main():
    print("--- Basic Range Example ---")
    # Loop from 0 to 4
    for i in range(5):
        print(f"Iteration: {i}")

    print("\n--- Range with Start and Stop ---")
    # Loop from 1 to 5
    for i in range(1, 6):
        print(f"Number: {i}")

    print("\n--- Range with Step ---")
    # Loop from 0 to 10 with step of 2
    for i in range(0, 11, 2):
        print(f"Even number: {i}")

    print("\n--- Reverse Range ---")
    # Loop from 10 down to 1
    for i in range(10, 0, -1):
        print(f"Countdown: {i}")

if __name__ == "__main__":
    main()
