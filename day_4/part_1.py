from util.generate_input_lines import generate_input_lines


def main():
    count_of_pairs_that_fully_overlap = 0
    for assignment_pair in generate_input_lines("day_4/input.txt"):
        assignment_pair = [
            assignment.split("-") for assignment in assignment_pair.split(",")
        ]

        assignment_one = assignment_pair[0]
        assignment_two = assignment_pair[1]

        if _does_first_range_fully_contain_second_range(
            assignment_one, assignment_two
        ) or _does_first_range_fully_contain_second_range(
            assignment_two, assignment_one
        ):
            count_of_pairs_that_fully_overlap += 1

    print(count_of_pairs_that_fully_overlap)
    return count_of_pairs_that_fully_overlap


def _does_first_range_fully_contain_second_range(range_one, range_two):
    return (int(range_one[0]) <= int(range_two[0])) and (
        int(range_one[1]) >= int(range_two[1])
    )


if __name__ == "__main__":
    main()
