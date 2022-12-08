from typing import List


class TreeHeightGrid:
    def __init__(self):
        self._row_map = {}
        self._column_map = {}

    @property
    def row_count(self):
        return len(self._row_map)

    @property
    def column_count(self):
        return len(self._column_map)

    def get_row(self, row_id: int):
        try:
            return self._row_map[row_id]
        except KeyError:
            raise RowNotFoundError(row_id)

    def get_column(self, column_id: int):
        try:
            self._column_map[column_id]
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
        row_edge_ids = [0, self.row_count - 1]
        column_edge_ids = [0, self.column_count - 1]

        visible_tree_count = 0

        for row_id, row in self._row_map.items():
            if row_id in row_edge_ids:
                visible_tree_count += len(row)
                continue
            
            max_height_to_left = 0
            max_height_to_right = max(row)
            for column_id, tree_height in enumerate(row):
                if column_id in column_edge_ids:
                    visible_tree_count += 1
                    continue

    def _is_tree_visible_laterally(self, tree_height, row_id, row):

        

    def _is_tree_visible_vertically(self):
        pass


class TreeRow:
    def __init__(self):
        self._column_map


class ColumnNotFoundError(Exception):
    def __init__(self, identifier):
        super(ColumnNotFoundError, self).__init__(
            "Column not found: {}".format(identifier)
        )


class RowNotFoundError(Exception):
    def __init__(self, identifier):
        super(RowNotFoundError, self).__init__("Row not found: {}".format(identifier))
