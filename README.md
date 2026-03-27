<div align="center">
  
# 🔮 NEXUS-OSINT PRO v3.0
### *Professional Open Source Intelligence Tool + Dark Web Search*

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)]()
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)]()
[![Termux](https://img.shields.io/badge/Termux-Compatible-red.svg)]()
[![Dark Web](https://img.shields.io/badge/Dark-Web-black.svg)]()

</div>

## 🎯 Что нового в v3.0?

### 🔥 НОВЫЕ ВОЗМОЖНОСТИ:

| Функция | Описание |
|---------|----------|
| 🕸️ **Dark Web Search** | Поиск в Tor сети и onion-сайтах |
| 🔍 **200+ Платформ** | Расширенный поиск username |
| 📧 **Утечки данных** | Проверка через HIBP API |
| 🏢 **Анализ домена** | WHOIS, DNS, поддомены |
| 📊 **HTML Отчеты** | Красивые визуальные отчеты |

## 🚀 Быстрая установка

### Termux (Android)
```bash
pkg update && pkg upgrade -y
pkg install python git tor -y
git clone https://github.com/fallcorey/NEXUS-OSINT.git
cd NEXUS-OSINT
pip install -r requirements.txt
python main.py -h
