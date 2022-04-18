from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

#make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        #we could said it to 10, but it may be better to just establish a Global Constant.
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    #choosing a random number between 1 and 100
    print("Welcome to the guessing game.")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Psst! The answer is {answer}")

    
    turns = set_difficulty()
    
    
    #repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
    #let use guess number
        print(f"You have {turns} turns remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()
#track number of turns and reduce by 1 if they get it wrong







