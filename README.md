# Game of Life - Advanced Console Version

## Overview

This project is an enhanced Python implementation of Conway's Game of Life, designed with a focus on **customizability**, **optimization**, and expanding upon the features of the original Game of Life. This version allows users to fully control the game's environment, from grid size to the evolution ruleset, all within a terminal-based interface.

## Key Features

### 1. **Highly Customizable Environment**
- **Grid Size**: Users can define the exact number of rows and columns, allowing for a tailored experience that fits any terminal window size.
- **Initialization Options**: Start with a completely random grid or load specific patterns from a file, offering a range of starting scenarios.
- **Speed Control**: Adjust the speed of the simulation to observe the evolution of cells in real-time or slow it down for detailed analysis.
- **Ruleset Flexibility**: The game supports the classic ruleset, with a framework in place to easily introduce custom rules for more complex simulations.

### 2. **Optimized for Performance**
- **Efficient Grid Management**: The game leverages the `numpy` library for efficient grid operations, ensuring smooth performance even on larger grids.
- **Dynamic Terminal Resizing**: The terminal is automatically resized to optimally display the grid, enhancing the visual experience without manual adjustments.
- **Minimal Computational Overhead**: Only essential operations are performed during each generation cycle, reducing unnecessary computations and speeding up the game.

### 3. **Enhanced Features from the Original Game of Life**
- **Visual Output**: The grid is rendered in the terminal with live cells displayed in green (`O`) and dead cells in grey (`.`), providing a clear and visually appealing representation.
- **Interactive Simulation**: After each run, users can save the current state, allowing them to preserve interesting patterns or continue a simulation from a saved point.
- **Pattern File Support**: Users can load and save custom patterns, making it easy to experiment with different initial conditions and share configurations with others.

## Game Ruleset

The evolution of the grid from one generation to the next is governed by the following rules:

1. **Underpopulation**: A live cell with fewer than two living neighbors dies in the next generation.
2. **Equilibrium**: A live cell with two or three living neighbors survives to the next generation.
3. **Overpopulation**: A live cell with more than three living neighbors dies in the next generation.
4. **Reproduction**: A dead cell with exactly three living neighbors becomes a live cell in the next generation.

These rules, applied to every cell on the grid simultaneously, lead to various outcomes such as static patterns, oscillators, or even moving patterns like spaceships. The game evolves until the grid reaches a stable configuration, either becoming static, oscillating, or completely empty.

## Getting Started

### Prerequisites

- **Python 3.x**
- **Numpy Library**

You can install the required library using pip:

```bash
pip install numpy
```
### Running the Game

To launch the game, run the following command:

```bash
python game_of_life.py
```
You'll be guided through several prompts to customize your simulation:

1. **Grid Size**: Define the number of rows (10-60) and columns (10-118).
2. **Speed**: Set the simulation speed in generations per second.
3. **Pattern**: Optionally, load a pattern from a file or generate a random initial grid.
4. **Ruleset**: Choose the ruleset for cell evolution (currently "classic" with options for expansion).
5. **Number of Generations**: Specify how many generations to simulate or run the game endlessly.

### Custom Pattern Files

Pattern files are simple text files where:
- `O` represents a live cell.
- `.` (or any non-`O` character) represents a dead cell.

These files can be easily created or edited, providing a straightforward way to experiment with different starting configurations.

### Interactive Features

- **Save Game State**: After the simulation ends, the current grid can be saved to a file for later use or further experimentation.
- **Replay or Exit**: Users can choose to run the simulation again with the same or modified settings.

## Extending the Game

### Adding Custom Rulesets

To expand the game's possibilities, new rulesets can be added in the `create_next_grid` function. This allows for the exploration of variations on the classic Game of Life rules or entirely new cellular automata behaviors.

### Cross-Platform Support

The game is designed to work across different platforms, with specific adjustments for Windows and Linux systems. If an unsupported platform is detected, the game will provide guidance for manual adjustments.

## Contributing

Contributions are welcome to enhance the game's features, optimize performance further, or introduce new rulesets. Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License.

## Acknowledgments

- **Conway's Game of Life**: The original inspiration, providing a simple yet profound model of cellular automata.
