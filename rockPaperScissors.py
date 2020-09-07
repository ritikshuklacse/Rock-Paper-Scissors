import random, sys

print('ROCK, PAPER, SCISSORS')

# These 3 variables wil help us to keep track of the number of wins, losses and ties
wins = 0
losses = 0
ties = 0

while True:     # The main game loop
    print('%s Wins, %s Losses, %s Ties \n\n\n'% (wins, losses, ties))
    while True:     # The player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()      # quit the program if player wants to quit
        elif playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break       # Break out of the player input loop
        print('Type one of r, p, s or q')

    # Now we will display what the player had chosen
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print("SCISSORS versus...")

    # Now we will display what computer chooses
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Let us now display and set our wins/losses/ties accordingly
    if playerMove == computerMove:
        print("It's a tie!")
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins =  wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses+1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1
