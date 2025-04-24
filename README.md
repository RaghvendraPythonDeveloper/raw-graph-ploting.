
# x = y Graph Plotting

## Overview

This project allows you to plot a simple **x = y** diagonal graph in the terminal or save it as a `.txt` file. The graph is generated using basic Python logic without relying on any external libraries or tools. It showcases how to plot basic graphs using only standard Python functions.

## Features

- Plots a graph of the equation **x = y**.
- Graph is printed in a text-based format.
- Can save the output to a `.txt` file.
- Provides a simple way to understand graph plotting logic.

## How It Works

- The graph plots points where the **x-coordinate is equal to the y-coordinate**.
- You can specify the size of the graph by adjusting the **x-axis** and **y-axis** values.
- The graph will be printed in the terminal or written to a text file.

## Installation

No installation is needed. Just clone this repository and run the code using Python.

```bash
git clone <repository-url>
cd <repository-folder>
python x_y_graph.py
```

## Usage

To create the graph, simply run the code. By default, the graph will be saved in a file named `graph.txt`. You can also modify the code to customize the axis size.

Example:

```python
def printing():
    x_axis = 20
    y_axis = 20
    with open("graph.txt", "w") as file:
        for y in range(0, y_axis + 1):
            for x in range(0, x_axis + 1):
                if y == x:
                    file.write("*")
                    break
                else:
                    file.write(" ")
            file.write("\n")
```

This will plot a simple diagonal line from **x = 0** to **x = y = 20**.

## License

This project is open-source and free to use. Feel free to modify and contribute!
