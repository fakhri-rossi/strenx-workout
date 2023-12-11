import os, time

DB_NAME = "data.txt"
routine_path = "./routines/"
routines = []
exercises = []
temp_routine = []
old_name = 0
# HATI-HATI, index 0 temp_routine berisi judul routine, sisanya data exercise

# header => 33 spasi kosong sebelah kiri, 34 routine name, 33 spasi kosong kanan
TEMPLATE = {
    "routine_name": " "*34,
    "exercise_name": " "*30,
    "exercise_type": " "*30,
    "muscle_target": " "*30,
    "reps": " "*4,
    "kg": " "*4,
    "time": " "*5,
    "no": " "*4
}

def clear_temp_routines():
    temp_routine.clear()

def create_temp_routine(routine_name:str):
    file_name = "./routines/"+routine_name+".txt"
    temp_routine.append(routine_name)

    try:
        with open(file_name, "r") as file:
            content = file.readlines()
            for line in content:
                temp_routine.append(line[:-1])

    except:
        print("Gagal membuat temp routine")

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
            
    except:
        print("Gagal membuka database exercise")

def refresh_routines():
    routines.clear()
    for (root, dirs, files) in os.walk(routine_path):
        for file in files:
            if ".txt" in file:
                routines.append(file[:-4])

def refresh_temp_routines(routine_name):
    clear_temp_routines()
    create_temp_routine(routine_name)

def create():
    try:
        routine_title = temp_routine[0]
        data = temp_routine
        n = len(data)
        file_name = routine_path + routine_title + ".txt"

        with open(file_name, "w", encoding='utf-8') as file:
            for i in range(1,n):
                line = data[i] + "\n"
                file.write(line)

        # me-remove file lama jika rutinitas di rename
        global old_name
        if old_name != 0:
            old_file = f"./routines/{old_name}.txt"
            print(old_file)
            os.remove(old_file)
            old_file = ""
            old_name = 0

    except:
        print("Pembuatan rutinitas gagal")

