from collections import deque

from util.generate_input_lines import generate_input_lines
from day_7.directory import Directory

MAX_TOTAL_DIRECTORY_SIZE = 100000


def main():
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

    total_size = _get_total_size_of_directories_that_meet_max_size(root_directory)

    print(total_size)


def _get_total_size_of_directories_that_meet_max_size(root_directory):
    total_size = 0
    directory_queue = deque([root_directory])

    while len(directory_queue) > 0:
        current_directory = directory_queue.popleft()
        current_directory_size = current_directory.total_size
        if current_directory_size <= MAX_TOTAL_DIRECTORY_SIZE:
            total_size += current_directory_size

        directory_queue.extend(current_directory.subdirectories)

    return total_size


if __name__ == "__main__":
    main()
