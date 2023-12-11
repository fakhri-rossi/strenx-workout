from . import Utility, Database, Edit

def new_routine():
    Utility.clear_screen()
    print("\n" + "="*100)
    print("Membuat Rutinitas")

    create_routine()

def create_routine():
    Database.clear_temp_routines()
    # Membuat judul rutinitas
    while True:
        routine_name = input("Nama Rutinitas: ")   

        if routine_name not in Database.routines:
            Database.temp_routine.append(routine_name)
            Database.create()
            break

        else:
            print("Rutinitas sudah ada, buat nama lain")
    Edit.edit(routine_name)
    Database.clear_temp_routines()
