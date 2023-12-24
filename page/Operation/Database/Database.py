import os, time

DB_NAME = "data.txt"
exercises_path = "./Page/Operation/Database/Data/exercise.txt"
history_file_path = "./Page/Operation/Database/Data/history.txt"
dirname = os.path.dirname(__file__)
routine_path = os.path.join(dirname, "Data\\routines\\")

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

def create_temp_list(routine_name:str):
    file_name = routine_path + routine_name + ".txt"
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
        global time_start, time_end
        with open(history_file_path, 'a', encoding="utf-8") as file:
            n = len(temp_list)

            data_str = ""
            # time_start,time_end,routine_name,exercises...
            data_str = f"{time_start},{time_end},{temp_list[0]}"

            for i in range(1,n):
                if temp_list[i][-1] == "y":
                    data_str += f",{temp_list[i][:-2]}"

            data_str += "\n"
            file.write(data_str)
            print("Berhasil merekap latihan")

    except:
        print('file history tidak ditemukan')

def init_app():
    # file checking
    if not os.path.isdir(routine_path):
        os.mkdir(routine_path)

    refresh_routine_names()

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

def refresh_routine_names():
    routine_names.clear()
    
    for (root, dirs, files) in os.walk(routine_path):
        for file in files:
            if ".txt" in file:
                routine_names.append(file[:-4])

def refresh_temp_routines(routine_name:str):
    temp_list.clear()
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
            old_file = f"{routine_path}{old_name}.txt"
            os.remove(old_file)
            old_file = ""
            old_name = 0

    except:
        print("Pembuatan rutinitas gagal")

def delete_routine(routine_name:str):
    file_path = f"{routine_path}{routine_name}.txt"
    try:
        os.remove(file_path)
        print("Berhasil menghapus Rutinitas")
    except:
        print("Gagal menghapus rutinitas")

def update_routine():
    try:
        data = temp_list
        routine_title = data[0]
        n = len(data)
        file_name = routine_path + routine_title + ".txt"

        with open(file_name, "w", encoding='utf-8') as file:
            for i in range(1,n):
                line = data[i][:-2] + "\n"
                file.write(line)

        # me-remove file lama jika rutinitas di rename
        global old_name
        if old_name != 0:
            old_file = f"{routine_path}{old_name}.txt"
            print(old_file)
            os.remove(old_file)
            old_file = ""
            old_name = 0

    except:
        print("Pembuatan rutinitas gagal")

def read_history():
    with open(history_file_path, "r") as file:
        content = file.readlines()
    return content