Особености работы, если вы вошли
1) Скачать Словарь и Распоковать 
и хотите вернуться назад укажите любое другое не верное значение
не 1 а 7 и выдав не верную команду вернут назад на панель 
не верные указания будут возвращать назад так проще

И если нужно скачать не один словарь, и список 
достаточно указать цыфрами те словари через кому списком
которые вам нужны
Вот так
Укажыте Словари: 1,2,3,4,5,6

И списком будет от 1 по 6 номер будет загружаться словари списком
Аналогичный процес по расшифровки 
Выбери Словари: 1,2,3,4
будет крутить с 1 по 4

Команда: remove (Авто Удаление Программы)
это удаляет Программу полностью

----------------Для Linex---------------
Скачать Программу
apt install git -y
git clone https://github.com/VitalySherbakov/Process_Cloud_CPU

Запуск Скрипта
bash ./Process_Cloud_CPU/Termux_Linex_CPU.sh

Удалить Программу
rm -r Process_Cloud_CPU

----------------Для Смартфона--------------
Ссылка на Загрузку Termux
https://f-droid.org/ru/packages/com.termux/

Установка
pkg upgrade -y

Загрузка
pkg install proot-distro

Список Дистрибутивов
proot-distro list

Установка Ubuntu
proot-distro install ubuntu

Вход в Консоль Ubuntu
proot-distro login ubuntu

Обновить Зарание
apt update -y && upgrade -y

---------------------Описание Общее----------------------
{
    "Version": 1.003,
    "Windows_AircrackNg": "aircrack-ng-1.7-win\\bin\\aircrack-ng.exe",
    "Dir_CAPS": "WIFICAPS",
    "Dir_Dicts_Downloads": "DownloadDicts",
    "Dir_Dicts": "Dicts",
    "Passwords": "Passs",
    "FileDicts":"DictsDownload.json",
    "Type_URLS": "GoogleDisk",
    "Arhivator": "tar"
}

Windows_AircrackNg - Программа AircrackNg только для Windows
Dir_CAPS - Папка Файлов Caps для расшыфровки
Dir_Dicts_Downloads - Файлы загрузки словарей
Dir_Dicts - Уже готовые словари распакованые
Passwords - Файлы Паролей
FileDicts - Файл Json ссылок и файлов словарей
Type_URLS - Тип Ссылок GoogleDisk/DirectLink  (Гугл Диск/Прямая Ссылка) 
Arhivator - Использование Архиватора


--------------Словари Архивы DictsDownload.json---------------
Конструкция Файла Списка Словарей имеет вот такой вид

[
    {
        "Name": "00000000_99999999",
        "Files": ["00000000-99999999.txt"],
        "Urls": {
            "7Z": "https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1dH1Jk1yUnXLykqSS76fsUuvoxamwFOSS",
            "ZIP": "", 
            "RAR": ""}
    },
    {
        "Name": "000000000_999999999_max",
        "Files": ["000000000-999999999_max.txt"],
        "Urls": {
            "7Z": "https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1fZNqHM9_VzHAidRoGM7MDAmnSEgnvnF0",
            "ZIP": "", 
            "RAR": ""}
    }
]

Где Представляет один Словарь с Именем 00000000_99999999 , Атрибут Name
Имя накладываеться к Архиву Указаном настройке и получаем архив 00000000_99999999.7z
Внутри Архива содержыться список файлов "Files": ["00000000-99999999.txt"]
Ну и естественно ссылка на этот Архив Прямой Ссылкой "Urls": {"7Z": "Прямая Ссылка"}
в нашем случаи на Google Диск, на усмотрение можно добавить свои словари изменив
и прибавив еще таких конструкций

{
        "Name": "00000000_99999999",
        "Files": ["00000000-99999999.txt"],
        "Urls": {
            "7Z": "https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1dH1Jk1yUnXLykqSS76fsUuvoxamwFOSS",
            "ZIP": "", 
            "RAR": ""}
}