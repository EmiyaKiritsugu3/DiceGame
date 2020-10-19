from random import randint


def main():
    player1wins = 0
    player2wins = 0
    rounds = 1

    while rounds != 10:
        print('Round ', rounds)
        player1 = dice_roll()
        player2 = dice_roll()
        print('Player 1 Roll: ', player1)
        print('Player 2 Roll: ', player2)

        if player1 == player2:
            print('Draw!\n')
        elif player1 > player2:
            player1wins = player1wins + 1
            print('Player 1 Wins!\n')
        else:
            player2wins = player2wins + 1
            print('Player 2 Wins!\n')

        rounds = rounds + 1
    if player1wins == player2wins:
        print('Draw!')
    elif player1wins > player2wins:
        print('Player 1 Wins - Rounds Won: ', player1wins)
    else:
        print('Player 2 Wins - Rounds Won: ', player2wins)


def dice_roll():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    return dice1, dice2


main()
