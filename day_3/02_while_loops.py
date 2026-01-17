# 02_while_loops.py
# Topic: While loops
# This program demonstrates the usage of while loops.

def main():
    print("--- Basic While Loop (Countdown) ---")
    count = 5
    while count > 0:
        print(f"Count: {count}")
        count -= 1
    print("Blast off!")

    print("\n--- While Loop with User Input Simulation ---")
    # Simulating a scenario where we loop until a condition is met
    secret_number = 7
    guess = 0
    attempt = 1
    
    # Simulating guesses
    guesses = [3, 9, 7] 
    
    index = 0
    while guess != secret_number:
        if index < len(guesses):
            guess = guesses[index]
            print(f"Attempt {attempt}: Guessed {guess}")
            index += 1
            attempt += 1
        else:
            break
            
    print("Found the secret number!")

if __name__ == "__main__":
    main()
