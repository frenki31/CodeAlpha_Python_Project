import requests
import random

word_url = 'https://www.mit.edu/~ecprice/wordlist.100000'
request = requests.get(word_url)
words = request.text.splitlines()
word = random.choice(words)
correct_guess = word
guessed_word = "*" * len(word)
count = 0
while correct_guess != guessed_word:
    # print(word)
    print(f'Word to guess: {guessed_word}')
    incorrect_guesses = 0
    while incorrect_guesses < (len(word)*2-2):
        guess_letter = str(input("Guess a letter: "))
        if guess_letter not in word:
            if incorrect_guesses < (len(word)*2-3):
                incorrect_guesses += 1
                print(f"Wrong guess. You have {(len(word)*2-2)-incorrect_guesses} incorrect guesses remaining.")
            elif incorrect_guesses == (len(word)*2-3):
                print("Game over! You reached the guesses limit")
                break
        else:
            for i, letter in enumerate(word):
                if letter == guess_letter:
                    index = i
                    guessed_word = guessed_word[:index]+guess_letter+guessed_word[index+1:]
            print(f'Guessed word until now: {guessed_word}')
            count += 1
        if guessed_word == correct_guess:
            print(f"Congratulations!! You guessed it!")
            break
        else:
            continue
    break