from collections import deque
from util.generate_input_lines import generate_input_lines, generate_list_segments

#             [M] [S] [S]
#         [M] [N] [L] [T] [Q]
# [G]     [P] [C] [F] [G] [T]
# [B]     [J] [D] [P] [V] [F] [F]
# [D]     [D] [G] [C] [Z] [H] [B] [G]
# [C] [G] [Q] [L] [N] [D] [M] [D] [Q]
# [P] [V] [S] [S] [B] [B] [Z] [M] [C]
# [R] [H] [N] [P] [J] [Q] [B] [C] [F]
#  1   2   3   4   5   6   7   8   9

# ['    ', '    ', '    ', '[M] ', '[S] ', '[S] ', '    ', '    ', '   ']
# ['    ', '    ', '[M] ', '[N] ', '[L] ', '[T] ', '[Q] ', '    ', '   ']
# ['[G] ', '    ', '[P] ', '[C] ', '[F] ', '[G] ', '[T] ', '    ', '   ']
# ['[B] ', '    ', '[J] ', '[D] ', '[P] ', '[V] ', '[F] ', '[F] ', '   ']
# ['[D] ', '    ', '[D] ', '[G] ', '[C] ', '[Z] ', '[H] ', '[B] ', '[G]']
# ['[C] ', '[G] ', '[Q] ', '[L] ', '[N] ', '[D] ', '[M] ', '[D] ', '[Q]']
# ['[P] ', '[V] ', '[S] ', '[S] ', '[B] ', '[B] ', '[Z] ', '[M] ', '[C]']
# ['[R] ', '[H] ', '[N] ', '[P] ', '[J] ', '[Q] ', '[B] ', '[C] ', '[F]']
# [' 1  ', ' 2  ', ' 3  ', ' 4  ', ' 5  ', ' 6  ', ' 7  ', ' 8  ', ' 9 ']
# []


def main():
    should_create_stacks = True
    crate_stacks = {}

    for input_line in generate_input_lines(
        "day_5/input.txt", line_transformation_func=lambda x: x.rstrip("\n")
    ):
        if should_create_stacks:
            row = list(generate_list_segments(input_line, segment_size=4))
            print(row)

            if len(row) == 0:
                should_create_stacks = False
                continue

            _add_input_row_to_crate_stacks(row, crate_stacks)

        else:
            number_commands = [
                int(word) for word in input_line.split(" ") if word.isdigit()
            ]

            number_of_crates_to_move = number_commands[0]
            stack_to_move_from = number_commands[1]
            stack_to_move_to = number_commands[2]

            for _ in range(0, number_of_crates_to_move):
                try:
                    moving_crate = crate_stacks[stack_to_move_from].pop()
                    crate_stacks[stack_to_move_to].append(moving_crate)

                except IndexError:
                    pass

    print(crate_stacks)

    crates_on_top = [crate_stacks[idx + 1].pop() for idx in range(0, len(crate_stacks))]
    print("".join(crates_on_top))


def _add_input_row_to_crate_stacks(input_row, crate_stacks):
    for idx, cell in enumerate(input_row):
        stack_number = idx + 1
        crate_label_list = list(filter(str.isalpha, cell))
        crate_label = crate_label_list[0] if crate_label_list else None

        if crate_label:
            try:
                crate_stacks[stack_number].appendleft(crate_label)
            except KeyError:
                crate_stacks[stack_number] = deque([crate_label])


if __name__ == "__main__":
    main()
