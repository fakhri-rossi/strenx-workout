from . import Database, Utility, View
import os

def delete_routine(index):
    routine_name = Database.Database.routine_names[index]
    agree = Utility.user_confirm(f"Yakin ingin menghapus {routine_name}?")

    if agree:
        Database.delete_routine(routine_name)
    else:
        print("Tidak jadi menghapus")
    
    Utility.wait()
    