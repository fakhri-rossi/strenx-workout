import os
from .import Database, Operation

def clear_screen():
    sistem_operasi = os.name
    match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
          
def user_confirm(message:str) -> bool:
      message += " (y/n): "

      while True:
        agree = input(message).lower()
        if agree == "y":
            return True
        elif agree == "n":
            return False
        else:
             print("Input jawaban yang valid!")

def file_to_list(file_name:str) -> list:
    line_list = []
    with open(file_name, "r") as file:
        content = file.readlines()

        for line in content:
            line_list.append(line[:-1])
    return line_list
    
def ask_number(message:str) -> int:
    while True:
        try:
            index = int(input(message))-1
            if index < -1 or index >= len(Database.routines):
                print("Nomor rutinitas tidak tersedia!")
                continue

            else:
                routine_name = Database.routines[index]
                return index

        except:
            print("Masukkan angka valid!")

def ask_reps() -> int:
     while True:
        try:
            reps = int(input("Reps: "))
            return reps
        except:
            print("Masukkan Repetisi yang valid!")
      
def ask_kg():
    try:
        kg = int(input("Berat beban: "))
        return kg
    except:
        print("Masukkan berat yang valid!")

def ask_timer()-> str:
    while True:
        timer = input("Time (mm:ss): ")
        if timer[2] != ":":
            print("Input valid time!")
            continue
        else:
            try:
                inttime = int(timer[:2])
                inttime = int(timer[3:])
                return timer
            except:
                print("Input valid time!")
                continue