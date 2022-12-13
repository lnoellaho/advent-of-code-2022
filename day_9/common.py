from enum import Enum


class MovementDirection(Enum):
    UP = "U"
    DOWN = "D"
    RIGHT = "R"
    LEFT = "L"


class RopePositionTracker:
    def __init__(self, head_starting_position, tail_starting_position):
        self._current_head_position = head_starting_position
        self._current_tail_position = tail_starting_position
        self.unique_tail_positions = set([tuple(tail_starting_position)])

    def move_head(self, direction, step_count):
        movement_direction = MovementDirection(direction)

        for _ in range(0, step_count):
            match movement_direction:
                case MovementDirection.UP:
                    self._current_head_position[1] += 1
                case MovementDirection.DOWN:
                    self._current_head_position[1] -= 1
                case MovementDirection.LEFT:
                    self._current_head_position[0] -= 1
                case MovementDirection.RIGHT:
                    self._current_head_position[0] += 1
            print("h", self._current_head_position)

            self._move_tail_adjacent_to_head(movement_direction)

    def _move_tail_adjacent_to_head(self, movement_direction):
        if (
            abs(self._current_head_position[0] - self._current_tail_position[0]) > 1
            and abs(self._current_head_position[1] - self._current_tail_position[1])
            == 1
        ) or (
            abs(self._current_head_position[1] - self._current_tail_position[1]) > 1
            and abs(self._current_head_position[0] - self._current_tail_position[0])
            == 1
        ):
            self._move_tail_diagonally(movement_direction)
        elif (
            abs(self._current_head_position[0] - self._current_tail_position[0]) != 1
            and abs(self._current_head_position[1] - self._current_tail_position[1])
            != 1
        ):
            if self._current_head_position != self._current_tail_position:
                self._move_tail_one_position(movement_direction)

        print("t", self._current_tail_position)
        print("_____")
        self.unique_tail_positions.add(tuple(self._current_tail_position))

    def _move_tail_diagonally(self, movement_direction):
        assert isinstance(movement_direction, MovementDirection)
        match movement_direction:
            case MovementDirection.UP:
                self._current_tail_position[0] = self._current_head_position[0]
                self._current_tail_position[1] = self._current_head_position[1] - 1
            case MovementDirection.DOWN:
                self._current_tail_position[0] = self._current_head_position[0]
                self._current_tail_position[1] = self._current_head_position[1] + 1
            case MovementDirection.LEFT:
                self._current_tail_position[0] = self._current_head_position[0] + 1
                self._current_tail_position[1] = self._current_head_position[1]
            case MovementDirection.RIGHT:
                self._current_tail_position[0] = self._current_head_position[0] - 1
                self._current_tail_position[1] = self._current_head_position[1]

    def _move_tail_one_position(self, movement_direction):
        assert isinstance(movement_direction, MovementDirection)

        match movement_direction:
            case MovementDirection.UP:
                self._current_tail_position[1] += 1
            case MovementDirection.DOWN:
                self._current_tail_position[1] -= 1
            case MovementDirection.LEFT:
                self._current_tail_position[0] -= 1
            case MovementDirection.RIGHT:
                self._current_tail_position[0] += 1
