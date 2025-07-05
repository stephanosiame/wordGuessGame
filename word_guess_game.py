import random

name = input("What is your name? ")

print("Good Luck!", name)

words = [
    'rainbow', "programming", 'computer', 'python', 'Mathematics', 'science', 'stephano', 
]

word = random.choice(words)

print ("Gues The character")
guesses = ''
turn = 12

while turn > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end =" ")
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You Win!")
        print(f"The Word is {word}")
        break

    print()
    guess = input("guess character: ")
    guesses += guess

    if guess not in word:
        turn -= 1
        print("Wrong")
        print("You have", + turn, "more guesses")

        if turn == 0:
            print("You Loose")