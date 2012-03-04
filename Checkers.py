'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=204
'''
class Board():
     # define the constant for the board
    EMPTY = '-'
    RED = 'R'
    BLACK = 'B'   
    
    _board = []
    
    def __init__(self, nRows, nColumns):
        self._nRows = nRows
        self._nColumns = nColumns
        self.initBoard()
    
    def initBoard(self):
        board = []
        for i in range(self._nRows):
            row = []
            for j in range(self._nColumns):
                row.append(self.EMPTY)
            board.append(row)
        self._board = board
    
    def checkPosition(self, i, j):
        valid = True
        if i < 0 or i >= self._nRows:
            valid = False
        if j < 0 or j >= self._nColumns:
            valid = False
        return valid
    
    def hasPiece(self, i, j, color = 'B'):
        hasPiece = False
        if self.checkPosition(i, j):
            hasPiece = self._board[i][j] == color
        return hasPiece
    
    def placePiece(self, i, j, color = 'B'):
        self._board[i][j] = color
    
class Checker():
    
    def move(self, board, i, j):
        if (board.hasPiece(i+1, j+1) and not board.hasPiece(i+2, j+2) and board.checkPosition(i+2, j+2))  or (board.hasPiece(i+1, j-1) and not board.hasPiece(i+2, j-2) and board.checkPosition(i+2, j-2)):
            while i<>board._nRows-1:
                if board.hasPiece(i+1, j+1) and not board.hasPiece(i+2, j+2) and board.checkPosition(i+2, j+2):
                    i+=2
                    j+=2
                elif board.hasPiece(i+1, j-1) and not board.hasPiece(i+2, j-2) and board.checkPosition(i+2, j-2):
                    i+=2
                    j-=2
                else:
                    break
        elif not board.hasPiece(i+1, j):
            i+=1
        return i, j
    
    def count(self, board, i, j):
        # Initialize the count of the number of movements
        moves = -1
        while i<>board._nRows-1:
            moves+=1
            i, j = self.move(board, i, j)
        return moves

def main():
    checker = Checker()
    board = Board(8, 8)
    board.placePiece(2, 1)
    board.placePiece(0, 3)
    board.placePiece(4, 3)
    board.placePiece(5, 6)
    board.placePiece(4, 2)
    print checker.count(board, 0, 0)

if __name__ == '__main__':
    main()
