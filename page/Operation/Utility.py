import os,time
from .import Database

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
        if timer[2] != ":" or len(timer) != 5:
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

def get_current_time()->str:
    return time.strftime("%Y-%m-%d-%H-%M-%S-%z", time.gmtime())

def get_routine_total()->int:
    return len(Database.Database.routine_names)