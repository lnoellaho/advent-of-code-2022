from collections import deque

from day_7.common import create_directory_tree

TOTAL_DISK_SPACE = 70000000
DISK_SPACE_NEEDED = 30000000


def main():
    root_directory = create_directory_tree()
    directory_size = _get_smallest_directory_size_needed_to_free_up_disk_space(
        root_directory
    )
    print(directory_size)


def _get_smallest_directory_size_needed_to_free_up_disk_space(root_directory):
    unused_space = TOTAL_DISK_SPACE - root_directory.total_size
    disk_space_to_be_freed = DISK_SPACE_NEEDED - unused_space

    directory_queue = deque([root_directory])
    directory_size_to_be_deleted = root_directory.total_size

    while len(directory_queue) > 0:
        current_directory = directory_queue.popleft()
        current_directory_size = current_directory.total_size
        if (
            current_directory_size >= disk_space_to_be_freed
            and current_directory_size < directory_size_to_be_deleted
        ):
            directory_size_to_be_deleted = current_directory_size

        directory_queue.extend(current_directory.subdirectories)

    return directory_size_to_be_deleted


if __name__ == "__main__":
    main()
