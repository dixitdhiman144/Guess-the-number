import random

#Guess by User

def guess(num):
    rand_no = random.randint(1,num)
    guess = 0
    while rand_no != guess:
        guess = int(input(f"guess a number between 1 and {num}: "))
        if rand_no > guess :
            print("Sorry, guess again. Your guess is too low")
        else:
            print("Sorry, guess again. Your guess is too high")
        
    print("Your guess is right - ",rand_no)


# guess(20)


#Guess bu computer

def computer_guess(num):
    print(f"Please select a number between 1 and {num}")
    start_num = 1
    guess = True
    while guess :
        c_guess = random.randint(start_num, num)
        user_feedback = input(f"{c_guess} is your selected number: ")
        if "n" == user_feedback[0].lower():
            user_feedback_high = input(f"{c_guess} is higher then your selected number: ")
            if "y" == user_feedback_high[0].lower():
                num = c_guess
            else:
                start_num = c_guess
        else:
            guess = False
    print(f"Yay! Your selected Number is {c_guess}")

def computer_guess_(x):
    low = 1
    high = x
    feed_back = ""
    while feed_back != "C":
        guess =  random.randint(low, high)
        feed_back = input(f"Is {guess} correct(C), too high(H), too low(L): ")[0].upper()
        if feed_back == "H":
            high = guess - 1
        elif feed_back == "L":
            low = guess + 1
    print(f"Yay! The computer guessed your number - {guess}")        

computer_guess_(20)