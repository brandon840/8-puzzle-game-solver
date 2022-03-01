import copy

# Contains the numbers 1 to 8 with an empty space denoted by x
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class Node:
    def __init__(self, level, grid, solution):
        self.g_score = level
        self.grid = grid
        self.solution = solution

    def get_h_score(self):
        h_score = 0
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid)):
                if self.grid[i][j] != self.solution[i][j]:
                    h_score = h_score + 1

        return h_score

    def get_new_grid(self, row, column, direction):
        temp_grid = copy.deepcopy(self.grid)

        try:
            if direction == UP:
                temp_grid[row][column] = temp_grid[row][column - 1]
                temp_grid[row][column - 1] = "_"

            elif direction == RIGHT:
                temp_grid[row][column] = temp_grid[row + 1][column]
                temp_grid[row + 1][column] = "_"

            elif direction == LEFT:
                temp_grid[row][column] = temp_grid[row - 1][column]
                temp_grid[row - 1][column] = "_"

            elif direction == DOWN:
                temp_grid[row][column] = temp_grid[row][column + 1]
                temp_grid[row][column + 1] = "_"

        except:
            return []

        else:
            return temp_grid

    # WTF
    def get_children(self, level, solution):
        all_children = []
        n = len(self.grid)

        for row in range(0, n):
            for column in range(0, n):
                if self.grid[row][column] == "_":

                    for i in range(0, 4):
                        new_grid = self.get_new_grid(row, column, i)

                        # Non-empty grid, AKA we are able to move the empty space in a certain direction
                        if len(new_grid) != 0:
                            all_children.append(Node(level, new_grid, solution))

        return all_children


class Puzzle:

    def __init__(self):
        self.grid = []
        self.solution = []
        self.nodes = []

    # Create prompt for user and get the starting grid and solution grids
    def prompt(self):
        print("Enter the number of squares in your puzzle (including the empty space)")
        total = int(input())
        print("Please enter the starting position of the puzzle. Using '_' for the empty space")
        print("Example input: ")
        print("1 2 3")
        print("_ 4 5")
        print("6 7 8")

        for i in range(0, int(total ** 0.5)):
            line = input()
            self.grid.append(line.split())

        print("Please enter the end position of the puzzle.")
        for i in range(0, int(total ** 0.5)):
            line = input()
            self.solution.append(line.split())

        print()

    @staticmethod
    def get_best_child(nodes):
        best_score = float('inf')
        best_node = None

        for node in nodes:
            if (node.get_h_score() + node.g_score) < best_score:
                best_score = node.get_h_score() + node.g_score
                best_node = node

        return best_node

    @staticmethod
    def print_step(node):
        for line in node.grid:
            x = " ".join(line)
            print(x)

        print("\n")

    def solve(self):
        self.prompt()
        level = 0
        current_node = Node(level, self.grid, self.solution)

        puzzle_not_solved = True
        while puzzle_not_solved:
            children = current_node.get_children(level+1, self.solution)
            best_child = self.get_best_child(children)  # Get best child by f score
            if best_child.get_h_score() == 0:
                puzzle_not_solved = False

            self.print_step(best_child)
            current_node = best_child
            level=level+1


if __name__ == "__main__":
    p = Puzzle()
    p.solve()
