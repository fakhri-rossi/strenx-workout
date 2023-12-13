from . import Utility, Database, Edit

def new_routine():
    Utility.clear_screen()
    print("="*100)
    print("Membuat Rutinitas")
    print("="*100)
    print("0. kembali")

    Database.clear_temp_routines()
    # Membuat judul rutinitas
    while True:
        routine_name = input("Nama Rutinitas: ")

        if len(routine_name) > len(Database.TEMPLATE["routine_name"]):
            print("Nama terlalu panjang!")
            print("Panjang maksimal adalah 34 kata")
        
        elif routine_name == "0":
            return

        elif routine_name not in Database.routines:
            Database.temp_routine.append(routine_name)
            # Database.create()
            break

        else:
            print("Rutinitas sudah ada, buat nama lain")

    Edit.edit(routine_name)
    Database.clear_temp_routines()

# def create_routine():
#     Database.clear_temp_routines()
#     # Membuat judul rutinitas
#     while True:
#         routine_name = input("Nama Rutinitas: ")   

#         if routine_name not in Database.routines:
#             Database.temp_routine.append(routine_name)
#             Database.create()
#             break

#         else:
#             print("Rutinitas sudah ada, buat nama lain")
#     Edit.edit(routine_name)
#     Database.clear_temp_routines()
