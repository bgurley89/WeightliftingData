from dataclasses import dataclass, field
from typing import List


@dataclass()
class Exercise:
    date: int = 0
    exercise: str = ""
    load: List = field(default_factory=list)
    reps: int = 0
    sets: int = 0

    def list_exercise(self):
        if self.reps != 0:
            print(self.exercise, " - ", self.load, " x ", self.reps, " / ", self.sets)
        else:
            print(self.exercise, " - ", self.load)


def process_work(_input=str):
    # Function to split the input string for LOADxREPS/SETS
    if "x" in _input:
        _load, _rs = _input.split('x', 1)
        _reps, _sets = _rs.split('/', 1)
    else:
        _load = _input.split(',')
        _reps = 0
        _sets = 0

    return _load, _reps, _sets
