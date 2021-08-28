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
Printed: 2021-08-25, Wednesday

Workout length: 35.0 mins 
Sets: 5 
Reps: 14 
Rest: 90 seconds 
 
2 pump burpee
flutter kick
ruck squat

Set checkbox [] [] [] [] [] 

Cardio: heavy ruck, 12.0 mins
```