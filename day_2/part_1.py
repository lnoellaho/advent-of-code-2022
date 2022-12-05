from util.generate_input_lines import generate_input_lines
from enum import Enum

class ShapeEquivalent(Enum):
    X = "A"
    Y = "B"
    Z = "C"

class ShapeScore(Enum):
    X = 1
    Y = 2
    Z = 3

class RoundOutcomeScore(Enum):
    LOST = 0
    DRAW = 3
    WON = 6

WINNING_COMBINATIONS = [("A", "Y"), ("B", "Z"), ("C", "X")]

def main():
    total_score = 0
    for line in generate_input_lines("day_2/input.txt"):
        score_for_round = 0
        play_guide = line.split(" ")
        score_for_round += ShapeScore[play_guide[1]].value

        if play_guide[0] == ShapeEquivalent[play_guide[1]].value:
            score_for_round += RoundOutcomeScore.DRAW.value
        
        elif tuple(play_guide) in WINNING_COMBINATIONS:
            score_for_round += RoundOutcomeScore.WON.value
        
        else:
            score_for_round += RoundOutcomeScore.LOST.value
        
        total_score += score_for_round

    print(total_score)
    return total_score
    

if __name__ == "__main__":
    main()