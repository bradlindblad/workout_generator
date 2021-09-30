# workout_generator
 Generate a random bodyweight workout. For any given workout length, create over 6,000 unique workouts so you're always stressing your body in new and exciting ways.



# Usage
```bash
python3 python/main.py
```
Or run with pipenv:
```
pipenv run python3 python/main.py
```

Creates a randomized bodyweight workout, taking these inputs in CLI:

- Workout length in minutes
- Cardio option
- Desired output location of text file containing workout

It samples random exercises from python/options.csv, which you can modify for more variety.

# Example workout

```
Printed: 2021-09-20, Monday

Workout length: 18.0 mins 
Sets: 6 
Reps: 6 
Rest: 90 seconds 
 
ruck military press
navy seal
ruck push up
3 pump burpee
Push-up
ruck shoulder raise

Set checkbox [1] [2] [3] [4] [5] [6] 
```