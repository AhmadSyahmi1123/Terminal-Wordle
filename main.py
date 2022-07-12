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
    clue = random_word[hint].upper()
    print(f"Petunjuk: {clue}")

def Mode():
    mode = input("Choose a mode: (E)asy, (M)edium, (H)ard: ").upper()
    print("Please enter a mode!")
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

def checkguess(guess, correct):
    guess_counts, correct_counts = {}, {}
    for char in correct:
        correct_counts[char] = correct_counts.get(char, 0) + 1
    correct_letter = ""
    for g_char, c_char in zip(guess, correct):
        guess_counts[g_char] = guess_counts.get(g_char, 0) + 1
        if g_char == c_char:
            correct_letter += Back.GREEN + g_char if guess_counts[g_char] <= correct_counts[g_char] else Back.RED + g_char
        elif g_char in correct:
            correct_letter += Back.YELLOW + g_char
        else:
            correct_letter += Back.RED + g_char
    return correct_letter
    
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
        #if guess not in word_list:
            #print("Please enter a valid guess!")
            #continue

        guesses -= 1

        check = checkguess(guess, random_word)
        
        #for i, (l1, l2) in enumerate(zip(random_word, guess)):
            #if l1 == l2:
                #correct_letter += Back.GREEN + l1
        
        '''
        # Check if the character is correct
        for letter in guess:
            if letter == random_word[pos]:
                    correct_letter += Back.GREEN + guess[pos]
            elif letter not in random_word:
                correct_letter += Back.RED + guess[pos]
            else:
                correct_letter += Back.YELLOW + guess[pos]
            pos += 1
            correct_letter.split(" ")
            '''
        print(check)
        
        # if all character given by user are correct, break the loop
        if guess[0:4] == random_word[0:4]:
            print('Good job!')
            time.sleep(5)
            break
        # if all character given by user are wrong ten times, break the loop
        if guesses == 0:
            print(f"Wrong... the word is {random_word}")
            time.sleep(5)
            break

if __name__ == "__main__":
    word_list = words()
    random_word = choice(word_list)
    print("Welcome to Terminal Wordle!")
    Run_Game()
