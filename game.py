from random import randint

secret_number = randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Guess the number between 1 and 10: "))
    attempts -= 1

    if guess == secret_number:
        print("Congratulations! You guessed the number ✅")
        break
    elif guess < secret_number:
        print("Too low! Try again!")
    else:
        print("Too high! Try again!")

    if attempts > 0:
        print(f"You have {attempts} attempts left.")
    else:
        print("Game over! You've used all your attempts.")
        print(f"The number was: {secret_number}")
