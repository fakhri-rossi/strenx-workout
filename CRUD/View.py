from . import Utility, Database, Operation

def print_routine(routine_name):
    file_name = Database.routine_path + routine_name + ".txt"

    with open(file_name, "r") as file:
        title = file.readline()
        lines = []

        print("\n" + "="*50)
        print(routine_name)
        print("-"*50)

def run_routine():
    pass
def display_routine():
    pass

def display_exercise():
    with open("exercise.txt","r+") as file:
        file.seek()
        content = file.readlines()
        print("\nList Exercise: ")
        list_exercise = []
        for data in content:
            list_exercise.append(data)
        print(list_exercise)

def create_routine():
    Utility.clear_screen()
    print("\n" + "="*100)
    print("Membuat Rutinitas")

    while True:
        routine_name = input("Nama Rutinitas: ")   
        if routine_name not in Database.routines:
            Operation.create(routine_name)
            break
        else:
            print("Rutinitas sudah ada, buat nama lain")
    
    while True:
        Utility.clear_screen()
        print_routine(routine_name)

        print("1. Edit")
        print("2. Tambahkan set")
        print("3. Hapus set")
        print("00 untuk menambahkan Exercise")
        print("01 untuk menyimpan dan keluar")
        print("02 untuk batal dan keluar")
        print("\n'nomor(titik)opsi' untuk memilih")
        print("Contoh: 3.1 untuk mengedit exercise no.3")

        user_option = input("Pilihan Anda: ")
        match user_option:
            case "00": Operation.select_exercise()
            case "02": break

        # display_exercise()
        wait = input(":: ")

def edit_routine():
    pass
def delete_routine():
    pass
def history():
    pass