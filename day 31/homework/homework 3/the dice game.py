import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Game!")

    # first we have to get the players names obv
    player1_name = input("Enter the name for Player 1: ")
    player2_name = input("Enter the name for Player 2: ")

    # than roll the dice for each player
    result_player1 = roll_dice()
    result_player2 = roll_dice()

    # and display the final results
    print(f"\n{player1_name} rolled a {result_player1} on a 6-sided dice.")
    print(f"{player2_name} rolled a {result_player2} on a 6-sided dice.")

    # find the winner
    if result_player1 > result_player2:
        print(f"\nCongratulations, {player1_name} wins!")
    elif result_player1 < result_player2:
        print(f"\nCongratulations, {player2_name} wins!")
    else:
        print("\nIt's a tie!")

if __name__ == "__main__":
    main()