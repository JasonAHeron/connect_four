from board import GameBoard
from collections import namedtuple


Player = namedtuple('player', ['name', 'piece'])


def create_player(player_number):
    player_name = raw_input('Enter player {} name: '.format(player_number))
    player_piece = raw_input('Enter player {} piece: '.format(player_number))
    if len(player_piece) > 1:
        print 'Player pieces are one character, truncating your piece to {}'.format(player_piece[:1])
    return Player(name=player_name, piece=player_piece[:1].upper())


def run_game(player_one, player_two):
    print 'Starting Game'
    game = GameBoard()
    turn = 0
    while game.winner is None:
        #player one plays even turns
        if turn % 2 == 0:
            current_player = player_one
        #player two plays odd turns
        else:
            current_player = player_two

        # get player input
        print game
        print '   '.join(str(number) for number in range(game.columns))
        column = raw_input('{} which column to place {}? '.format(
            current_player.name,
            current_player.piece
        ))

        # try to insert piece into board, retry turn if failure
        if not game.insert_piece(column, current_player.piece):
            print 'Column either full or invalid, please make another move'
            continue

        turn += 1
    print game
    print '{} wins in {} turns'.format(current_player.name, turn)


if __name__ == '__main__':
    player_one = create_player('one')
    player_two = create_player('two')
    if player_two.piece == player_one.piece:
        print 'players must choose different pieces'
        exit(1)
    run_game(player_one, player_two)
