

player1 = 'X'
player2 = 'O'

class Board:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '] , [' ', ' ', ' ']]
    
    def display_board(self):
        print('    0   1   2 ')
        for i in range(len(self.board)): 
            print(i, end = '   ') # end creates the spaces between 0 1 2
            for j in range(len(self.board[i])):
                if j < 2: # gets rid of the last | at the end of the tic tac toe 
                    if self.board[i][j] == ' ':
                        print('  | ', end = '')
                    else: 
                        print(f'{self.board[i][j]} | ', end = '')
                              
                else: 
                    if self.board[i][j] == ' ':
                        print(' ', end = '')
                    else:
                        print(f'{self.board[i][j]}', end = '')
            print('')
            if i < 2:
                print('   -----------') #creates the horizontal lines and gets rid of the last horizontal line
    
    def empty_square(self, row, col):
        if self.board[row][col] == ' ':
            return True
        else:
            return False
        
    def move(self, row, col, counter):
        if counter % 2 == 0:
            self.board[row][col] = player1
        else:
            self.board[row][col] = player2
            

    def win_condition(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
            
            elif self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
                return True

            elif self.board[2][0] == self.board[1][1] == self.board[0][2] != ' ':
                return True
        else:
            return False 
        
    def full_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.empty_square(i, j):
                    return False
        return True
    
if __name__ == "__main__":
    board = Board()
    '''
    print("enter number of rows and columns")
    row = int(input("Rows: "))
    col = int(input("Cols: "))
    '''
    isFull = False
    counter = 0
    while not isFull:
        board.display_board()
        if counter % 2 == 0:
            print("Player 1's turn")
        else:
            print("Player 2's turn")

        row = int(input('row: '))
        col = int(input('col: \n'))
        while row == '' or col == '' or row < 0 or col < 0 or row > 2 or col > 2 or not board.empty_square(row, col):
            print("invalid coordinates. Try again.\n")
            board.display_board()
            row = int(input('row: '))
            col = int(input('col: \n'))

        board.move(row, col, counter)

        if board.win_condition() and counter % 2 == 0:
            print("player 1 won\n")
            board.display_board()
            print()
            exit()
        elif board.win_condition() and counter % 2 != 0:
            print("player 2 won\n")
            board.display_board()
            print()
            exit()

        if board.full_board():
            board.display_board()
            print("draw\n")
            exit()

        counter += 1