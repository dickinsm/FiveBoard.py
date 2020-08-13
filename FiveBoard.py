# Author: Makaliah Dickinson
# Date: 8/13/2020
# Description: Write a class that represents the board for a two-player game that is similar to tic-tac-toe but larger.
#              It is played on a 15x15 board, the player tries to get 5 pieces in a row. The row of pieces can be
#              vertical, horizontal, or diagonal. 

class FiveBoard:
    __l = None
    __current_state = None

    def __init__(self):  # constructor of class
        self.__current_state = "UNFINISHED"
        self.__l = []
        for i in range(15):
            temp = []
            for j in range(15):
                temp.append(" ")
            self.__l.append(temp)  # append list of empty strings to l

    def get_current_state(self):  # return current state
        return self.__current_state

    def make_move(self, row, col, value):
        if self.__l[row][col] != " ":
            return False
        elif self.get_current_state() in ["X_WON", "O_WON", "DRAW"]:  # return false if state is in any elements of list
            return False
        else:
            self.__l[row][col] = value  # change the value of board at given location
            return True

    def print_board(self):  # prints the elements of board
        for i in self.__l:
            for j in i:
                print(j, end=" ")
            print()


board = FiveBoard()
board.make_move(6, 5, 'x')
board.make_move(2, 1, 'x')
board.make_move(3, 2, 'x')
print(board.get_current_state())  # print the current state
board.print_board()  # print the board
