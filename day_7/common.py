from util.generate_input_lines import generate_input_lines
from day_7.directory import Directory


def create_directory_tree():
    root_directory = Directory(name="/", parent_directory=None)
    current_directory = None

    for terminal_output in generate_input_lines("day_7/input.txt"):
        if terminal_output.startswith("$"):
            if terminal_output.startswith("$ cd"):
                terms = terminal_output.split(" ")
                next_path = terms[-1]

                if next_path == "/":
                    current_directory = root_directory
                elif next_path == "..":
                    current_directory = current_directory.parent_directory
                else:
                    current_directory = current_directory.find_subdirectory_by_name(
                        next_path
                    )
        else:
            terms = terminal_output.split(" ")
            if terms[0] == "dir":
                current_directory.add_subdirectory(terms[1])
            elif terms[0].isdigit():
                current_directory.add_file(terms[1], int(terms[0]))

    return root_directory
