from board import GameBoard

def test_diagonal_win():
    game = GameBoard()
    game.insert_piece(0, 'X')
    game.insert_piece(1, 'Y')
    game.insert_piece(1, 'X')
    game.insert_piece(2, 'Y')
    game.insert_piece(2, 'Y')
    game.insert_piece(2, 'X')
    game.insert_piece(3, 'Y')
    game.insert_piece(3, 'Y')
    game.insert_piece(3, 'Y')
    assert game.winner is None
    game.insert_piece(3, 'X')
    assert game.winner == 'X'

def test_horizontal_win():
    game = GameBoard()
    game.insert_piece(0, 'X')
    game.insert_piece(1, 'X')
    game.insert_piece(2, 'X')
    assert game.winner is None
    game.insert_piece(3, 'X')
    assert game.winner == 'X'

def test_vertical_win():
    game = GameBoard()
    game.insert_piece(0, 'X')
    game.insert_piece(0, 'X')
    game.insert_piece(0, 'X')
    assert game.winner is None
    game.insert_piece(0, 'X')
    assert game.winner == 'X'

def test_bad_int_entry():
    # ensure board state remains unchanged upon bad int entry
    game = GameBoard()
    empty_board = str(game)
    game.insert_piece(12315, 'X')
    assert str(game) == empty_board

def test_bad_string_entry():
    # ensure board state remains unchanged upon bad string entry
    game = GameBoard()
    empty_board = str(game)
    game.insert_piece('test', 'X')
    assert str(game) == empty_board

def test_good_int_entry():
    # ensure board state changes upon correct int entry
    game = GameBoard()
    empty_board = str(game)
    game.insert_piece(0, 'X')
    assert str(game) != empty_board

def test_good_string_entry():
    # ensure board state changes upon correct string entry
    game = GameBoard()
    empty_board = str(game)
    game.insert_piece('0', 'X')
    assert str(game) != empty_board

def test_insert_piece_success():
    # ensure correctly inserting piece results in successful return
    game = GameBoard()
    assert game.insert_piece(0, 'X') is True

def test_insert_piece_failure():
    # ensure incorrectly inserting piece results in failure return
    game = GameBoard()
    assert game.insert_piece('test', 'X') is False


# win conditions
test_diagonal_win()
test_horizontal_win()
test_vertical_win()

# bad entry
test_bad_int_entry()
test_bad_string_entry()

# good entry
test_good_int_entry()
test_good_string_entry()

# basic operations
test_insert_piece_success()
test_insert_piece_failure()

print "Tests passing"
