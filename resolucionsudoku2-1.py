import random

class Sudoku:
    def __init__(self):
        self.board = []

    def generate_sudoku(self):
        base = 3
        side = base * base

        def pattern(r, c): 
            return (base * (r % base) + r // base + c) % side

        def shuffle(s): 
            return random.sample(s, len(s))

        rBase = range(base)
        rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
        cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
        nums = shuffle(range(1, base * base + 1))

        self.board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    def remove_elements(self, remove_count):
        for _ in range(remove_count):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            while self.board[row][col] == 0:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
            self.board[row][col] = 0

    def print_sudoku(self):
        for row in self.board:
            print(" ".join(map(str, row)))

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)  # row, col
        return None

    def is_valid(self, num, pos):
        # Check row
        for i in range(9):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(9):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board[i][j] == num and (i, j) != pos:
                    return False

        return True

    def solve_sudoku_backtracking(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.is_valid(i, (row, col)):
                self.board[row][col] = i

                if self.solve_sudoku_backtracking():
                    return True

                self.board[row][col] = 0

        return False

    def solve_sudoku_bruteforce(self):
        def is_valid_board(board):
            def is_valid_block(block):
                block = [num for num in block if num != 0]
                return len(block) == len(set(block))

            for i in range(9):
                if not is_valid_block([board[i][j] for j in range(9)]):
                    return False
                if not is_valid_block([board[j][i] for j in range(9)]):
                    return False

            for i in range(3):
                for j in range(3):
                    if not is_valid_block(
                        [board[m][n] for m in range(i * 3, i * 3 + 3) for n in range(j * 3, j * 3 + 3)]
                    ):
                        return False

            return True

        def solve_board(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == 0:
                        for num in range(1, 10):
                            board[i][j] = num
                            if is_valid_board(board) and solve_board(board):
                                return True
                            board[i][j] = 0
                        return False
            return True

        solve_board(self.board)

    def create_sudoku(self):
        difficulty = input("Elige el nivel de dificultad (easy, medium, hard, expert): ")
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

        self.generate_sudoku()
        print("Sudoku completo:")
        self.print_sudoku()
        
        self.remove_elements(remove_count)
        print("\nSudoku incompleto:")
        self.print_sudoku()

# Ejemplo de uso
sudoku_game = Sudoku()
sudoku_game.create_sudoku()

print("\nResolviendo Sudoku con backtracking:")
if sudoku_game.solve_sudoku_backtracking():
    sudoku_game.print_sudoku()
else:
    print("No se puede resolver el Sudoku con backtracking.")

sudoku_game = Sudoku()
sudoku_game.create_sudoku()

print("\nResolviendo Sudoku con fuerza bruta:")
sudoku_game.solve_sudoku_bruteforce()
sudoku_game.print_sudoku()
