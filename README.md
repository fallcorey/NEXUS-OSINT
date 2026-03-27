<div align="center">
  
# 🔮 NEXUS-OSINT
### *Professional Open Source Intelligence Tool*

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)]()
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)]()
[![Termux](https://img.shields.io/badge/Termux-Compatible-red.svg)]()

</div>

## 🎯 Что такое NEXUS-OSINT?

**NEXUS-OSINT** - это мощный инструмент для сбора информации из открытых источников, оптимизированный для работы в Termux (Android) и Linux терминалах.

## ✨ Возможности

| Модуль | Описание | Пример |
|--------|----------|--------|
| 🔍 **Username** | Поиск на 100+ платформах | `-u username` |
| 📧 **Email** | Проверка утечек, Gravatar | `-e email@example.com` |
| 📱 **Phone** | Определение оператора, страны | `-p +79991234567` |
| 🌐 **IP** | Геолокация, провайдер, VPN | `-i 8.8.8.8` |
| 🏢 **Domain** | WHOIS, DNS, поддомены | `-d example.com` |

## 🚀 Быстрая установка

### Termux (Android)
```bash
# 1. Установите Termux из F-Droid
# 2. Выполните команды:
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/fallcorey/NEXUS-OSINT.git
cd NEXUS-OSINT
bash setup.sh
python main.py
