from util.generate_input_lines import generate_input_lines


def main():
    count_of_pairs_that_overlap = 0
    for assignment_pair in generate_input_lines("day_4/input.txt"):
        assignment_pair = [
            [int(section) for section in assignment.split("-")]
            for assignment in assignment_pair.split(",")
        ]

        assignment_one = assignment_pair[0]
        assignment_two = assignment_pair[1]

        if _do_pairs_overlap(assignment_one, assignment_two):
            count_of_pairs_that_overlap += 1

    print(count_of_pairs_that_overlap)
    return count_of_pairs_that_overlap


def _do_pairs_overlap(range_one, range_two):
    return (range_one[0] <= range_two[0] and range_one[1] >= range_two[0]) or (
        range_two[0] <= range_one[0] and range_two[1] >= range_one[0]
    )


if __name__ == "__main__":
    main()
