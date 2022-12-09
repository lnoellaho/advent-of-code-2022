from typing import List
from functools import reduce


class TreeHeightGrid:
    def __init__(self):
        self._row_map = {}
        self._column_map = {}

    @property
    def row_count(self):
        if not hasattr(self, "_row_count"):
            self._row_count = len(self._row_map)
        return self._row_count

    @property
    def column_count(self):
        if not hasattr(self, "_column_count"):
            self._column_count = len(self._column_map)
        return self._column_count

    @property
    def row_edge_ids(self):
        if not hasattr(self, "_row_edge_ids"):
            self._row_edge_ids = [0, self.row_count - 1]
        return self._row_edge_ids

    @property
    def column_edge_ids(self):
        if not hasattr(self, "_column_edge_ids"):
            self._column_edge_ids = [0, self.column_count - 1]
        return self._column_edge_ids

    def get_row(self, row_id: int):
        try:
            return self._row_map[row_id]
        except KeyError:
            raise RowNotFoundError(row_id)

    def get_column(self, column_id: int):
        try:
            return self._column_map[column_id]
        except KeyError:
            raise ColumnNotFoundError(column_id)

    def append_row(self, row_id: int, row: List[int]):
        self._row_map[row_id] = row
        for idx, cell in enumerate(row):
            try:
                self._column_map[idx].append(cell)
            except KeyError:
                self._column_map[idx] = [cell]

    def count_visible_trees(self):
        visible_tree_count = 0

        for row_id in range(0, len(self._row_map)):
            for column_id in range(0, len(self._column_map)):
                if self._is_tree_on_edge(row_id, column_id):
                    visible_tree_count += 1
                    continue

                if self._is_tree_visible_from_one_direction(row_id, column_id):
                    visible_tree_count += 1

        return visible_tree_count

    def find_highest_scenic_score(self):
        highest_scenic_score = 0

        for row_id in range(1, len(self._row_map) - 1):
            for column_id in range(1, len(self._column_map) - 1):
                scenic_score = self._calculate_scenic_score(row_id, column_id)
                if scenic_score > highest_scenic_score:
                    highest_scenic_score = scenic_score

        return highest_scenic_score

    def _calculate_scenic_score(self, row_id, column_id):
        current_tree_height = self.get_row(row_id)[column_id]

        return reduce(
            lambda x, y: x * y,
            [
                self._count_trees_in_view(current_tree_height, tree_range)
                for tree_range in self._get_tree_ranges_surrounding_tree_centerpoint(
                    row_id, column_id
                )
            ],
        )

    def _is_tree_visible_from_one_direction(self, row_id, column_id):
        current_tree_height = self.get_row(row_id)[column_id]

        for tree_range_to_scan in self._get_tree_ranges_surrounding_tree_centerpoint(
            row_id, column_id
        ):
            if self._count_trees_in_view(
                current_tree_height,
                tree_range_to_scan,
                include_last_tree_in_sight=False,
            ) == len(tree_range_to_scan):
                return True

        return False

    def _get_tree_ranges_surrounding_tree_centerpoint(self, row_id, column_id):
        row = self.get_row(row_id)
        column = self.get_column(column_id)

        trees_above = column[row_id - 1 :: -1]
        trees_below = column[row_id + 1 :]
        trees_to_left = row[column_id - 1 :: -1]
        trees_to_right = row[column_id + 1 :]

        return [trees_above, trees_below, trees_to_left, trees_to_right]

    def _count_trees_in_view(
        self,
        current_tree_height,
        adjacent_trees_to_scan,
        include_last_tree_in_sight=True,
    ):
        tree_count = 0
        for tree in adjacent_trees_to_scan:
            if tree >= current_tree_height:
                if include_last_tree_in_sight:
                    tree_count += 1
                break

            tree_count += 1

        return tree_count

    def _is_tree_on_edge(self, row_id, column_id):
        return row_id in self.row_edge_ids or column_id in self.column_edge_ids

    # crude attempt at a different strategy for optimization below
    # works but not sure it's worth it
    # saving a map of the max values as you go through to save on some iterating

    # def count_visible_trees(self):
    #     row_edge_ids = [0, self.row_count - 1]
    #     column_edge_ids = [0, self.column_count - 1]

    #     visible_tree_count = 0
    #     column_max_height_map = {
    #         column_id: {"top": 0, "bottom": max(self.get_column(column_id))}
    #         for column_id, tree in enumerate(self.get_row(0))
    #     }

    #     for row_id, row in self._row_map.items():
    #         max_row_height_to_left = 0
    #         max_row_height_to_right = max(row)
    #         for column_id, tree_height in enumerate(row):
    #             tree_is_visible = False
    #             if column_id in column_edge_ids or row_id in row_edge_ids:
    #                 tree_is_visible = True

    #             if tree_height == column_max_height_map[column_id]["bottom"]:
    #                 trees_to_the_bottom = self.get_column(column_id)[row_id + 1 :]
    #                 if trees_to_the_bottom:
    #                     column_max_height_map[column_id]["bottom"] = max(
    #                         trees_to_the_bottom
    #                     )

    #             if tree_height > column_max_height_map[column_id]["top"]:
    #                 column_max_height_map[column_id]["top"] = tree_height
    #                 tree_is_visible = True
    #             elif tree_height > column_max_height_map[column_id]["bottom"]:
    #                 tree_is_visible = True

    #             if tree_height == max_row_height_to_right:
    #                 trees_to_the_right = row[column_id + 1 :]
    #                 if trees_to_the_right:
    #                     max_row_height_to_right = max(trees_to_the_right)

    #             if tree_height > max_row_height_to_left:
    #                 tree_is_visible = True
    #                 max_row_height_to_left = tree_height
    #             elif tree_height > max_row_height_to_right:
    #                 tree_is_visible = True

    #             if tree_is_visible:
    #                 visible_tree_count += 1

    #     return visible_tree_count


class ColumnNotFoundError(Exception):
    def __init__(self, identifier):
        super(ColumnNotFoundError, self).__init__(
            "Column not found: {}".format(identifier)
        )


class RowNotFoundError(Exception):
    def __init__(self, identifier):
        super(RowNotFoundError, self).__init__("Row not found: {}".format(identifier))
