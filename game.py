from board import Board
from owners import Owner

class Game:

    def __init__(self, dimension):
        self.board = Board(dimension)
        self.current_player = Owner.BLACK
        self.possible_moves = []


    def change_turn(self):
        if (self.current_player == Owner.BLACK):
            self.current_player = Owner.WHITE
        else:
            self.current_player = Owner.BLACK

    def check_for_moves(self):
        self.possible_moves = self.board.check_available_moves(self.current_player)

    #to be used after checking for moves
    def can_player_act(self):
        if (len(self.possible_moves)==0):
            return False
        return True

    def is_game_over(self):
        count_possible_black = len(self.board.check_available_moves(Owner.BLACK))
        count_possible_white = len(self.board.check_available_moves(Owner.WHITE))
        if (count_possible_black!=0 or count_possible_white!= 0):
            return False
        return True


    def show_current_player(self):
        if (self.current_player == Owner.BLACK):
            print("BLACK TURN") 
        else:
            print("WHITE turn") 
            
    def print_score(self):
        self.board.print_score()

    
    def receive_column(self):
        column = input("Select column: ")
        if (len(column)>1):
            raise Exception("Column value must be a capital letter")
        number_value = ord(column)
        number_value = number_value - 65
        if (number_value < 0 or number_value > self.board.get_dimension()-1):
            print("Invalid column input")
        return number_value

    def receive_row(self):
        row = input("Select row: ")
        row = int(row)
        if (row < 0 or row > self.board.get_dimension()-1):
            raise Exception("Invalid row value introduced")
        return row

    def receive_input(self):
        try:
            row = int(self.receive_row())
            column = self.receive_column()
        except:
            return (-1,-1)
        return(row,column)

    def show_hints(self):
        print("Possible moves: ",end="")
        for row,column in self.possible_moves:
            print("({},{})".format(row, chr(column+65)), end = "")
        print("")

    def input_is_valid(self, input_touple):
        row = input_touple[0]
        column = input_touple[0]
        if (row == -1 and column == -1):
            return False
        for row,column in self.possible_moves:
            if (input_touple[0] == row and input_touple[1] == column):
                return True
    
        return False

    def draw_board(self):
        self.board.print_board()

    def set_piece(self, piece_position):
        self.board.set_piece(self.current_player,piece_position[0],piece_position[1])