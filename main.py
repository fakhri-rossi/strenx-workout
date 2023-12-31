from Page import Routine, History
from Operation import Utility, Database

if __name__=="__main__":
    Database.init_app()

    is_continue = True

    while is_continue:
        Database.refresh_routine_names()
        Utility.clear_screen()
        print("Welcome to Strenx Workout!")
        print("===============================")
        print("1. Lihat Rutinitas")
        print("2. Lihat Histori Latihan")
        print("0. Keluar")

        while True:
            user_option = input("Masukan opsi: ")
            match user_option:
                case "1": 
                    Routine.routine_page( )
                    break
                case "2": 
                    History.history_page()
                    break
                case "0": 
                    is_continue = False
                    break
                case _: print("Opsi tidak tersedia")
            
