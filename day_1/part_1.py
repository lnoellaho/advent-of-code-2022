from util.generate_input_lines import generate_input_lines


def main():
    max_calories = 0
    current_elf_calorie_total = 0
    for line in generate_input_lines("day_1/input.txt"):
        if line == "":
            if current_elf_calorie_total > max_calories:
                max_calories = current_elf_calorie_total

            current_elf_calorie_total = 0
        else:
            current_elf_calorie_total += int(line)
    print(max_calories)
    return max_calories


if __name__ == "__main__":
    main()
