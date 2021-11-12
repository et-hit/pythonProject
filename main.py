import random
import time
import sys
import json
import requests


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        time.sleep(0.02)


def get_words(num):
    url = 'https://random-word-api.herokuapp.com/word?number='
    response = requests.get(url + str(num)).text
    return json.loads(response)


def guess_game():
    lowlimit = 1
    uplimit = 1
    number = random.randint(lowlimit, uplimit)
    tries = 0
    delay_print("Very good, you have chosen Guessing game.\nNow, what is your name? ")
    uname = input()
    delay_print("Hello " + uname + ".\n" + "I will imagine a number between "
                + lowlimit.__str__() + " and " + uplimit.__str__() + ".\nYou will have to guess it!\n")
    guess = int(input("Have a guess... "))
    while guess != number:
        if tries != 0:
            guess = int(input("Try again..."))
        if guess < number:
            print("My number is higher than {0}".format(guess))
            tries += 1
        if guess > number:
            print("My number is lower than {0}".format(guess))
            tries += 1
        if guess == number:
            tries += 1
            delay_print(
                "\nCorrect, it is {0}".format(number) + ", and it only took "
                + tries.__str__() + " tries!" + "\nPress Enter to continue...")
            input()
            play_game()
    delay_print("\nCorrect, it is {0}".format(number) + ", and it only took "
                + (tries + 1).__str__() + " tries!" + "\nPress Enter to continue...")


def timing_game():
    delay_print("\nGood, you have selected the timing game.")
    time.sleep(0.5)
    delay_print("\n\nPlease choose how many words you would like me to get from the internet: ")
    size = int(input())
    ourwords = get_words(size)
    time.sleep(1)
    if size == 1:
        delay_print("I have selected 1 random word, now it is time to write it as "
                    "fast as you can!\nI WILL MEASURE THE TIME!!!")
    else:
        delay_print("I have selected " + size.__str__() +
                    " random words, now it is time to write them as fast as you can!\n"
                    "I WILL MEASURE THE TIME!!!")

    ready = "n"
    while ready != "y":
        delay_print("\nEnter 'y' if you are ready: ")
        ready = input()
        if ready == "y":

            print("\nCOUNTDOWN")
            time.sleep(1)
            print("--== 3 ==--")
            time.sleep(1)
            print("--== 2 ==--")
            time.sleep(1)
            print("--== 1 ==--")
            time.sleep(1)
            print("GO!!!\n")
            t0 = time.time()
            finished = int(0)
            mistakes = 0
            while finished < size:
                print("TYPE THE WORD: " + ourwords[finished])
                typed = input().__str__()
                if typed == ourwords[finished]:
                    print("GREAT!")
                    finished += 1
                else:
                    print("incorrect")
                    mistakes += 1
                    continue

            t1 = time.time()
            total = t1 - t0
            delay_print("Great, your time was: " + ("%.2f" % total).__str__() + " seconds, or "
                        + ("%.2f" % (total / size)).__str__() + " seconds per word.")
            time.sleep(0.5)
            if mistakes == 1:
                delay_print("\nYou made 1 mistake")
            else:
                delay_print("\nYou made " + mistakes.__str__() + " mistakes")

            time.sleep(1)
            delay_print("\nPress Enter to continue... ")
            input()
            play_game()


def play_game():
    delay_print("\n| GAME SELECTION |")
    delay_print("\n\n1: Timing game - Computer picks random words, you need to type them as fast as you can!\n")
    delay_print("2: Guess game - Computer picks a random number, you have to guess it!\n")
    delay_print("Input 1 or 2 and press Enter to choose: ")
    choice = int(input())
    if choice == 1:
        timing_game()
    if choice == 2:
        guess_game()
    else:
        delay_print("You have to choose game 1 or 2")
        play_game()


delay_print("Hello, Would you like to play a game? [y/n] ")
question = input()
if question == "y" or question == "Y":
    play_game()
else:
    delay_print("Ok, come back if you change your mind!")
