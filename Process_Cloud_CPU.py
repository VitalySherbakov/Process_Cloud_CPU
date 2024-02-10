import os, sys, time, re, json, datetime, random
import requests
import urllib.request
from alive_progress import alive_bar
from alive_progress.styles import showtime
from os.path import basename

dir_path = os.path.dirname(os.path.realpath(__file__))

class Process_Cloud(object):
    """Настройки Приложения"""
    SettingFile=f"{dir_path}/SettingApp.json"
    """Адресс Настроек"""
    SettingDicts=f"{dir_path}/DictsDownload.json"
    """Словари"""
    def __init__(self, encod="utf-8"):
        pass
    def CreateDir(self, pathdir: str):
        if not os.path.exists(pathdir):
            os.mkdir(pathdir)
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
    def Check_Download_Link(self,link: str):
        """Проверка Наличия Загрузки Файла"""
        try:
            response = requests.head(link)
            if response.status_code == 200:
                content_type = response.headers.get('content-type')
                if content_type and 'application/octet-stream' in content_type:
                    return True
            return False
        except requests.exceptions.RequestException:
            return False
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
    def InputWhile(self, text: str):
        """Ввод Данных Цыкловый"""
        Flag,Res=True,""
        while Flag:
            Res=input(text)
            if not Res.strip():
                print("Пустое Значение!")
            else:
                Flag=False
        return Res
    def DownloadFile2(self, url: str, filepath: str, style="classic"):
        """Загрузить Файл 2"""
        Flag=False
        try:
            urllib.request.urlretrieve(url, filepath)
            # command=f'wget -O "{filepath}" "{url}"'
            # os.system(command)
            # response = requests.get(url, stream=True)
            # total_size = int(response.headers.get("content-length", 0))
            # block_size = 1024  # задайте размер блока загрузки по вашему усмотрению
            # with open(filepath, "wb") as f, alive_bar(total_size, bar=style) as bar:
            #     for data in response.iter_content(block_size):
            #         f.write(data)
            #         bar(len(data))
            Flag=True
        except Exception as ex:
            print(f"ERROR DOWNLOAD: {ex}!")
        return Flag
    def DownloadFile(self, url: str, filepath: str, style="classic"):
        """Загрузить Файл"""
        Flag=False
        try:
            #urllib.request.urlretrieve(url, filepath)
            # command=f'wget -O "{filepath}" "{url}"'
            # os.system(command)
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get("content-length", 0))
            block_size = 1024  # задайте размер блока загрузки по вашему усмотрению
            with open(filepath, "wb") as f, alive_bar(total_size, bar=style) as bar:
                for data in response.iter_content(block_size):
                    f.write(data)
                    bar(len(data))
            Flag=True
        except Exception as ex:
            print(f"ERROR DOWNLOAD: {ex}!")
        return Flag
    def LinkValid(self, url: str):
        """Проверка Ссылка"""
        Flag=False
        regex = r'^(https?://)?([a-zA-Z0-9-]+\.)*[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})(:\d{2,5})?(/.*)?$'
        if re.match(regex, url):
            Flag=True
        # response = requests.head(url)
        # if response.status_code in codes:
        #     Flag=True
        return Flag
    def Pause(self):
        """Пауза"""
        input("-------------------Enter-------------------")
    def PauseProcess(self):
        """Пауза 2"""
        input("-------------Начать-------------")