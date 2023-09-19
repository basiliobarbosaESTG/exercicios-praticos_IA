class DipoleAction:
    """
    a Dipole action is simple - it only takes the value of the column to play
    """
    __col: int
    __row: int

    def __init__(self, row:int, col: int, is_pass=False):
        self.__row = row
        self.__col = col
        self.__is_pass = is_pass

    def is_pass(self):
        return self.__is_pass

    def get_col(self):
        return self.__col
    
    def get_row(self):
        return self.__row
