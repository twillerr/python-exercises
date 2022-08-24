import random

body = ("   O",
        "   O\n   |\n   |",
        "   O\n  /|\n   |",
        "   o\n  /|\ \n   |",
        "   o\n  /|\ \n   |\n  /",
        "   o\n  /|\ \n   |\n  / \\")

def display_body(i):
    print("________")
    print(body[i])
    print((5-i)*("\n")+"________")

           
while True:
    print("Welcome to Hangman!")

    #target word for user to guess
    with open("sowpods.txt", "r") as f:
        words = f.readlines()
        word = words[random.randint(0,len(words))].strip()

    #series of underscores same length as target word
    res = ["_" for i in range(0,len(word))]

    past_guesses =set()

    #number of incorrect guesses so far
    c=0


    while c<6:
        guess = input("Guess a letter:").capitalize()

        #this is the indexes of letters in word that match the user guess
        matching_pos = {i for i in range(0,len(word)) if word[i] == guess}

        if guess in past_guesses:
            print("You have already guessed that letter!")

        #check if no letter matches in the target word
        elif len(matching_pos) == 0:
            c+=1
            past_guesses.add(guess)
            display_body(c-1)
            print("That letter is not in the word! You have {x} guesses left.".format(x=6-c))

        #edit undescore list with the letters that match in the target word
        else:
            for r in matching_pos:
                res[r] = guess
                past_guesses.add(guess)
            print(" ".join(res))

            #check if all letters in result match
            if res == list(word):
                print("You Win!")
                break

    print("Game over. The word was {x}!".format(x=word))

    ask = input("Play again? (y/n):   ")

    if ask == "n":
        print("Closing")
        break

