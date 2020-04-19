#Initial setup

secret_number = 7.1
guess_count = 0
#GAME LIMITS
easy_guess_limit = 6
medium_guess_limit = 4
hard_guess_limit = 3

#GAME TURNS LEFT
turns_easy = 6
turns_medium = 4
turns_hard = 3

print("WELCOME TO CAESARSAGE GUESSING GAME")
choice = str(input("THIS GAME HAS 3 DIFFICUITY!\n CHOOSE YOUR DIFFICUITY BY TYPING: \n EASY ******* or \n MEDDIUM ******* or \n HARD ******* \n: "))

    #FUNCTION FOR CHOICES

def choices_option():
        #EASY CONDITION
    if choice.lower() == "easy":
        print("*** EASY RULES *** \n 1. Number to guess must be between 1 and 10 \n 2. You have a maximum of 6 guesses \n 3. Guess number can be in decimal place with highest as 1dp")
        return easy_mode(guess_count,turns_easy)
        #MEDIUM CONDITION
    elif choice.lower() == "medium":
        print("*** MEDIUM RULES *** \n 1. Number to guess must be between 1 and 20 \n 2. You have a maximum of 4 guesses \n 3. Guess number can be in decimal place with highest as 1dp")
        return medium_mode(guess_count,turns_medium)
        #HARD CONDITION
    elif choice.lower() == "hard":
        print("*** HARD RULES *** \n 1. Number to guess must be between 1 and 50 \n 2. You have a maximum of 3 guesses \n 3. Guess number can be in decimal place with highest as 1dp")
        return hard_mode(guess_count,turns_hard)

    #FUNCTION FOR EASY DIFFICUITY
def easy_mode(guess_count, turns_easy):
    try:
        while guess_count <= easy_guess_limit:
            guess = float(input("Guess a number : \n"))
            guess_count +=1
            turns_easy -=1
            if guess == secret_number:
                print("You got it right")
                break
            elif guess_count == easy_guess_limit:
                print("Game Over!!!")
                break
            else:
                if guess >10:
                    print("Number must be between 1 and 10 !!!")
                else:
                    print(f"That was wrong \n You have {turns_easy} left")
    except ValueError:
        print("WRONG INPUT!!!") 

    #FUNCTION FOR MEDIUM DIFFICUITY
def medium_mode(guess_count,turns_medium):
    try:
        while guess_count <= medium_guess_limit:
            guess = float(input("Guess a number : \n"))
            guess_count +=1
            turns_medium -=1
            if guess == secret_number:
                print("You got it right")
                break
            elif guess_count == medium_guess_limit:
                print("Game Over !!!")
                break
            else:
                if guess > 10:
                    print("Number must be between 1 and 20 !!!")
                else:
                    print(f"That was wrong \n You have {turns_hard} left")
    except:
        print("WRONG INPUT!!!")

    #FUNCTION FOR HARD DIFFICUITY
def hard_mode(guess_count,turns_hard):
    try:
        while guess_count <= hard_guess_limit:
            guess = float(input("Guess a number : \n"))
            guess_count +=1
            turns_hard -=1
            if guess == secret_number:
                    print("You got it right")
                    break
            elif guess_count == hard_guess_limit:
                    print("Game Over!!!")
                    break
            else:
                if guess > 50:
                    print("Number must be between 1 and 50 !!!")
                else:
                    print(f"That was wrong \n You have {turns_hard} left")    
    except:
        print("WRONG INPUT!!!")                
    
    #FUNCTION FOR EXECUTIONS
def main():
    choices_option()

main()