from random import randint

count = 1
secret_number = randint(1, 10)
while True:
    guess = int(input("Guess the number between 1 and 10: "))
    count += 1
    if count >=3:
        print("Game over! You've used all your attempts. The secret number was:", secret_number)
        break

    if guess == secret_number:
        print("Congratulations! You guessed the number✅.")
        break
    if guess < secret_number:
        print("Too low! Try again!")
    elif guess > secret_number:
        print("Too high! Try again!")
    else:
        print("Wrong guess❌. Try again!")
        