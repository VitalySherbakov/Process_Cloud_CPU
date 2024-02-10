import os, sys, time, re, json, datetime, random
from Process_Cloud_CPU import Process_Cloud, Process_Panel
import py7zr

dir_path = os.path.dirname(os.path.realpath(__file__))

app = Process_Cloud()
panel = Process_Panel()

platform_name=sys.argv[1] #Получить Платформу для доступа

print(f"---------------------------------------------------")
print(f"Платформа: {platform_name}")
print(f"Папка: {dir_path}")

dict_arhivator={"7z": "7Z", "zip": "ZIP", "rar": "RAR"}
# Переменные
dict_num=0 # Количество
# Процес
while True:
    Settings=app.ReadJson(app.SettingFile)
    arhivator = str(Settings["Arhivator"]) # Архив
    arhivator = arhivator.lower()
    select_arhivator = dict_arhivator[arhivator] # Выбор Ссылок
    # Создание Папок
    dir_caps=f"{dir_path}/{Settings['Dir_CAPS']}"
    dir_dircts_down=f"{dir_path}/{Settings['Dir_Dicts_Downloads']}"
    dir_dircts=f"{dir_path}/{Settings['Dir_Dicts']}"
    dir_pass=f"{dir_path}/{Settings['Passwords']}"
    if not os.path.exists(dir_caps):
        os.system(f'mkdir "{dir_caps}"')
    if not os.path.exists(dir_dircts_down):
        os.system(f'mkdir "{dir_dircts_down}"')
    if not os.path.exists(dir_dircts):
        os.system(f'mkdir "{dir_dircts}"')
    if not os.path.exists(dir_pass):
        os.system(f'mkdir "{dir_pass}"')
    Dict_Download = app.ReadJson(app.SettingDicts)
    # Словари
    current_date = datetime.datetime.now()
    current_date_str = current_date.strftime("%d.%m.%Y %H:%M:%S")
    print(f"-------------------------{current_date_str}--------------------------")
    print(f"1) Список Словарей для Загрузки")
    print(f"2) Список Словарей Уже Загруженых")
    print(f"3) Работа с Словарями")
    print(f"4) Работа с CAP файлами Расшыфровка")
    result = app.InputWhile("Номер Выбора: ")
    if result=="1":
        panel.List_Dicts(Dict_Download)
    if result=="2":
        panel.List_Dicts_Exists(Dict_Download,dir_dircts) 
    if result=="3":
        panel.List_Dicts(Dict_Download)
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
                select_url = Settings["Type_URLS"]
                if select_arhivator in sel_dic["Urls"]:
                    if select_url=="GoogleDisk":
                        url=sel_dic["Urls"][select_arhivator]
                        url_google = app.GetGoogleLink(url)
                        path_download = f"{dir_path}/{Settings['Dir_Dicts_Downloads']}/{sel_dic['Name']}.{arhivator}"
                        if app.Check_Download_Link(url_google)==True:
                            result3=app.DownloadFile(url_google, path_download)
                            if result3==True:
                                if dict_arhivator[arhivator]=="7Z":
                                    dit_dicts_ext = Settings['Dir_Dicts']
                                    with py7zr.SevenZipFile(f"{path_download}", mode='r') as archive:
                                        archive.extractall(f"{dir_path}/{dit_dicts_ext}")
                                        os.remove(path_download)
                                        print(f"Словарь {sel_dic['Name']} Загружен!")
                                if dict_arhivator[arhivator]=="ZIP":
                                    dit_dicts_ext = Settings['Dir_Dicts']
                                    command = f'"zip" "{path_download}" -d "{dir_path}/{dit_dicts_ext}"'
                                    os.system(command)
                                    #print(command)
                                    os.remove(path_download)
                                    print(f"Словарь {sel_dic['Name']} Загружен!")
                                if dict_arhivator[arhivator]=="RAR":
                                    dit_dicts_ext = Settings['Dir_Dicts']
                                    command = f'"rar" x "{path_download}" -o "{dir_path}/{dit_dicts_ext}"'
                                    os.system(command)
                                    #print(command)
                                    os.remove(path_download)
                                    print(f"Словарь {sel_dic['Name']} Загружен!")
                        else:
                            print(f"Нету Ссылки на {sel_dic['Name']} Словарь")
                    if select_url=="DirectLink":
                        url=sel_dic["Urls"][select_arhivator]
                        path_download = f"{dir_path}/{Settings['Dir_Dicts_Downloads']}/{sel_dic['Name']}.{arhivator}"
                        if app.Check_Download_Link(url)==True:
                            result3=app.DownloadFile(url, path_download)
                            if result3==True:
                                if dict_arhivator[arhivator]=="7Z":
                                    dit_dicts_ext = Settings['Dir_Dicts']
                                    with py7zr.SevenZipFile(f"{path_download}", mode='r') as archive:
                                        archive.extractall(f"{dir_path}/{dit_dicts_ext}")
                                        os.remove(path_download)
                                        print(f"Словарь {sel_dic['Name']} Загружен!")
                                if dict_arhivator[arhivator]=="ZIP":
                                    dit_dicts_ext = Settings['Dir_Dicts']
                                    command = f'"zip" "{path_download}" -d "{dir_path}/{dit_dicts_ext}"'
                                    os.system(command)
                                    #print(command)
                                    os.remove(path_download)
                                    print(f"Словарь {sel_dic['Name']} Загружен!")
                                if dict_arhivator[arhivator]=="RAR":
                                    dit_dicts_ext = Settings['Dir_Dicts']
                                    command = f'"rar" x "{path_download}" -o "{dir_path}/{dit_dicts_ext}"'
                                    os.system(command)
                                    #print(command)
                                    os.remove(path_download)
                                    print(f"Словарь {sel_dic['Name']} Загружен!")
                        else:
                            print(f"Нету Ссылки на {sel_dic['Name']} Словарь")
                else:
                    print(f"Нету Такого {arhivator} Архиватора!")
        if result2=="2":
            pass
    if result=="4":
        pass
    elif result!="1" and result!="2":
        print(f"Не Верная {result} Команда!")
    app.Pause()