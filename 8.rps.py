'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''


print('''Please pick one:
            rock
            scissors
            paper''')
while True:
    game_dict = {'rock':1, 'scissors':2, 'paper':3}
    player_a = input('Player a, give chose your weapon: ')
    player_b = input('Player b, give chose your weapon: ')
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b

    if dif in [-1,2]:
        print('player a wins!')
        if str(input('Do you want to play again: Y/N\n')) == 'Y':
            continue
        else:
            print('Game over')
            break
    elif dif in [-2,1]:
        print('player b wins!')
        if str(input('Do you want to play again: Y/N\n')) == 'Y':
            continue
        else:
            print('Game over')
            break
    else:
        print('Draw\n')



''''
def compare(p1, p2):
    if p1 == p2:
        return('Tie!')
    elif p1 == 'rock':
        if p2 == 'scissors':
            return('p1 wins!')
        else:
            return('p2 wins')
    elif p1 == 'scissors':
        if p2 == 'paper':
            return('p1 wins!')
        else:
            return('p2 wins!')

print(compare(p1, p2))'''