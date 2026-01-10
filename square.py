class Square:

    # Constructor that determines the squares value and status
    # Value is an int which will determine whether or not that square is a bomb (10) and the count it will show
    # Revealed is a boolean which will determine if that square is hidden or revealed
    def __init__(self, value, revealed):
        self.value = value
        self.revealed = revealed

    # Pass in the user selected column and row values, and map them to the proper values for the board array
    # Returns true for a valid move and false for an invalid one
    def transCords(col, row, boardSize):
        col = col - 1
        row = boardSize - row

        if col >= 0 and col < boardSize and row >= 0 and row < boardSize:
            return True
        else:
            return False