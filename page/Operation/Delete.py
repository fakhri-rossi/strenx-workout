from . import Database, Utility, View
import os

def delete_routine():
    n_data = len(Database.Database.temp_list)
    Utility.clear_screen()
    print("="*51)
    print("Hapus Rutinitas")
    print("="*51)
    # spill summarized routines
    View.print_summarized_routine()

    while True:
        try:
            index = int(input("Nomor rutinitas yang ingin dihapus: "))-1
            if index < 0 or index >= n_data:
                print("Nomor rutinitas tidak tersedia!")
                continue

            else:
                routine_name = Database.Database.routine_names[index]
                agree = Utility.user_confirm("Yakin ingin menghapus?")
                if agree:
                    Database.delete_routine()
                else:
                    print("Tidak jadi menghapus")
        except:
            print("Masukkan angka valid!")

    
    