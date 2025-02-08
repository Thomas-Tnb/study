from random import randint

words = [
        "apple", "banana", "cherry", "dog", "elephant", "flower", "guitar", "happiness", "island", "jungle",
        "kangaroo", "lemon", "mountain", "notebook", "ocean", "penguin", "quasar", "rainbow", "sunshine", "tiger",
        "umbrella", "volcano", "watermelon", "xylophone", "yellow", "zeppelin", "adventure", "butterfly", "chocolate",
        "diamond", "enchanted", "fireworks", "glacier", "harmony", "illusion", "journey", "knight", "lighthouse",
        "moonlight", "nostalgia", "origami", "paradox", "quicksilver", "rendezvous", "serendipity", "twilight",
        "universe", "victory", "whisper", "zephyr"
    ]

word = words[randint(0, len(words) - 1)]
lives = 5
guesses = []
shownWord = list("_" * len(word))
print(shownWord)

print(f"Word : {word}")
while(lives > 0 and "_" in shownWord):
    guess = str(input("Guess a letter :"))[0]
    while guess in guesses: 
        guess = str(input("You already guessed this letter, guess another one :"))[0]
    else:
        for i in range(len(word)):
            if word[i] == guess:
                shownWord[i] = guess
        guesses.append(guess)
    if guess not in word:
        lives -= 1
    print(f"Word : {shownWord}\nGuesses : {guesses}    |    Lives : {lives}")
if lives > 0:
    print(f"Congratulations, you won!! The word was {word}\nYou still had {lives} lives.")
else:
    print(f"You lost, the word was {word}")


