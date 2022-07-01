import random
from replit import clear
import hangman_art
import hangman_words

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

lives = 6
end_of_game = False

display = []
for i in range(len(chosen_word)):
    display.append('_')

print(hangman_art.logo)
while not end_of_game:
    guess = input('Guess the letter: ').lower()
    clear()
    if guess in display:
        print(f'You already guessed {guess}')
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = chosen_word[i]


    print(f"{' '.join(display)}")
    print(hangman_art.stages[lives])
    if "_" not in display:
        end_of_game = True
        print(hangman_art.stages[lives])
        print("You win.")
    if guess not in chosen_word:
        lives -= 1
        print(f'You guessed {guess}. That is not in the word. You lose a life.')
        if lives == 0:
            end_of_game = True
            print(hangman_art.stages[lives])
            print("You lose.")