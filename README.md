<div align="center">
  
# 🔮 NEXUS-OSINT
### *Professional Open Source Intelligence Tool*

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/yourusername/NEXUS-OSINT)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://python.org)
[![Termux](https://img.shields.io/badge/Termux-Compatible-red.svg)](https://termux.com)

</div>

## 🎯 Что это?

**NEXUS-OSINT** - мощный инструмент для сбора информации из открытых источников. Работает в Termux (Android) и Linux.

## ✨ Возможности

| Модуль | Что делает |
|--------|------------|
| 🔍 Username | Поиск на 100+ платформах |
| 📧 Email | Проверка утечек, Gravatar |
| 📱 Phone | Определение оператора, страны |
| 🌐 IP | Геолокация, провайдер |
| 🏢 Domain | WHOIS, поддомены |

## 🚀 Быстрая установка

### Termux (Android)
```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/YOUR_USERNAME/NEXUS-OSINT.git
cd NEXUS-OSINT
bash setup.sh
python main.py
