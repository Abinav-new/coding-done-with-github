import random

def main():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        user_input = input("Guess the number (1-100) or type 'quit' to exit: ")
        if user_input.lower() == 'quit':
            print(f"Thanks for playing! The number was {number}.")
            break

        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number or 'quit' to exit.")
            continue

        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()
