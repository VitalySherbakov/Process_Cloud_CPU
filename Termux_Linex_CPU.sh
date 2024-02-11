versionscript=1.012
echo "Установка и Работа Process_Cloud CPU SV (Щ.В) (v $versionscript)"
distributivelinex=$(uname -a)
numberversionlinex=$(uname -a)
dirsource="Process_Cloud_CPU"

# ----------------------Functions----------------------
function function_install_cpu(){
	# Установка CPU
	apt update -y
	git clone https://github.com/aircrack-ng/aircrack-ng
    cd aircrack-ng
    bash "./autogen.sh"
    "./configure"
    make
    sudo make install
	apt update -y
    apt install aircrack-ng -y
	aircrack-ng --help
	cd ..
}
function function_pack(){
    # Установка Пакетов
    echo "Обновление..."
    apt update -y
    echo "Загрузка Пакетов 1..."
    apt install sudo -y
    sudo apt install ssh -y
    sudo apt install curl -y
    sudo apt install wget -y
    sudo apt install git -y
    sudo apt install rar -y
    sudo apt install zip -y
    sudo apt install p7zip-full -y
	sudo apt install unrar-free -y
    apt update -y
    echo "Загрузка Пакетов 2..."
    apt install -y build-essential
    DEBIAN_FRONTEND=noninteractive apt install -y tzdata
    apt install -y software-properties-common
    add-apt-repository -y ppa:deadsnakes/ppa
    apt update -y
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
function function_pack2(){
    # Установка Пакетов
    echo "Обновление..."
    apt update -y
    echo "Загрузка Пакетов 1..."
    apt install sudo -y
    sudo apt install ssh -y
    sudo apt install curl -y
    sudo apt install wget -y
    sudo apt install git -y
    sudo apt install rar -y
    sudo apt install zip -y
    sudo apt install p7zip-full -y
	sudo apt install unrar-free -y
    apt update -y
    echo "Загрузка Пакетов 2..."
    apt install -y build-essential
    apt install -y software-properties-common
    add-apt-repository -y ppa:deadsnakes/ppa
    apt update -y
    apt install -y python3.10 python3-pip
    echo "Загрузка Пакетов 3..."
    python3.10 --version
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    sudo python3.10 get-pip.py
    rm -r get-pip.py
    pip install --upgrade pip
    python3.10 -m pip install requests
    python3.10 -m pip install alive-progress
    python3.10 -m pip install tqdm
    python3.10 -m pip install py7zr
    python3.10 -m pip install rarfile
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
    echo "Команда: cpu (Установка утелиты для всех Linex, кроме Kali)"
    echo "Команда: run (Запуск Скрипта)"
    echo "Команда: exit (Выход)"
    echo "Введите Команду:"
    read command
    if [ "$command" == "pack" ]; then
        access_ubuntu
		function_pack2
	fi
    if [ "$command" == "cpu" ]; then
        access_ubuntu
		function_install_cpu
	fi
    if [ "$command" == "run" ]; then
        python3.10 "./$dirsource/Linex_Main.py" "$1"
	fi
    if [ "$command" == "exit" ]; then
		#break
        exit
	fi
}

while true
do
    current_time=$(date +%d.%m.%Y\ %T) # тикущая дата
    echo "-------------------------$current_time--------------------------"
    echo "Платформа: $distributivelinex"
    echo "Версия: $numberversionlinex"
    access_ubuntu
    main "$distributivelinex"
    #if [ "$distributivelinex" == "Ubuntu" ]; then
        #access_ubuntu
        #main "$distributivelinex"
    #fi
    read -p "Нажмите Enter, чтобы продолжить"
done