import os, sys, time, re, json, datetime, random
from Process_Cloud_CPU import Process_Cloud, Process_Panel
#import py7zr

dir_path = os.path.dirname(os.path.realpath(__file__))

app = Process_Cloud()
panel = Process_Panel()

platform_name=sys.argv[1] #Получить Платформу для доступа

print(f"---------------------------------------------------")
print(f"Платформа: {platform_name}")
print(f"Папка: {dir_path}")

dict_arhivator={"7z": "7Z", "zip": "ZIP", "rar": "RAR"}
# Переменные
sessionfile="home.session"
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
    print(f"3) Скачать Словари")
    print(f"4) Скачать CAP Файл по Ссылке")
    print(f"5) Запуск Расшыфровки CAP")
    print(f"6) Использовать Сессию до Расшыфровки")
    print(f"7) Удалить Сессию до Расшыфровки")
    print(f"8) Список Паролей CAP файлов")
    print(f"9) Выход из Скрипта")
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
            try:
                select_dict = app.InputWhile("Укажыте Словари: ")
                mass_dicts = select_dict.split(",")
                for down in mass_dicts:
                    num_dic = int(down)
                    num_dic = num_dic-1
                    if len(Dict_Download)>-1:
                        sel_dic = Dict_Download[num_dic]
                        print(f"Выбран Словарь: {sel_dic['Name']}")
                        print(f"Список Файлов: {sel_dic['Files']}")
                        #app.PauseProcess()
                        select_url = Settings["Type_URLS"]
                        if select_arhivator in sel_dic["Urls"]:
                            if select_url=="GoogleDisk":
                                url=sel_dic["Urls"][select_arhivator]
                                url_google = app.GetGoogleLink(url)
                                path_download = f"{dir_path}/{Settings['Dir_Dicts_Downloads']}/{sel_dic['Name']}.{arhivator}"
                                if True: #app.Check_Download_Link(url_google)==True
                                    result3=app.DownloadFile(url_google, path_download)
                                    if result3==True:
                                        if dict_arhivator[arhivator]=="7Z":
                                            dit_dicts_ext = Settings['Dir_Dicts']
                                            #with py7zr.SevenZipFile(f"{path_download}", mode='r') as archive:
                                                #archive.extractall(f"{dir_path}/{dit_dicts_ext}")
                                            command = f'7z x "{path_download}" "{dir_path}/{dit_dicts_ext}"'
                                            print(command)
                                            os.system(command)
                                            print(f"Словарь {sel_dic['Name']} Загружен!")
                                            if os.path.exists(path_download)==True:
                                                os.remove(path_download)   
                                        if dict_arhivator[arhivator]=="ZIP":
                                            dit_dicts_ext = Settings['Dir_Dicts']
                                            command = f'"zip" "{path_download}" -d "{dir_path}/{dit_dicts_ext}"'
                                            os.system(command)
                                            #print(command)
                                            if os.path.exists(path_download)==True:
                                                os.remove(path_download)
                                            print(f"Словарь {sel_dic['Name']} Загружен!")
                                        if dict_arhivator[arhivator]=="RAR":
                                            dit_dicts_ext = Settings['Dir_Dicts']
                                            command = f'"rar" x "{path_download}" -o "{dir_path}/{dit_dicts_ext}"'
                                            os.system(command)
                                            #print(command)
                                            if os.path.exists(path_download)==True:
                                                os.remove(path_download)
                                            print(f"Словарь {sel_dic['Name']} Загружен!")
                                else:
                                    print(f"Нету Ссылки на {sel_dic['Name']} Словарь")
                            if select_url=="DirectLink":
                                url=sel_dic["Urls"][select_arhivator]
                                path_download = f"{dir_path}/{Settings['Dir_Dicts_Downloads']}/{sel_dic['Name']}.{arhivator}"
                                if True: #app.Check_Download_Link(url)==True
                                    result3=app.DownloadFile(url, path_download)
                                    if result3==True:
                                        if dict_arhivator[arhivator]=="7Z":
                                            dit_dicts_ext = Settings['Dir_Dicts']
                                            #with py7zr.SevenZipFile(f"{path_download}", mode='r') as archive:
                                                #archive.extractall(f"{dir_path}/{dit_dicts_ext}")
                                            command = f'7z x "{path_download}" "{dir_path}/{dit_dicts_ext}"'
                                            print(command)
                                            os.system(command)
                                            print(f"Словарь {sel_dic['Name']} Загружен!")
                                            if os.path.exists(path_download)==True:
                                                os.remove(path_download)
                                        if dict_arhivator[arhivator]=="ZIP":
                                            dit_dicts_ext = Settings['Dir_Dicts']
                                            command = f'"zip" "{path_download}" -d "{dir_path}/{dit_dicts_ext}"'
                                            os.system(command)
                                            #print(command)
                                            if os.path.exists(path_download)==True:
                                                os.remove(path_download)
                                            print(f"Словарь {sel_dic['Name']} Загружен!")
                                        if dict_arhivator[arhivator]=="RAR":
                                            dit_dicts_ext = Settings['Dir_Dicts']
                                            command = f'"rar" x "{path_download}" -o "{dir_path}/{dit_dicts_ext}"'
                                            os.system(command)
                                            #print(command)
                                            if os.path.exists(path_download)==True:
                                                os.remove(path_download)
                                            print(f"Словарь {sel_dic['Name']} Загружен!")
                                else:
                                    print(f"Нету Ссылки на {sel_dic['Name']} Словарь")
                        else:
                            print(f"Нету Такого {arhivator} Архиватора!")
            except Exception as ex:
                print(f"Ошыбка: {ex}!")
        if result2=="2":
            if os.path.exists(dir_dircts)==True:
                # Список Файлов
                filesAll = os.listdir(dir_dircts)
                for fi in filesAll:
                    os.remove(fi)
                print("Папка Словарями Очищена!")
            else:
                print(f"Нету Папки {dir_dircts} Словарей!")
    if result=="5":
        listcaps=panel.List_Caps(dir_caps)
        select_cap = app.InputWhile("Выбери файл CAP: ")
        if len(listcaps)>-1:
            int_cap = int(select_cap)
            int_cap=int_cap-1
            filecap=listcaps[int_cap]
            namecapfile=filecap
            namecap=os.path.splitext(namecapfile)[0] #Только Имя Файла
            if os.path.exists(f"{dir_pass}/{namecap}_pass.txt")==False:
                filecap=f"{dir_caps}/{filecap}"
                listing_dicts=panel.List_Dicts_Exists(Dict_Download,dir_dircts)
                select_dicts = app.InputWhile("Выбери Словари: ")
                mass_dicts = select_dicts.split(",")
                for down in mass_dicts:
                    num_dic = int(down)
                    num_dic = num_dic-1
                    if len(listing_dicts)>-1:
                        sel_dic_name = listing_dicts[num_dic]
                        files_dicts=panel.GetDictsFiles(Dict_Download, sel_dic_name)
                        print(f"Выбран Словарь: {sel_dic_name}")
                        print(f"Список Файлов: {files_dicts}")
                        for dic in files_dicts:
                            #if os.path.exists(sessionfile)==False:
                            cmd=f'aircrack-ng -w "{dir_dircts}/{dic}" -N "{dir_path}/{sessionfile}" -l "{dir_pass}/{namecap}_pass.txt" "{filecap}"'
                            #cmd=f'aircrack-ng -w "{dir_dircts}/{dic}" -l "{dir_pass}/{namecap}_pass.txt" "{filecap}"'
                            os.system(cmd)
            if os.path.exists(f"{dir_pass}/{namecap}_pass.txt")==True:
                print("Пароль Найден!")
                password=app.ReadFile(f"{dir_pass}/{namecap}_pass.txt")
                print(f"Пароль: {password} | Файл {namecap}_pass.txt")
                break
    if result=="8":
        panel.List_Passwords(dir_pass)
    if result=="4":
        panel.List_Caps(dir_caps)
        cap_file = app.InputWhile("Только Имя CAP файл: ")
        cap_url = app.InputWhile("Ссылка CAP: ")
        result_cap=app.DownloadFile(cap_url, f"{dir_caps}/{cap_file}.cap")
        if result_cap:
            print(f"CAP {cap_file}.cap Загружен!")
        else:
            print(f"CAP {cap_file}.cap Не Загружен!")
        panel.List_Caps(dir_caps)
    if result=="6":
        cmd=f'aircrack-ng -R "{dir_path}/{sessionfile}"'
        os.system(cmd)
    if result=="7":
        if os.path.exists(f"{dir_path}/{sessionfile}")==True:
            os.remove(f"{dir_path}/{sessionfile}")
            print(f"Файл {dir_path}/{sessionfile} Сессии Удален!")
        else:
            print(f"Файл {dir_path}/{sessionfile} Нету!")
    if result=="9":
        break
    elif result!="1" and result!="2" and result!="3" and result!="4" and result!="5" and result!="6" and result!="7" and result!="8" and result!="9":
        print(f"Не Верная {result} Команда!")
    app.Pause()