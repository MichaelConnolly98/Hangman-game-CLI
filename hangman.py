from hangman_utils import select_word, build_guessed_word, game_over, draw_hanged_man, join_guessed_letters, get_player_input, max_incorrect_guesses


if __name__ == '__main__':
    # initial setup
    target_word = select_word()
    guessed_letters = set()
    guessed_word = build_guessed_word(target_word, guessed_letters)
    wrong_guesses = 0
    print(r"""
        -
       | |
       | |__      __  _   _  __      ___   _   _  __    _     __  _   _  __   
       |     \   /  \| | | \|  \   /     \| | | \|  \ /  \   /  \| | | \|  \  
       |  __  | |  _   | |   _  | |    _    | |   _   _   | |  _   | |   _  | 
       | |  | | | (_|  | | |  | | |   (_|   | | |  | | |  | | (_|  | | |  | | 
       |_|  |_| |____ _| |_|  |_|  \ ___    | |_|  |_| |__| |____ _| |_|  |_| 
                                      ___|  |
                                    /_____ /      
                                    
""")
    print(' ************ Welcome to Hangman! ************ ')

    # game loop
    while not game_over(wrong_guesses, target_word, guessed_letters):
        draw_hanged_man(wrong_guesses)
        print(f" ************ Your word is: {guessed_word} ************ ")
        print(
            " ************ Current guessed letters: "
            f"{join_guessed_letters(guessed_letters)}\n"
        )

        player_guess = get_player_input(guessed_letters)
        if player_guess in target_word:
            print(' ************ Great guess! ************ ')
        else:
            print(" ************ Sorry, it's not there. ************ ")
            wrong_guesses += 1
            print(f" ************ Number of wrong guesses: {wrong_guesses}/6 ************ ")
        
        guessed_letters.add(player_guess)
        guessed_word = build_guessed_word(target_word, guessed_letters)

    # Game over
    draw_hanged_man(wrong_guesses)
    if wrong_guesses == max_incorrect_guesses:
        print(" ************ Sorry, you lost! ************ ")
        print(f" ************ The correct word was: {target_word} ************ ")
        print(" ************ Better luck next time ************ ")
    else:
        print(" ************ Congrats! Your did it! ************ ")
        print(f" ************ Your word was: {target_word} ************ ")

        #change formatting so print statements in CLI are prettier