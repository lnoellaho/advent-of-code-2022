def generate_input_lines(input_file_path):
    with open(input_file_path, "r") as f:
        for line in f:
            line = line.strip()
            yield line
