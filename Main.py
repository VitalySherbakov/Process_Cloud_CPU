from Process_Cloud_CPU import Process_Cloud

app = Process_Cloud()

url="https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1iHXTLVYhxOpY5IA_ujQToCoabai-x-CC"
if app.Check_Download_Link(url)==True:
    print("Ссылка Есть!")
else:
    print("Ссылки нету!")


