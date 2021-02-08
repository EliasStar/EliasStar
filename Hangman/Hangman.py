from turtle import *
from random import randrange

turns = 11

scale = 5
offsetX = 100

turtleSpeed = 5

name = input("What is your name? ")

print("Hello", name + "!")
print("You can guess one or more letter at once. For each wrong letter you will get closer to getting hanged.\n")
print("You have", turns, "tries. If you guess correct, you won't lose a try.")

with open("words.txt") as words:
    content = words.readlines()
content = [x.strip() for x in content]

word = content[randrange(0,len(content))]

guesses = ''

reset()
hideturtle()
penup()
pensize(5)
pencolor(1, 0, 0)
speed(turtleSpeed)

print("\n\nTime to play hangman!\n\n")

def draw(step):

    if step == 10:
        left(90)
        goto(-15*scale + offsetX, -50*scale)

        speed(0)
        pendown()
        circle(35*scale, 180, 180)
        penup()
        speed(turtleSpeed)

    elif step == 9:
        goto(-50*scale + offsetX, -15*scale)

        pendown()
        goto(-50*scale + offsetX, 65*scale)
        penup()

    elif step == 8:
        pendown()
        goto(15*scale + offsetX, 65*scale)
        penup()

    elif step == 7:
        goto(-50*scale + offsetX, 45*scale)

        pendown()
        goto(-30*scale + offsetX, 65*scale)
        penup()

    elif step == 6:
        goto(15*scale + offsetX, 65*scale)

        pendown()
        goto(15*scale + offsetX, 45*scale)
        penup()

    elif step == 5:
        right(90)

        speed(0)
        pendown()
        circle(10*scale)
        penup()
        speed(turtleSpeed)

    elif step == 4:
        left(90)
        goto(15*scale + offsetX, 25*scale)

        pendown()
        goto(15*scale + offsetX, 0)
        penup()

    elif step == 3:
        left(45)

        pendown()
        fd(15*scale)
        penup()

    elif step == 2:
        goto(15*scale + offsetX, 0)
        right(90)

        pendown()
        fd(15*scale)
        penup()

    elif step == 1:
        left(45+180)
        goto(15*scale + offsetX, 17.5*scale)
        left(60)

        pendown()
        fd(15*scale)
        penup()

    elif step == 0:
        goto(15*scale + offsetX, 17.5*scale)
        right(120)

        pendown()
        fd(15*scale)
        penup()


while turns > 0:
    wrongLetters = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")

        else:
            print("_", end=" ")
            wrongLetters += 1

    if wrongLetters == 0:
        print("\nYou won!")
        break


    guess = input("\nGuess one or more letter/s: ")
    guesses += guess

    lettersWrong = 0

    for char in guess:
        if char not in word:
            turns -= 1

            if turns <= 0:
                turns = 0

            draw(turns)

            lettersWrong += 1

    print(lettersWrong, "wrong")
    print("You have", + turns, 'more guesses.\n')

    if turns == 0:
        print("\nYou lost!\nThe word was", word + ".")
