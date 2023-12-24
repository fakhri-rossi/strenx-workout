from . import Utility
from .Database import Database

def str_duration(time_start:dict, time_end:dict) -> str:
    time_start = int(time_start['hour'])*3600 + int(time_start['minute'])*60 + int(time_start["second"])
    time_end = int(time_end['hour'])*3600 + int(time_end['minute'])*60 + int(time_end["second"])
    duration = time_end - time_start

    hour = duration // 3600
    duration -= hour*3600
    minute = duration // 60
    duration -= minute*60
    second = duration

    if hour < 1:  # kalau dibawah 1 jam maka jam tidak dispill
        hour = ""
    else:
        hour = f"{hour} jam"

    minute = f"{minute} menit"
    second = f"{second} detik"

    duration = f"{hour} {minute} {second}"
    return duration
    

def time_to_dict(time_str:str) -> dict:
    # time_start = time.strftime("%Y-%m-%d-%H-%M-%S-%z", time.gmtime())
    # 2023-12-10-17-17-02-+0700
    dict1 = {
        "year": "",
        "month": "",
        "date": "",
        "hour": "",
        "minute": "",
        "second": "",
        "gm_time": "",
    }

    time_str = time_str.split("-")

    dict1["year"] = time_str[0]
    dict1["month"] = time_str[1]
    dict1["date"] = time_str[2]
    dict1["hour"] = time_str[3]
    dict1["minute"] = time_str[4]
    dict1["second"] = time_str[5]
    dict1["gm_time"] = time_str[6][1:]

    if len(dict1["hour"]) < 2:
        dict1["hour"] = f"0{dict1['hour']}"

    return dict1


def print_history():
    content = Database.read_history()
    n_line = len(content)

    if content != 0:
        num = 1
        for i in range(n_line-1, -1, -1):
        # time_start,time_end,routine_name,exercises...
            exercises = []
            exercises_dict = {}
            data_break = content[i].split(",")
            n = len(data_break)

            time_start = time_to_dict(data_break[0])
            time_end = time_to_dict(data_break[1])

            date = time_start["date"]
            month = Utility.month_to_name(time_start["month"])
            year = time_start["year"]

            duration = str_duration(time_start, time_end)
            routine_name = data_break[2]
            data_break[-1] = data_break[-1][:-1] #buat ngilangin /n

            for i in range(3, n, 4):
            # exercise_name,reps,kg,timer
                exercises.append(data_break[i])
            
            if len(exercises) > 0:
                for exercise in exercises:
                    exercises_dict[exercise] = exercises.count(exercise)

                exercises = ''
                for key, value in exercises_dict.items():
                    exercises += f"{key} {value} set, "

                exercises = exercises[:-2] # buat ngilangin ', ' di akhir
            else:
                exercises = "Tidak ada"

            print(f"{num}. {date} {month} {year} | {time_start['hour']}:{time_start['minute']} | {duration}")
            print(f"{routine_name} | [{exercises}]")
            # print("-"*50)
            print()

            num +=1   
        
    else:
        print("Belum ada histori latihan")

