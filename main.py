#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse
import json
import requests
from datetime import datetime

class NEXUS_OSINT:
    def __init__(self):
        self.version = "2.0.0"
        self.results = {}
        
    def banner(self):
        """Красивый баннер"""
        banner_text = """
╔══════════════════════════════════════════════════════════════╗
║  ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗                ║
║  ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝                ║
║  ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗                ║
║  ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║                ║
║  ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║                ║
║  ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝                ║
║                    NEXUS-OSINT v2.0                         ║
║              Professional OSINT Tool                        ║
╚══════════════════════════════════════════════════════════════╝
        """
        print(banner_text)
        print("=" * 60)
        print("[+] GitHub: https://github.com/ВАШ_ЛОГИН/NEXUS-OSINT")
        print("[+] Version: 2.0.0")
        print("=" * 60)
    
    def search_username(self, username):
        """Поиск по username на различных платформах"""
        print(f"\n[*] Поиск username: {username}")
        print("-" * 50)
        
        platforms = [
            {"name": "GitHub", "url": f"https://github.com/{username}"},
            {"name": "Twitter", "url": f"https://twitter.com/{username}"},
            {"name": "Instagram", "url": f"https://instagram.com/{username}"},
            {"name": "Reddit", "url": f"https://reddit.com/user/{username}"},
            {"name": "Telegram", "url": f"https://t.me/{username}"},
            {"name": "YouTube", "url": f"https://youtube.com/@{username}"},
            {"name": "TikTok", "url": f"https://tiktok.com/@{username}"},
            {"name": "Pinterest", "url": f"https://pinterest.com/{username}"},
            {"name": "Twitch", "url": f"https://twitch.tv/{username}"},
            {"name": "VK", "url": f"https://vk.com/{username}"},
        ]
        
        found = []
        for platform in platforms:
            try:
                response = requests.get(platform["url"], timeout=5)
                if response.status_code == 200:
                    found.append(platform)
                    print(f"[+] Найдено на {platform['name']}: {platform['url']}")
                elif response.status_code == 404:
                    print(f"[-] {platform['name']}: не найден")
            except:
                print(f"[!] {platform['name']}: ошибка соединения")
        
        if not found:
            print("\n[-] Username не найден ни на одной платформе")
        else:
            print(f"\n[+] Всего найдено: {len(found)} платформ")
        
        return found
    
    def search_email(self, email):
        """Анализ email"""
        print(f"\n[*] Анализ email: {email}")
        print("-" * 50)
        
        # Проверка формата
        if "@" not in email or "." not in email:
            print("[-] Неверный формат email")
            return
        
        domain = email.split("@")[1]
        username = email.split("@")[0]
        
        print(f"[+] Домен: {domain}")
        print(f"[+] Username: {username}")
        
        # Проверка Gravatar
        import hashlib
        email_hash = hashlib.md5(email.lower().encode()).hexdigest()
        gravatar_url = f"https://www.gravatar.com/avatar/{email_hash}"
        print(f"[+] Gravatar: {gravatar_url}")
        
        return {"email": email, "domain": domain}
    
    def track_ip(self, ip):
        """Информация по IP адресу"""
        print(f"\n[*] Анализ IP: {ip}")
        print("-" * 50)
        
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
            data = response.json()
            
            if data["status"] == "success":
                print(f"[+] Страна: {data['country']}")
                print(f"[+] Город: {data['city']}")
                print(f"[+] Регион: {data['regionName']}")
                print(f"[+] Провайдер: {data['isp']}")
                print(f"[+] Организация: {data['org']}")
                print(f"[+] Координаты: {data['lat']}, {data['lon']}")
                return data
            else:
                print("[-] IP не найден")
        except:
            print("[-] Ошибка при получении данных")
        
        return None
    
    def save_report(self, filename=None):
        """Сохранение отчета"""
        if not self.results:
            print("[-] Нет данных для сохранения")
            return
        
        if not filename:
            filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=4, ensure_ascii=False)
        
        print(f"[+] Отчет сохранен в {filename}")
    
    def run(self):
        """Запуск инструмента"""
        self.banner()
        
        parser = argparse.ArgumentParser(description='NEXUS-OSINT - Professional OSINT Tool')
        parser.add_argument('-u', '--username', help='Поиск по username')
        parser.add_argument('-e', '--email', help='Анализ email')
        parser.add_argument('-i', '--ip', help='Информация по IP адресу')
        parser.add_argument('-o', '--output', help='Сохранить отчет в файл')
        
        args = parser.parse_args()
        
        # Проверка аргументов
        if len(sys.argv) == 1:
            parser.print_help()
            print("\n[*] Примеры использования:")
            print("  python main.py -u john_doe")
            print("  python main.py -e user@example.com")
            print("  python main.py -i 8.8.8.8")
            sys.exit(0)
        
        # Выполнение запросов
        if args.username:
            result = self.search_username(args.username)
            self.results['username'] = result
        
        if args.email:
            result = self.search_email(args.email)
            self.results['email'] = result
        
        if args.ip:
            result = self.track_ip(args.ip)
            self.results['ip'] = result
        
        # Сохранение отчета
        if args.output and self.results:
            self.save_report(args.output)
        
        print("\n" + "=" * 60)
        print("[✓] Анализ завершен!")
        print("=" * 60)

if __name__ == "__main__":
    try:
        tool = NEXUS_OSINT()
        tool.run()
    except KeyboardInterrupt:
        print("\n\n[!] Прервано пользователем")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Ошибка: {e}")
        sys.exit(1)
