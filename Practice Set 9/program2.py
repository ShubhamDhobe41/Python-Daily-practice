'''
The game() function in a program lets a user play a game and returns the score 
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.
'''

import os

# Dummy game function (you can replace it with your actual game logic)
def game():
    # Example: let’s say the score is user input (for demo purpose)
    score = int(input("Enter your score: "))
    return score


def update_high_score(filename="Hi-score.txt"):
    # Get current game score
    score = game()

    # Check if file exists and read high score
    if os.path.exists(filename):
        with open(filename, "r") as f:
            content = f.read().strip()
            high_score = int(content) if content.isdigit() else 0
    else:
        high_score = 0

    print(f"Previous High Score: {high_score}")
    print(f"Your Score: {score}")

    # Update high score if current score is greater
    if score > high_score:
        print("🎉 New High Score! Updating file...")
        with open(filename, "w") as f:
            f.write(str(score))
    else:
        print("No new high score.")


# Run program
update_high_score()

    
        
    