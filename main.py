import page as page

if __name__=="__main__":
    page.init_app()

    is_continue = True

    while is_continue:
        page.refresh_routine_names()
        page.Utility.clear_screen()
        print("Welcome to Strenx Workout!")
        print("===============================")
        print("1. Lihat Rutinitas")
        print("2. Lihat Histori Latihan")
        print("3. Lihat Statistik")
        print("0. Keluar")

        while True:
            user_option = input("Masukan opsi: ")
            match user_option:
                case "1": 
                    page.routine( )
                    break
                case "2": 
                    page.history_page()
                    break
                case "3": 
                    print("Melihat statistik")
                    break
                case "0": 
                    is_continue = False
                    break
                case _: print("Opsi tidak tersedia")
            
