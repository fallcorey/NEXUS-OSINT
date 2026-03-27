#!/bin/bash

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}=================================${NC}"
echo -e "${GREEN}   NEXUS-OSINT Установка${NC}"
echo -e "${BLUE}=================================${NC}"

# Проверка Termux
if command -v termux-setup-storage &> /dev/null; then
    echo -e "${GREEN}[+] Обнаружен Termux${NC}"
    pkg update -y
    pkg install python python-pip -y
    pip install -r requirements.txt
    echo -e "${GREEN}[+] Установка завершена!${NC}"
    echo -e "${GREEN}[+] Запустите: python main.py${NC}"
    exit 0
fi

# Проверка Linux
if command -v apt &> /dev/null; then
    echo -e "${GREEN}[+] Обнаружен Debian/Ubuntu${NC}"
    sudo apt update
    sudo apt install python3 python3-pip -y
    pip3 install -r requirements.txt
    echo -e "${GREEN}[+] Установка завершена!${NC}"
    echo -e "${GREEN}[+] Запустите: python3 main.py${NC}"
    exit 0
fi

echo -e "${RED}[!] Неподдерживаемая система${NC}"
