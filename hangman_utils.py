from random import choice
import string

def select_word():
    with open('word.txt', 'r') as words:
        word_list = words.readlines()
        return choice(word_list).strip()
    
def get_player_input(guessed_letters):
    while True:
        player_input = input("Guess a letter: ").lower()
        if validate_input(player_input, guessed_letters):
            return player_input
        
def validate_input(player_input, guessed_letters):
    return (
        len(player_input) == 1
        and player_input in string.ascii_lowercase
        and player_input not in guessed_letters
    )

def join_guessed_letters(guessed_letters):
    return ' '.join(sorted(guessed_letters))

def build_guessed_word(target_word, guessed_letters):
    current_letters = []
    for letter in target_word:
        if letter in guessed_letters:
            current_letters.append(letter)
        else:
            current_letters.append("_")
    return " ".join(current_letters)

def draw_hanged_man(wrong_guesses):
    hanged_man = [
    r"""
                        ________
                        ||      ||
                                ||
                                ||
                                ||
                                ||
                                ||
                                ||
                                ||
                                ||
                                ||
                ------------------
                               
""",
r"""
                        ________
                        |       ||
                       (_)      ||
                                ||
                                ||
                                ||
                                ||
                                ||
                                ||
                                ||
                                ||
                ------------------
                               
""",
r"""
                        ________
                        |       ||
                       (_)      ||
                      -----     ||
                       |||      ||
                       |||      ||
                                ||
                                ||
                                ||
                                ||
                                ||
                ------------------
                               
""",
r"""
                        ________
                        |       ||
                       (_)      ||
                      -----     ||
                   //  |||      ||
                  //   |||      ||
                                ||
                                ||
                                ||
                                ||
                                ||
                ------------------
                               
""",
r"""
                        ________
                        |       ||
                       (_)      ||
                      -----     ||
                   //  |||  \\  ||
                  //   |||   \\ ||
                                ||
                                ||
                                ||
                                ||
                                ||
                ------------------
                               
""",
r"""
                        ________
                        |       ||
                       (_)      ||
                      -----     ||
                   //  |||  \\  ||
                  //   |||   \\ ||
                       ===      ||
                     //         ||
                    ||          ||
                    ||          ||
                                ||
                ------------------
                               
""",
r"""
                        ________
                        |       ||
                       (_)      ||
                      -----     ||
                   //  |||  \\  ||
                  //   |||   \\ ||
                       ===      ||
                     //   \\    ||
                    ||     ||   ||
                    ||     ||   ||
                                ||
                ------------------
                               
"""
]

    print(hanged_man[wrong_guesses])


max_incorrect_guesses = 6

def game_over(wrong_guesses, target_word, guessed_letters):
    if wrong_guesses == max_incorrect_guesses:
        return True
    if set(target_word) <= guessed_letters:
        return True
    return False