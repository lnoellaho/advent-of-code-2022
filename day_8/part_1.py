from util.generate_input_lines import generate_input_lines
from day_8.common import TreeGrid


def main():
    tree_grid = TreeGrid()
    for row_idx, tree_row_input in enumerate(generate_input_lines("day_8/input.txt")):
        tree_grid.append_row(
            row_idx, [int(tree_height) for tree_height in list(tree_row_input)]
        )

    
    visible_tree_count = tree_grid.count_visible_trees()

    print(tree_grid.__dict__)

    print(visible_tree_count)


if __name__ == "__main__":
    main()
