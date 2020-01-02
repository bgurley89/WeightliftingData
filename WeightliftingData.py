import Exercise as Ex
import Session as Ts
import json
import dataclasses


def manual_session_entry():
    training_day = Ts.Session()
    entry = Ex.Exercise()
    _date = 0
    _exercise = ""
    _work = ""
    _load = []
    _reps = 0
    _sets = 0

    print("*** New Training Session Entry ***")
    print("Enter date as YYYYMMDD: ")
    _date = int(input())
    print("Enter new exercise: ")
    _exercise = input()

    while _exercise != "done":
        print("Enter working sets as LOADxREPS/SETS or building as LOAD,LOAD,LOAD,... : ")
        _work = input()

        _load, _reps, _sets = Ex.process_work(_work)

        entry = Ex.Exercise(date=_date, exercise=_exercise, load=_load, reps=_reps, sets=_sets)
        training_day.set_date(_date)
        training_day.add_exercise(entry)

        print("Enter new exercise or 'done' to quit: ")
        _exercise = input()

    training_day.print_session()

    return training_day


def write_session_to_file(filename, session):
    # Write new JSON objects as line appended to end of given file
    new_json_obj = json.dumps(dataclasses.asdict(session))
    with open(filename, 'a') as outfile:
        outfile.write('\n' + new_json_obj)

    print('\nSession successfully written to ' + filename)


def read_session_from_file(filename):
    # Read file line by line and process each line as a JSON object
    dict_data = []

    with open(filename) as json_file:
        for line in json_file:
            dict_data.append(json.loads(line))

        dates = [session['date'] for session in dict_data]
        exercises = [workout['training'] for workout in dict_data]
        day = exercises[0]
        print(type(day))

        #print(type(exercises))
        #
        print(exercises)
        #snday = [snatch['exercise'] for snatch in exercises]


        print("\nFile ", filename, " contains the follow training sessions dated:")
        print(dates)


def main():
    #session_data = manual_session_entry()
    #write_session_to_file('data.txt', session_data)
    read_session_from_file('data.txt')


if __name__ == "__main__":
    main()
