from util.generate_input_lines import generate_input_lines, generate_list_segments
from string import ascii_lowercase
from string import ascii_uppercase

ITEM_TYPE_PRIORITY_SCORES = {
    letter: idx + 1 for idx, letter in enumerate(ascii_lowercase)
}

ITEM_TYPE_PRIORITY_SCORES.update(
    {
        letter: idx + (len(ascii_lowercase) + 1)
        for idx, letter in enumerate(ascii_uppercase)
    }
)


def main():
    total_priority_score = 0
    for elf_group_rucksacks in generate_list_segments(
        list(generate_input_lines("day_3/input.txt")), segment_size=3
    ):
        rucksacks = [set(rucksack) for rucksack in elf_group_rucksacks]

        items_in_all_rucksacks = rucksacks[0].intersection(*rucksacks[1:])

        for item in items_in_all_rucksacks:
            total_priority_score += ITEM_TYPE_PRIORITY_SCORES[item]

    print(total_priority_score)
    return total_priority_score


if __name__ == "__main__":
    main()
