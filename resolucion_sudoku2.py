import random

def generate_sudoku():
    base  = 3
    side  = base*base

    def pattern(r,c): return (base*(r%base)+r//base+c)%side

    def shuffle(s): return random.sample(s,len(s)) 
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

    return board

def remove_elements(board, remove_count):
    for _ in range(remove_count):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0

def print_sudoku(board):
    for row in board:
        print(" ".join(map(str, row)))

def create_sudoku():
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

    sudoku_board = generate_sudoku()
    remove_elements(sudoku_board, remove_count)

    print("Sudoku incompleto:")
    print_sudoku(sudoku_board)
    print("\nSudoku completo:")
    print_sudoku(generate_sudoku())

# Ejemplo de uso
create_sudoku()

