class Queen:
    def __init__(self, row, column):
        if (row < 0): raise ValueError("row not positive")
        if (row > 7): raise ValueError("row not on board")
        if (column < 0): raise ValueError("column not positive")
        if (column > 7): raise ValueError("column not on board")
        self.row = row
        self.column = column
    def can_attack(self, queen):
        if (self.row == queen.row and self.column == queen.column):
            raise ValueError("Invalid queen position: both queens in the same square")
        return (self.row == queen.row
            or self.column == queen.column
            or abs(self.row - queen.row) == abs(self.column - queen.column))
    
if __name__ == "__main__":
    queen1 = Queen(2, 4)
    print(queen1.can_attack(Queen(2, 6)))