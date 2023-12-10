from . import Database, Utility, View

def select_exercise():
    # Print all exercises
    View.print_exercises()
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
                reps = int(input("Reps: "))
            else: 
                reps = "-"
            if exercise_type == "weight-based":
                kg = int(input("Kg: "))
            else:
                kg = "-"
            if exercise_type == "time-based":
                while True:
                    timer = input("Time (mm:ss): ")
                    if timer[2] != ":":
                        print("Input valid time!")
                        continue
                    else:
                        try:
                            inttime = int(timer[:2])
                            inttime = int(timer[3:])
                            break
                        except:
                            print("Input valid time!")
                            continue
            else:
                timer = "-"

            str_exercise = f"{exercise_name},{reps},{kg},{timer}"
            print(str_exercise)

            agree = Utility.user_confirm("Apakah Anda yakin?")
            if agree:
                Database.temp_routine.append(str_exercise)
                break
            else:
                break
        
        except:
            print("Masukkan input yang valid!")
            
def create():
    try:
        routine_title = Database.temp_routine[0]
        data = Database.temp_routine
        n = len(data)
        file_name = Database.routine_path + routine_title + ".txt"

        with open(file_name, "w", encoding='utf-8') as file:
            for i in range(1,n):
                line = data[i] + "\n"
                file.write(line)

    except:
        print("Pembuatan rutinitas gagal")

def edit(routine_title):
    try:
        file_name = Database.routine_title 
        with open(file_name, "r+", encoding="utf-8") as file:
            print("Berhasil edit")
    except:
        print("Gagal Edit")

def read(routine_title):
    try:
        file_name = Database.routine_title 
        with open(file_name, "r", encoding="utf-8") as file:
            print("Berhasil melihat")
            content = file.readlines()
            print(content)
    except:
        print("Gagal Edit")