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
        print("1_ Lihat Detail Rutinitas")
        print("2_ Jalankan Rutinitas")
        print("3_ Buat Rutinitas")
        print("4_ Edit Rutinitas")
        print("5_ Hapus Rutinitas")
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
                user_option[1] = int(user_option[1]) - 1 # karena indeks dimlai dari nol

                if user_option[1] < 0 or user_option[1] >= n_data:
                    print("Nomor rutinitas tidak ada")
                    continue

            except:
                print("Nomor exercise tidak valid")
                continue

            match user_option[0]:
                case "1":
                    Operation.Utility.clear_screen()
                    Operation.print_detailed_routine(user_option[1])
                    agree = Operation.Utility.user_confirm("Apakah Anda ingin menjalankan rutinitas ini?")

                    if agree:
                        Operation.run(user_option[1])
                        is_continue = False
                        break
                    else:
                        break
                    
                case "2":
                    Operation.run_routine()
                case "3":
                    Operation.create_routine()
                case "4":
                    Operation.edit_routine()
                case "5":
                    Operation.delete_routine()
                # case "0":
                #     is_continue = False
                #     return
                case _:
                    print("Opsi tidak valid")
            
