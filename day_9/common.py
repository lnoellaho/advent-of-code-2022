from enum import Enum


class MovementDirection(Enum):
    UP = "U"
    DOWN = "D"
    RIGHT = "R"
    LEFT = "L"


class RopePositionTracker:
    def __init__(self, knot_count=2):
        self._knot_positions = {knot_id: [0, 0] for knot_id in range(0, knot_count)}
        self.unique_tail_positions = set([tuple(self._knot_positions[knot_count - 1])])

    def move_rope(self, direction, step_count):
        movement_direction = MovementDirection(direction)

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

            for current_knot_id in range(1, len(self._knot_positions)):
                self._move_knot_adjacent_to_previous_knot(
                    current_knot_id - 1, current_knot_id
                )
                if current_knot_id == len(self._knot_positions) - 1:
                    self.unique_tail_positions.add(
                        tuple(self._knot_positions[current_knot_id])
                    )

    def _move_knot_adjacent_to_previous_knot(self, previous_knot_id, current_knot_id):
        previous_knot_x = self._knot_positions[previous_knot_id][0]
        previous_knot_y = self._knot_positions[previous_knot_id][1]
        current_knot_x = self._knot_positions[current_knot_id][0]
        current_knot_y = self._knot_positions[current_knot_id][1]

        if (abs(previous_knot_x - current_knot_x) > 1) or (
            abs(previous_knot_y - current_knot_y) > 1
        ):
            if previous_knot_x > current_knot_x:
                self._knot_positions[current_knot_id][0] += 1

            if previous_knot_x < current_knot_x:
                self._knot_positions[current_knot_id][0] -= 1

            if previous_knot_y > current_knot_y:
                self._knot_positions[current_knot_id][1] += 1

            if previous_knot_y < current_knot_y:
                self._knot_positions[current_knot_id][1] -= 1


# part 1 solution before part 2 came along

# class RopePositionTracker:
#     def __init__(self, head_starting_position, tail_starting_position):
#         self._current_head_position = head_starting_position
#         self._current_tail_position = tail_starting_position
#         self.unique_tail_positions = set([tuple(tail_starting_position)])

#     def move_head(self, direction, step_count):
#         movement_direction = MovementDirection(direction)

#         for _ in range(0, step_count):
#             match movement_direction:
#                 case MovementDirection.UP:
#                     self._current_head_position[1] += 1
#                 case MovementDirection.DOWN:
#                     self._current_head_position[1] -= 1
#                 case MovementDirection.LEFT:
#                     self._current_head_position[0] -= 1
#                 case MovementDirection.RIGHT:
#                     self._current_head_position[0] += 1
#             print("h", self._current_head_position)

#             self._move_tail_adjacent_to_head(movement_direction)

#     def _move_tail_adjacent_to_head(self, movement_direction):
#         if (
#             abs(self._current_head_position[0] - self._current_tail_position[0]) > 1
#             and abs(self._current_head_position[1] - self._current_tail_position[1])
#             == 1
#         ) or (
#             abs(self._current_head_position[1] - self._current_tail_position[1]) > 1
#             and abs(self._current_head_position[0] - self._current_tail_position[0])
#             == 1
#         ):
#             self._move_tail_diagonally(movement_direction)
#         elif (
#             abs(self._current_head_position[0] - self._current_tail_position[0]) != 1
#             and abs(self._current_head_position[1] - self._current_tail_position[1])
#             != 1
#         ):
#             if self._current_head_position != self._current_tail_position:
#                 self._move_tail_one_position(movement_direction)

#         print("t", self._current_tail_position)
#         print("_____")
#         self.unique_tail_positions.add(tuple(self._current_tail_position))

#     def _move_tail_diagonally(self, movement_direction):
#         assert isinstance(movement_direction, MovementDirection)
#         match movement_direction:
#             case MovementDirection.UP:
#                 self._current_tail_position[0] = self._current_head_position[0]
#                 self._current_tail_position[1] = self._current_head_position[1] - 1
#             case MovementDirection.DOWN:
#                 self._current_tail_position[0] = self._current_head_position[0]
#                 self._current_tail_position[1] = self._current_head_position[1] + 1
#             case MovementDirection.LEFT:
#                 self._current_tail_position[0] = self._current_head_position[0] + 1
#                 self._current_tail_position[1] = self._current_head_position[1]
#             case MovementDirection.RIGHT:
#                 self._current_tail_position[0] = self._current_head_position[0] - 1
#                 self._current_tail_position[1] = self._current_head_position[1]

#     def _move_tail_one_position(self, movement_direction):
#         assert isinstance(movement_direction, MovementDirection)

#         match movement_direction:
#             case MovementDirection.UP:
#                 self._current_tail_position[1] += 1
#             case MovementDirection.DOWN:
#                 self._current_tail_position[1] -= 1
#             case MovementDirection.LEFT:
#                 self._current_tail_position[0] -= 1
#             case MovementDirection.RIGHT:
#                 self._current_tail_position[0] += 1
