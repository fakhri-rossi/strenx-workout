import os,time
from .import Database

done_status = ["y","n"]

def clear_screen():
    sistem_operasi = os.name
    match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

def wait():
    wait = input("Enter untuk melanjutkan")
       
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
            if reps > 200 or reps < 1:
                print("Repetisi tidak masuk akal!")
                continue
            return reps
        
        except:
            print("Masukkan Repetisi yang valid!")
      
def ask_kg():
    while True:
        try:
            kg = int(input("Berat beban (kg): "))
            if kg > 999 or kg < 1:
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

        elif not timer[:2].isnumeric() or not timer[3:].isnumeric():
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

def ask_routine_name()->str:
    while True:
        routine_name = input("Nama Rutinitas: ")   

        if routine_name not in Database.Database.routine_names:
            Database.Database.temp_list.append(routine_name)
            # Database.Database.write_routine()
            return routine_name

        else:
            print("Rutinitas sudah ada, buat nama lain")

def get_current_time()->str:
    current_time = time.strftime("%Y-%m-%d-%H-%M-%S-%z", time.gmtime())
    current_time = current_time.split("-")
    hour = int(current_time[3])
    gmt = int(current_time[6][1:3])

    hour += gmt
    
    if len(str(hour)) < 2:
        hour = "0" + str(hour)
    else:
        hour = str(hour)
    
    current_time[3] = hour
    current_time = '-'.join(current_time)

    return current_time

def get_routine_total()->int:
    return len(Database.Database.routine_names)

def edit_set(index:int):
    data = Database.Database.temp_list[index]
    data_break = data.split(",")

    # reps
    if data_break[1] != "-":
        reps = ask_reps()
    else:
        reps = "-"
    # kg
    if data_break[2] != "-":
        kg = ask_kg()
    else:
        kg = "-"
    # timer
    if data_break[3] != "-":
        timer = ask_timer()
    else:
        timer = "-"

    data_str = f"{data_break[0]},{reps},{kg},{timer}"
    Database.Database.temp_list[index] = data_str # update data

def add_set(index:int):
    data = Database.Database.temp_list[index]
    if data[-1] in done_status:
        data = data[:-2] + ",n"

    Database.Database.temp_list.insert(index+1,data)

def delete_set(index:int):
    Database.Database.temp_list.pop(index)

def rename_routine():
    new_name = input("Nama rutinitas: ")
    while True:
        if new_name in Database.Database.routine_names:
            print("Nama rutinitas sudah ada")
        else:
            Database.Database.temp_list[0] = new_name
