import os
from .import Database

def wait():
    wait = input("Tekan enter untuk lanjut ")

def clear_screen():
    sistem_operasi = os.name
    match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
          
def month_to_name(month:int) -> str:
    month = int(month)
    match month:
        case 1:
            month = "Januari"
        case 2:
            month = "Februari"
        case 3:
            month = "Maret"
        case 4:
            month = "April"
        case 5:
            month = "Mei"
        case 6:
            month = "Juni"
        case 7:
            month = "Juli"
        case 8:
            month = "Agustus"
        case 9:
            month = "September"
        case 10:
            month = "Oktober"
        case 11:
            month = "November"
        case 12:
            month = "Desember"
        case _:
            month = "error month"

    return month

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

            if reps <= 0 or reps > 999:
                print("Repetisi tidak masuk akal!")
                continue

            return reps
        except:
            print("Masukkan Repetisi yang valid!")
      
def ask_kg():
    while True:
        try:
            kg = int(input("Berat beban (kg): "))
            if kg < 0 or kg > 999:
                print("Berat beban tidak masuk akal!")
                continue

            return kg
        except:
            print("Masukkan berat yang valid!")

def ask_timer()-> str:
    while True:
        timer = input("Time (mm:ss): ")
        if timer[2] != ":" or len(timer) != 5:
            print("Input valid time!")
            continue
        else:
            try:
                # inttime = int(timer[:2])
                # inttime = int(timer[3:])
                if timer[:2].isnumeric() and timer[3:].isnumeric():
                    return timer
                else:
                    print("Waktu tidak valid!")
            except:
                print("Input valid time!")
                continue

def sets_done_checking():
    data = Database.temp_routine
    sets_done = 0
    n = len(data)

    for i  in range(1,n):
        if data[i][-1] == "y":
            sets_done += 1

    Database.sets_done = sets_done