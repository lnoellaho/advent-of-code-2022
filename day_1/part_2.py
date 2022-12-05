from util.generate_input_lines import generate_input_lines

def main():
    total_of_top_3_elf_calories = sum(_get_top_3_elf_calories())
    print(total_of_top_3_elf_calories)
    return total_of_top_3_elf_calories

def _get_top_3_elf_calories():
    return sorted(_get_all_elf_calories(), reverse=True)[:3]

def _get_all_elf_calories():
    elf_calories = []
    current_elf_calorie_total = 0
    for line in generate_input_lines("day_1/input.txt"):
        if line == "":
            elf_calories.append(current_elf_calorie_total)
            current_elf_calorie_total = 0
        else:
            current_elf_calorie_total += int(line)
            
    return elf_calories

if __name__ == "__main__":
    main()