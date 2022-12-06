from util.generate_input_lines import generate_input_lines
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
    for rucksack_contents in generate_input_lines("day_3/input.txt"):
        rucksack_items = list(rucksack_contents)
        rucksack_item_count = len(rucksack_contents)

        compartment_1, compartment_2 = (
            set(rucksack_items[: rucksack_item_count // 2]),
            set(rucksack_items[rucksack_item_count // 2 :]),
        )

        items_in_both_compartments = compartment_1.intersection(compartment_2)

        for item in items_in_both_compartments:
            total_priority_score += ITEM_TYPE_PRIORITY_SCORES[item]

    print(total_priority_score)
    return total_priority_score


if __name__ == "__main__":
    main()
