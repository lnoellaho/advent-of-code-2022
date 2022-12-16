from util.generate_input_lines import generate_input_lines


class SignalStrengthTracker:
    def __init__(self, cycles_to_track):
        self._tracked_cycles = cycles_to_track
        self._signal_strengths = {cycle_number: 0 for cycle_number in cycles_to_track}

    @property
    def tracked_cycles(self):
        return self._tracked_cycles

    def set_signal_strength(self, cycle_number, signal_strength):
        self._signal_strengths[cycle_number] = signal_strength

    def get_sum_of_tracked_signal_strengths(self):
        return sum(self._signal_strengths.values())


class CPU:
    def __init__(self, signal_strength_tracker, x_register_starting_value=1):
        self._x_register = x_register_starting_value
        self._cycle_number = 0
        self._signal_strength_tracker = signal_strength_tracker

    def add_x(self, number_to_add):
        self._x_register += number_to_add

    def increase_cycle_by_one(self):
        self._cycle_number += 1
        if self._cycle_number in self._signal_strength_tracker.tracked_cycles:
            self._signal_strength_tracker.set_signal_strength(
                self._cycle_number, self.calculate_signal_strength()
            )

    def calculate_signal_strength(self):
        return self._cycle_number * self._x_register


def main():
    signal_strength_tracker = SignalStrengthTracker([20, 60, 100, 140, 180, 220])
    cpu = CPU(signal_strength_tracker)
    for instruction_input in generate_input_lines("day_10/input.txt"):
        command = instruction_input.split(" ")

        if command[0] == "addx":
            cpu.increase_cycle_by_one()
            cpu.increase_cycle_by_one()
            cpu.add_x(int(command[1]))

        if command[0] == "noop":
            cpu.increase_cycle_by_one()

    print(signal_strength_tracker.get_sum_of_tracked_signal_strengths())


if __name__ == "__main__":
    main()
