from random import randint, choice
import colorama
from colorama import Back
import time
from words import words

colorama.init(autoreset=True)


def Petunjuk():
    indeks = len(perkataan_rawak)
    # pick random number for an index
    hint = randint(0, indeks - 1)
    # the random number then becomes the index of the word
    petunjuk = perkataan_rawak[hint]
    print(f"Petunjuk: {petunjuk}")

def Mode():
    mode = input("Choose a mode: (E)asy, (M)edium, (H)ard: ").upper()
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
    bil_tekaan = Mode()
    Petunjuk()
    while bil_tekaan > 0:
        print(f"Anda ada {bil_tekaan} tekaan!")
        tekaan = input("Perkataan tekaan: ").upper()
        if len(tekaan) > len(perkataan_rawak):
            print("Perkataan tekaan mesti tidak melebihi 5 huruf!")
            continue
        if tekaan == "":
            print("Perkataan tekaan tidak boleh kosong!")
            continue

        bil_tekaan -= 1
        huruf_yg_betul = []
        # Check if the character is correct
        for huruf in range(len(perkataan_rawak)):
            # if character entered is in the word and in correct position,
            # add it to the correct_char with green background
            if tekaan[huruf] == perkataan_rawak[huruf]:
                huruf_yg_betul.append(Back.GREEN + tekaan[huruf])
            # if character entered is in the word but in incorrect position,
            # add it to correct_char with yellow background
            if tekaan[huruf] in perkataan_rawak and tekaan[huruf] != perkataan_rawak[huruf]:
                huruf_yg_betul.append(Back.YELLOW + tekaan[huruf])
            else:
                # if character entered is not in the word,
                # add it to correct_char with red background
                if tekaan[huruf] != perkataan_rawak[huruf]:
                    huruf_yg_betul.append(Back.RED + tekaan[huruf])
        print(*huruf_yg_betul)
        # if all character given by user are correct, break the loop
        if tekaan[0:4] == perkataan_rawak[0:4]:
            print('Tahniah! Anda meneka dengan betul!')
            time.sleep(5)
            break
        # if all character given by user are wrong ten times, break the loop
        if bil_tekaan == 0:
            print(f"Salah... Perkataan yang betul adalah {perkataan_rawak}")
            time.sleep(5)
            break

if __name__ == "__main__":
    senarai_perkataan = words()
    perkataan_rawak = choice(senarai_perkataan)
    print("Welcome to Terminal Wordle!")
    Run_Game()
