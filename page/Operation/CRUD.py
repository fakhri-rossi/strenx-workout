from . import Utility, Database, View

def new_routine():
    Utility.clear_screen()
    print("="*100)
    print("Membuat Rutinitas")
    print("="*100)

    Database.Database.temp_list.clear()
    # Membuat judul rutinitas
    routine_name = Utility.ask_routine_name()  
    edit_page(routine_name = routine_name)

def delete_routine(index):
    routine_name = Database.Database.routine_names[index]
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
        routine_name = Database.Database.routine_names[index]
    
    else:
        print("Eror: rutinitas tidak ditemukan")
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
                        Utility.wait()
                
                    else:
                        is_continue = False
                        print("Rutinitas tidak disimpan")
                        Utility.wait()
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
                            Utility.edit_set(user_option[0])
                            break

                        case "2":
                            Utility.add_set(user_option[0])
                            break

                        case "3":
                            Utility.delete_set(user_option[0])
                            break

        Utility.clear_screen()   

