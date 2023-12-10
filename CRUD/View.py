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

    while True:
        print(Database.routines)
        try:
            index = int(input("Nomor rutinitas yang ingin diupdate: "))
            if index < 1 or index > len(Database.routines):
                print("Nomor rutinitas tidak tersedia!")
                continue
            else:
                # routine_name = Database.routines[index-1]
                # Operation.edit(routine_name)
                break
        except:
            print("Masukkan angka valid!")
    routine_name = Database.routines[index-1]
    Operation.edit(routine_name)
                    
def delete_routine():
    pass
def history():
    pass