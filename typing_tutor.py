"""
4.1PP Selection and Repetition
"""

__author__ = "Ritham Chhetri"

import timeit

def show_heading(heading: str):
    """
    Displays the given heading in ALL CAPS, underlined by asterisks,
    followed by a blank line.
    """
    
    # Display heading in upper case
    formatted_heading = heading.upper()
    print(formatted_heading)
    
    # Display len(heading) tildes ~
    tildes_line = "~" * len(heading)
    print(tildes_line)
    
    # Display a blank line
    print()


def one_attempt(word: str) -> bool:
    """
    Tests the user's ability to type the given word, providing feedback on
    the attempt. Returns True if they typed it correctly, False otherwise.
    """
    attempt: str    #the user's typed word
    # c orrect = True #Initially True
    
    # Prompt user to type the word
    attempt = input(f"Type '{word}': ")
    
    # Check if the attempt is equal to the word
    if attempt == word:
        print("Correct!")
        return True
    else:
        print("Try again")
        return False
    

def practise_typing(word: str, required: int) -> int:
    """
    Tests the user's typing ability by having them type the given word
    correctly, including capitalisation, required times before finishing.
    Returns the total number of attempts.
    """
    attempts = 0 #the total number of attempts made by the user
    correct = 0
    one_attempt(word)
    
    
    while correct < required:
        attempts += 1
        if one_attempt(word):
            correct += 1
    
    return attempts

def main():
    WORD = "bee"      # the practice word; treat as constant
    REPEATS = 4       # number of required correct repeats; treat as constant
    start_time: float # start time of practise
    end_time: float   # end time of practice
    attempted: int    # number of attempts the user actually took

    show_heading("Touch Typing Tutorial")
    print(f"Today's practice word is '{WORD}' (do not type the quotes)")
    print(f"You need to type {WORD} {REPEATS} times correctly, as quickly as you can")
    print()

    #Run the practice session
    input("Press Enter to start the timed test")
    start_time = timeit.default_timer()
    attempted = practise_typing(WORD, REPEATS)
    end_time = timeit.default_timer()

    #Report on the user's performance
    print("Attempts:", attempted)
    print(f"Accuracy: {100 * REPEATS / attempted:.0f}%")
    print(f"Total time: {end_time - start_time:3.1f} s")
    print()
    show_heading("New word every day!")


if __name__ == "__main__":
    main()