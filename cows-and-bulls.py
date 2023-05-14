import random
import colorama

def output_list(list_of_guesses):
    for guess in list_of_guesses:
        print(guess[0], "-", guess[1], "cows,", guess[2], "bulls")

def check_list_for_guess(player_string, list_of_guesses):
    found = 0
    for guess in list_of_guesses:
        if guess[0] == player_string:
            found = found + 1
    return found

def check_for_duplicates(player_string):
    """ If a digit in player_string is a duplicate, then one duplicate is added to the returned integer. """
    found = 0
    for i in range(4):
        if player_string.count(player_string[i]) > 1:
            found = found + 1
    return found
    
def check_for_bulls(generated_string, player_string):
    """ If a digit in player_string matches *THE SAME* position digit in generated_string, then one bull is counted. """
    found = 0
    for i in range(4):
        if player_string[i] == generated_string[i]:
            found = found + 1
    return found

def check_for_cows(generated_string, player_string):
    """If a digit in player_string matches a digit in *ANY* position in generated_string, then one cow is counted."""
    found = 0
    for i in range(4):
        for j in range(4):
            #i != j is needed so that we are not comparing the same number with itself
            if i != j and player_string[i] == generated_string[j]:
                found = found + 1
    return found

def get_guess(guess_list):
    """get_guess is responsible for validating the player's guess, using indefinite iteration to enforce the rules of the game."""
    while True:
        choice = input("Enter a 4-digit number or EXIT|LIST|HINT: ").upper()
        # Check the user input to ensure they've only entered a number 0 - 8
        if len(choice) != 4:
            print("Your guess must be exactly 4 digits.")
        elif choice in ["LIST","EXIT","HINT"]:
            return choice
        elif choice.isnumeric() == False:
            print("Your guess must only contain numbers 0 - 9.")
        elif check_for_duplicates(choice) > 0:
            print("Your guess cannot contain duplicate digits.")
        elif check_list_for_guess(choice, guess_list) > 0:
            print(choice, "has already been a guess.")
        else:
            return choice

def create_four_digit_number():
    """ create_four_digit_number() returns a four unique digits as a string. """
    numberSequence = ""

    for counter in range(4):
        numberSequence = numberSequence + random_digit(numberSequence)
    
    return numberSequence

def random_digit(existing_digits):
    """ random_digit() returns a unique digit that doesn't exist in the existing_digits parameter. """
    randomNum = str(random.randint(0, 9))
    while randomNum in existing_digits:
        randomNum = str(random.randint(0, 9))
    
    return randomNum


print("***********************************************")
print("*          Welcome to Cows and Bulls          *")
print("***********************************************")

play_again = "Y"

while play_again == "Y":

    #Create the number the user is trying to guess
    generated = create_four_digit_number()
    print("Randomly generated number:", generated)

    #Setting up the local variables
    user_input = ""
    guesses = 0
    guess_list = []
    hint_provided = 0

    #Main game loop, only stops when EXIT is input or the guess is correct
    while user_input != "EXIT" and user_input != generated:
        
        #Get validated user input
        user_input = get_guess(guess_list)
        
        #Process menu options before a user guess
        if user_input == "LIST":
            output_list(guess_list)

        elif user_input == "HINT":
            if hint_provided == 0:
                hint_provided = generated[random.randint(0, 3)]
                print(hint_provided, "is in the number!")
            else:
                print("Nice try, only one hint per game!")

        elif user_input == "EXIT":
            print("Number was", generated)
            
        else:
            cows = check_for_cows(generated, user_input)
            bulls = check_for_bulls(generated, user_input)
            guesses = guesses + 1

            if user_input == generated:
                print("Your guess was correct!")
            else:
                #Guess/Stats added to the list, used when the user inputs LIST and for input validation
                guess_list.append([user_input, cows, bulls]) 
                
                #Give feedback to the user
                print(user_input, "-", colorama.Fore.RED, cows, "cows,", colorama.Fore.GREEN, bulls, "bulls", colorama.Style.RESET_ALL)

        
    print("You took", guesses, "guesses")

    #Ask if the player wants to play again
    play_again = input("Would you like to play again (Y)es or (N)o?")[0].upper()
