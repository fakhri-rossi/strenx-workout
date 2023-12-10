from . import Utility, Database, Operation

name_space = Database.TEMPLATE["exercise_name"]
type_space = Database.TEMPLATE["exercise_name"]
reps_space = Database.TEMPLATE["reps"]
kg_space = Database.TEMPLATE["kg"]
time_space = Database.TEMPLATE["time"]
no_space = Database.TEMPLATE["no"]
muscle_target = Database.TEMPLATE["muscle_target"]

def print_routine(routine_name):
    file_name = Database.routine_path + routine_name + ".txt"

    with open(file_name, "r") as file:
        title = file.readline()
        lines = []

        print("\n" + "="*50)
        print(routine_name)
        print("-"*50)

def print_routine_list(routine_name):
    # file_name = Database.routine_path + routine_name + ".txt"
    data = Database.temp_routine
    n = len(data)
    print(data)

    # print heading
    # print("\n" + "="*50)
    print(routine_name)
    print("\n" + "-"*51)
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
        print("Belum ada exrcise apapun")
    print()
    

def run_routine():
    pass
def display_routine():
    pass

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

        muscle_target = Database.exercises[i]["type"].split(" ")
        muscle_target = ", ".join(muscle_target)
        muscle_target += muscle_target[len(muscle_target):]

        print(f"{no}|{exercise_name}|{exercise_type}|{muscle_target}")
        counter += 1

def new_routine():
    Utility.clear_screen()
    Database.temp_routine.clear()
    print("\n" + "="*100)
    print("Membuat Rutinitas")

    while True:
        routine_name = input("Nama Rutinitas: ")   
        if routine_name not in Database.routines:
            Database.temp_routine.append(routine_name)
            break

        else:
            print("Rutinitas sudah ada, buat nama lain")
    
    while True:
        Utility.clear_screen()
        print_routine_list(routine_name)

        print("1. Edit")
        print("2. Tambahkan set")
        print("3. Hapus set")

        print("\nOpsi lain: ")
        print("00 untuk menambahkan Exercise")
        print("01 untuk menyimpan dan keluar")
        print("02 untuk batal dan keluar")
        
        print("\n'nomor(titik)opsi' untuk memilih")
        print("Contoh: 3.1 untuk mengedit exercise no.3")

        user_option = input("Pilihan Anda: ")
        match user_option:
            case "00": Operation.select_exercise()
            case "01": 
                Operation.create()
                break
            case "02": break


def edit_routine():
    pass
def delete_routine():
    pass
def history():
    pass