from creacion_sudoku import Sudoku


class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def solve(self):
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True
        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid_move(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False

    def is_valid_move(self, row, col, num):
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False
        return True

    def find_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None
    

def main():
    sudoku = Sudoku()
    sudoku.initialize_grid()
    
    difficulty = input("Elige el nivel de dificultad (easy, medium, hard, expert): ").lower()
    while difficulty not in ["easy", "medium", "hard", "expert"]:
        print("Nivel de dificultad no válido.")
        difficulty = input("Por favor, elige un nivel de dificultad válido (easy, medium, hard, expert): ").lower()
    
    sudoku.generate_initial_numbers()
    solver = SudokuSolver(sudoku.board)
    solver.solve()
    
    solved_board = solver.board
    sudoku.print_board()  
    print("Sudoku resuelto:")
    sudoku.print_board(solved_board)  

main()
