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

<<<<<<< HEAD
        user_option = input("Masukan opsi: ")
        match user_option:
            case "1": CRUD.run_routine( )
            case "2": CRUD.print_all_routines()
            case "3": CRUD.new_routine()
            case "4": CRUD.edit_routine()
            case "5": CRUD.delete_routine()
            case "6": CRUD.history_page()
            case "0": break
            case _: print("Opsi tidak tersedia")
        
        # is_continue = input("Keluar? (y/n): ")
        # if is_continue.lower() == "y":
        #     break
=======
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
            
>>>>>>> test
