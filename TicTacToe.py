# TODO: Need to only accept x or o in constructor
# TODO: Filter inout for making a move to 1-9
# TODO: Fix the god ugly line in Game.commit_move() that decides row
# TODO: Investigate protecting variables
# TODO: Consider removing winning_player variable
# TODO: Add inout check to commit move, or somewhere relevant. Make sure occupied sqaures can't be written to
# TODO: Consider combining check_move and commit_move
# TODO: Consider removing the inital display_board from take_turn, perhaps it should be somewhere else
# TODO: Force input in take_turn to be an integer 1-9
# TODO: Write test for toggle_current_player
# TODO: Write test for get_starting_player
# TODO: Write test for play
# TODO: fix the god ugly victory checks


class Game:
	def __init__(self, *starting_player):
		print("")
		print("==========================")	
		print("Welcome to Tic-Tac-Toe!")
		self.board = [["  ","  ","  "],["  ","  ","  "],["  ","  ","  "]]
		if starting_player:
			self.current_player = starting_player[0]
		else:
			self.current_player = self.get_starting_player()
			self.play() # Game only autoplays if no arguments passed to Game constructor
		
	
	def get_starting_player(self):
		while True:
			starting_player = input("Enter starting player (X or O): ").upper()
			if starting_player == "X" or starting_player == "O":
				return starting_player
			else:
				print("You must enter either 'X' or 'O'")
	
	def check_square_is_empty(self, square_number):
		row = (square_number + 2) // 3 - 1 # this is a bit gross but it works
		column = square_number % 3 - 1
		if self.board[row][column] == "  ":
			return True
		else:
			return False
	
	def commit_move(self, square_number, player_symbol):
		row = (square_number + 2) // 3 - 1 # this is a bit gross but it works
		column = square_number % 3 - 1
		self.board[row][column] = player_symbol
		
	def display_board(self):
		for row in self.board:
			for square in row:
				print(f"[ {square} ]  ", end = "")
			print("\n")
			
	def check_victory(self):
		# Check each row
		for i in range(3):
			if self.board[i][0] != "  " and self.board[i][0] == self.board[i][1] == self.board[i][2]:
				return self.board[i][0]
		# Check each column
		for i in range(3):
			if self.board[0][i] != "  " and self.board[0][i] == self.board[1][i] == self.board[2][i]:
				return self.board[0][i]
		# Check each diagonal
		if self.board[0][0] != "  " and self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[0][2] != "  " and self.board[0][2] == self.board[1][1] == self.board[2][0]:
			return self.board[1][1]
		# return None if no victory
		return None
		
	def toggle_current_player(self):
		if self.current_player == "X":
			self.current_player = "O"
		else:
			self.current_player = "X"
	
	def take_turn(self, player_symbol):
		print("")
		print("==========================")
		self.display_board()
		print(f"Player {player_symbol} it's your turn.")
		while True:
			move = input("Which square would you like to make your move in (1-9)? ")
			try:
				move = int(move)
			except ValueError:
				print("That wasn't an integer, please only enter integers.")
				continue
			if not (0 < move < 10):
				print("That integer wasn't between 1 and 9. Please only enter integers between 1 and 9.")
			elif not self.check_square_is_empty(move):
				print("That square is already occupied. Please pick a free square.")
			else:
				break # only exit to loop
		self.commit_move(move, player_symbol)
	
	def play(self):
		while True:			
			self.take_turn(self.current_player)
			winner = self.check_victory()
			if winner == None:				
				self.toggle_current_player()
			else:
				print("")
				print("==========================")
				self.display_board()
				print(f"{winner} wins!")
				break
			
def test_constructor_and_display_board():
	test_game = Game("X")
	test_game.display_board()
	test_game.board = [["1","2","3"],["4","5","6"],["7","8","9"]]
	test_game.display_board()
	test_game.board = [["X","O","X"],["O","X","O"],["X","O","X"]]
	test_game.display_board()
	
def test_check_square_is_empty():
	test_game = Game("X")
	test_game.board = [["X","O","  "],["  ","X","O"],["X","  ","X"]]
	test_game.display_board()
	for i in range(1, 10):
		print(i)
		print(test_game.check_square_is_empty(i))

def test_commit_move():
	test_game = Game("X")
	print("1 X")
	test_game.commit_move(1,"X")
	test_game.display_board()
	print("4 O")
	test_game.commit_move(4,"O")
	test_game.display_board()
	print("9 X")
	test_game.commit_move(9,"X")
	test_game.display_board()
	print("3 X")
	test_game.commit_move(3,"X")
	test_game.display_board()
	print("7 O")
	test_game.commit_move(7,"O")
	test_game.display_board()
	
def test_check_victory():
	test_board_list = [
		[
		["X","O","X"],
		["O","X","O"],
		["X","O","X"]
		],
		[
		["O","O","O"],
		["O","X","O"],
		["X","O","X"]
		]
		]
	for test_board in test_board_list:
		test_game = Game("X")
		test_game.board = test_board
		test_game.display_board()
		print(test_game.check_victory())
		print("")
		print("")
		
def test_take_turn_multiple_times():
	number_of_tests = 9 # Don't set this above 9, it can only legally execute 9 times before you'll have to manually break the program to get out
	test_game = Game()
	for i in range(9):
		test_game.take_turn(test_game.current_player)
		test_game.toggle_current_player()
		
def test_construct_without_arg():
	Game()

def run_test(test_function):
	print("")
	print("==========================")
	print(f"{test_function.__name__}()")
	print("")
	test_function()
	print("==========================")

automatic_tests_list = [
	test_constructor_and_display_board,
	test_check_square_is_empty,
	test_commit_move,
	test_check_victory
]
interactive_tests_list = [
	# test_take_turn_multiple_times
	test_construct_without_arg
]

run_automatic_tests = True
run_interactive_tests = True

if run_automatic_tests:
	for test in automatic_tests_list:
		run_test(test)
if run_interactive_tests:
	for test in interactive_tests_list:
		run_test(test)