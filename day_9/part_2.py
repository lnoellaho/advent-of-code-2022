import sys
import os

current_loc = os.path.realpath(__file__)
parent_dir = os.path.dirname(os.path.dirname(current_loc))
sys.path.append(parent_dir)

from util.generate_input_lines import generate_input_lines
from enum import Enum


class MovementDirection(Enum):
    UP = "U"
    DOWN = "D"
    RIGHT = "R"
    LEFT = "L"


class RopePositionTracker:
    def __init__(self, knot_count):
        # self._current_head_position = head_starting_position
        # self._current_tail_position = tail_starting_position

        self._knot_positions = {knot_id: [0, 0] for knot_id in range(0, knot_count)}
        self.unique_tail_positions = set([tuple(self._knot_positions[knot_count - 1])])

    def move_rope(self, direction, step_count):
        movement_direction = MovementDirection(direction)
        print(direction, step_count)
        for _ in range(0, step_count):
            match movement_direction:
                case MovementDirection.UP:
                    self._knot_positions[0][1] += 1
                case MovementDirection.DOWN:
                    self._knot_positions[0][1] -= 1
                case MovementDirection.LEFT:
                    self._knot_positions[0][0] -= 1
                case MovementDirection.RIGHT:
                    self._knot_positions[0][0] += 1
            print("h", self._knot_positions[0])

            for next_knot_id in range(1, len(self._knot_positions)):
                self._move_next_knot_adjacent_to_current_knot(
                    next_knot_id - 1, next_knot_id, movement_direction
                )
                if next_knot_id == len(self._knot_positions) - 1:
                    self.unique_tail_positions.add(
                        tuple(self._knot_positions[next_knot_id])
                    )
                if next_knot_id < 4:
                    print(next_knot_id, self._knot_positions[next_knot_id])
                    print("_____")

    # R 4
    # U 4
    # L 3
    # D 1
    # R 4
    # D 1
    # L 5
    # R 2
    def _move_next_knot_adjacent_to_current_knot(
        self, current_knot_id, next_knot_id, movement_direction
    ):
        if (
            abs(
                self._knot_positions[current_knot_id][0]
                - self._knot_positions[next_knot_id][0]
            )
            > 1
            and abs(
                self._knot_positions[current_knot_id][1]
                - self._knot_positions[next_knot_id][1]
            )
            == 1
        ) or (
            abs(
                self._knot_positions[current_knot_id][1]
                - self._knot_positions[next_knot_id][1]
            )
            > 1
            and abs(
                self._knot_positions[current_knot_id][0]
                - self._knot_positions[next_knot_id][0]
            )
            == 1
        ):
            self._move_next_knot_diagonally(
                current_knot_id, next_knot_id, movement_direction
            )
        elif (
            abs(
                self._knot_positions[current_knot_id][0]
                - self._knot_positions[next_knot_id][0]
            )
            != 1
            and abs(
                self._knot_positions[current_knot_id][1]
                - self._knot_positions[next_knot_id][1]
            )
            != 1
        ):
            if (
                self._knot_positions[current_knot_id]
                != self._knot_positions[next_knot_id]
            ):
                self._move_next_knot_one_position(next_knot_id, movement_direction)

    def _move_next_knot_diagonally(
        self, current_knot_id, next_knot_id, movement_direction
    ):
        assert isinstance(movement_direction, MovementDirection)
        match movement_direction:
            case MovementDirection.UP:
                self._knot_positions[next_knot_id][0] = self._knot_positions[
                    current_knot_id
                ][0]
                self._knot_positions[next_knot_id][1] = (
                    self._knot_positions[current_knot_id][1] - 1
                )
            case MovementDirection.DOWN:
                self._knot_positions[next_knot_id][0] = self._knot_positions[
                    current_knot_id
                ][0]
                self._knot_positions[next_knot_id][1] = (
                    self._knot_positions[current_knot_id][1] + 1
                )
            case MovementDirection.LEFT:
                self._knot_positions[next_knot_id][0] = (
                    self._knot_positions[current_knot_id][0] + 1
                )
                self._knot_positions[next_knot_id][1] = self._knot_positions[
                    current_knot_id
                ][1]
            case MovementDirection.RIGHT:
                self._knot_positions[next_knot_id][0] = (
                    self._knot_positions[current_knot_id][0] - 1
                )
                self._knot_positions[next_knot_id][1] = self._knot_positions[
                    current_knot_id
                ][1]

    def _move_next_knot_one_position(self, next_knot_id, movement_direction):
        assert isinstance(movement_direction, MovementDirection)

        match movement_direction:
            case MovementDirection.UP:
                self._knot_positions[next_knot_id][1] += 1
            case MovementDirection.DOWN:
                self._knot_positions[next_knot_id][1] -= 1
            case MovementDirection.LEFT:
                self._knot_positions[next_knot_id][0] -= 1
            case MovementDirection.RIGHT:
                self._knot_positions[next_knot_id][0] += 1


def main():
    rope_position_tracker = RopePositionTracker(10)
    for rope_head_motion_input in generate_input_lines("day_9/input.txt"):
        rope_head_motion = rope_head_motion_input.split(" ")
        rope_position_tracker.move_rope(rope_head_motion[0], int(rope_head_motion[1]))

    print(rope_position_tracker.unique_tail_positions)


if __name__ == "__main__":
    main()
