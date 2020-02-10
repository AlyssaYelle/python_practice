class Game:

    def __init__(self):
        self.game_over = False
        self.winner = None
        self.x_player = None
        self.o_player = None
        self.moves_remaining = 9

    def play(self):
        board = Board()

        self.select_players()

        while not self.game_over:
            self.play_round(board)




    def select_players(self):
        self.x_player = Console("X", input("Player 1, please enter your name:  "))

        if input("Would you like to play the computer or another person?\nPress 1 for the computer\nPress 2 to play another person.\n") == "2":
            self.o_player = Console("O", input("Player 2, please enter your name:  "))
        else:
            print("Our computer is sleeping now. Please try to play later.")
            return


    def play_round(self, board):
        board.print_board()

        move_x_player = self.x_player.add_token(board)
        board.update_board(self.x_player.token, move_x_player)
        self.moves_remaining -= 1


        board.print_board()

        if self.moves_remaining > 0:
            move_o_player = self.o_player.add_token(board)
            board.update_board(self.o_player.token, move_o_player)
            self.moves_remaining -= 1
        else: 
            self.game_over = True






class Board:

    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.state = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]


    def print_board(self):
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
        self.board[move[0]][move[1]] = token
        self.state.remove(move)



class Player:

    def __init__(self, token, name):
        self.name = name
        self.token = token
        self.possible_states = None

    def add_token(self):
        raise NotImplementedError

    def view_board(self, board):
        self.possible_states = board.state



class Console(Player):

    def add_token(self, board):
        self.view_board(board)

        move = [int(input(self.name + ", please enter a row value:  ")), int(input(self.name + ", please enter a column value:  "))]

        while move not in self.possible_states:
            print("Invalid input.")
            move = [int(input(self.name + ", please enter a row value:  ")), int(input(self.name + ", please enter a column value:  "))]

        return move



if __name__ == "__main__":

    game = Game()
    game.play()




