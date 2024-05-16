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

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

    squares = side*side
    empties = squares * 3//4
    for p in random.sample(range(squares),empties):
        board[p//side][p%side] = 0

    return board

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num or \
                board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
            return False
    return True

def remove_cells(board, remove_count):
    cells_removed = 0
    while cells_removed < remove_count:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            cells_removed += 1

def print_sudoku(board):
    for row in board:
        print(" ".join(map(str, row)))

def main():
    difficulty = input("Selecciona el nivel de dificultad (easy, medium, hard, expert): ").lower()
    if difficulty not in ["easy", "medium", "hard", "expert"]:
        difficulty = "medium"  # Por defecto, medio

    if difficulty == "easy":
        remove_count = random.randint(45, 55)
    elif difficulty == "medium":
        remove_count = random.randint(55, 60)
    elif difficulty == "hard":
        remove_count = random.randint(60, 65)
    elif difficulty == "expert":
        remove_count = random.randint(65, 70)

    sudoku_board = generate_sudoku()
    remove_cells(sudoku_board, remove_count)
    print("Sudoku generado:")
    print_sudoku(sudoku_board)

    solve_sudoku(sudoku_board)
    print("\nSudoku resuelto parcialmente:")
    print_sudoku(sudoku_board)

if __name__ == "__main__":
    main()
