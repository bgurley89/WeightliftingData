from dataclasses import dataclass, field
from typing import List
import Exercise


@dataclass()
class Session:
    date: int = 0
    training: List[object] = field(default_factory=list)

    def set_date(self, _date):
        self.date = _date

    def add_exercise(self, new):
        self.training.append(new)

    def print_session(self):
        # This function ONLY prints an Exercise dataclass object with the listed fields
        print("\nTraining Session for ", self.date)

        for exrs in self.training:
            print("    ", exrs.exercise)
            if exrs.reps != 0:
                print("        Working: ", exrs.load, " - ", exrs.reps, " x ", exrs.sets, " sets")
            else:
                print("        Sets: ", *exrs.load)
