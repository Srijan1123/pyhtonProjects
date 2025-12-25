import random

# Let's add word list first
word_list = ["python", "dotnet", "kathmandu", "nepal", "snake", "programming", "kantipur"]

# Let's set the difficulty level
difficulties = {
    "easy": 10,
    "medium": 6,
    "hard": 3
}

def hangman_game():
    print("\n== Hangman Game ==")
    print("Choose difficulty: Easy / Medium / Hard")
    
    # Ask difficulty
    while True:
        difficulty = input("Enter a difficulty level: ").lower()
        if difficulty in difficulties:
            lives = difficulties[difficulty]
            break
        else:
            print("Invalid choice! Please choose Easy, Medium or Hard.")
    
    # Provide random word
    word = random.choice(word_list).lower()
    word_letters = list(word)
    display = ["_"] * len(word)
    guessed_letters = []
    
    print(f"\nThe word has {len(word)} letters: {' '.join(display)}")
    
    # Game loop
    while lives > 0 and "_" in display:
        print(f"\nLives left: {lives}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single alphabet letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)

        # let's Check the guess
        if guess in word_letters:
            for i, letter in enumerate(word_letters):
                if letter == guess:
                    display[i] = guess
            print(" Correct guess!")
        else:
            lives -= 1
            print("❌ Wrong guess!")
        
        print("Word: " + " ".join(display))
    
    #let's see the  End result
    if "_" not in display:
        print("\n Congratulations! You guessed the word:", word)
    else:
        print("\n You lost! The word was:", word)


hangman_game()
