import sys, os
previous_dirname = os.path.dirname(__file__) + "\.."
sys.path.append(previous_dirname)

from Operation import Utility, History

def history_page():
    is_continue = True

    while is_continue:
        Utility.clear_screen()
        print("="*100)
        print("Histori Rutinitas")
        print("="*100)
        
        History.print_history()

        print("\n" + "="*100)
        print("0. Kembali")
        user_option = input("Opsi: ")
        # print("(nomor).1 Lihat detail latihan")

        match user_option:
            case "0":
                is_continue = False
                break
            
            case _:
                print("Opsi tidak valid")
