from datetime import datetime
import os
import pandas as pd
from prompt_toolkit import prompt
import random

HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


opt = pd.read_csv(os.path.join(HOME, "python", "options.csv"))


LENGTH = int(prompt("Enter workout length in mins: "))
LENGTH = LENGTH * 60

CARDIO = prompt("Cardio? (y/n) ")
CARDIO = CARDIO.upper()
# CARDIO = "Y"
OUTPUT_LOC = os.path.join(HOME, "workout.txt")
OUTPUT_LOC = prompt("Output location (default: repo): ")

# Functions ------------------------------------


def create_cardio(opt):
    """
    Creates cardio session.
    """
    selection = opt[opt.cardio == 1]

    # get random
    cardio = selection.sample(1).name.values[0]

    return cardio


def get_rest():
    """
    Returns rest interval.
    """
    r = [30, 60, 90, 120]
    return random.sample(r, 1)


def get_reps():
    """
    Get random rep count
    """
    return random.sample(range(5, 15, 1), 1)


# Begin logic ----------------------------------

# Est cardio
if CARDIO.upper() == "Y":
    c = create_cardio(opt)
    c_time = round(LENGTH * 0.5, 0)

# Est. number of sets based on length of workout
sets = 0
if LENGTH < 20:
    sets = random.sample(range(3, 7, 1), 1)[0]
if LENGTH >= 20 and LENGTH < 30:
    sets = random.sample(range(4, 8, 1), 1)[0]
if LENGTH >= 30:
    sets = random.sample(range(5, 9, 1), 1)[0]

# Est rest between sets
rest = get_rest()[0]

# Calc work time

if CARDIO.upper() == "N":
    work_time = LENGTH - (rest * (sets - 1))
elif CARDIO.upper() == "Y":
    work_time = LENGTH - (rest * (sets - 1)) - c_time

# Get number reps per exercise
reps = get_reps()[0]

# Get number exercises to randomly grab
move_time = reps * 3  # figure 5 seconds per rep on average

n_exercises_to_grab = round(round(work_time / move_time, 0) / sets, 0)

# Create empty list to append chosen exercises to
exercises = []

pool = opt[opt.cardio != 1]

# Get random exercises
other_ex = pool.sample(int(n_exercises_to_grab))
l = len(other_ex)
more_to_append = list(other_ex.name.values[0:l])

for i in more_to_append:
    exercises.append(i)


# PRINT Debug------------
# exercises

# print(f"{LENGTH} desired workout")
# print(f"{sets} sets")
# print(f"{reps} reps")
# print(f"{rest} rest secs")
# print(f"{work_time} work time")
# # print(f"{c} cardio duration: {c_time}")
# work_time/60


# WRITE TO TXT

write_here = os.path.join(OUTPUT_LOC, "workout.txt")

with open(write_here, "w") as f:
    f.write(
        "Printed: "
        + datetime.today().strftime("%Y-%m-%d")
        + ", "
        + datetime.today().strftime("%A")
        + "\n\n"
    )
    f.write(f"Workout length: {LENGTH/60} mins \n")
    f.write(f"Sets: {sets} \nReps: {reps} \nRest: {rest} seconds \n \n")
    for i in exercises:
        f.write(i + "\n")
    f.write("\nSet checkbox ")
    for i in range(sets):
        f.write("[] ")
    if CARDIO.upper() == "Y":
        f.write(f"\n\nCardio: {c}, {round(c_time / 60, 0)} mins")

    f.close()

print(f"workout.txt written to {write_here}.")
