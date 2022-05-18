import random

NUM_DIGITS = 3 #Max nb of the answer nb 
MAX_GUESS = 10 


def main():
    print('''Bagels a deductive logic game.
          By Al Sweigart al@inventwithpython.com
          I am thinking of a {}-digit number with no repeated digits.
 Try to guess what it is. Here are some clues:
 When I say: That means:
 Pico One digit is correct but in the wrong position.
 Fermi One digit is correct and in the right position.
 Bagels No digit is correct.

 For example, if the secret number was 248 and your guess was 843, the
 clues would be Fermi Pico.'''.format(NUM_DIGITS))
    

    while True:     #Main game loop
        # This stores the secret number the player needs to guess:
        secret_number = get_secret_number()
        print("I have thought up a number")
        print('You have {} guesses to get it '.format(MAX_GUESS))
        
        numGuesses =1
        while numGuesses <= MAX_GUESS:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess {}'.format(numGuesses))
                guess = input('> ')
                
            clues = getClues(guess,secret_number)
            print(clues)
            numGuesses += 1
            
            if guess == secret_number:
                break
            if numGuesses > MAX_GUESS:
                print('You ran out of guesses')
                print('The answer was {}'.format(secret_number))
                
            #Ask the player to rematch player
            
            print('Do you want to play again')
            if input('> ').lower().startswith('y'):
                break
            print('Thank you for playing')
    
    
    def get_secret_number():
        """Returns a string made up of NUM_DIGITS unique random digits."""
        numbers = list('0123456789')
        random.shuffle(numbers)
        
        
                
            
        
        
        
