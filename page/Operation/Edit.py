from . import Database, View, Utility

done_status = ["y","n"]

def edit_page(**kwargs):
    if "routine_name" in kwargs:
        routine_name = kwargs["routine_name"]

    elif("index" in kwargs):
        index = int(kwargs["index"])
        routine_name = Database.Database.routine_names[index]
    
    else:
        print("Eror nama rutinitas tidak ditemukan")
        return
    
    Database.create_temp_list(routine_name)
    is_continue = True
    
    while is_continue:
        Utility.clear_screen()
        View.print_routine()

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
                    View.select_exercise()
                    break

                case "01": 
                    agree = Utility.user_confirm("Simpan perubahan rutinitas?")
                    if agree:
                        Database.write_routine()
                        is_continue = False
                
                    else:
                        is_continue = False
                    break

                case "02": 
                    # rename_routine()
                    new_name = Utility.ask_routine_name()
                    Database.Database.old_name = Database.Database.temp_list[0] # menyimpan nama rutinitas lama ke dalam variabel
                    Database.Database.temp_list[0] = new_name
                    routine_name = Database.Database.temp_list[0]
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
                    if user_option[0] >= len(Database.Database.temp_list) or user_option[0] < 1:
                        print("Nomor exercise tidak ada")
                        continue

                    match user_option[1]:
                        case "1":
                            print("Edit set")
                            edit_set(user_option[0])
                            break

                        case "2":
                            add_set(user_option[0])
                            break

                        case "3":
                            delete_set(user_option[0])
                            break

        Utility.clear_screen()   
    # Database.clear_temp_routines()

def edit_set(index:int):
    data = Database.Database.temp_list[index]
    data_break = data.split(",")

    # reps
    if data_break[1] != "-":
        reps = Utility.ask_reps()
    else:
        reps = "-"
    # kg
    if data_break[2] != "-":
        kg = Utility.ask_kg()
    else:
        kg = "-"
    # timer
    if data_break[3] != "-":
        timer = Utility.ask_timer()
    else:
        timer = "-"

    data_str = f"{data_break[0]},{reps},{kg},{timer}"
    Database.Database.temp_list[index] = data_str # update data

def add_set(index:int):
    data = Database.Database.temp_list[index]
    if data[-1] in done_status:
        data = data[:-2] + ",n"

    Database.Database.temp_list.insert(index+1,data)

def delete_set(index:int):
    Database.Database.temp_list.pop(index)

def rename_routine():
    new_name = input("Nama rutinitas: ")
    while True:
        if new_name in Database.Database.routine_names:
            print("Nama rutinitas sudah ada")
        else:
            Database.Database.temp_list[0] = new_name
            # Database.write_routine()
    # Database.refresh_temp_routines(new_name)
