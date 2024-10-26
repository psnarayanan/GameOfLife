import time
import os
import random
import sys
import numpy as np

def clear_screen():
    if sys.platform.startswith('win'):
        os.system("cls")
    elif sys.platform.startswith('linux'):
        os.system("clear")
    else:
        print("OS Error. Please open a github issue.\n\r")

def create_initial_grid(rows, cols, pattern=None):
    if pattern:
        return load_pattern(pattern, rows, cols)
    return np.random.choice([0, 1], size=(rows, cols), p=[0.8, 0.2])

def load_pattern(pattern, rows, cols):
    grid = np.zeros((rows, cols), dtype=int)
    with open(pattern, 'r') as file:
        for r, line in enumerate(file):
            for c, char in enumerate(line.strip()):
                if r < rows and c < cols:
                    grid[r][c] = 1 if char == 'O' else 0
    return grid

def save_grid(grid, filename):
    with open(filename, 'w') as file:
        for row in grid:
            file.write(''.join('O' if cell else '.' for cell in row) + '\n')

def print_grid(rows, cols, grid, generation, live_cells, dead_cells):
    clear_screen()
    output_str = f"Generation {generation} - Live Cells: {live_cells}, Dead Cells: {dead_cells}, Density: {live_cells / (rows * cols):.2f}\n\r"
    output_str += "\n\r".join(" ".join("\033[92mO\033[0m" if cell else "\033[90m.\033[0m" for cell in row) for row in grid)
    print(output_str, end=" ")

def create_next_grid(rows, cols, grid, next_grid, ruleset):
    neighbors = sum(np.roll(np.roll(grid, i, 0), j, 1) for i in (-1, 0, 1) for j in (-1, 0, 1) if (i != 0 or j != 0))
    if ruleset == "classic":
        next_grid[:] = np.where((neighbors == 3) | ((grid == 1) & (neighbors == 2)), 1, 0)
    # Add more rulesets here

def grid_changing(grid, next_grid):
    return not np.array_equal(grid, next_grid)

def get_integer_value(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            print(f"Input was not inside the bounds (value <= {low} or value >= {high}).")
        except ValueError:
            print("Input was not a valid integer value.")

def resize_terminal(rows, cols):
    cols = max(cols, 32)
    if sys.platform.startswith('win'):
        os.system(f"mode con: cols={cols * 2} lines={rows + 5}")
    elif sys.platform.startswith('linux'):
        sys.stdout.write(f"\x1b[8;{rows + 3};{cols * 2}t")
    else:
        print("Terminal Resize Failed. Please open a github issue.\n\r")

def run_game():
    clear_screen()
    rows = get_integer_value("Enter the number of rows (10-60): ", 10, 60)
    clear_screen()
    cols = get_integer_value("Enter the number of cols (10-118): ", 10, 118)
    speed = float(input("Enter the speed (generations per second): "))
    resize_terminal(rows, cols)

    pattern = input("Enter the pattern file name (or press Enter for random): ").strip()
    pattern = pattern if pattern else None

    current_generation = create_initial_grid(rows, cols, pattern)
    next_generation = np.zeros((rows, cols), dtype=int)

    ruleset = input("Enter the ruleset (classic): ").strip()
    ruleset = ruleset if ruleset else "classic"

    generations_input = input("Enter the number of generations (or -1 for endless): ").strip()
    generations = int(generations_input) if generations_input.isdigit() else -1

    while True:
        for gen in range(1, generations + 1) if generations != -1 else iter(int, 1):
            live_cells = np.sum(current_generation)
            dead_cells = rows * cols - live_cells
            if not grid_changing(current_generation, next_generation):
                break
            print_grid(rows, cols, current_generation, gen, live_cells, dead_cells)
            create_next_grid(rows, cols, current_generation, next_generation, ruleset)
            time.sleep(1 / speed)
            current_generation, next_generation = next_generation, current_generation

        live_cells = np.sum(current_generation)
        dead_cells = rows * cols - live_cells
        print_grid(rows, cols, current_generation, gen, live_cells, dead_cells)
        save_option = input("Save the current state? (y/n): ").strip().lower()
        if save_option == 'y':
            filename = input("Enter the filename to save: ").strip()
            save_grid(current_generation, filename)
        
        run_again = input("<Enter> to exit or r to run again: ").strip().lower()
        if run_again != 'r':
            break

if __name__ == "__main__":
    run = "r"
    while run == "r":
        run = run_game()