from . import Utility, Database, Edit

def new_routine():
    Utility.clear_screen()
    print("="*100)
    print("Membuat Rutinitas")
    print("="*100)

    Database.Database.temp_list.clear()
    # Membuat judul rutinitas
    routine_name = Utility.ask_routine_name()  
    Edit.edit_page(routine_name = routine_name)

