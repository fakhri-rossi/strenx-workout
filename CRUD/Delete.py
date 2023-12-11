from . import Database, Utility, View
import os

def delete_routine():
    Database.refresh_routines()
    Utility.clear_screen()
    print("="*51)
    print("Hapus Rutinitas")
    print("="*51)
    # spill summarized routines
    View.print_summarized_routine()

    while True:
        print(Database.routines)
        try:
            index = int(input("Nomor rutinitas yang ingin dihapus: "))
            if index < 1 or index > len(Database.routines):
                print("Nomor rutinitas tidak tersedia!")
                continue
            else:
                break
        except:
            print("Masukkan angka valid!")

    routine_name = Database.routines[index-1]
    agree = Utility.user_confirm("Yakin ingin menghapus?")
    if agree:
        os.remove(f"./routines/{routine_name}.txt")
    else:
        print("Tidak jadi menghapus")
    