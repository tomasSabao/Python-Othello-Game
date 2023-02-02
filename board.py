from owners import Owner
from board_tile import Board_tile
from termcolor import colored

class Board:
    def __init__(self, dimension):
        self.board = []
        self.dimension = dimension
        #the board has "dimension" columns which are empty 
        for x in range (0,dimension):
            self.board.append([])
        for i in range (0,dimension):
            for x in range(0,dimension):
                self.board[i].append(Board_tile(False, Owner.OWNERLESS))
        initial_pos = int(dimension/2)-1
        self.board[initial_pos][initial_pos].change_owner(Owner.WHITE)
        self.board[initial_pos][initial_pos].occupy()

        self.board[initial_pos+1][initial_pos].change_owner(Owner.BLACK)
        self.board[initial_pos+1][initial_pos].occupy()
        
        self.board[initial_pos][initial_pos+1].change_owner(Owner.BLACK)
        self.board[initial_pos][initial_pos+1].occupy()

        self.board[initial_pos+1][initial_pos+1].change_owner(Owner.WHITE)
        self.board[initial_pos+1][initial_pos+1].occupy()
        
    def check_available_moves(self, player):
        possible_moves = []
        for row in range (0, self.dimension):
            for column in range (0,self.dimension):
                if (self.board[column][row].is_occupied()):
                    continue
                if (self.check_piece(player, row, column)):
                    possible_moves.append((row,column))
        return possible_moves

    def get_dimension(self):
        return self.dimension

    def check_piece(self, player, row, column):
        #check right
        tiles_to_turn = []
        column_iter = column+1
        while (column_iter < self.dimension):
            owner =  self.board[column_iter][row].get_owner()
            if (owner == Owner.OWNERLESS):
                break
            if (owner != player):
                tiles_to_turn.append((row, column_iter))
            if (owner == player):
                if (len(tiles_to_turn)!= 0):
                    return True
                else:
                    break
            column_iter+=1

        tiles_to_turn=[]   
        column_iter = column-1
        while (column_iter > -1):
            owner =  self.board[column_iter][row].get_owner()
            if (owner == Owner.OWNERLESS):
                break
            if (owner != player):
                tiles_to_turn.append((row, column_iter))
            if (owner == player):
                if (len(tiles_to_turn)!= 0):
                    return True
                else:
                    break
            column_iter-=1

        tiles_to_turn=[]
        row_iter = row+1
        while (row_iter < self.dimension):
            owner =  self.board[column][row_iter].get_owner()
            if (owner == Owner.OWNERLESS):
                break
            if (owner != player):
                tiles_to_turn.append((row_iter, column))
            if (owner == player):
                if (len(tiles_to_turn)!= 0):
                    return True
                else:
                    break
            row_iter+=1

        tiles_to_turn=[]
        row_iter = row-1
        while (row_iter > -1):
            owner =  self.board[column][row_iter].get_owner()
            if (owner == Owner.OWNERLESS):
                break
            if (owner != player):
                tiles_to_turn.append((row_iter, column))
            if (owner == player):
                if (len(tiles_to_turn)!= 0):
                    return True
                else:
                    break
            row_iter-=1

        #diagonally right downwards
        tiles_to_turn=[]
        row_iter = row+1
        column_iter = column+1
        while (row_iter < self.dimension and column_iter < self.dimension):
            owner =  self.board[column_iter][row_iter].get_owner()
            if (owner == Owner.OWNERLESS):
                break
            if (owner != player):
                tiles_to_turn.append((row_iter, column_iter))
            if (owner == player):
                if (len(tiles_to_turn)!= 0):
                    return True
                else:
                    break
            row_iter+=1
            column_iter+=1
        #diagonally right upwards
        tiles_to_turn=[]

        row_iter = row-1
        column_iter = column+1
        while (row_iter >-1 and column_iter < self.dimension):
            owner =  self.board[column_iter][row_iter].get_owner()
            if (owner == Owner.OWNERLESS):
                break
            if (owner != player):
                tiles_to_turn.append((row_iter, column_iter))
            if (owner == player):
                if (len(tiles_to_turn)!= 0):
                    return True
                else:
                    break
            row_iter-=1
            column_iter+=1
        
        #diagonally left upwards
        tiles_to_turn=[]
        row_iter = row-1
        column_iter = column-1
        while (row_iter >-1 and column_iter > -1):
            owner =  self.board[column_iter][row_iter].get_owner()
            if (owner == Owner.OWNERLESS):
                break
            if (owner != player):
                tiles_to_turn.append((row_iter, column_iter))
            if (owner == player):
                if (len(tiles_to_turn)!= 0):
                    return True
                else:
                    break
            row_iter-=1
            column_iter-=1
        #diagonally left downwards
        tiles_to_turn=[]

        row_iter = row+1
        column_iter = column-1
        while (row_iter < self.dimension and column_iter < self.dimension):
            owner =  self.board[column_iter][row_iter].get_owner()
            if (owner == Owner.OWNERLESS):
                break
            if (owner != player):
                tiles_to_turn.append((row_iter, column_iter))
            if (owner == player):
                if (len(tiles_to_turn)!= 0):
                    return True
                else:
                    break
            row_iter+=1
            column_iter-=1
            
    def set_piece(self, player, row, column):
        #check right

        
        tiles_to_turn = []
        column_iter = column+1
        while (column_iter < self.dimension):
            owner =  self.board[column_iter][row].get_owner()
            if (owner == Owner.OWNERLESS):
                break
            if (owner != player):
                tiles_to_turn.append((row, column_iter))
            if (owner == player):
                if (len(tiles_to_turn) != 0):
                    self.board[column][row].occupy()
                    self.board[column][row].change_owner(player)
                    for target_row, target_column in tiles_to_turn:
                        self.board[target_column][target_row].change_owner(player)
                else:
                    break
            column_iter+=1

        tiles_to_turn=[]   
        column_iter = column-1
        while (column_iter > -1):
            owner =  self.board[column_iter][row].get_owner()
            if (owner == Owner.OWNERLESS):
                break
            if (owner != player):
                tiles_to_turn.append((row, column_iter))
            if (owner == player):
                if (len(tiles_to_turn) != 0):
                    self.board[column][row].occupy()
                    self.board[column][row].change_owner(player)
                    for target_row, target_column in tiles_to_turn:
                        self.board[target_column][target_row].change_owner(player)
                else:
                    break
            column_iter-=1

        tiles_to_turn=[]
        row_iter = row+1
        while (row_iter < self.dimension):
            owner =  self.board[column][row_iter].get_owner()
            if (owner == Owner.OWNERLESS):
                break
            if (owner != player):
                tiles_to_turn.append((row_iter, column))
            if (owner == player):
                if (len(tiles_to_turn) != 0):
                    self.board[column][row].occupy()
                    self.board[column][row].change_owner(player)
                    for target_row, target_column in tiles_to_turn:
                        self.board[target_column][target_row].change_owner(player)
                else:
                    break
            row_iter+=1

        tiles_to_turn=[]
        row_iter = row-1
        while (row_iter > -1):
            owner =  self.board[column][row_iter].get_owner()
            if (owner == Owner.OWNERLESS):
                break
            if (owner != player):
                tiles_to_turn.append((row_iter, column))
            if (owner == player):
                if (len(tiles_to_turn) != 0):
                    self.board[column][row].occupy()
                    self.board[column][row].change_owner(player)
                    for target_row, target_column in tiles_to_turn:
                        self.board[target_column][target_row].change_owner(player)
                else:
                    break
            row_iter-=1

        #diagonally right downwards
        tiles_to_turn=[]
        row_iter = row+1
        column_iter = column+1
        while (row_iter < self.dimension and column_iter < self.dimension):
            owner =  self.board[column_iter][row_iter].get_owner()
            if (owner == Owner.OWNERLESS):
                break
            if (owner != player):
                tiles_to_turn.append((row_iter, column_iter))
            if (owner == player):
                if (len(tiles_to_turn) != 0):
                    self.board[column][row].occupy()
                    self.board[column][row].change_owner(player)
                    for target_row, target_column in tiles_to_turn:
                        self.board[target_column][target_row].change_owner(player)
                else:
                    break
            row_iter+=1
            column_iter+=1

        #diagonally right upwards
        tiles_to_turn=[]
        row_iter = row-1
        column_iter = column+1
        while (row_iter >-1 and column_iter < self.dimension):
            owner =  self.board[column_iter][row_iter].get_owner()
            if (owner == Owner.OWNERLESS):
                break
            if (owner != player):
                tiles_to_turn.append((row_iter, column_iter))
            if (owner == player):
                if (len(tiles_to_turn) != 0):
                    self.board[column][row].occupy()
                    self.board[column][row].change_owner(player)
                    for target_row, target_column in tiles_to_turn:
                        self.board[target_column][target_row].change_owner(player)
                else:
                    break
            row_iter-=1
            column_iter+=1
        
        #diagonally left upwards
        tiles_to_turn=[]
        row_iter = row-1
        column_iter = column-1
        while (row_iter >-1 and column_iter > -1):
            owner =  self.board[column_iter][row_iter].get_owner()
            if (owner == Owner.OWNERLESS):
                break
            if (owner != player):
                tiles_to_turn.append((row_iter, column_iter))
            if (owner == player):
                if (len(tiles_to_turn) != 0):
                    self.board[column][row].occupy()
                    self.board[column][row].change_owner(player)
                    for target_row, target_column in tiles_to_turn:
                        self.board[target_column][target_row].change_owner(player)
                else:
                    break
            row_iter-=1
            column_iter-=1

        #diagonally left downwards
        tiles_to_turn=[]
        row_iter = row+1
        column_iter = column-1
        while (row_iter < self.dimension and column_iter < self.dimension):
            owner =  self.board[column_iter][row_iter].get_owner()
            if (owner == Owner.OWNERLESS):
                break
            if (owner != player):
                tiles_to_turn.append((row_iter, column_iter))
            if (owner == player):
                if (len(tiles_to_turn) != 0):
                    self.board[column][row].occupy()
                    self.board[column][row].change_owner(player)
                    for target_row, target_column in tiles_to_turn:
                        self.board[target_column][target_row].change_owner(player)
                else:
                    break
            row_iter+=1
            column_iter-=1

    def print_score(self):
        white_score = 0
        black_score = 0
        for row in range (0,self.get_dimension()):
            for column in range (0,self.get_dimension()):
                owner = self.board[column][row].get_owner()
                if (owner == Owner.OWNERLESS):
                    continue
                if (owner == Owner.BLACK):
                    black_score+=1
                if (owner == Owner.WHITE):
                    white_score+=1
        print("WHITE Score: {}".format(white_score))
        print("BLACK Score: {}".format(black_score))

    def print_board(self):
        ##printing top column
        print(" |",end="")
        initial_ascii = 65
        for i in range(0, self.dimension):
            print(chr(initial_ascii + i) + '|', end = "")
        print("")
        for row in range(0,self.dimension):
            for column in range(0, self.dimension):
                if (column == 0):
                    print("{}|".format(row), end = "")
                    
                owner = self.board[column][row].get_owner()
                if (owner == Owner.OWNERLESS):
                    print('\x1b[4;30;42m' + ' |' + '\x1b[0m' , end="")
                if (owner == Owner.BLACK):
                    print('\x1b[4;34;42m' + 'X', end="")
                    print('\x1b[3;30;42m' + '|' + '\x1b[0m' , end="")
                if (owner == Owner.WHITE):
                    print('\x1b[4;37;42m' + 'Y' + '\x1b[0m' , end="")
                    print('\x1b[3;30;42m' + '|' + '\x1b[0m' , end="")   
                if (column == self.dimension-1):
                    print("")