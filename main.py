from random import randint

secret_number = randint(1, 10)
while True:
    guess = int(input("Guess the number between 1 and 10: "))
    if guess == secret_number:
        print("Congratulations! You guessed the number.")
        break
    else:
        print("Wrong guess. Try again!")