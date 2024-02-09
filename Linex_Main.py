import os, sys, time, re, json, datetime, random
from Process_Cloud_CPU import Process_Cloud

dir_path = os.path.dirname(os.path.realpath(__file__))

app = Process_Cloud()

platform_name=sys.argv[1] #Получить Платформу для доступа

print(f"Платформа: {platform_name}")
print(f"Папка: {dir_path}")

while True:
    current_date = datetime.datetime.now()
    current_date_str = current_date.strftime("%d.%m.%Y %H:%M:%S")
    print(f"-------------------------{current_date_str}--------------------------")
    print(f"1) Работа с Словарями")
    print(f"2) Работа с CAP файлами Расшыфровка")
    result = app.InputWhile("Номер Выбора: ")
    if result=="1":
        pass 
    if result=="2":
        pass
    elif result!="1" and result!="2":
        print(f"Не Верная {result} Команда!")
    app.Pause()