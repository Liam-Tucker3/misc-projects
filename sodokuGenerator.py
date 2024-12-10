import random

def is_valid(board, row, col, num):
    # Check if `num` can be placed at board[row][col]
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    box_row, box_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
    return True

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

def generate_complete_sudoku():
    board = [[0] * 9 for _ in range(9)]
    solve_sudoku(board)
    return board

def generate_sudoku_with_clues(clue_positions):
    # Generate the full solved Sudoku board
    solved_board = generate_complete_sudoku()
    # Create a puzzle with only the clues
    puzzle = [[0] * 9 for _ in range(9)]
    for row, col in clue_positions:
        puzzle[row][col] = solved_board[row][col]
    return solved_board, puzzle

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def scramble_board(board, seed):
    if seed is not None:
        random.seed(seed)
    # Generate a random mapping of digits 1-9
    digits = list(range(1, 10))
    scrambled_digits = digits[:]
    random.shuffle(scrambled_digits)
    digit_mapping = {original: scrambled for original, scrambled in zip(digits, scrambled_digits)}

    # Apply the mapping to the board
    scrambled_board = [
        [digit_mapping[num] if num != 0 else 0 for num in row] for row in board
    ]
    return scrambled_board

# Example usage
clue_positions = [(1, 1), (2, 1), (0, 4), (2, 4), (1, 7), (1, 8), (3, 1), (4, 2), (5, 1), (4, 5), (3, 7), (4, 7), (7, 0), (7, 2), (6, 3), (7, 3), (8, 3), (6, 5), (7, 5), (8, 5), (7, 8)]
solved_board, sudoku_puzzle = generate_sudoku_with_clues(clue_positions)
scrambled_board, scrambled_puzzle = scramble_board(solved_board, seed=1210), scramble_board(sudoku_puzzle, seed=1210)

print("Generated Sudoku Puzzle:")
print_board(scrambled_puzzle)

print("\nSolved Sudoku Board:")
print_board(scrambled_board)
