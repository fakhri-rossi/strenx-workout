from . import Database, Utility, View
import os

name_space = Database.TEMPLATE["exercise_name"]
type_space = Database.TEMPLATE["exercise_name"]
reps_space = Database.TEMPLATE["reps"]
kg_space = Database.TEMPLATE["kg"]
time_space = Database.TEMPLATE["time"]
no_space = Database.TEMPLATE["no"]
muscle_target = Database.TEMPLATE["muscle_target"]

def create_routine():
    Database.clear_temp_routines()
    # Membuat judul rutinitas
    while True:
        routine_name = input("Nama Rutinitas: ")   

        if routine_name not in Database.routines:
            Database.temp_routine.append(routine_name)
            Database.create()
            break

        else:
            print("Rutinitas sudah ada, buat nama lain")
    edit(routine_name)
    Database.clear_temp_routines()
    
    
def select_exercise():
    # Print all exercises
    print_exercises()
    n = len(Database.exercises)

    # ask user option
    while True:
        try:
            user_option = int(input("No exercise yang ingin ditambah: ")) - 1

            if user_option >= n or user_option < 0:
                print("Masukkan angka yang valid")

            else:
                break
        except:
            print("Masukkan angka yang valid")
    
    exercise_name = Database.exercises[user_option]["name"]
    exercise_type = Database.exercises[user_option]["type"]

    while True:
        try:
            if exercise_type != "time-based":
                reps = Utility.ask_reps()
            else: 
                reps = "-"
            if exercise_type == "weight-based":
                kg = Utility.ask_kg()
            else:
                kg = "-"
            if exercise_type == "time-based":
                timer = Utility.ask_timer()
            else:
                timer = "-"

            str_exercise = f"{exercise_name},{reps},{kg},{timer}"

            Database.temp_routine.append(str_exercise)
            break
        
        except:
            print("Masukkan input yang valid!")

def edit(routine_name):
    Database.refresh_temp_routines(routine_name)
    is_continue = True
    
    while is_continue:
        Utility.clear_screen()
        print(Database.temp_routine)
        print_routine(routine_name)

        print("_1 Edit")
        print("_2 Tambahkan set")
        print("_3 Hapus set")

        print("\nOpsi lain: ")
        print("00 untuk menambahkan Exercise")
        print("01 untuk keluar")
        print("02 untuk ganti nama rutinitas")
        
        print("\n'nomor(spasi)opsi' untuk memilih")
        print("Contoh: 3 1 untuk mengedit exercise no.3")

        while True:
            user_option = input("Pilihan Anda: ")
            match user_option:
                case "00": 
                    select_exercise()
                    Database.create()
                    break

                case "01": 
                    Database.create()
                    is_continue = False
                    break

                case "02": 
                    new_name = input("Nama rutinitas: ")
                    Database.temp_routine[0] = new_name
                    Database.create()

                    # menghapus file rutinitas lama
                    os.remove((f"./routines/{routine_name}.txt"))

                    # memperbarui nama rutinitas
                    routine_name = new_name
                    break

                case _:
                    user_option = user_option.split(" ")
                    if len(user_option) > 2:
                        print("Masukkan opsi yang valid!")
                        continue
                    try:
                        user_option[0] = int(user_option[0])
                    except:
                        print("Masukkan angka, bukan yang lain!")
                        continue
                    if user_option[0] > len(Database.temp_routine):
                        print("Nomor exercise tidak ada")
                        continue

                    match user_option[1]:
                        case "1":
                            print("Edit set")
                            edit_set(user_option[0])
                            break

                        case "2":
                            add_set(user_option[0])
                            break

                        case "3":
                            delete_set(user_option[0])
                            break

            Database.refresh_temp_routines(routine_name)           
        Database.create()        
        Database.refresh_temp_routines(routine_name)
        Utility.clear_screen()   
    Database.clear_temp_routines()

def print_exercises():  
    # print heading
    Utility.clear_screen()
    print("Select Exercise")
    print("-"* 93)
    print(f"No  |Exercise Name" + " "*17 + "|Exercise Type" + " "*17 +"|Muscle Target" + " "*17)
    print("-"* 93)

    n = len(Database.exercises)

    # print content
    counter = 1
    for i in range(n):
        str_counter = str(counter)
        no = f"{str_counter + Database.TEMPLATE['no'][len(str_counter):]}"

        exercise_name = Database.exercises[i]["name"]
        exercise_name += name_space[len(exercise_name):]

        exercise_type = Database.exercises[i]["type"]
        exercise_type += type_space[len(exercise_type):]

        muscle_target = Database.exercises[i]["muscle_target"].split(" ")
        muscle_target = ", ".join(muscle_target)
        muscle_target += muscle_target[len(muscle_target):]

        print(f"{no}|{exercise_name}|{exercise_type}|{muscle_target}")
        counter += 1

def print_routine(routine_name):
    Database.clear_temp_routines()
    Database.create_temp_routine(routine_name)
    data = Database.temp_routine
    n = len(data)

    # print heading
    print("\n" + "="*51)
    print(routine_name)
    print("="*51)
    print("No  |Exercise" + " "*22 + "|Reps|Kg  |Timer")
    print("-"*51)

    if n > 1:
        for i in range(1,n):
            data_break = data[i].split(",")
            name = data_break[0] + name_space[len(data_break[0]):]
            reps = data_break[1] + reps_space[len(data_break[1]):]
            kg = data_break[2] + kg_space[len(data_break[2]):]
            timer = data_break[3]
            no = f"{i}" + no_space[len(str(i)):]

            print(f"{no}|{name}|{reps}|{kg}|{timer}")

    else:
        print("Belum ada exercise apapun")
    print()

def print_summarized_routine():

    Database.refresh_routines()
    titles = Database.routines
    no = 1
    for title in titles:
        Database.clear_temp_routines()
        Database.create_temp_routine(title)
        data_temp = Database.temp_routine
        name = data_temp[0]
        n = len(data_temp)

        if n > 1:
            exercises = []
            for i in range(1,n):
                data_break = data_temp[i].split(",")
                exercises.append(data_break[0])
            exercises = ", ".join(exercises)
        else:
            exercises = "(tidak ada)"

        print(f"{no}. {name}: {exercises}")

        no += 1
    

def edit_set(index:int):
    data = Database.temp_routine[index]
    data_break = data.split(",")

    # reps
    if data_break[1] != "-":
        reps = Utility.ask_reps()
    else:
        reps = "-"
    # kg
    if data_break[2] != "-":
        kg = Utility.ask_kg()
    else:
        kg = "-"
    # timer
    if data_break[3] != "-":
        timer = Utility.ask_timer()
    else:
        timer = "-"

    data_str = f"{data_break[0]},{reps},{kg},{timer}"
    Database.temp_routine[index] = data_str # update data

def add_set(index:int):
    data = Database.temp_routine[index]
    Database.temp_routine.insert(index+1,data)

def delete_set(index:int):
    Database.temp_routine.pop(index)

def read(routine_title):
    try:
        file_name = Database.routine_title 
        with open(file_name, "r", encoding="utf-8") as file:
            print("Berhasil melihat")
            content = file.readlines()
            print(content)
    except:
        print("Gagal Edit")
