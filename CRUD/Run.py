from . import Database, Utility, View, Edit
import time

def run_routine():
    Database.refresh_routines()
    Utility.clear_screen()

    # heading
    print("="*51)
    print("Jalankan Rutinitas")
    print("="*51)

    # spill summarized routines
    View.print_summarized_routine()
    print("0. Batal")
    index = Utility.ask_number("Rutinitas yang ingin dijalankan: ")

    if index > -1:
        routine_name = Database.routines[index]
        run_page(routine_name)
    else:
        print("Tidak jadi menjalankan rutinitas")

def run_page(routine_name):
    time_start = time.strftime("%Y-%m-%d-%H-%M-%S-%z", time.gmtime())
    Database.refresh_temp_routines(routine_name)
    Database.create_temp_history(time_start, routine_name)
    is_continue = True
    routine_change = False
    
    while is_continue:
        Utility.clear_screen()
        print(Database.temp_history)
        print(Database.temp_routine)
        View.print_running_workout(routine_name)

        print("\n'nomor(spasi)opsi' untuk memilih")
        print("Contoh: 3 1 untuk mengedit exercise no.3")

        print("_1 Edit")
        print("_2 Tambahkan set")
        print("_3 Hapus set")
        print("_4 Ceklis/batalkan ceklis set")

        print("\nOpsi lain: ")
        print("00 Menambahkan exercise")
        print("01 Ceklis semua exercise")
        print("02 Selesai")
        print("03 Batalkan olahraga")
        
        while True:
            user_option = input("\nPilihan Anda: ")
            match user_option:
                case "00": 
                    View.select_exercise()
                    break

                case "01": 
                    data = Database.temp_history
                    n = len(data)
                    for i in range(2, n):
                        Database.temp_history[i] = Database.temp_history[i][:-1] + "y"
                    break

                case "02": 
                    agree = Utility.user_confirm("Selesai berolahraga?")
                    if agree:
                        Database.add_history()
                        is_continue = False
                        break
                    else:
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
                    if len(user_option) > 2:
                        print("Masukkan opsi yang valid!")
                        continue
                    try:
                        user_option[0] = int(user_option[0])# karena indeks isi ruitnitas dimulai dari 2
                    except:
                        print("Masukkan angka, bukan yang lain!")
                        continue
                    if user_option[0] >= len(Database.temp_routine) or user_option[0] < 1:
                        print("Nomor exercise tidak ada")
                        continue

                    match user_option[1]:
                        case "1":
                            print("Edit set")
                            Edit.edit_set(user_option[0])
                            routine_change = True
                            break

                        case "2":
                            Edit.add_set(user_option[0])
                            routine_change = True               
                            break

                        case "3":
                            Edit.delete_set(user_option[0])
                            routine_change = True
                            break

                        case "4":
                            check_set(user_option[0]+1)
                            break

                        case _:
                            print("Opsi tidak tersedia")
                            break

        Utility.clear_screen()   
    Database.clear_temp_routines()

def check_set(index:int):
    if Database.temp_history[index][-1] == "n":
        Database.temp_history[index] = Database.temp_history[index][:-1] + "y"

    elif Database.temp_history[index][-1] == "y":
        Database.temp_history[index] = Database.temp_history[index][:-1] + "n"
    else:
        print("Gagal mencentang")
    