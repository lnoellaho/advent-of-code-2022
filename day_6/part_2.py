from collections import deque
from util.generate_input_lines import generate_input_lines

START_OF_MESSAGE_MARKER_CHARACTER_LIMIT = 14


def main():
    datastream_buffer = list(list(generate_input_lines("day_6/input.txt"))[0])

    first_potential_start_of_message_marker = datastream_buffer[
        :START_OF_MESSAGE_MARKER_CHARACTER_LIMIT
    ]
    if (
        len(set(first_potential_start_of_message_marker))
        == START_OF_MESSAGE_MARKER_CHARACTER_LIMIT
    ):
        return START_OF_MESSAGE_MARKER_CHARACTER_LIMIT

    potential_start_of_packet_marker = deque(first_potential_start_of_message_marker)

    for idx, signal_character in enumerate(
        datastream_buffer[START_OF_MESSAGE_MARKER_CHARACTER_LIMIT:]
    ):
        potential_start_of_packet_marker.popleft()
        potential_start_of_packet_marker.append(signal_character)

        if (
            len(set(potential_start_of_packet_marker))
            == START_OF_MESSAGE_MARKER_CHARACTER_LIMIT
        ):
            current_character_count = idx + START_OF_MESSAGE_MARKER_CHARACTER_LIMIT + 1
            print(current_character_count)
            break


if __name__ == "__main__":
    main()
