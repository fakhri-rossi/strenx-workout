from . import Utility, View

def str_duration(time_start:dict, time_end:dict) -> str:
    duration = ""
    hour = int(time_end["hour"]) - int(time_start["hour"])
    if hour < 1:  # kalau dibawah 1 jam maka jam tidak dispill
        hour = ""
    else:
        hour = f"{hour} jam"

    minute = int(time_end["minute"]) - int(time_start["minute"])
    minute = f"{minute} menit"

    second = int(time_end["second"]) - int(time_start["second"])
    second = f"{second} detik"

    duration = f"{hour} {minute} {second}"
    return duration
    

def time_dict(time_str:str) -> dict:
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
    dict1["gm_time"] = time_str[6][1:]

    dict1["minute"] = time_str[4]
    dict1["second"] = time_str[5]

    dict1["hour"] = str(int(time_str[3]) + int(time_str[6][1:3]))
    if len(dict1["hour"]) < 2:
        dict1["hour"] = f"0{dict1['hour']}"

    return dict1

def history_read():
    with open("history.txt", "r") as file:
        content = file.readlines()
        n_line = len(content)

        for i in range(n_line-1, -1, -1):
            # time_start,time_end,routine_name,exercises...
            data_break = content[i].split(",")
            time_start = time_dict(data_break[0])
            time_end = time_dict(data_break[1])

            date = time_start["date"]
            month = Utility.month_to_name(time_start["month"])
            year = time_start["year"]

            duration = str_duration(time_start, time_end)
            routine_name = data_break[2]
            n = len(data_break)
            data_break[-1] = data_break[-1][:-1] #buat ngilangin /n
            exercises = []
            exercises.append(routine_name)

            for i in range(3, n, 4):
                # exercise_name,reps,kg,timer
                exercises.append(f"{data_break[i]},{data_break[i+1]},{data_break[i+2]},{data_break[i+3]}")

            print("\n"+"="*50)
            print(f"{routine_name}")
            print(f"{date} {month} {year} | {time_start['hour']}:{time_start['minute']}")
            print(f"Durasi: {duration}")
            print("-"*50)

            View.print_routine(list_source = exercises)
            