from util.generate_input_lines import generate_input_lines
from day_9.common import RopePositionTracker


def main():
    rope_position_tracker = RopePositionTracker([0, 0], [0, 0])
    for rope_head_motion_input in generate_input_lines("day_9/input.txt"):
        rope_head_motion = rope_head_motion_input.split(" ")
        rope_position_tracker.move_head(rope_head_motion[0], int(rope_head_motion[1]))

    print(len(rope_position_tracker.unique_tail_positions))


if __name__ == "__main__":
    main()
