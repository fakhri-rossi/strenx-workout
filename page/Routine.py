import sys, os
previous_dirname = os.path.dirname(__file__) + "\.."
sys.path.append(previous_dirname)

from Operation import CRUD, Database, Utility
from . import Workouting

temp_list = Database.temp_list
routine_names = Database.routine_names
exercises_dict = Database.exercises

name_space = Database.TEMPLATE["exercise_name"]
kg_space = Database.TEMPLATE["kg"]
reps_space = Database.TEMPLATE["reps"]
no_space = Database.TEMPLATE["no"]

def routine_page():
    is_continue = True

    while is_continue:
        Utility.clear_screen()
        print("=========================")
        print("DAFTAR RUTINITAS")
        print("=========================")
        print_summarized_routine()
        print("=========================")
        print("Opsi:")
        print("_1 Lihat Detail Rutinitas")
        print("_2 Jalankan Rutinitas")
        print("_3 Edit Rutinitas")
        print("_4 Hapus Rutinitas")
        print("\nOpsi lain:")
        print("0 Kembali")
        print("1 Buat rutinitas baru")

        while True:
            n_data = Utility.get_routine_total()

            user_option = input("\nnomor rutinitas(spasi)opsi: ")
            if user_option == "0":
                is_continue = False
                break

            elif user_option == "1":
                CRUD.new_routine()
                is_continue = False
                break

            user_option = user_option.split(" ")

            if len(user_option) != 2:
                print("Opsi tidak valid!")
                continue

            # memvalidasi index rutinitas
            try:
                user_option[0] = int(user_option[0]) - 1 # karena indeks dimlai dari nol

                if user_option[0] < 0 or user_option[0] >= n_data:
                    print("Nomor rutinitas tidak ada")
                    continue

            except:
                print("Nomor exercise tidak valid")
                continue

            match user_option[1]:
                case "1":
                    Utility.clear_screen()
                    print_routine(index=user_option[0])
                    agree = Utility.user_confirm("Apakah Anda ingin menjalankan rutinitas ini?")

                    if agree:
                        Workouting.workouting_page(user_option[0])
                        is_continue = False
                        break
                    else:
                        break
                    
                case "2":
                    Workouting.workouting_page(user_option[0])
                    is_continue = False
                    break

                case "3":
                    CRUD.edit_page(index = user_option[0])
                    is_continue = False
                    break

                case "4":
                    CRUD.delete_routine(user_option[0])
                    break

                case _:
                    print("Opsi tidak valid")

def print_summarized_routine():
    Database.refresh_routine_names()
    routine_names = Database.routine_names
    no = 1

    if len(Database.routine_names) > 0:
        for routine_name in routine_names:
            Database.create_temp_list(routine_name)
            temp_data = Database.temp_list
            n = len(Database.temp_list)

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

def print_routine(**kwargs):
    if "index" in kwargs:
        index = kwargs["index"]
        Database.create_temp_list(Database.routine_names[index])

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
