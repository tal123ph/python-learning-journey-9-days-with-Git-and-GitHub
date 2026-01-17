# 04_nested_loops.py
# Topic: Nested loops
# This program demonstrates nested loops (a loop inside another loop).

def main():
    print("--- Nested Loop: Multiplication Table ---")
    # Generating a small multiplication table for numbers 1 to 3
    for i in range(1, 4):
        print(f"Multiplication Table for {i}:")
        for j in range(1, 4):
            results = i * j
            print(f"  {i} x {j} = {results}")
        print("-" * 20)

    print("\n--- Nested Loop: Coordinate Grid ---")
    # Printing coordinates for a 3x3 grid
    rows = 3
    cols = 3
    for r in range(rows):
        for c in range(cols):
            print(f"({r},{c})", end=" ")
        print() # Newline after each row

if __name__ == "__main__":
    main()
