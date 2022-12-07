from collections import deque
from typing import List

from util.generate_input_lines import generate_input_lines

MAX_TOTAL_DIRECTORY_SIZE = 100000


def main():
    root_directory = Directory(name="/", parent_directory=None)

    current_directory = None
    for terminal_output in generate_input_lines("day_7/input.txt"):
        if terminal_output.starts_with("$"):
            if terminal_output.starts_with("$ cd"):
                terms = terminal_output.split(" ")
                next_path = terms[-1]

                if next_path == "/":
                    current_directory = root_directory
                elif next_path == "..":
                    current_directory = current_directory.parent_directory
                else:
                    # might have to see if directory exists first
                    current_directory = current_directory.find_subdirectory_by_name(
                        next_path
                    )

        else:
            terms = terminal_output.split(" ")
            if terms[0] == "dir":
                current_directory.add_subdirectory(terms[1])
            elif terms[0].isdigit():
                current_directory.add_file(terms[1], terms[0])

    total_size = _get_total_size_of_directories_that_meet_max_size(root_directory)


if __name__ == "__main__":
    main()


def _get_total_size_of_directories_that_meet_max_size(root_directory):
    total_size = 0
    current_directory = root_directory

    while current_directory:
        current_directory_size = current_directory.get_total_size()
        if current_directory_size <= MAX_TOTAL_DIRECTORY_SIZE:
            total_size += current_directory_size

        current_directory = alal


class Directory:
    def __init__(self, name: str, parent_directory: "Directory" = None):
        self.name = name
        self.parent_directory = parent_directory
        self._subdirectories = {}
        self._files = set()
        self.size = 0

    def add_subdirectory(self, name):
        try:
            self.find_subdirectory_by_name(name)
        except SubdirectoryNotFoundError:
            self._subdirectories[name] = self.__class__(
                name=name, parent_directory=self
            )

    def find_subdirectory_by_name(self, name):
        try:
            return self._subdirectories[name]
        except KeyError:
            raise SubdirectoryNotFoundError(name)

    def add_file(self, name, size):
        file = (name, size)
        if file not in self._files:
            self._files.add((name, size))
            self.size += size

    def get_total_size(self):
        total_size = self.size

        for subdirectory in self._subdirectories.values():
            total_size += subdirectory.get_total_size()

        return total_size


class SubdirectoryNotFoundError(Exception):
    def __init__(self, identifier):
        super(SubdirectoryNotFoundError, self).__init__(
            "Subdirectory not found: {}".format(identifier)
        )
