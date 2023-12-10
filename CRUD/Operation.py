from . import Database, Utility

def select_exercise():
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
        exercise_name += Database.TEMPLATE["exercise_name"][len(exercise_name):]

        exercise_type = Database.exercises[i]["type"]
        exercise_type += Database.TEMPLATE["exercise_type"][len(exercise_type):]

        muscle_target = Database.exercises[i]["type"].split(" ")
        muscle_target = ", ".join(muscle_target)
        muscle_target += Database.TEMPLATE["muscle_target"][len(muscle_target):]

        print(f"{no}|{exercise_name}|{exercise_type}|{muscle_target}")
        counter += 1

    # ask user option
    while True:
        try:
            user_option = int(input("No exercise yang ingin ditambah: ")) - 1

            if user_option >= n or user_option < 1:
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
                kg = float(input("Kg: "))
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

            str_exercise = f"{reps},{kg},{timer}"
            print(str_exercise)

            agree = Utility.user_confirm("Apakah Anda yakin?")
            if agree:
                break
            else:
                break
        
        except:
            print("Masukkan input yang valid!")
            
def create(routine_title):
    try:
        file_name = Database.routine_path + routine_title + ".txt"
        with open(file_name, "w", encoding='utf-8') as file:
            file.write()
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