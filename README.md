# English - Polish Dictionary
#### Video Demo: https://www.youtube.com/watch?v=GgGcsqdQx-w

#### Description:
To run the program you are not required to give any arguments. It can be run by simply running the line "python project.py" on the terminal.

After writing the line python project.py, the program looks for a project.json file. If there isn't one the program creates it. The project.json file contains a dictionary which it's keys are English words and values are Polish translation of the English words. After using the program at least once, and quitting through the quit function of the program that is given in the main menu, the words you have given in the program is saved in the "project.json" file. Since the process of saving is done in the quit function, the program will not save the dictionary if you quit the program with other ways (i.e. ctrl+c).

After the process given above, program goes into forever loop in the main function which is the main menu of the program. The user is given 4 options,

1. Add new words to the dictionary.
    This option is to add new words to the dictionary. After the user choose this option, they are required to give an English word to be translated into Polish. The "translate" library is used for this translation. If the given word is from another language the "translate" library gives the input as itself back, and when the program recognizes the return which is exactly the same as input, it does not save the word into the dictionary. This also can be the situation if the given English word is exactly the same in Polish, so the user will be informed about this. Also, this function does not take more than one word at a time and, does not take a number as the input. If the given word already exist in the dictionary, the user will be informed and the word will not be saved in the dictionary again. If everything goes according to the plan, the user will be given "English word" -> "Translation" and will receive the message the word has been saved to the dictionary succesfully.

2. See the dictionary.
    This option will show the user all of the saved words in the dictionary. Including the words which user has added into the dictionary in the current process and the words already exist in the json file. The user will see the words as "English word" -> "Polish translation", and there will be one word per line.

3. Play the quiz game.
    This option will require another input as a number, which can not be larger than the amount of words in the dictionary. Also the user can not give a word as an input at this part. The user will be asked to translate the same amount of words that they have given as the number input. If the user gives the correct translation they will receive the text "That's right!", and if the user gives the incorrenct answer they will receive the correct answer. After the answer the user will move on to the next word. After answering all the words the user will receive the score as (Correct answers given in the quiz)/(Number input/Number of words).

4. Quit program.
    This option will overwrite the project.json file and save all the new words with the previous words into the json file, give the user a goodbye message, and finally quit the program.

There will be a number input for user to choose one of these actions as "Choose an action; ", and the user is required to give the option number (i.e. input of "1" for the first function, "2" for the second). The user can not give a word as the input and can not give a number that is not 1, 2, 3 or 4.

After the user choose an option and complete the action of it, they are required to give another input to go back to the main menu. This input does not matter for it will not be saved. On the program this action will be asked as "Press enter to go back to the menu.", and pressing enter with or without any input will return the user to the main menu.