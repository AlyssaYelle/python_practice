'''
Alyssa Jones

Python 3.7

Allows user to run a tic tac toe game in the console and play against another person.

In the future will add functionality to allow user to play AI
'''


class Game:

    def __init__(self):
        '''
        game has two players, x & o, and a board
        may or may not have a winner
        need to keep track of the state of the game
        '''
        self.board = None
        self.game_over = False
        self.winner = None
        self.x_player = None
        self.o_player = None
        self.moves_remaining = 9

    def play(self):
        '''
        initializes a Board
        plays the game
        '''

        # init board
        self.board = Board()

        # pick which players will be human and which will be AI
        self.select_players()

        # play rounds of tic tac toe until the game is over
        while not self.game_over:
            self.play_round()

        # print out board and winner
        self.board.print_board()
        self.declare_winner()




    def select_players(self):
        '''
        prompts user(s) to enter their information in order to create Player
        '''

        # accepts any input for name and creates a console player
        self.x_player = Console("X", input("Player 1, please enter your name:  "))

        # prompts user to select opponent type until user enters valid input
        opponent_type = input("Would you like to play the computer or another person?\nPress 1 for the computer\nPress 2 to play another person.\n")

        while opponent_type not in ["1", "2"]:
            opponent_type = input("Would you like to play the computer or another person?\nPress 1 for the computer\nPress 2 to play another person.\n")

        # set o player to another console player class if user enters 2, otherwise exit
        # TODO: write computer player class
        if opponent_type == "2":
            self.o_player = Console("O", input("Player 2, please enter your name:  "))
        else:
            print("Our computer is sleeping now. Please try to play later.")
            return


    def play_round(self):
        '''
        allows both players to add tokens to Board
        cuts round short if the board fills up or the x player fills a row/col/diag
        '''


        for player in [self.x_player, self.o_player]:

            # if moves remain in game, call players method to add token to board
            # otherwise end game
            if self.moves_remaining > 0:
                self.board.print_board()
                move = player.add_token(self.board)
                self.board.update_board(player.token, move)

                # after player makes a move check if it is a winning move
                # if so, update winner and set game_over = True and return
                if self.check_for_winning_move(player, move):
                    self.winner = player
                    self.game_over = True
                    return

                self.moves_remaining -= 1
            else:
                self.game_over = True
                return
    

    def check_for_winning_move(self, last_player, move):
        '''
        checks to see if the most recent move filled a row, column, or diagonal
        '''

        # check if player filled a column
        col_win = set([((move[0] + 1) % 3, move[1]), ((move[0] + 2) % 3, move[1]), move]).issubset(set(last_player.moves_made))

        # check if player filled a row
        row_win = set([(move[0], (move[1] + 1) % 3), (move[0], (move[1] + 2) % 3), move]).issubset(set(last_player.moves_made))

        # check if player filled a diagonal
        diag_win = set([(0, 0), (1, 1), (2, 2)]).issubset(set(last_player.moves_made)) | set([(2, 0), (1, 1), (0, 2)]).issubset(set(last_player.moves_made))

        # returns true if last move filled a row OR column OR diagonal, else false
        if row_win | col_win | diag_win:
            return True
        else:
            return False


    def declare_winner(self):
        '''
        prints game results to console
        '''
        if self.winner is None:
            print("\nIt's a tie!")
        else:
            print("\n" + self.winner.name + " wins!")




class Board:

    def __init__(self):
        '''
        initially board is empty and all positions are available for use
        '''
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.state = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]


    def print_board(self):
        '''
        pretty printing for tic tac toe board
        rows and columns are labeled to make it easier for console players to select a board position
        '''

        row_val = 0
        print("Column:    0      1      2")

        for row in self.board:
            row_str = "Row " + str(row_val) + ":  "
            row_val += 1
            for col in row:
                token = col if col != " " else "_"
                row_str += " |_" + token + "_| "
            print(row_str)

    def update_board(self, token, move):
        '''
        updates board after user places their token somewhere
        '''

        # places token on board
        self.board[move[0]][move[1]] = token

        # removes position from available positions
        self.state.remove(move)



class Player:
    '''
    abstract player class
    '''

    def __init__(self, token, name):
        '''
        player has a name, token, and list of moves made
        '''
        self.name = name
        self.token = token
        self.moves_made = []

    def add_token(self):
        '''
        add_token should be implemented in child classes
        '''
        raise NotImplementedError

    def view_board(self, board):
        '''
        allows player to see where they can add tokens
        '''
        return board.state



class Console(Player):
    '''
    child class of Player
    human player who plays tic tac toe via console
    '''

    def add_token(self, board):
        '''
        prompts user to select an available board position to place their token
        '''
        possible_moves = self.view_board(board)

        move = (int(input(self.name + ", please enter a row value:  ")), int(input(self.name + ", please enter a column value:  ")))

        while move not in possible_moves:
            print("Invalid input.")
            move = (int(input(self.name + ", please enter a row value:  ")), int(input(self.name + ", please enter a column value:  ")))

        self.moves_made.append(move)

        return move



if __name__ == "__main__":

    game = Game()
    game.play()





