from . import Utility, Database, Operation
import os

def run_routine():
    pass

def print_all_routines():
    Utility.clear_screen()
    Database.clear_temp_routines()
    Database.refresh_routines()

    for routine in Database.routines:
        # file_name = "./routines/" + routine + ".txt"
        Operation.print_routine(routine)
        Database.clear_temp_routines()
        print()

def new_routine():
    Utility.clear_screen()
    print("\n" + "="*100)
    print("Membuat Rutinitas")

    Operation.create_routine()

def edit_routine():
    Database.refresh_routines()
    Utility.clear_screen()
    print("="*51)
    print("Mengedit Rutinitas")
    print("="*51)
    # spill summarized routines
    Operation.print_summarized_routine()
    print("0. Tidak jadi mengupdate")

    while True:
        try:
            index = int(input("Nomor rutinitas yang ingin diupdate: "))-1
            if index < -1 or index >= len(Database.routines):
                print("Nomor rutinitas tidak tersedia!")
                continue

            elif index == -1:
                print("Tidak jadi meng-update rutinitas")
                break

            else:
                routine_name = Database.routines[index]
                Operation.edit(routine_name)
                break
        except:
            print("Masukkan angka valid!")
    
                    
def delete_routine():
    Database.refresh_routines()
    Utility.clear_screen()
    print("="*51)
    print("Hapus Rutinitas")
    print("="*51)
    # spill summarized routines
    Operation.print_summarized_routine()

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
    
def history():
    pass