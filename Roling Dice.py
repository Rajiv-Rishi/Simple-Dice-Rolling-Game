import random

def display_dice(die_value):
    dice_faces = {
        1: (
            "┌───────┐\n"
            "│       │\n"
            "│   ●   │\n"
            "│       │\n"
            "└───────┘"
        ),
        2: (
            "┌───────┐\n"
            "│ ●     │\n"
            "│       │\n"
            "│     ● │\n"
            "└───────┘"
        ),
        3: (
            "┌───────┐\n"
            "│ ●     │\n"
            "│   ●   │\n"
            "│     ● │\n"
            "└───────┘"
        ),
        4: (
            "┌───────┐\n"
            "│ ●   ● │\n"
            "│       │\n"
            "│ ●   ● │\n"
            "└───────┘"
        ),
        5: (
            "┌───────┐\n"
            "│ ●   ● │\n"
            "│   ●   │\n"
            "│ ●   ● │\n"
            "└───────┘"
        ),
        6: (
            "┌───────┐\n"
            "│ ●   ● │\n"
            "│ ●   ● │\n"
            "│ ●   ● │\n"
            "└───────┘"
        )
    }
    return dice_faces[die_value]

def roll_dice():
    input("Press Enter to roll the dice...")
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    
    print(f"\nDie 1:\n{display_dice(die1)}")
    print(f"\nDie 2:\n{display_dice(die2)}")
    print(f"\nTotal: {die1} + {die2} = {total}")
    return total

print("🎲 Welcome to the Dice Rolling Game! 🎲")
print("\nHow to play:")
print("- Roll two dice on your first turn")
print("- If you roll 7 or 11, you win!")
print("- If you roll 2, 3, or 12, you lose!")
print("- Any other number becomes your 'point'")
print("- Keep rolling until you either roll your point again (win) or roll a 7 (lose)")

while True:
    print("\n--- New Round ---")
    first_roll = roll_dice()

    if first_roll in (7, 11):
        print("🎉 Natural! You win!")
    elif first_roll in (2, 3, 12):
        print("💥 Craps! You lose!")
    else:
        point = first_roll
        print(f"\nPoint is {point}. Roll again!")
        while True:
            subsequent_roll = roll_dice()
            if subsequent_roll == point:
                print(f"🎉 Hit the point! You win!")
                break
            elif subsequent_roll == 7:
                print("💥 Seven out! You lose!")
                break
            else:
                print(f"Roll again... (Trying for {point})")

    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again not in ('y', 'yes'):
        print("Thanks for playing! Goodbye!")
        break