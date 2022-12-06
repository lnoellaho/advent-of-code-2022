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
            
            for idx, cell in enumerate(row):
                stack_number = idx+1
                crate_labels = list(filter(str.isalpha, cell))
                stack[stack_number].

                    
        else:
            pass
        # number_commands = [
        #     int(word)
        #     for word in rearrangement_procedure_step.split(" ")
        #     if word.isdigit()
        # ]


def _create_crate_stacks():
    pass


if __name__ == "__main__":
    main()
