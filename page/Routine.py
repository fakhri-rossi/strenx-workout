from . import Operation

def routine():
    Operation.print_summarized_routine()
    print("=========================")
    print("1_ Lihat Detail Rutinitas")
    print("2_ Jalankan Rutinitas")
    print("3_ Buat Rutinitas")
    print("4_ Edit Rutinitas")
    print("5_ Hapus Rutinitas")
    print("0_ Kembali")

    while True:
        user_option = input("opsi(spasi)nomor rutinitas: ")
        user_option = user_option.split(" ")

        if len(user_option) != 2:
            print("Opsi tidak valid!")
            continue

        try:
            user_option[1] = int(user_option[1]) - 1 # karena indeks dimlai dari nol
        except:
            print("Nomor exercise tidak valid")
            continue

        match user_option[0]:
            case "1":
                Operation.print_detailed_routine(user_option[1])
            case "2":
                Operation.run_routine()
            case "3":
                Operation.create_routine()
            case "4":
                Operation.edit_routine()
            case "5":
                Operation.delete_routine()
            case "0":
                break
            case _:
                print("Opsi tidak valid")