class Queen:
    def __init__(self, row: int, column: int):
        if row < 0:
            raise ValueError("row not positive")
        if column < 0:
            raise ValueError("column not positive")
        if row >= 8 or row < 0:
            raise ValueError("row not on board")
        if column >= 8 or column < 0:
            raise ValueError("column not on board")


        self.row = row
        self.column = column

    def can_attack(self, another_queen: "Queen") -> bool:
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        
        if self.row == another_queen.row:
            return True
        
        if self.column == another_queen.column:
            return True
        
        row = self.row
        column = self.column

        #evalúo la izquierda hacia arriba
        while row > 0 and column > 0:
            row -= 1
            column -= 1
            if row == another_queen.row and column == another_queen.column:
                return True
            
        row = self.row
        column = self.column

        #evalúo la izquierda hacia abajo
        while row < 8 and column > 0:
            row += 1
            column -= 1
            if row == another_queen.row and column == another_queen.column:
                return True
            
        row = self.row
        column = self.column

        #evalúo la derecha hacia arriba
        while row > 0 and column < 8:
            row -= 1
            column += 1
            if row == another_queen.row and column == another_queen.column:
                return True
        
        row = self.row
        column = self.column

        #evalúo la derecha hacia abajo
        while row < 8 and column < 8:
            row += 1
            column += 1
            if row == another_queen.row and column == another_queen.column:
                return True
            
        return False


if __name__ == "__main__":
    queen1 = Queen(2, 2)
    print(queen1.can_attack(Queen(0, 4)))