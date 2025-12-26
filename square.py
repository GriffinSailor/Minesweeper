class Square:

    # Constructor that determines the squares value and status
    # Value is an int which will determine whether or not that square is a bomb (10) and the count it will show
    # Revealed is a boolean which will determine if that square is hidden or revealed
    def __init__(self, value, revealed):
        self.value = value
        self.revealed = revealed

    # Extends a list of coordinates with those of the squares that touch the given x and y values
    def connectingSquares(x, y, connectedSquares):
        # x - 1, y + 1
        if (x - 1, y + 1) not in connectedSquares:
            connectedSquares.append((x - 1, y + 1))
        # x, y + 1
        if (x, y + 1) not in connectedSquares:
            connectedSquares.append((x, y + 1))
        # x + 1, y + 1
        if (x + 1, y + 1) not in connectedSquares:
            connectedSquares.append((x + 1, y + 1))
        # x - 1, y
        if (x - 1, y) not in connectedSquares:
            connectedSquares.append((x - 1, y))
        # x + 1, y
        if (x + 1, y) not in connectedSquares:
            connectedSquares.append((x + 1, y))
        # x - 1, y - 1
        if (x - 1, y - 1) not in connectedSquares:
            connectedSquares.append((x - 1, y - 1))
        # x, y - 1
        if (x, y - 1) not in connectedSquares:
            connectedSquares.append((x, y - 1))
        # x + 1, y - 1
        if (x + 1, y - 1) not in connectedSquares:
            connectedSquares.append((x + 1, y - 1))
