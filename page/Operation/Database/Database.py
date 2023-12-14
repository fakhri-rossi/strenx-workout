import os, time

DB_NAME = "data.txt"
routine_path = "./Data/routines/"
exercises_path = "./Data/exercises.txt"
routine_names = []
exercises = []
temp_list = []
old_name = 0
time_start = ""
time_end = ""
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
    temp_list.clear()

def create_temp_list(routine_name:str):
    file_name = "./routines/"+routine_name+".txt"
    temp_list.clear()
    temp_list.append(routine_name)

    try:
        with open(file_name, "r") as file:
            content = file.readlines()
            for line in content:
                temp_list.append(line[:-1])

    except:
        print("Gagal membuat temp routine")

def write_history():
    try:
        with open("history.txt", 'a', encoding="utf-8") as file:
            time_end = time.strftime("%Y-%m-%d-%H-%M-%S-%z", time.gmtime())
            n = len(temp_list)

            data_str = ""
            # time_start,time_end,routine_name,exercises...
            data_str = f"{time_start},{time_end},{temp_list[0]}"

            for i in range(1,n):
                if temp_list[i][-1] == "y":
                    data_str += f",{temp_list[i][:-2]}"

            data_str += "\n"
            file.write(data_str)

    except:
        print('file history tidak ditemukan')

def init_app():
    for (root, dirs, files) in os.walk(routine_path):
        for file in files:
            if ".txt" in file:
                routine_names.append(file[:-4])
   
    try:
        with open(exercises_path, "r", ) as file:
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
    routine_names.clear()
    for (root, dirs, files) in os.walk(routine_path):
        for file in files:
            if ".txt" in file:
                routine_names.append(file[:-4])

def refresh_temp_routines(routine_name):
    clear_temp_routines()
    create_temp_list(routine_name)

def write_routine():
    try:
        routine_title = temp_list[0]
        data = temp_list
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

