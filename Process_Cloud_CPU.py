import os, sys, time, re, json, datetime, random

dir_path = os.path.dirname(os.path.realpath(__file__))

class Process_Cloud(object):
    """Настройки Приложения"""
    settingfile=f"{dir_path}/SettingApp.json"
    """Адресс Настроек"""
    settingdicts=f"{dir_path}/DictsDownload.json"
    """Словари"""
    def __init__(self, encod="utf-8"):
        pass
    def ReadFile(self, file: str, encod="utf-8"):
        """Чтение Файла"""
        text=""
        if os.path.exists(file):
            try:
                with open(file, 'r', encoding=encod) as f:
                    text = f.read()
            except Exception as ex:
                print(f"ERROR FILE: {ex}!")
        return text
    def ReadJson(self, file: str, encod="utf-8"):
        """Чтение Json"""
        data=None
        if os.path.exists(file):
            try:
                with open(file, 'r', encoding=encod) as f:
                    data = json.load(f)
            except Exception as ex:
                print(f"ERROR DICTS: {ex}!")
        else:
            print(f"ERROR: Нету {file} Файла!")
        return data
    def GetGoogleLink(self, link: str):
        """Получить Прямую Ссылку на Google Link"""
        url_down=None
        if not link.strip():
            print("Ссылка Пуста!")
        else:
            repl="https://drive.google.com/file/d/"
            link=link.strip() #удаления пробелов с начала и конца строки
            id_disk=link.replace(repl,"")
            masss=id_disk.split('/')
            id_disk=masss[0]
            url_down=f"https://drive.google.com/uc?export=download&confirm=no_antivirus&id={id_disk}"
        return url_down
    def Pause():
        input("-------------------Enter-------------------")