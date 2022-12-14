def generate_input_lines(input_file_path, line_transformation_func=lambda x: x.strip()):
    with open(input_file_path, "r") as f:
        for line in f:
            line = line_transformation_func(line)
            yield line


def generate_list_segments(li, segment_size=1):
    for offset in range(0, len(li), segment_size):
        yield li[offset : offset + segment_size]
