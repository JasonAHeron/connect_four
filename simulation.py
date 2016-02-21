from board import GameBoard

def run_simulation():
    print 'Game Start'
    game = GameBoard()
    game.insert_piece(0,'X')
    print game
    print '#'* 10, 'winner: {}'.format(game.winner), '#'* 10
    game.insert_piece(1, 'Y')
    print game
    print '#'* 10, 'winner: {}'.format(game.winner), '#'* 10
    game.insert_piece(0,'X')
    print game
    print '#'* 10, 'winner: {}'.format(game.winner), '#'* 10
    game.insert_piece(2, 'Y')
    print game
    print '#'* 10, 'winner: {}'.format(game.winner), '#'* 10
    game.insert_piece(0,'X')
    print game
    print '#'* 10, 'winner: {}'.format(game.winner), '#'* 10
    game.insert_piece(2, 'Y')
    print game
    print '#'* 10, 'winner: {}'.format(game.winner), '#'* 10
    game.insert_piece(0,'X')
    print game
    print '#'* 10, 'winner: {}'.format(game.winner), '#'* 10


if __name__ == '__main__':
    run_simulation()
