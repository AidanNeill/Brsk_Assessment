# File: Brsk_Assessment.py

# Author: Aidan Neill
# Date: 24/10/2023

# Usage:
# 1. Make sure the 'words_alpha.txt' file is in the same directory as this script.
# 2. Follow the instruction found in "=== Program User Guide ===.txt"

import random

def read_word_list(file_path):
    """"
    Error handling if file_path is not found in current directory
    """

    try:
        with open(file_path, "r") as file:
            word_list = [line.strip() for line in file]
        return word_list
    except FileNotFoundError:
        print("The 'words_alpha.txt' file does not exist. Please make sure it's in the correct location or provide the correct path.")
        exit(1)

def find_replacement_word(word, word_list):
    """
    Finds and returns a replacement word from the given list based on the same length and starting letter.
    If no replacement is found, it returns the original word.
    """
    replacement_list = []
    for w in word_list:
        if len(w) == len(word) and w[0] == word[0]:
            replacement_list.append(w)

    if replacement_list:
        replacement_word = random.choice(replacement_list)
        return replacement_word
    
    return word

def replace_sentence(sentence, word_list):
    """
    Replaces words in a sentence with words from the given list based on the same length and starting letter.
    """
    words = sentence.split()
    new_sentence = []
    for word in words:
        new_sentence.append(find_replacement_word(word, word_list))

    updated_sentence = ' '.join(new_sentence)
    return updated_sentence

# Read the word list.
word_list = read_word_list("words_alpha.txt")

user_choice="2"

while True:
    # Take user input for a sentence.
    if user_choice=="2":
        input_sentence = input("\nEnter a sentence: ")

        while not input_sentence:
            print("\nInput sentence is empty. Please provide a sentence.\n")
            input_sentence = input("Enter a sentence: ")
    
        output_sentence = replace_sentence(input_sentence, word_list)

        # Print the original and modified sentences.
        print("\nOriginal Sentence:", input_sentence)
        print("Modified Sentence:", output_sentence,"\n")


    else:
        output_sentence = replace_sentence(input_sentence, word_list)

        # Print the original and modified sentences.
        print("\nOriginal Sentence:", input_sentence)
        print("Modified Sentence:", output_sentence,"\n")

    print("0. End program")
    print("1. Regenerate sentence")
    print("2. Enter a new sentence")
        
    user_choice = input("Please select the number from the above options: ")
    
    while user_choice not in ["0", "1", "2"]:
        print("\nInvalid choice. Please select a valid option.\n")
        user_choice = input("Please select the number from the above options: ")

    if user_choice == "1" or user_choice == "2" :
        continue  # Continue the loop 
    elif user_choice == "0":
        break  # End the program


 

    
