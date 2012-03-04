'''
Problem Statement is represented by red game pieces and player 2 is represented by black game
pieces.  

There are two types of moves for a game piece.  The first will be referred to
as a simple move.  It involves moving a game piece diagonally 1 space. This
means that the piece would be moved either up 1 space and right 1 space or up 1
space and left 1 space.  Here are examples of a simple move.  ('-' is an
unoccupied space, 'R' is a red piece, 'B' is a black piece, complete board may
not be shown in diagram)


- - - - - - - -        - - - - - - - -  
- - - - - - - -  --->  - - R - - - - -  
- R - - - - - -        - - - - - - - -  
                  or
- - - - - - - -        - - - - - - - -  
- - - - - - - -  --->  R - - - - - - -  
- R - - - - - -        - - - - - - - -  

The second type of move is referred to as a jump.  A jump involves moving over
*one* of the opponents pieces and landing in an empty space.  A jump to the
right would involve a piece moving diagonally two spaces to the right(right two
and up two). Similarly, a jump to the left would involve a piece moving
diagonally two spaces to the left(left two and up two).  See the following
diagrams.

- - - - - - - -        - - - - - - - -  
- - - - - - - -  --->  - - - - R - - -  
- B - B - - - -        - B - B - - - -  
- - R - - - - -        - - - - - - - -  
                  or
- - - - - - - -        - - - - - - - -  
- - - - - - - -  --->  R - - - - - - -  
- B - B - - - -        - B - B - - - -  
- - R - - - - -        - - - - - - - -  

Implement a class Checkers containing a method compute.  compute should return
an int representing the fewest number of moves it will take for player 1 to
move his red piece to the opposite end of the board.  If player 1 cannot get to
the opposite end of the board using the moves described above, compute should
return -1.

DEFINITION
Class Name: Checkers
Method Name: compute
Parameters: String, String[]
Returns: int
Method signature (be sure your method is public): int compute (String startPos,
String[] pieces);

TopCoder will ensure the validity of the inputs.  Inputs are valid if all of
the following criteria are met:
- pieces will contain between 0 and 50, inclusive, elements.
- Each element of pieces will be in the form "column,row" (quotation marks are
for clarity only) where column and row are integers between 0 and 7, inclusive.
- startPos will be in the form "column,row" (quotation marks are for clarity
only) where column and row are integers between 0 and 7, inclusive.
- No two elements of pieces or startPos can have the same "column,row" value
(that is, no two pieces may be placed on the same square of the board).

NOTES
- Consecutive jumps count as 1 move.
- A game piece's location is not restricted the way it is in "real" checkers
(pieces can be placed at or moved to any unoccupied location on the board).
- To successfully perform either type of move, the destination square must be
on the board and not occupied by another piece. 
- Input will be in coordinate format "x,y" (quotation marks are for clarity
only) where the bottom left spot on the board is "0,0", the bottom right spot
on the board is "7,0", the top left is "0,7" and the top right is "7,7".
- The opposite end of the board is defined as the top row of the board,
specifically, any location on the board where the y (row) coordinate is 7.
-  The red piece can only move or jump in the direction of the opposite end of
the board.  For example, each move or jump (including subsequent jumps in the
case of multiple jumps) must have a row value that is greater than that of the
previous position of that piece.

EXAMPLES
1.
        Fig. 1               Fig. 2              Fig. 3              Fig. 4
  7 - - - - - - - -    7 - - - - - - - -   7 - - - - - - - -   7 - - - - - - R -
  6 - - - - - B - -    6 - - - - - B - -   6 - - - - - B - -   6 - - - - - B - -
  5 - - - - - - - -    5 - - - - - - - -   5 - - - - R - - -   5 - - - - - - - -
  4 - - - - - - - -    4 - - - - - R - -   4 - - - - - - - -   4 - - - - - - - -
  3 B - - - B - - -    3 B - - - B - - -   3 B - - - B - - -   3 B - - - B - - -
  2 - - - - B - - -    2 - - - - B - - -   2 - - - - B - - -   2 - - - - B - - -
  1 - - B - - - - -    1 - - B - - - - -   1 - - B - - - - -   1 - - B - - - - -
  0 - R - - - - - -    0 - - - - - - - -   0 - - - - - - - -   0 - - - - - - - -
    0 1 2 3 4 5 6 7      0 1 2 3 4 5 6 7     0 1 2 3 4 5 6 7     0 1 2 3 4 5 6 7

  startPos = "1,0"
  pieces = {"2,1", "0,3", "4,3", "5,6", "4,2"}
  
  Fig. 1: The initial setup of the board.  Move count = 0; 
Fig. 2: The red piece has made a jump from 1,0 to 3,2 and then from 3,2 to
5,4.  Remember, this only counts as a single move.  Move count = 1; 
Fig. 3: The red piece has made a simple move from 5,4 to 4,5.  Move count =
2; 
  Fig. 4: The red piece has jumped from 4,5 to 6,7.  Move count = 3;

  So the output is: 3
Because the fewest number of moves from startPos to the opposite end of the
board is 3. 

2.
  startPos = "4,4"
  pieces = {}
  return: 3  
 
3.
  startPos = "4,4"
  pieces = {"6,6", "5,5", "3,5", "2,6"}
  return: -1 

4.
  startPos = "4,1"
  pieces = {"2,4", "3,4", "4,4", "5,4", "2,6", "3,6", "4,6", "5,6"}
  return: 3 


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