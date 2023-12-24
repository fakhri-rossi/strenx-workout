from . import Operation

def history_page():
    is_continue = True

    while is_continue:
        Operation.clear_screen()
        print("="*50)
        print("Histori Rutinitas")
        print("="*50)
        
        Operation.print_history()

        print("0. Kembali")
        user_option = input("Opsi: ")
        # print("(nomor).1 Lihat detail latihan")

        match user_option:
            case "0":
                is_continue = False
                break
            
            case _:
                print("Opsi tidak valid")
