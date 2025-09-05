import random

words = ["python", "hangman", "computer", "engineer", "random"]
word = random.choice(words)
guessed_word = ["_"] * len(word)

attempts = 6
guessed_letters = []

print("Welcome to Hangman Game!")
print("The word has", len(word), "letters.")
print(" ".join(guessed_word))

while attempts > 0 and "_" in guessed_word:
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        continue
    if guess in guessed_letters:
        continue
    guessed_letters.append(guess)
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)
    print(" ".join(guessed_word))

if "_" not in guessed_word:
    print("You guessed the word:", word)
else:
    print("Game Over! The word was:", word)