from . import Utility, Database, View
import os

name_space = Database.TEMPLATE["exercise_name"]
type_space = Database.TEMPLATE["exercise_name"]
reps_space = Database.TEMPLATE["reps"]
kg_space = Database.TEMPLATE["kg"]
time_space = Database.TEMPLATE["time"]
no_space = Database.TEMPLATE["no"]
muscle_target = Database.TEMPLATE["muscle_target"]

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

def print_routine(**kwargs):
    # kalo ada sumber dari list maka data akan diambil dari list tersebut
    if "list_source" in kwargs:
        data = kwargs["list_source"]
    
    # jika tidak maka mengambil data dari temp_routine
    else:
        data = Database.temp_routine
        routine_name = Database.temp_routine[0]
        # print heading
        print("="*51)
        print(routine_name)
        print("="*51)

    n = len(data)

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

def print_running_workout(routine_name):
    data = Database.temp_history
    n = len(data)

    # print heading
    print("\n" + "="*57)
    print(routine_name)
    print("="*57)
    print("No  |Exercise" + " "*22 + "|Reps|Kg  |Timer|Done?")
    print("-"*57)

    if n > 2:
        for i in range(2,n):
            data_break = data[i].split(",")
            name = data_break[0] + name_space[len(data_break[0]):]
            reps = data_break[1] + reps_space[len(data_break[1]):]
            kg = data_break[2] + kg_space[len(data_break[2]):]
            timer = data_break[3] + time_space[len(data_break[3]):]
            no = f"{i-1}" + no_space[len(str(i)):]
            done = data_break[4]
            if done == "y":
                done = "V"
            else:
                done = "O"

            print(f"{no}|{name}|{reps}|{kg}|{timer}|  {done}  ")

    else:
        print("Belum ada exercise apapun")
    print()
   

def select_exercise():
    print_exercises()
    n = len(Database.exercises)

    # ask user option
    while True:
        try:
            user_option = int(input("\nNo exercise yang ingin ditambah: ")) - 1

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


def print_summarized_routine():

    Database.refresh_routines()
    titles = Database.routines
    no = 1
    for title in titles:
        Database.clear_temp_routines()
        Database.create_temp_routine(title)
        data_temp = Database.temp_routine
        n = len(data_temp)

        if n > 1:
            exercises = []
            for i in range(1,n):
                data_break = data_temp[i].split(",")
                exercises.append(data_break[0])

            # menghitung jumlah set tiap gerakan di dalam rutinitas
            exercise_name = set(exercises)
            temp_dict = {}

            for name in exercise_name:
                temp_dict[name] = exercises.count(name)

            exercises = ""
            for key, item in temp_dict.items():
                exercises += f"{key} {item} set, "
            
            exercises = exercises[:-2] # ngilangin koma dan spasi pada exerc terakhir

        else:
            exercises = "tidak ada"

        name = data_temp[0] + name_space[len(data_temp[0]):]
        print(f"{no}. {name}: [{exercises}]")

        no += 1
   

def print_all_routines():
    Utility.clear_screen()
    Database.clear_temp_routines()
    Database.refresh_routines()

    for routine in Database.routines:
        Database.refresh_temp_routines(routine)
        View.print_routine()
        Database.clear_temp_routines()
        print()

    wait = input("Tekan enter untuk lanjut")

               