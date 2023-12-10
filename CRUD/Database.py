import os

DB_NAME = "data.txt"
routine_path = "./routines/"
routines = []
exercises = []
temp_routine = []
# HATI-HATI, index 0 temp_routine berisi judul routine, sisanya data exercise

# header => 33 spasi kosong sebelah kiri, 34 routine name, 33 spasi kosong kanan
TEMPLATE = {
    "routine_name": " "*34,
    "exercise_name": " "*30,
    "exercise_type": " "*30,
    "muscle_target": " "*30,
    "reps": " "*4,
    "kg": " "*4,
    "time": "MM:SS",
    "no": " "*4
}

def init_app():
    for (root, dirs, files) in os.walk(routine_path):
        for file in files:
            if ".txt" in file:
                routines.append(file[:-4])
   
    try:
        with open("exercise.txt", "r", ) as file:
            content = file.readlines()

            for line in content:
                line_break = line.split(",")
                exercise_name = line_break[0]
                exercise_type = line_break[1]
                muscle_target = line_break[2][:-1]

                exercises.append({"name":exercise_name,
                                    "type": exercise_type,
                                    "muscle_target": muscle_target})
            
            print(exercises)

    except:
        print("Gagal membuka database exercise")
