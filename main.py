import CRUD as CRUD

if __name__=="__main__":
    CRUD.init_app()
    while True:
        CRUD.refresh_routines()
        CRUD.clear_screen()

        print("Welcome to Strenx Workout!")
        print("===============================")
        print("1. Jalankan Rutinitas")
        print("2. Lihat Rutinitas")
        print("3. Buat Rutinitas")
        print("4. Edit Rutinitas")
        print("5. Hapus Rutinitas")
        print("6. Lihat Histori")
        print("0. Keluar")

        user_option = input("Masukan opsi: ")
        match user_option:
            case "1": print("Menjalankan Rutinitas")
            case "2": CRUD.print_all_routines()
            case "3": CRUD.new_routine()
            case "4": CRUD.edit_routine()
            case "5": print("Menghapus Rutinitas")
            case "6": print("Melihat Histori")
            case "0": break
            case _: print("Opsi tidak tersedia")
        
        is_continue = input("Keluar? (y/n): ")
        if is_continue.lower() == "y":
            break