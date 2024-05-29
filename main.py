from copy import deepcopy

import pdb

def seed(selection: int = 1) -> list[list[list[int]], int, int]:
    if selection == 1:
        return [[[0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0],
                 [0, 1, 1, 1, 0],
                 [0, 0, 1, 1, 0],
                 [0, 0, 1, 0, 0]],
                 5, 5]
    elif selection == 2:
        return [[[0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 1, 1, 1, 1, 0],
                 [0, 0, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 1, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]],
                 7, 10]
    elif selection == 3:
        return [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
                 10, 10]
    elif selection == 4:
        return [[[0, 1, 0],
                 [0, 1, 0],
                 [0, 1, 0]],
                3, 3]
    elif selection == 5:
        return [[[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 1, 1, 0, 0, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                9, 5]

def next_iteration(current_board: list[list[int]], width: int, height: int) -> list[list[int]]:
    next_board: list[list[int]] = [[0 for _ in range(width)] for _ in range(height)]
    i: int = 0
    j: int = 0
    neighbor_count: int = 0
    for row in range(0, height):
        for col in range(0, width):
            neighbor_count = 0
            r = row - 1
            c = col - 1
            # * r and c will be the coordinates (r, c) of the top-left corner
            # * neighbor (could be the cell itself) 
            if r < 0:
                r = 0
            elif r >= height - 1:
                r -= 1
            else:
                pass
            if c < 0:
                c = 0
            elif c >= width - 1:
                c -= 1
            else:
                pass
            j = r
            i = c
            while ((j <= row + 1) and (j < height)):
                i = c
                while ((i <= col + 1) and (i < width)):
                    neighbor_count += current_board[j][i]
                    i += 1
                j += 1
            if (current_board[row][col] == 1):
                neighbor_count -= 1
            if (neighbor_count < 2) or (neighbor_count > 3):
                # * Underpopulation and overpopulation
                next_board[row][col] = 0
            else:
                if neighbor_count == 3:
                    # * Reproduction
                    next_board[row][col] = 1
                elif (neighbor_count == 2) and (current_board[row][col] == 1):
                    # * Lives on to the next generation
                    next_board[row][col] = 1
                elif (neighbor_count == 2) and (current_board[row][col] == 0):
                    next_board[row][col] = 0
            # print(neighbor_count, current_board[row][col], next_board[row][col], "(", row, ",", col, ")", "(", r, ",", c, ")", "(", row + 1, ",", col + 1, ")")
    return next_board

def print_board(board: list[list[int]]) -> None:
    for row in board:
        row = ["⬜" if cell == 1 else "⬛" for cell in row]
        for cell in row:
            print(cell, end="")
        print()
    print()

def main():
    width: int = 0
    height: int = 0
    game_board: list[list[int]] = [[0 for _ in range(width)] for _ in range(height)]
    current_board: list[list[int]] = [[0 for _ in range(width)] for _ in range(height)]
    next_board: list[list[int]] = [[0 for _ in range(width)] for _ in range(height)]

    valid_selection: bool = False
    while not valid_selection:
        try:
            selection: int = int(input("Please insert the starting pattern (1-5): "))
            if selection in [1, 2, 3, 4, 5]:
                valid_selection = True
            else:
                raise ValueError
        except ValueError:
            print("Invalid selection. Please try again.")
    number_of_moves: int = int(input("Please insert the number of moves: "))
    
    game_board, width, height = seed(selection)
    print("Iteration 1")
    print_board(game_board)

    for i in range(0, number_of_moves):
        current_board = deepcopy(game_board)
        next_board = next_iteration(current_board, width, height)
        game_board = deepcopy(next_board)
        print("Iteration", i + 2)
        print_board(game_board)

if __name__ == "__main__":
    main()
