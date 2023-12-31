import sys, os
previous_dirname = os.path.dirname(__file__) + "\.."
sys.path.append(previous_dirname)

from Operation import CRUD, Database, Utility

name_space = Database.TEMPLATE["exercise_name"]
type_space = Database.TEMPLATE["exercise_name"]
reps_space = Database.TEMPLATE["reps"]
kg_space = Database.TEMPLATE["kg"]
time_space = Database.TEMPLATE["time"]
no_space = Database.TEMPLATE["no"]
muscle_target = Database.TEMPLATE["muscle_target"]

temp_list = Database.temp_list

def workouting_page(index:int):
    Database.time_start = Utility.get_current_time()
    routine_name = Database.routine_names[index]
    Database.create_temp_list(routine_name)
    is_continue = True
    routine_change = False
    
    while is_continue:
        Utility.clear_screen()
        n_data = len(temp_list)
        print_running_workout()

        print("\nnomor(spasi)opsi untuk memilih")
        print("Contoh: 3 1 untuk mengedit exercise no.3")

        print("_1 Ceklis set/batalkan ceklis set")
        print("_2 Edit exercise")
        print("_3 Duplikatkan exercise")
        print("_4 Hapus exercise")

        print("\nOpsi lain: ")
        print("00 Menambahkan exercise")
        print("01 Ceklis semua exercise")
        print("02 Selesai")
        print("03 Batalkan olahraga")
        
        while True:
            user_option = input("\nnomor(spasi)opsi: ")
            match user_option:
                case "00": 
                    CRUD.select_exercise()
                    routine_change = True
                    break

                case "01": 
                    for i in range(1, n_data):
                        temp_list[i] = temp_list[i][:-1] + "y"
                    break

                case "02": 
                    if n_data > 1:
                        agree = Utility.user_confirm("Selesai berolahraga?")
                        if agree:
                            Database.time_end = Utility.get_current_time()
                            Database.write_history()
                            is_continue = False
                            
                        else:
                            break

                        if routine_change:
                            agree = Utility.user_confirm("Anda merubah susunan rutinitas. Apakah Anda ingin mengupdate rutinitas?")
                            if agree:
                                Database.update_routine()
                                # konfirmasi sistem terdapat di function update_routine()
                                Utility.wait()
                            else:
                                print("Perubahan pada rutinitas tidak disimpan")
                                Utility.wait()
                        break
                    # untuk antisipasi jika user menyelesaikan latihan kosong
                    else:
                        print("Anda belum menyelesaikan latihan apapun")
                        print("Anda tidak bisa merekap latihan")
                        exit = Utility.user_confirm("Apakah Anda ingin keluar?")

                        if exit:
                            is_continue = False
                            break

                case "03": 
                    agree = Utility.user_confirm("Yakin membatalkan olahraga?")
                    if agree:
                        is_continue = False
                        break
                    else:
                        break

                case _:
                    user_option = user_option.split(" ")
                    if len(user_option) != 2:
                        print("Masukkan opsi yang valid!")
                        continue
                    try:
                        user_option[0] = int(user_option[0])# karena indeks isi rutinitas dimulai dari 1
                    except:
                        print("Masukkan angka, bukan yang lain!")
                        continue
                    if user_option[0] >= n_data or user_option[0] < 1:
                        print("Nomor exercise tidak ada")
                        continue

                    match user_option[1]:
                        case "1":
                            check_set(user_option[0])
                            break

                        case "2":
                            print("Edit set")
                            Utility.edit_set(user_option[0])
                            routine_change = True
                            break

                        case "3":
                            Utility.add_set(user_option[0])
                            routine_change = True               
                            break

                        case "4":
                            Utility.delete_set(user_option[0])
                            routine_change = True
                            break

                        case _:
                            print("Opsi tidak tersedia")
                            continue

        Utility.clear_screen()   

def check_set(index:int):
    if temp_list[index][-1] == "n":
        temp_list[index] = temp_list[index][:-1] + "y"

    elif temp_list[index][-1] == "y":
        temp_list[index] = temp_list[index][:-1] + "n"
    else:
        print("Gagal mencentang")
    
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
                Database.temp_list[i] = f"{Database.temp_list[i]},n"

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
   