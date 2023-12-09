import CRUD as CRUD

if __name__=="__main__":
    while True:
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
            case "2": print("Melihat Rutinitas")
            case "3": print("Membuat Rutinitas")
            case "4": print("Mengedit Rutinitas")
            case "5": print("Menghapus Rutinitas")
            case "6": print("Melihat Histori")
            case "0": break
            case _: print("Opsi tidak tersedia")
        
        is_exit = input("Apakah Anda ingin keluar? (y/n): ")
        if is_exit.lower() == "y":
            break