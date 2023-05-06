import random

print("H A N G M A N\n")

won = 0
lose = 0

while True:
    mode = str(input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: '))
    word_list = ["python", "java", "swift", "javascript"]
    number_attempts = 8
    random_word = random.choice(word_list)
    length_word = len(random_word)
    sliced_word = "-" * length_word
    attempt_letter = set()
    listed_letter = set()
    tested_letter = ""

    if mode == "results":
        print(f"You won: {won} times")
        print(f"You lost: {lose} times")

    if mode == "exit":
        break

    while number_attempts != 0 and mode == "play":

        letter = ""
        print(sliced_word)
        if len(letter) != 1:
            tested_letter = str(input("Input a letter: "))
            if len(tested_letter) != 1:
                print("Please, input a single letter.")
                continue
            else:
                if not tested_letter.islower() or not tested_letter.isalpha():
                    print("Please, enter a lowercase letter from the English alphabet.")
                else:
                    if tested_letter in attempt_letter:
                        print("You've already guessed this letter.")
                    else:
                        attempt_letter.add(tested_letter)
                        letter = tested_letter

        if letter in random_word:
            for i, char in enumerate(random_word):
                if char == letter:
                    if char not in listed_letter:
                        sliced_word = sliced_word[:i] + letter + sliced_word[i + 1:]
                        if random_word.count(letter) == sliced_word.count(letter):
                            listed_letter.add(letter)

            if sliced_word == random_word:
                print(f"You guessed the word {random_word}!\nYou survived!")
                won += 1
                break
        else:
            print("That letter doesn't appear in the word.")
            number_attempts -= 1

    if number_attempts == 0:
        print("you lost!")
        lose += 1
