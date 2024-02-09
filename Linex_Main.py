import os, sys, time, re, json, datetime, random
from Process_Cloud_CPU import Process_Cloud

dir_path = os.path.dirname(os.path.realpath(__file__))

app = Process_Cloud()

platform_name=sys.argv[1] #Получить Платформу для доступа

print(f"Платформа: {platform_name}")
print(f"Папка: {dir_path}")

while True:
    Settings=app.ReadSetting(app.SettingFile)
    Dict_Download = app.ReadDicts(app.SettingDicts)
    print(app.SettingDicts)
    print(Dict_Download)
    current_date = datetime.datetime.now()
    current_date_str = current_date.strftime("%d.%m.%Y %H:%M:%S")
    print(f"-------------------------{current_date_str}--------------------------")
    print(f"1) Работа с Словарями")
    print(f"2) Работа с CAP файлами Расшыфровка")
    result = app.InputWhile("Номер Выбора: ")
    if result=="1":
        print("------------Словари-------------")
        for li in Dict_Download:
            name=li["Name"]
            files = li["Files"]
            print(f"1) Словарь {name} Количество {len(files)}")
        print(f"1) Скачать Словарь и Распоковать")
        print(f"2) Работа с CAP файлами Расшыфровка") 
        print(f"3) Работа с CAP файлами Расшыфровка") 
    if result=="2":
        pass
    elif result!="1" and result!="2":
        print(f"Не Верная {result} Команда!")
    app.Pause()