from creacion_sudoku import Sudoku

# Crear instancia de Sudoku
sudoku = Sudoku()
sudoku.initialize_grid()

# Pedir nivel al usuario
print("Selecciona el nivel de dificultad: easy, medium, hard, expert")
difficulty = input("Nivel: ").lower()

# Generar Sudoku
sudoku.generate_initial_numbers()
sudoku.remove_numbers(difficulty)

# Imprimir Sudoku sin resolver
print("\nSudoku sin resolver:")
sudoku.print_board()

# Resolver Sudoku
if sudoku.solve_sudoku():
    print("\nSudoku resuelto:")
    sudoku.print_board()
else:
    print("\nNo se pudo resolver el Sudoku.")