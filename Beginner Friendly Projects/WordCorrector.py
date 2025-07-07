#we want to code a program that checks our words and correct the spellings
#pip install pyspellchecker to use the method


from spellchecker import SpellChecker 

Corrector = SpellChecker()





# a loop to ask the question over and over again
while True:

    print("****************************************")
    #get the word
    word = input("Please enter your word (Press Q to quit): ")
    print("****************************************")

    
#exit
    if word.lower() == "q":
        print("GoodBye")
        break

#check if the word is correct
    elif word in Corrector.word_frequency:
        print(f"{word} is Correct!")
#if not
    else:
        correct_word = Corrector.correction(word)
        print (f"The word {word} is incorrect or having spelling mistake.\nThe correct word is {correct_word}.")


    
