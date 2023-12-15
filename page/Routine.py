from . import Operation

def routine():
    is_continue = True

    while is_continue:
        Operation.Utility.clear_screen()
        print("=========================")
        print("DAFTAR RUTINITAS")
        print("=========================")
        Operation.print_summarized_routine()
        print("=========================")
        print("_1 Lihat Detail Rutinitas")
        print("_2 Jalankan Rutinitas")
        print("_3 Buat Rutinitas")
        print("_4 Edit Rutinitas")
        print("_5 Hapus Rutinitas")
        print("0 Kembali")

        while True:
            n_data = Operation.Utility.get_routine_total()

            user_option = input("\nopsi(spasi)nomor rutinitas: ")
            if user_option == "0":
                is_continue = False
                break

            user_option = user_option.split(" ")

            if len(user_option) != 2:
                print("Opsi tidak valid!")
                continue

            try:
                user_option[0] = int(user_option[0]) - 1 # karena indeks dimlai dari nol

                if user_option[0] < 0 or user_option[0] >= n_data:
                    print("Nomor rutinitas tidak ada")
                    continue

            except:
                print("Nomor exercise tidak valid")
                continue

            match user_option[1]:
                case "1":
                    Operation.Utility.clear_screen()
                    Operation.print_detailed_routine(user_option[0])
                    agree = Operation.Utility.user_confirm("Apakah Anda ingin menjalankan rutinitas ini?")

                    if agree:
                        Operation.run(user_option[0])
                        is_continue = False
                        break
                    else:
                        break
                    
                case "2":
                    Operation.run(user_option[0])
                    is_continue = False
                    break
                case "3":
                    Operation.create_routine()
                    is_continue = False
                    break
                case "4":
                    Operation.edit_page(index = user_option[0])
                    is_continue = False
                    break
                case "5":
                    Operation.delete_routine()
                    break
                case _:
                    print("Opsi tidak valid")
            
