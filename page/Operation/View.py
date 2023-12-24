from . import Utility, Database
import os

name_space = Database.Database.TEMPLATE["exercise_name"]
type_space = Database.Database.TEMPLATE["exercise_name"]
reps_space = Database.Database.TEMPLATE["reps"]
kg_space = Database.Database.TEMPLATE["kg"]
time_space = Database.Database.TEMPLATE["time"]
no_space = Database.Database.TEMPLATE["no"]
muscle_target = Database.Database.TEMPLATE["muscle_target"]

routine_names = Database.Database.routine_names
temp_list = Database.Database.temp_list
exercises_dict = Database.Database.exercises

def print_exercises():  
    # print heading
    Utility.clear_screen()
    print("Select Exercise")
    print("-"* 93)
    print(f"No  |Exercise Name" + " "*17 + "|Exercise Type" + " "*17 +"|Muscle Target" + " "*17)
    print("-"* 93)

    n = len(exercises_dict)

    # print content
    counter = 1
    for i in range(n):
        str_counter = str(counter)
        no = f"{str_counter + no_space[len(str_counter):]}"

        exercise_name = exercises_dict[i]["name"]
        exercise_name += name_space[len(exercise_name):]

        exercise_type = exercises_dict[i]["type"]
        exercise_type += type_space[len(exercise_type):]

        muscle_target = exercises_dict[i]["muscle_target"].split("-")
        muscle_target = ", ".join(muscle_target)
        muscle_target += muscle_target[len(muscle_target):]

        print(f"{no}|{exercise_name}|{exercise_type}|{muscle_target}")
        counter += 1

def print_detailed_routine(index):
    if index < 0 or index >= len(routine_names):
        print("Nomor rutinitas tidak ada\n")
        return
    
    else:
        # indeks pertama temp_routine berisi nama routine
        Database.Database.create_temp_list(routine_names[index])
        routine_name = temp_list[0]
        print("="*51)
        print(routine_name)
        print("="*51)

        n = len(temp_list)

        print("No  |Exercise" + " "*22 + "|Reps|Kg  |Timer")
        print("-"*51)

        if n > 1:
            for i in range(1,n):
                data_break = temp_list[i].split(",")
                name = data_break[0] + name_space[len(data_break[0]):]
                reps = data_break[1] + reps_space[len(data_break[1]):]
                kg = data_break[2] + kg_space[len(data_break[2]):]
                timer = data_break[3]
                no = f"{i}" + no_space[len(str(i)):]

                print(f"{no}|{name}|{reps}|{kg}|{timer}")

        else:
            print("Belum ada exercise apapun")
        print()


def print_routine():        
    data = temp_list
    routine_name = temp_list[0]
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

def print_running_workout():
    data = temp_list
    n = len(data)
    routine_name = temp_list[0]

    # print heading
    print("\n" + "="*57)
    print(routine_name)
    print("="*57)
    print("No  |Exercise" + " "*22 + "|Reps|Kg  |Timer|Done?")
    print("-"*57)

    if n > 1:
        for i in range(1,n):
            if temp_list[i].count(",") == 3:
                Database.Database.temp_list[i] = f"{Database.Database.temp_list[i]},n"

            data_break = data[i].split(",")
            name = data_break[0] + name_space[len(data_break[0]):]
            reps = data_break[1] + reps_space[len(data_break[1]):]
            kg = data_break[2] + kg_space[len(data_break[2]):]
            timer = data_break[3] + time_space[len(data_break[3]):]
            no = f"{i}" + no_space[len(str(i)):]
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
    n = len(exercises_dict)

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
    
    exercise_name = exercises_dict[user_option]["name"]
    exercise_type = exercises_dict[user_option]["type"]

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

            Database.Database.temp_list.append(str_exercise)
            break
        
        except:
            print("Masukkan input yang valid!")


def print_summarized_routine():
    Database.Database.refresh_routine_names()
    routine_names = Database.Database.routine_names
    no = 1

    if len(Database.Database.routine_names) > 0:
        for routine_name in routine_names:
            Database.create_temp_list(routine_name)
            temp_data = Database.Database.temp_list
            n = len(Database.Database.temp_list)

            if n > 1:
                exercises = []
                for i in range(1,n):
                    data_break = temp_data[i].split(",")
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

            name = temp_data[0] + name_space[len(temp_data[0]):]
            print(f"{no}. {name}: [{exercises}]")

            no += 1
    else:
        print("Belum ada rutinitas yang terdaftar")
           

def print_summarized_history():
    
    pass