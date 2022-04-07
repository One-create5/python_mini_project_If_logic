#!/usr/bin/env python3

import os
import random
from countryCapitalBank import bank

def getRandomCountryCap():
    rand = random.choice(list(bank.items()))
    return rand

def gameIntro():
    print("Welcome to Guess A Capital")
    print("You will have 3 opportunities to guess the capital of a randon country")

def getUserInput(country):
    userInput = input(f"\nWhat is the capital of {country}? ").strip().capitalize()
    return userInput

def runGame():
    count = 0
    randomCountry = getRandomCountryCap()
    country = randomCountry[0]
    capital = randomCountry[1]
    
    while count < 3:
        if(count != 0 ):
            os.system("clear")
            print(f"Sorry {userInput} is not the capital of {country}.")
            userInput = getUserInput(country)
        else:
            userInput = getUserInput(country)

        if userInput == capital:
            print("\n*** CONGRATULATIONS YOU WON ***")
            print(f"The capital of {country} is {capital}!\n")
            break
        else:
            count += 1
    
    if count == 3:
        print("\n****** YOU LOST ******")
        print(f"The capital of {country} is {capital}.\n")


def main():
    gameIntro()
    runGame()
main()


