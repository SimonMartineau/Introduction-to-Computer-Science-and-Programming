#https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-6-recursion/MIT6_00SCS11_ps2.pdf
# Problem Set 2d
# Name: Simon Martineau
# Time: 0:

import random
import string
#functions
def findLetterInString(guessed_letter, search_word):
    search_word = search_word.upper()
    return search_word.find(guessed_letter.upper())
def updateDisplay(guess_letter):
    display_list = list(display_answer)
    answer_list = list(answer)
    for letter_counter in range(0,len(answer)):
        if guess_letter.lower() == answer_list[letter_counter]:
            display_list[letter_counter] = guess_letter.lower()
    return "".join(display_list)
#variable declaration
wordlist = ['pineapple', 'dog', 'cookie', 'cupcake', 'cat']
answer = random.choice(wordlist)
alphabet = string.ascii_uppercase;
guess_amount = 8
guessed_letters = ""
display_answer = ""
#set up the game
print("Welcome to Hangman!")
for letter in answer:
    display_answer += '_'
print("You will have ", guess_amount ," guesses to select the missing letters.")
while(answer != display_answer and guess_amount != 0):
    #play the game
    print("The word is ", display_answer)
    print('Remaining guesses:', guess_amount)
    print("You have guess: ", guessed_letters)
    guess_letter = input("Enter a letter as your guess: ")
    while findLetterInString(guess_letter, alphabet) == -1 or findLetterInString(guess_letter, guessed_letters) != -1:
        guess_letter = input("Enter a letter as your guess which you have not selected before: ")
    if findLetterInString(guess_letter, answer) != -1:
        print("Found :", guess_letter)
        display_answer = updateDisplay(guess_letter)
    else:
        guess_amount-=1
        print(guess_letter , "Not found")
    guessed_letters += guess_letter
    print("==============================================")
    
#win or lose
if guess_amount == 0:
    last_guess = input("You have one final guess! type in the whole word: ")
    if last_guess.lower() == answer.lower():
        print("You barely won!")
    else:
        print("You have lost!")
else:
    print("You have won!")
print("The answer was ",answer)  
