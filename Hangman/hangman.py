import numpy as np
import logo
import words

print('\n')
print(logo.h_logo)

random_word = np.random.choice(words.words).lower()
print('\n')
print("Randomly chosen word for sample game: ", random_word)

display = []
for i in range(len(random_word)):
    display += '_'

game = True
life = 5

while game == True:
    print('\n')
    guess = input("Enter the guess letter: ")

    position = 0
    for letter in random_word:
        if letter == guess:
            print('\n')
            print("The guess was right")
            display[position] = guess
            print(display) 
        position += 1
        

    if guess not in random_word:
        life -= 1
        print(f"The guess was wrong, your current life: {life}/5")

    if '_' not in display:
        print('\n')
        print("*** You Won ***")
        game = False

    if life == 0:
        print('\n')
        print("*** You Lose ***")
        game = False
