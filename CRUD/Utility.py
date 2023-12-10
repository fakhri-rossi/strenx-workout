import os

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
    
      