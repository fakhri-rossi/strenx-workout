from . import Utility, Database, Edit

def new_routine():
    Utility.clear_screen()
    print("="*100)
    print("Membuat Rutinitas")
    print("="*100)

    Database.clear_temp_routines()
    # Membuat judul rutinitas
    while True:
        routine_name = input("Nama Rutinitas: ")   

        if routine_name not in Database.routines:
            Database.Database.temp_list.append(routine_name)
            Database.Database.write_routine()
            break

        else:
            print("Rutinitas sudah ada, buat nama lain")

    Edit.edit(routine_name)
    Database.clear_temp_routines()

