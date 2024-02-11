from Process_Cloud_CPU import Process_Cloud

app = Process_Cloud()

# url="https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1iHXTLVYhxOpY5IA_ujQToCoabai-x-CC"
# if app.Check_Download_Link(url)==True:
#     print("Ссылка Есть!")
# else:
#     print("Ссылки нету!")
# https://drive.google.com/file/d/1-Raivg0fw-ESQ6S882iSXAlFaLCl5efi/view?usp=sharing
url="https://drive.usercontent.google.com/download?id=1HMLYa--Gf7cpZC7zmCjHxhFjZh_koXf5&export=download&authuser=0&confirm=t&uuid=f0d4a353-6e9f-4397-b3e5-3fce09ffaf84&at=APZUnTUnCmEdz-qf85n9L8tRlJAy%3A1707609409517"

#url_google = app.GetGoogleLink(url)
#print(url_google)

app.DownloadFile(url,"WiFi_DOM_XXXX.7z")


