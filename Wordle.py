import random

# Random fruits

def choose_word():
    words = ["apple", "grape", "mango", "peach", "berry"]
    return random.choice(words)


# yaha pe function guess ko check karega

def check_guess(secret_word, guess):
    result = []
    
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            result.append("🟢")   # Correct position
        elif guess[i] in secret_word:
            result.append("🟡")   # Wrong position
        else:
            result.append("⚫")   # Not in word
            
    return result


# function jo feedback show karega

def display_result(guess, feedback):
    for i in range(len(guess)):
        print(guess[i], feedback[i], end=" ")
    print()


# main vala function

def play_wordle():
    secret_word = choose_word()
    attempts = 6
    
    print("Welcome to Wordle!")
    
    while attempts > 0:
        guess = input("Enter a 5-letter word: ").lower()
        
        if len(guess) != 5:
            print("Word must be 5 letters!")
            continue
        
        feedback = check_guess(secret_word, guess)
        display_result(guess, feedback)
        
        if guess == secret_word:
            print("🎉 Congratulations! You guessed the word!")
            return
        
        attempts -= 1
        print("Attempts left:", attempts)
    
    print("😢 Game Over! The word was:", secret_word)


# Run the game
play_wordle()