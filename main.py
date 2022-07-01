from random import randint, choice
import colorama
from colorama import Back
import time
from words import words

colorama.init(autoreset=True)


def Clue():
    index = len(random_word)
    # pick random number for an index
    hint = randint(0, index - 1)
    # the random number then becomes the index of the word
    clue = random_word[hint]
    print(f"Petunjuk: {clue}")

def Mode():
    mode = input("Choose a mode: (E)asy, (M)edium, (H)ard: ").upper()
    print("Sila masukkan mode yang betul!")
    easy = 10
    medium = 7
    hard = 5
    match mode:
        case "E":
            return easy
        case "M":
            return medium
        case "H":
            return hard
    
def Run_Game():
    guesses = Mode()
    Clue()
    while guesses > 0:
        print(f"You have {guesses} guesses!")
        guess = input("Your Guess: ").upper()
        
        if len(guess) > len(random_word):
            print("The word is too long!")
            continue
        if guess == "":
            print("Please enter a guess!")
            continue

        guesses -= 1
        pos = 0
        correct_letter = ''
        # Check if the character is correct
        for letter in guess:
            # if character entered is in the word and in correct position,
            # add it to the correct_char with green background
            if letter == random_word[pos]:
                correct_letter += Back.GREEN + guess[pos]
            # if character entered is in the word but in incorrect position,
            # add it to correct_char with yellow background
            elif (letter in random_word[pos]) and (letter != random_word[pos]):
                correct_letter += Back.YELLOW + guess[pos]
            else:
                # if character entered is not in the word,
                # add it to correct_char with red background
                if letter != random_word[pos]:
                    correct_letter += Back.RED + guess[pos]
            pos += 1
            correct_letter.split(" ")
        print(correct_letter)
        
        # if all character given by user are correct, break the loop
        if guess[0:4] == random_word[0:4]:
            print('Tahniah! Anda meneka dengan betul!')
            time.sleep(5)
            break
        # if all character given by user are wrong ten times, break the loop
        if guesses == 0:
            print(f"Salah... Perkataan yang betul adalah {random_word}")
            time.sleep(5)
            break

if __name__ == "__main__":
    word_list = ["HAPPY"]
    random_word = choice(word_list)
    print("Welcome to Terminal Wordle!")
    Run_Game()
