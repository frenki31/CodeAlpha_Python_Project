import requests
import random

word_url = 'https://www.mit.edu/~ecprice/wordlist.100000'
request = requests.get(word_url)
words = request.text.splitlines()
word = random.choice(words)
correct_guess = word
guessed_word = ""
count = 0
while correct_guess != guessed_word:
    print(word)
    print(f'Word to guess: {"*" * len(word)}')
    incorrect_guesses = 0
    while incorrect_guesses < 5:
        guess_letter = str(input(f"Guess letter {str(count + 1)}: "))
        if guess_letter != word[count]:
            if incorrect_guesses < 4:
                print("Incorrect guess. Try again...")
                incorrect_guesses += 1
            elif incorrect_guesses == 4:
                print("Game over! You reached the retries limit")
                break
        else:
            guessed_word += guess_letter
            incorrect_guesses = 0
            count += 1
        if guessed_word == correct_guess:
            print("Congratulations!! You guessed it!")
            break
        else:
            continue
    break