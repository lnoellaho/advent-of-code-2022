from util.generate_input_lines import generate_input_lines
from day_8.common import TreeHeightGrid


def main():
    tree_grid = TreeHeightGrid()

    for row_idx, tree_row_input in enumerate(generate_input_lines("day_8/input.txt")):
        tree_grid.append_row(
            row_idx, [int(tree_height) for tree_height in list(tree_row_input)]
        )

    visible_tree_count = tree_grid.count_visible_trees()

    print(visible_tree_count)
    # answer: 1736


if __name__ == "__main__":
    main()
