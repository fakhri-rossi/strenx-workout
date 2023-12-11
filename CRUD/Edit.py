from . import Database, View, Utility

def edit_routine():
    Database.refresh_routines()
    Utility.clear_screen()

    # heading
    print("="*51)
    print("Mengedit Rutinitas")
    print("="*51)
    # spill summarized routines
    View.print_summarized_routine()

    print("0. Batal")
    index = Utility.ask_number("Rutinitas yang ingin diupdate: ")

    if index > -1:
        routine_name = Database.routines[index]
        edit(routine_name)
    else:
        print("Tidak jadi meng-update rutinitas")
      

def edit(routine_name):
    Database.refresh_temp_routines(routine_name)
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
                        Database.create()
                        is_continue = False
                
                    else:
                        is_continue = False
                    break

                case "02": 
                    # rename_routine()
                    new_name = input("Nama rutinitas: ")
                    Database.old_name = Database.temp_routine[0] # menyimpan nama rutinitas lama ke dalam variabel
                    Database.temp_routine[0] = new_name
                    routine_name = Database.temp_routine[0]
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
                    if user_option[0] >= len(Database.temp_routine) or user_option[0] < 1:
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
    data = Database.temp_routine[index]
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
    Database.temp_routine[index] = data_str # update data

def add_set(index:int):
    data = Database.temp_routine[index]
    Database.temp_routine.insert(index+1,data)

def delete_set(index:int):
    Database.temp_routine.pop(index)

def rename_routine():
    new_name = input("Nama rutinitas: ")
    Database.temp_routine[0] = new_name
    Database.create()
    # Database.refresh_temp_routines(new_name)
