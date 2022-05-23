# Hangman Game

MAX_TRIES = 7


def main():
    old_letters_guessed = [""]
    num_of_tries = 1

    Welcome()
    words_file_path = input("Path to HangmanWords.txt file: ")
    word_index = input("Please enter number for choosing word: ")

    # Choose word from file
    word_index_in_file, secret_word = choose_word(words_file_path, word_index)

    print("Let's get start! \n")
    print_hangman(num_of_tries)
    show_hidden_word(secret_word, old_letters_guessed)

    while (num_of_tries < MAX_TRIES) and not (check_win(secret_word, old_letters_guessed)):
        letter_guessed = input("\nGuess a letter: ")
        is_letter_valid = try_update_letter_guessed(letter_guessed, old_letters_guessed)

        if is_letter_valid:
            if not letter_is_right_guest(secret_word, letter_guessed):
                num_of_tries = num_of_tries + 1
                print(":(")
                print_hangman(num_of_tries)
            else:
                show_hidden_word(secret_word, old_letters_guessed)

    if check_win(secret_word, old_letters_guessed):
        print("You won!!")

    else:
        print("You lost!")
        print("The secret word: " + secret_word)


# This function print hangman welcome screen
def Welcome():
    print("""                   
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                        __/ |
                       |___/



                              """)


# This function check if the user input is valid and return boolean
def check_valid_input(letter_guessed, old_letters_guessed):
    if ((letter_guessed not in old_letters_guessed) and
            (letter_guessed.isalpha()) and
            (len(letter_guessed) == 1)):
        return True

    return False


# This function check if the user won the game and return boolean
def check_win(secret_word, old_letters_guessed):
    count_correct_letters = 0
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False

    return True


# This function print the board game with correct current letters
def show_hidden_word(secret_word, old_letters_guessed):
    print()
    for letter in secret_word:
        if letter in old_letters_guessed:
            print(letter + ' ', end='')
        else:
            print("_ ", end='')
    print()


# This function check if current letter is currect and return boolean
def letter_is_right_guest(secret_word, letter_guessed):
    if letter_guessed in secret_word:
        return True

    return False


# This function
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.extend(letter_guessed)
        return True
    else:
        old_letters_guessed.sort()
        speartor = " -> "
        print("X")
        print(speartor.join(old_letters_guessed))
        return False


# This function open .txt file and select word from it with requested number
def choose_word(words_file_path, index):
    appears_once = set()
    with open(words_file_path, "r") as file_words:
        words = file_words.read().split(' ')
        for word in words:
            if word not in appears_once:
                appears_once.add(word)
    appears_once = list(appears_once)
    selected_word_index = (int(index) % len(appears_once))

    return len(appears_once), appears_once[selected_word_index].lower()


# This function print hangman pictures parallel of wrong guesses
def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {
        1: '''x-------x''',
        2: '''x-------x
|
|
|
|
|
''',
        3: '''x-------x
|       |
|       0
|
|
|''',
        4: '''x-------x
|       |
|       0
|       |
|
|''',
        5: '''x-------x
|       |
|       0
|      /|\\
|
|''',
        6: '''x-------x
|       |
|       0
|      /|\\
|      /
|''',
        7: '''
x-------x
|       |
|       0
|      /|\\
|      / \\
|'''
    }
    print(HANGMAN_PHOTOS[num_of_tries])


if __name__ == "__main__":
    main()


