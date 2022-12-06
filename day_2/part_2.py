from util.generate_input_lines import generate_input_lines
from enum import Enum


class HandShapeScore(Enum):
    A = 1
    B = 2
    C = 3


class RoundOutcomeScore(Enum):
    LOST = 0
    DRAW = 3
    WON = 6


PLAY_STRATEGY_TO_ROUND_OUTCOME_MAP = {
    "X": RoundOutcomeScore.LOST,
    "Y": RoundOutcomeScore.DRAW,
    "Z": RoundOutcomeScore.WON,
}

WINNING_PLAYS = {"A": "B", "B": "C", "C": "A"}

LOSING_PLAYS = {value: key for key, value in WINNING_PLAYS.items()}


def main():
    total_score = 0

    for line in generate_input_lines("day_2/input.txt"):
        score_for_round = 0
        play_guide = line.split(" ")

        round_outcome = PLAY_STRATEGY_TO_ROUND_OUTCOME_MAP[play_guide[1]]
        score_for_round += round_outcome.value

        if round_outcome == RoundOutcomeScore.DRAW:
            score_for_round += HandShapeScore[play_guide[0]].value

        elif round_outcome == RoundOutcomeScore.WON:
            score_for_round += HandShapeScore[WINNING_PLAYS[play_guide[0]]].value

        else:
            score_for_round += HandShapeScore[LOSING_PLAYS[play_guide[0]]].value

        total_score += score_for_round

    print(total_score)
    return total_score


if __name__ == "__main__":
    main()
