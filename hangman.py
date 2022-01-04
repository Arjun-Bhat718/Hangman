
def hangman():
    import random
    
    word_list = ('ant alligator antelope bear sloth raccoon deer sheep chicken turkey rabbit pig horse giraffe lion tiger elephant hyena owl shark robin penguin seal dog cat mouse rat spider crocodile monkey kangaroo goat cow zebra wolf duck eagle crow flamingo ostrich parrot octopus prawn salmon trout bass shrimp dolphin whale orca emu whale ostrich annaconda fox hyena seahorse bison bear zebra buffalo panda koala Iguana Okapi Warthog Antelope Anteater Cockapoo Cockroach Alligator Stegasaurus TREX').split()
    letterGuess = []
    
    word = random.choice(word_list)

    tries = 7
    guessed = False
    spaces = '-'*len(word)

    hangman_list = [
    """
    _____________
    |             |
    |            ( )
    |             |
    |            /|\
    |             |
    |             |
    |            / \
    |____
    """
    ,
    """
     _____________
    |             |
    |            ( )
    |             |
    |            /|\
    |             |
    |             |
    |            / 
    |____
    """
    ,
    """ _____________
    |             |
    |            ( )
    |             |
    |            /|\
    |             |
    |             |
    |            
    |____
    """
    ,
    """
     _____________
    |             |
    |            ( )
    |             |
    |            /|\
    |             
    |             
    |            
    |____
    """
    ,
    """
    _____________
    |             |
    |            ( )
    |             |
    |            /|
    |             
    |             
    |            
    |____
    """
    ,
    """
     _____________
    |             |
    |            ( )
    |             |
    |             |
    |             
    |             
    |            
    |____
    """
    ,
    """
    _____________
    |             |
    |            ( )
    |             
    |            
    |             
    |             
    |            
    |____
    """
    ,
    """
    _____________
    |             |
    |            
    |             
    |            
    |             
    |             
    |             
    |____
    """

    ]

    while guessed != True and tries>0: 
        print(hangman_list[tries])
        print(spaces)
        print('You have',tries,'tries left')
        print('The word has',len(word),'letters')
        guess = input('Enter a letter or guess the word:')
        guess = guess.lower()
    
        if len(guess) == 1 and guess.isalpha():
            if guess in letterGuess:
                print('You have already guessed that letter')
            elif guess not in word:
                print('Sorry, but the letter is not in the word')
                letterGuess.append(guess)
                tries-=1
            else:
                print('Yay, the letter you guessed is in the word')
                letterGuess.append(guess)
                wordList = list(spaces)
            
            
                indices = [i for i,letter in enumerate(word) if letter==guess]
                for index in indices:
                    wordList[index] = guess
                    spaces = "".join(wordList)
                    if "-" not in spaces:
                        print('Good job, you guessed the word')
                        guessed = True
        elif len(guess)==len(word) and guess.isalpha():
            if guess == word:
                print('Good job, you guessed the word')
                guessed=True
            else:
                print('Sorry, your guess was wrong')
                tries-=1
        else:
            print('Please, enter a letter or word only')

    if tries==0:
        print('Sorry, you are out of tries')
        print('The word was',word)

hangman()



    
