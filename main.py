import page as page

if __name__=="__main__":
    page.init_app()
    while True:
        page.refresh_routines()
        page.clear_screen()

        print("Welcome to Strenx Workout!")
        print("===============================")
        print("1. Lihat Rutinitas")
        print("2. Lihat Histori Latihan")
        print("3. Lihat Statistik")
        # print("4. Lihat Rutinitas")
        print("0. Keluar")

        user_option = input("Masukan opsi: ")
        match user_option:
            case "1": page.routine( )
            case "2": page.print_all_routines()
            case "3": page.new_routine()
            case "4": page.edit_routine()
            case "5": page.delete_routine()
            case "6": page.history_read()
            case "0": break
            case _: print("Opsi tidak tersedia")
        
        # is_continue = input("Keluar? (y/n): ")
        # if is_continue.lower() == "y":
        #     break