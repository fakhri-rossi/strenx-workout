import sys, os
previous_dirname = os.path.dirname(__file__) + "\.."
sys.path.append(previous_dirname)

from . import Utility, Database
from Page import Routine

temp_list = Database.temp_list
routine_names = Database.routine_names
exercises_dict = Database.exercises

name_space = Database.TEMPLATE["exercise_name"]
type_space = Database.TEMPLATE["exercise_name"]
reps_space = Database.TEMPLATE["reps"]
kg_space = Database.TEMPLATE["kg"]
time_space = Database.TEMPLATE["time"]
no_space = Database.TEMPLATE["no"]
muscle_target = Database.TEMPLATE["muscle_target"]

def new_routine():
    Utility.clear_screen()
    print("="*100)
    print("Membuat Rutinitas")
    print("="*100)

    Database.temp_list.clear()
    # Membuat judul rutinitas
    routine_name = Utility.ask_routine_name()
    agree = Utility.user_confirm(f"Apakah Anda ingin membuat {routine_name}?")
    if agree:
        Database.temp_list.append(routine_name)
        Database.write_routine()
        print("Rutinitas berhasil dibuat")
        Utility.wait()
        edit_page(routine_name = routine_name)
    else:
        print("Rutinitas tidak jadi dibuat")
        Utility.wait()
        return        

def delete_routine(index):
    routine_name = Database.routine_names[index]
    agree = Utility.user_confirm(f"Yakin ingin menghapus {routine_name}?")

    if agree:
        Database.delete_routine(routine_name)
    else:
        print("Tidak jadi menghapus")
    
    Utility.wait()

def edit_page(**kwargs):
    if "routine_name" in kwargs:
        routine_name = kwargs["routine_name"]

    elif "index" in kwargs:
        index = int(kwargs["index"])
        routine_name = Database.routine_names[index]
    
    else:
        print("Eror: rutinitas tidak ditemukan")
        return
    
    Database.create_temp_list(routine_name)
    is_continue = True
    
    while is_continue:
        Utility.clear_screen()
        Routine.print_routine()

        print("\n'nomor(spasi)opsi' untuk memilih")
        print("Contoh: 3 1 untuk mengedit exercise no.3")

        print("_1 Edit")
        print("_2 Tambahkan set")
        print("_3 Hapus set")

        print("\nOpsi lain: ")
        print("00 Menambahkan exercise")
        print("01 Keluar")
        print("02 Rename rutinitas")

        while True:
            user_option = input("\nPilihan Anda: ")
            match user_option:
                case "00": 
                    select_exercise()
                    break

                case "01": 
                    agree = Utility.user_confirm("Simpan perubahan rutinitas?")
                    if agree:
                        Database.write_routine()
                        print("Rutinitas berhasil diedit")
                        is_continue = False
                        Utility.wait()
                
                    else:
                        is_continue = False
                        print("Perubahan rutinitas tidak disimpan")
                        Utility.wait()
                    break

                case "02": 
                    # rename_routine()
                    new_name = Utility.ask_routine_name()
                    Database.old_name = Database.temp_list[0] # menyimpan nama rutinitas lama ke dalam variabel
                    Database.temp_list[0] = new_name
                    routine_name = Database.temp_list[0]
                    break

                case _:
                    user_option = user_option.split(" ")
                    if len(user_option) != 2:
                        print("Masukkan opsi yang valid!")
                        continue
                    try:
                        user_option[0] = int(user_option[0])
                    except:
                        print("Masukkan angka, bukan yang lain!")
                        continue
                    if user_option[0] >= len(Database.temp_list) or user_option[0] < 1:
                        print("Nomor exercise tidak ada")
                        continue

                    match user_option[1]:
                        case "1":
                            print("Edit set")
                            Utility.edit_set(user_option[0])
                            break

                        case "2":
                            Utility.add_set(user_option[0])
                            break

                        case "3":
                            Utility.delete_set(user_option[0])
                            break

                        case _:
                            print("Opsi tidak tersedia!")

        Utility.clear_screen()   

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

            Database.temp_list.append(str_exercise)
            break
        
        except:
            print("Masukkan input yang valid!")

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