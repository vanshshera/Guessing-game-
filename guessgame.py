import random as r

lowest_num = 1
highest_num = 100

answer = r.randint(lowest_num,highest_num)
guesses = 0
is_running = True

print("-------------Number Guessing Game-------------")
print(f"Enter a Number Between{lowest_num},{highest_num}")

while is_running:
    guess = input("Enter your Guess-->")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print("That Number is out of range")
            print(f"Please select a number between{lowest_num}and{highest_num}")
        elif guess < answer:
            print("Too Low!!! Try again!!")
        elif guess > answer:
            print("Too High!! Try again!!!")
        else:
            print(f"CORRECT!! the answer was {answer}")
            print(f"Number of guesses--> {guesses}")
            is_running = False
    else:
        print("Invalid Guess")
        print(f"Please select a number between{lowest_num}and{highest_num}")