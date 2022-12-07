from collections import deque

from day_7.common import create_directory_tree

MAX_TOTAL_DIRECTORY_SIZE = 100000


def main():
    root_directory = create_directory_tree()
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
