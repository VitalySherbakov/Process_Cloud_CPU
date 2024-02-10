import os, sys, time, re, json, datetime, random
from Process_Cloud_CPU import Process_Cloud

dir_path = os.path.dirname(os.path.realpath(__file__))

app = Process_Cloud()

platform_name=sys.argv[1] #Получить Платформу для доступа

print(f"Платформа: {platform_name}")
print(f"Папка: {dir_path}")

dict_arhivator={"7z": "7z", "zip": "ZIP", "rar": "RAR"}
# Переменные
dict_num=0 # Количество
# Процес
while True:
    Settings=app.ReadJson(app.SettingFile)
    # Создание Папок
    app.CreateDir(f"{dir_path}/{Settings['Dir_CAPS']}")
    app.CreateDir(f"{dir_path}/{Settings['Dir_Dicts_Downloads']}")
    app.CreateDir(f"{dir_path}/{Settings['Dir_Dicts']}")
    app.CreateDir(f"{dir_path}/{Settings['Passwords']}")
    Dict_Download = app.ReadJson(app.SettingDicts)
    current_date = datetime.datetime.now()
    current_date_str = current_date.strftime("%d.%m.%Y %H:%M:%S")
    print(f"-------------------------{current_date_str}--------------------------")
    print(f"1) Список Словарей")
    print(f"2) Работа с Словарями")
    print(f"3) Работа с CAP файлами Расшыфровка")
    result = app.InputWhile("Номер Выбора: ")
    if result=="1":
        print("------------Словари-------------")
        for li in Dict_Download:
            dict_num+=1
            name=li["Name"]
            files = li["Files"]
            print(f"{dict_num}) {name} | Количество Файлов: {len(files)}")
        dict_num = 0
        print("--------------------------------")
    if result=="2":
        print("------------Словари-------------")
        for li in Dict_Download:
            dict_num+=1
            name=li["Name"]
            files = li["Files"]
            print(f"{dict_num}) {name} | Количество Файлов: {len(files)}")
        dict_num = 0
        print("--------------------------------")
        print(f"1) Скачать Словарь и Распоковать") 
        print(f"2) Очистить Все Словари")
        result2 = app.InputWhile("Номер Выбора: ")
        if result2=="1":
            select_dict = app.InputWhile("Укажыте Словари: ")
            num_dic = int(select_dict)
            num_dic = num_dic-1
            if len(Dict_Download)>-1:
                sel_dic = Dict_Download[num_dic]
                print(f"Выбран Словарь: {sel_dic['Name']}")
                print(f"Список Файлов: {sel_dic['Files']}")
                app.PauseProcess()
                arhivator = str(Settings["Arhivator"])
                select_url = Settings["Type_URLS"]
                if arhivator.upper() in sel_dic["Urls"]:
                    if select_url=="GoogleDisk":
                        url=sel_dic["Urls"][arhivator]
                        url_google = app.GetGoogleLink(url)
                        path_download = f"{dir_path}/{Settings['Dir_Dicts_Downloads']}/{sel_dic['Name']}.{dict_arhivator[arhivator.lower()]}"
                        result3=app.DownloadFile(url_google, path_download)
                        if result3==True:
                            if dict_arhivator[arhivator]=="ZIP":
                                dit_dicts_ext = Settings['Dir_Dicts']
                                os.system(f'"p7zip" x "{path_download}" -o "{dir_path}/{dit_dicts_ext}"')
                            if dict_arhivator[arhivator]=="7Z":
                                dit_dicts_ext = Settings['Dir_Dicts']
                                os.system(f'"zip" "{path_download}" -d "{dir_path}/{dit_dicts_ext}"')
                            if dict_arhivator[arhivator]=="RAR":
                                dit_dicts_ext = Settings['Dir_Dicts']
                                os.system(f'"rar" x "{path_download}" -o "{dir_path}/{dit_dicts_ext}"')
                    if select_url=="DirectLink":
                        url=sel_dic["Urls"][arhivator]
                        path_download = f"{dir_path}/{Settings['Dir_Dicts_Downloads']}/{sel_dic['Name']}.{dict_arhivator[arhivator.lower()]}"
                        result3=app.DownloadFile(url, path_download)
                        if result3==True:
                            if dict_arhivator[arhivator]=="ZIP":
                                dit_dicts_ext = Settings['Dir_Dicts']
                                os.system(f'"p7zip" x "{path_download}" -o "{dir_path}/{dit_dicts_ext}"')
                            if dict_arhivator[arhivator]=="7Z":
                                dit_dicts_ext = Settings['Dir_Dicts']
                                os.system(f'"zip" "{path_download}" -d "{dir_path}/{dit_dicts_ext}"')
                            if dict_arhivator[arhivator]=="RAR":
                                dit_dicts_ext = Settings['Dir_Dicts']
                                os.system(f'"rar" x "{path_download}" -o "{dir_path}/{dit_dicts_ext}"')
                else:
                    print(f"Нету Такого {arhivator} Архиватора!")
        if result2=="2":
            pass
    if result=="3":
        pass
    elif result!="1" and result!="2":
        print(f"Не Верная {result} Команда!")
    app.Pause()