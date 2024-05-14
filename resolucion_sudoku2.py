from collections import deque

class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def solve_sudoku(self):
        queue = deque([(self.board, 0, 0)])
        while queue:
            board, row, col = queue.popleft()
            if row == 9:  # Si hemos llegado al final, hemos resuelto el Sudoku
                return board
            if board[row][col] == 0:  # Si la celda está vacía, intentamos valores
                for num in range(1, 10):
                    if self.is_valid_move(board, row, col, num):
                        board[row][col] = num
                        queue.append((board.copy(), row + (col + 1) // 9, (col + 1) % 9))
                        board[row][col] = 0  # Deshacer el movimiento
                return None  # Si no hay ningún número válido para esta celda, el Sudoku no tiene solución
            else:
                queue.append((board.copy(), row + (col + 1) // 9, (col + 1) % 9))
        return None  # Si no quedan celdas por revisar, el Sudoku no tiene solución

    def is_valid_move(self, board, row, col, num):
        # Verificar si el número es válido en la fila, columna y cuadrante
        return all([
            num != board[row][j] for j in range(9)],  # Verificar fila
            num != board[i][col] for i in range(9)],  # Verificar columna
            num != board[3 * (row // 3) + i][3 * (col // 3) + j] for i in range(3) for j in range(3)  # Verificar cuadrante
            ])

# Ejemplo de uso
initial_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solver = SudokuSolver(initial_board)
solution = solver.solve_sudoku()

if solution:
    print("Sudoku resuelto:")
    for row in solution:
        print(row)
else:
    print("No se pudo resolver el Sudoku.")
