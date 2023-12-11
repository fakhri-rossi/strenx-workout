from . import Database, Utility, View, Edit, History
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
    History.time_start = time.strftime("%Y-%m-%d-%H-%M-%S-%z", time.gmtime())
    Database.refresh_temp_routines(routine_name)
    History.create_temp_history()
    is_continue = True
    routine_change = False
    
    while is_continue:
        Utility.clear_screen()
        print(History.temp_history)
        print(Database.temp_routine)
        View.print_running_workout()

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
            temp_data = Database.temp_routine
            user_option = input("\nPilihan Anda: ")
            match user_option:
                case "00": 
                    View.select_exercise()
                    routine_change = True
                    break

                case "01": 
                    n = len(temp_data)
                    for i in range(1, n):
                        temp_data[i] = temp_data[i][:-1] + "y"
                    break

                case "02": 
                    agree = Utility.user_confirm("Selesai berolahraga?")
                    if agree:
                        History.add_history()

                        if routine_change:
                            agree = Utility.user_confirm("APakah Anda ingin menyimpan perubahan pada rutinitas?")
                            if agree:
                                Edit.update_routine()

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
                    if len(user_option) != 2:
                        print("Masukkan opsi yang valid!")
                        continue

                    try:
                        user_option[0] = int(user_option[0])
                    except:
                        print("Masukkan angka, bukan yang lain!")
                        continue

                    if user_option[0] >= len(temp_data) or user_option[0] < 0:
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
                            check_set(user_option[0])
                            break

                        case _:
                            print("Opsi tidak tersedia")
                            break
                        
        if routine_change:
            History.create_temp_history()
        #     wait = input(":")

        Utility.clear_screen()   

def check_set(index:int):
    data = Database.temp_routine
    if data[index][-1] != "y":
        data[index] = data[index][:-1] + "y"

    elif data[index][-1] == "y":
        data[index] = data[index][:-1] + "n"
    else:
        print("Gagal mencentang")
    