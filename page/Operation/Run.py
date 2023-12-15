from . import Database, Utility, View, Edit
import time

def run_page():
    Database.refresh_routines()
    Utility.clear_screen()

    # heading
    print("="*51)
    print("Jalankan Rutinitas")
    print("="*51)

    # spill summarized routines
    View.print_summarized_routine()
    # print("0. Batal")

    try:
        index = Utility.ask_number("Rutinitas yang ingin dijalankan: ")-1

        if index < 0 or index >= len(Database.Database.routine_names):
            print("")
        else:
            run(index)
    except:
        print("Masukkan angka, bukan yang lain")

def run(index:int):
    Database.Database.time_start = Utility.get_current_time()
    routine_name = Database.Database.routine_names[index]
    Database.create_temp_list(routine_name)
    # Database.add_history()
    is_continue = True
    routine_change = False
    
    while is_continue:
        Utility.clear_screen()
        Database.Database.time_start = Utility.get_current_time()
        temp_list = Database.Database.temp_list
        n_data = len(temp_list)
        View.print_running_workout()

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
                    View.select_exercise()
                    break

                case "01": 
                    for i in range(1, n_data):
                        temp_list[i] = temp_list[i][:-1] + "y"
                    break

                case "02": 
                    if n_data > 2:
                        agree = Utility.user_confirm("Selesai berolahraga?")
                        if agree:
                            Database.Database.time_end = Utility.get_current_time()
                            Database.write_history()
                            is_continue = False
                            
                        else:
                            break

                        if routine_change:
                            print("Anda merubah susunan rutinitas")
                            agree = Utility.user_confirm("Apakah Anda ingin mengupdate rutinitas?")
                            if agree:
                                Database.update_routine()
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
                    if user_option[0] >= n_data or user_option[0] < 0:
                        print("Nomor exercise tidak ada")
                        continue

                    match user_option[1]:
                        case "1":
                            check_set(user_option[0])
                            break

                        case "2":
                            print("Edit set")
                            Edit.edit_set(user_option[0])
                            routine_change = True
                            break

                        case "3":
                            Edit.add_set(user_option[0])
                            routine_change = True               
                            break

                        case "4":
                            Edit.delete_set(user_option[0])
                            routine_change = True
                            break

                        case _:
                            print("Opsi tidak tersedia")
                            continue

        Utility.clear_screen()   

def check_set(index:int):
    temp_list = Database.Database.temp_list
    if temp_list[index][-1] == "n":
        temp_list[index] = temp_list[index][:-1] + "y"

    elif temp_list[index][-1] == "y":
        temp_list[index] = temp_list[index][:-1] + "n"
    else:
        print("Gagal mencentang")
    