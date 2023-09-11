from translate import Translator
import json
import sys
import random

translator = Translator(to_lang='pl')

# global dictionary declaration
data = dict()

try:
    with open("project.json", "r") as file:
        data = json.load(file)
except:
    with open("project.json", "w") as file:
        json.dump(data, file)

def main():
    global data

    while True:
        print('1. Add new words to the dictionary')
        print('2. See the dictionary')
        print('3. Play the quiz game')
        print('4. Quit program')

        try:
            action = int(input('Choose an action; '))
        except:
            print("Please input a valid number")
            continue

        if(action == 1):
            expand()
        elif(action == 2):
            observe()
        elif(action == 3):
            game()
        elif(action == 4):
            quit()
        else:
            print('Invalid action')

    
# Add a new word to the dictionary
def expand():
    global data

    while True:
        word = input('Enter a word: ').strip().lower().capitalize()
        if(any(char.isdigit() for char in word)):
            print('Word can not contain a number.')
            continue
        if(any(char.isspace() for char in word)):
            print('Please enter single word at a time.')
            continue
        else:
            translation = translator.translate(word)
            if(translation.lower() == word.lower()):
                print("Either we couldn't translate the word you put in or it has exactly the same spelling in Polish.")
                print("The word won't be registered into the dictionary.")
                continue
            break

    if word in data.keys():
        print('The word already exist in the dictionary!')
    else:
        data[word] = translation
    
    print(f'{word} -> {translation}')
    input('Press enter to go back to the menu.')

# Quit program
def quit():
    with open("project.json", "w") as file:
        json.dump(data, file)
    sys.exit('Good work! Hope to see you soon!')

# Observe the dictionary
def observe():
    global data

    for abc in data:
        print(f'{abc} -> {data[abc]}')
    
    input('Press enter to go back to the menu.')

# Play the quiz game

def game():
    global data

    while True:
        try:
            dict_keys = list(data.keys())
            difficulty = int(input('Enter the number of words that you want to see on the quiz; '))
            quiz = random.sample(dict_keys, difficulty)
            break
        except:
            validnum = len(dict_keys)
            print(f"Invalid input, please enter a NUMBER which is not larger than the number of words in your dictionary ({validnum}), or enter 0 to go back to the main menu.")


    score = 0

    for word in quiz:
        answer = input(f'{word} means; ').lower()

        if(answer == data[word].lower()):
            print("That's right!")
            score += 1
        else:
            print(f'The right answer is {data[word]}')

    print(f"Your score is {score}/{difficulty}")
    input('Press enter to go back to the menu.')



if __name__ == "__main__":
    main()