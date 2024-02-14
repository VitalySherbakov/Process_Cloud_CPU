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
    chmod -R 777 "aircrack-ng/"
    cd aircrack-ng
    bash "./autogen.sh"
    "./configure"
    make
    sudo make install
	apt update -y
    apt install aircrack-ng -y
	aircrack-ng --help
	cd ..
	echo "Авто Выход с Скрипта"
	echo "Повторно Войдите в Скрипт Командой"
	echo "bash ./Process_Cloud_CPU/Termux_Linex_CPU.sh"
	exit
}
function function_python(){
    apt update -y
    sudo apt-get install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libnl-3-dev libnl-genl-3-dev pkg-config libsqlite3-dev libpcre3-dev libffi-dev curl libreadline-dev ethtool libbz2-dev libtool autoconf -y
	apt update -y
    wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
	tar -xf Python-3.8.0.tgz
	rm -r Python-3.8.0.tgz
	chmod -R 777 "Python-3.8.0/"
	cd Python-3.8.0
	./configure --enable-optimizations
	make -j $(nproc)
	sudo make altinstall
	apt update -y
    wget -O get-pip.py https://bootstrap.pypa.io/get-pip.py
    sudo python3.8 get-pip.py
	pip install --upgrade pip
	python3.8 --version
	python3.8 -m pip install requests
	python3.8 -m pip install alive-progress
	python3.8 -m pip install tqdm
	python3.8 -m pip install py7zr
    python3.8 -m pip install pylzma
	python3.8 -m pip install rarfile
    python3.8 -m pip install urllib3==1.26.7
    cd ..
    rm -r Python-3.8.0
}
# function function_pack(){
#     # Установка Пакетов
#     echo "Обновление..."
#     apt update -y
#     echo "Загрузка Пакетов 1..."
#     apt install sudo -y
#     sudo apt install ssh -y
#     sudo apt install curl -y
#     sudo apt install wget -y
#     sudo apt install git -y
#     sudo apt install rar -y
#     sudo apt install zip -y
#     sudo apt install p7zip-full -y
# 	sudo apt install unrar-free -y
#     apt update -y
#     echo "Загрузка Пакетов 2..."
#     apt install -y build-essential
#     DEBIAN_FRONTEND=noninteractive apt install -y tzdata
#     apt install -y software-properties-common
#     add-apt-repository -y ppa:deadsnakes/ppa
#     apt update -y
#     apt install -y python3.8 python3-pip
#     echo "Загрузка Пакетов 3..."
#     python3.8 --version
#     curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#     sudo python3.8 get-pip.py
#     rm -r get-pip.py
#     pip install --upgrade pip
#     python3.8 -m pip install requests
#     python3.8 -m pip install alive-progress
#     python3.8 -m pip install tqdm
#     python3.8 -m pip install py7zr
#     python3.8 -m pip install rarfile
#     echo "-----Конец Установки Пакетов-----"
# }
function function_pack2(){
    # Установка Пакетов
    echo "Обновление..."
    apt update -y
    echo "Загрузка Пакетов 1..."
    apt install sudo -y
    apt install ssh -y
    apt install curl -y
    apt install wget -y
    apt install git -y
    apt install rar -y
    apt install zip -y
    apt install p7zip-full -y
	apt install unrar-free -y
    apt update -y
    echo "Загрузка Пакетов 2..."
    function_python
    echo "-----Конец Установки Пакетов-----"
	echo "Авто Выход с Скрипта"
	echo "Повторно Войдите в Скрипт Командой"
	echo "bash ./Process_Cloud_CPU/Termux_Linex_CPU.sh"
	exit
}
function access_ubuntu(){
	# Ubuntu полный доступ к папке
	nameuser=$USER
	chmod -R 777 "$dirsource/"
}
function auto_remove_program(){
    rm -rf "$dirsource"
}
# -----------------------------------------------------

function main(){
    # Основное Меню
    echo "Команда: pack (Установка необходимых пакетов)"
    echo "Команда: cpu (Установка утелиты для всех Linex, кроме Kali)"
    echo "Команда: run (Запуск Скрипта)"
    echo "Команда: remove (Авто Удаление Программы)"
    echo "Команда: exit (Выход)"
    echo "Введите Команду:"
    read command
    if [ "$command" == "remove_program" ]; then
        echo "Команда Вы Уверены в Удалении Программы Y/N"
        read command2
        if [ "$command2" == "y" || "$command2" == "Y" ]; then
            access_ubuntu
            auto_remove_program
            exit
        fi
	fi
    if [ "$command" == "pack" ]; then
        access_ubuntu
		function_pack2
	fi
    if [ "$command" == "cpu" ]; then
        access_ubuntu
		function_install_cpu
	fi
    if [ "$command" == "run" ]; then
        python3.8 "./$dirsource/Linex_Main.py" "$1"
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