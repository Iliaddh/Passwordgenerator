import random

word_list = ["ardvark", "baboon", "camel"]
display = []
lives = 6;
chosen_word = random.choice(word_list)
for underline in chosen_word:
    display += "_"
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower();

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")
    if guess not in chosen_word:
        lives -= 1;
        print(f"Your live is {lives}")

    if lives == 0:
        end_of_game = True
        print(f"You loose! The right answer was {chosen_word}")


