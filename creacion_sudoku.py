import random

class Sudoku:
    def __init__(self):
        self.board = [[0]*9 for _ in range(9)]

    def initialize_grid(self):
        # Inicialización de la cuadrícula
        self.board = [[0]*9 for _ in range(9)]

    def generate_initial_numbers(self):
        # Generación de números iniciales
        for _ in range(17):  # Número mínimo de pistas para garantizar una única solución
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            num = random.randint(1, 9)
            if self.is_valid_move(row, col, num):
                self.board[row][col] = num

    def solve_sudoku(self):
        # Backtracking (vuelta atrás)
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True
        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid_move(row, col, num):
                self.board[row][col] = num
                if self.solve_sudoku():
                    return True
                self.board[row][col] = 0
        return False

    def verify_unique_solution(self):
        # Verificación de solución única
        original_board = [row[:] for row in self.board]
        if not self.solve_sudoku():
            return False
        self.board = original_board
        return True

    def remove_numbers(self, difficulty):
        # Eliminación de números
        if difficulty == "easy":
            remove_count = random.randint(45, 55)
        elif difficulty == "medium":
            remove_count = random.randint(55, 60)
        elif difficulty == "hard":
            remove_count = random.randint(60, 65)
        elif difficulty == "expert":
            remove_count = random.randint(65, 70)
        else:
            remove_count = random.randint(55, 60)  # Por defecto, medio
        cells = [(row, col) for row in range(9) for col in range(9)]
        random.shuffle(cells)
        for _ in range(remove_count):
            row, col = cells.pop()
            self.board[row][col] = 0

    def is_valid_move(self, row, col, num):
        # Verificación de validez
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
        # Encontrar celda vacía
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def print_board(self):
        # Imprimir tablero
        for row in self.board:
            print(row)

# Ejemplo de uso
sudoku = Sudoku()
sudoku.initialize_grid()
sudoku.generate_initial_numbers()
sudoku.solve_sudoku()
sudoku.remove_numbers("medium")
sudoku.print_board()

print("")

sudoku1 = Sudoku()
sudoku1.initialize_grid()
sudoku1.generate_initial_numbers()
sudoku1.solve_sudoku()
sudoku1.remove_numbers("expert")
sudoku1.print_board()
