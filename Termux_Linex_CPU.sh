versionscript=1.012
echo "Установка и Работа Process_Cloud CPU SV (Щ.В) (v $versionscript)"
distributivelinex=$(lsb_release -is)
numberversionlinex=$(lsb_release -rs)
dirsource="Process_Cloud_CPU"

# ----------------------Functions----------------------
function function_pack(){
    # Установка Пакетов
    echo "Обновление..."
    apt-get update -y
    echo "Загрузка Пакетов 1..."
    apt-get install sudo -y
    sudo apt-get install ssh -y
    sudo apt-get install curl -y
    sudo apt-get install wget -y
    sudo apt-get install git -y
    sudo apt-get install p7zip-full -y
	sudo apt-get install unrar-free -y
    apt-get update -y
    echo "Загрузка Пакетов 2..."
    apt-get install -y build-essential
    DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata
    apt install -y software-properties-common
    add-apt-repository -y ppa:deadsnakes/ppa
    apt-get update -y
    apt install -y python3.8 python3-pip
    echo "Загрузка Пакетов 3..."
    python3.8 --version
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    sudo python3.8 get-pip.py
    rm -r get-pip.py
    pip install --upgrade pip
    python3.8 -m pip install requests
    python3.8 -m pip install alive-progress
    python3.8 -m pip install tqdm
    python3.8 -m pip install py7zr
    python3.8 -m pip install rarfile
    echo "-----Конец Установки Пакетов-----"
}
function access_ubuntu(){
	# Ubuntu полный доступ к папке
	nameuser=$USER
	chmod -R 777 "$dirsource/"
}
# -----------------------------------------------------

function main(){
    # Основное Меню
    echo "Команда: pack (Установка необходимых пакетов)"
    echo "Команда: run (Запуск Скрипта)"
    echo "Команда: exit (Выход)"
    echo "Введите Команду:"
    read command
    if [ "$command" == "pack" ]; then
        access_ubuntu
		function_pack
	fi
    if [ "$command" == "run" ]; then
        python3.8 "./$dirsource/Linex_Main.py" "$1"
	fi
    if [ "$command" == "exit" ]; then
		break
	fi
}

while true
do
    current_time=$(date +%d.%m.%Y\ %T) # тикущая дата
    echo "-------------------------$current_time--------------------------"
    echo "Платформа: $distributivelinex"
    echo "Версия: $numberversionlinex"
    if [ "$distributivelinex" == "Ubuntu" ]; then
        access_ubuntu
        main "$distributivelinex"
    fi
    read -p "Нажмите Enter, чтобы продолжить"
done