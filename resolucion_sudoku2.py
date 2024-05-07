from creacion_sudoku import Sudoku

def main():
    sudoku = Sudoku()
    sudoku.initialize_grid()
    
    difficulty = input("Elige el nivel de dificultad (easy, medium, hard, expert): ").lower()
    while difficulty not in ["easy", "medium", "hard", "expert"]:
        print("Nivel de dificultad no válido.")
        difficulty = input("Por favor, elige un nivel de dificultad válido (easy, medium, hard, expert): ").lower()
    
    sudoku.generate_initial_numbers()
    sudoku.solve_sudoku()
    sudoku.remove_numbers(difficulty)
    sudoku.print_board()
    
main()
