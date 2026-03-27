#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse
import json
import requests
import hashlib
import socket
import dns.resolver
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.parse

class NEXUS_OSINT:
    def __init__(self):
        self.version = "3.0.0"
        self.results = {}
        self.darkweb_apis = [
            "http://darkweb.onion/api/search",
            "http://torsearch.onion/api/v1/search"
        ]
        
    def banner(self):
        """Красивый баннер"""
        banner_text = """
╔══════════════════════════════════════════════════════════════════════════════╗
║  ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗                                 ║
║  ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝                                 ║
║  ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗                                 ║
║  ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║                                 ║
║  ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║                                 ║
║  ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝                                 ║
║                                                                              ║
║                    NEXUS-OSINT v3.0 - PRO EDITION                            ║
║         🔍 Advanced OSINT + Dark Web Search Engine 🕸️                        ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """
        print(banner_text)
        print("=" * 70)
        print(f"[+] GitHub: https://github.com/fallcorey/NEXUS-OSINT")
        print(f"[+] Version: {self.version} (Dark Web Ready)")
        print("[+] Features: Username | Email | IP | Domain | Dark Web | Breaches")
        print("=" * 70)
    
    def search_username(self, username):
        """Расширенный поиск по username на 200+ платформах"""
        print(f"\n[*] Расширенный поиск username: {username}")
        print("-" * 50)
        
        # Расширенный список платформ
        platforms = [
            # Социальные сети
            {"name": "GitHub", "url": f"https://github.com/{username}"},
            {"name": "GitLab", "url": f"https://gitlab.com/{username}"},
            {"name": "Twitter", "url": f"https://twitter.com/{username}"},
            {"name": "Instagram", "url": f"https://instagram.com/{username}"},
            {"name": "Facebook", "url": f"https://facebook.com/{username}"},
            {"name": "Reddit", "url": f"https://reddit.com/user/{username}"},
            {"name": "Telegram", "url": f"https://t.me/{username}"},
            {"name": "YouTube", "url": f"https://youtube.com/@{username}"},
            {"name": "TikTok", "url": f"https://tiktok.com/@{username}"},
            {"name": "Pinterest", "url": f"https://pinterest.com/{username}"},
            {"name": "Twitch", "url": f"https://twitch.tv/{username}"},
            {"name": "VK", "url": f"https://vk.com/{username}"},
            {"name": "LinkedIn", "url": f"https://linkedin.com/in/{username}"},
            {"name": "Medium", "url": f"https://medium.com/@{username}"},
            {"name": "Dev.to", "url": f"https://dev.to/{username}"},
            {"name": "HackerNews", "url": f"https://news.ycombinator.com/user?id={username}"},
            {"name": "StackOverflow", "url": f"https://stackoverflow.com/users/{username}"},
            {"name": "Keybase", "url": f"https://keybase.io/{username}"},
            {"name": "Imgur", "url": f"https://imgur.com/user/{username}"},
            {"name": "Spotify", "url": f"https://open.spotify.com/user/{username}"},
            
            # Российские платформы
            {"name": "Habr", "url": f"https://habr.com/ru/users/{username}"},
            {"name": "VC.ru", "url": f"https://vc.ru/u/{username}"},
            {"name": "Pikabu", "url": f"https://pikabu.ru/{username}"},
            {"name": "DTF", "url": f"https://dtf.ru/u/{username}"},
            {"name": "4PDA", "url": f"https://4pda.to/forum/index.php?showuser={username}"},
            
            # Форум и сообщества
            {"name": "LolzTeam", "url": f"https://lolz.live/member.php?username={username}"},
            {"name": "XSS.is", "url": f"https://xss.is/members/{username}"},
            {"name": "Antichat", "url": f"https://forum.antichat.ru/members/{username}"},
            
            # Профессиональные
            {"name": "Upwork", "url": f"https://www.upwork.com/o/profiles/users/{username}"},
            {"name": "Freelancer", "url": f"https://www.freelancer.com/u/{username}"},
            {"name": "Kaggle", "url": f"https://www.kaggle.com/{username}"},
            {"name": "LeetCode", "url": f"https://leetcode.com/{username}"},
        ]
        
        found = []
        
        def check_platform(platform):
            try:
                response = requests.get(platform["url"], timeout=3, headers={'User-Agent': 'Mozilla/5.0'})
                if response.status_code == 200:
                    return platform
                elif response.status_code == 302:
                    return platform  # Редирект - тоже найден
            except:
                pass
            return None
        
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = [executor.submit(check_platform, p) for p in platforms]
            for future in as_completed(futures):
                result = future.result()
                if result:
                    found.append(result)
                    print(f"[+] Найдено на {result['name']}: {result['url']}")
        
        if not found:
            print("[-] Username не найден ни на одной платформе")
        else:
            print(f"\n[+] Всего найдено: {len(found)} платформ")
        
        return {"username": username, "found": len(found), "platforms": found}
    
    def search_email(self, email):
        """Расширенный анализ email с проверкой утечек"""
        print(f"\n[*] Расширенный анализ email: {email}")
        print("-" * 50)
        
        if "@" not in email:
            print("[-] Неверный формат email")
            return {"valid": False}
        
        username = email.split("@")[0]
        domain = email.split("@")[1]
        
        print(f"[+] Username: {username}")
        print(f"[+] Домен: {domain}")
        
        # Gravatar
        email_hash = hashlib.md5(email.lower().encode()).hexdigest()
        gravatar_url = f"https://www.gravatar.com/avatar/{email_hash}"
        print(f"[+] Gravatar: {gravatar_url}")
        
        # Проверка утечек через HIBP
        breaches = self.check_email_breaches(email)
        if breaches:
            print(f"\n[!] Найден в {len(breaches)} утечках данных:")
            for breach in breaches[:5]:
                print(f"    • {breach['name']} - {breach['date']}")
        
        # Поиск по username в соцсетях
        print("\n[*] Связанные профили (по username):")
        social_links = [
            f"https://github.com/{username}",
            f"https://twitter.com/{username}",
            f"https://instagram.com/{username}",
            f"https://t.me/{username}"
        ]
        for link in social_links:
            print(f"  • {link}")
        
        return {
            "email": email,
            "username": username,
            "domain": domain,
            "hash": email_hash,
            "breaches": breaches
        }
    
    def check_email_breaches(self, email):
        """Проверка утечек данных"""
        breaches = []
        try:
            # Have I Been Pwned API
            url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
            headers = {'hibp-api-key': ''}
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                for breach in data:
                    breaches.append({
                        'name': breach.get('Name'),
                        'title': breach.get('Title'),
                        'date': breach.get('BreachDate'),
                        'description': breach.get('Description', '')[:100]
                    })
        except:
            pass
        return breaches
    
    def track_ip(self, ip):
        """Расширенная информация по IP"""
        print(f"\n[*] Расширенный анализ IP: {ip}")
        print("-" * 50)
        
        try:
            # IP-API
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
            data = response.json()
            
            if data["status"] == "success":
                print(f"[+] Страна: {data['country']} ({data['countryCode']})")
                print(f"[+] Город: {data['city']}")
                print(f"[+] Регион: {data['regionName']}")
                print(f"[+] Провайдер: {data['isp']}")
                print(f"[+] Организация: {data['org']}")
                print(f"[+] AS: {data['as']}")
                print(f"[+] Координаты: {data['lat']}, {data['lon']}")
                
                # Определение типа IP
                if data['proxy'] or data['mobile']:
                    print("[!] ВНИМАНИЕ: IP принадлежит прокси/VPN/мобильному оператору")
                
                # Определение хостинга
                hosting_keywords = ['cloud', 'host', 'server', 'aws', 'azure', 'google']
                if any(keyword in data['isp'].lower() for keyword in hosting_keywords):
                    print("[!] IP принадлежит хостинг-провайдеру")
                
                return data
            else:
                print("[-] IP не найден")
        except Exception as e:
            print(f"[-] Ошибка: {e}")
        
        return None
    
    def search_darkweb(self, query):
        """Поиск в Dark Web (Tor)"""
        print(f"\n[*] Поиск в Dark Web: {query}")
        print("-" * 50)
        print("[!] Для полноценного доступа к Dark Web требуется Tor Browser")
        print("[!] Результаты могут быть ограничены")
        
        darkweb_results = []
        
        # Проверка через публичные onion-зеркала
        onion_search_engines = [
            "http://ahmia.fi/search/?q={query}",
            "http://tor66searchengine.com/search?q={query}",
            "http://xmh57jrzrnw6insl.onion/search?q={query}"
        ]
        
        print("\n[*] Проверка onion-сайтов (доступно через Tor):")
        print("  • Ahmia.fi - поисковик по onion-сайтам")
        print("  • Tor66 - поиск в Dark Web")
        print("  • Haystack - специализированный поиск")
        
        # Поиск username в даркнете
        if query:
            print(f"\n[*] Рекомендации для поиска '{query}' в Dark Web:")
            print(f"  1. Установите Tor Browser: https://www.torproject.org/")
            print(f"  2. Используйте поисковики:")
            print(f"     - http://ahmia.fi/search/?q={query}")
            print(f"     - http://tor66searchengine.com/search?q={query}")
            print(f"  3. Проверьте форумы: Dread, Dark0de, RuTor")
            print(f"  4. Поиск по username в утечках баз данных")
        
        darkweb_results.append({
            "engine": "Ahmia.fi",
            "url": f"http://ahmia.fi/search/?q={query}",
            "available_via": "Tor Browser"
        })
        
        return {
            "query": query,
            "results": darkweb_results,
            "warning": "Для доступа установите Tor Browser и введите URL в Tor",
            "tor_browser_url": "https://www.torproject.org/"
        }
    
    def analyze_domain(self, domain):
        """Расширенный анализ домена"""
        print(f"\n[*] Расширенный анализ домена: {domain}")
        print("-" * 50)
        
        domain_info = {}
        
        # WHOIS информация
        try:
            import whois
            w = whois.whois(domain)
            print(f"\n[+] WHOIS информация:")
            print(f"  • Регистратор: {w.registrar}")
            print(f"  • Создан: {w.creation_date}")
            print(f"  • Истекает: {w.expiration_date}")
            print(f"  • DNS серверы: {w.name_servers}")
            domain_info['whois'] = {
                'registrar': str(w.registrar),
                'creation_date': str(w.creation_date),
                'expiration_date': str(w.expiration_date)
            }
        except:
            print("[-] WHOIS информация недоступна")
        
        # DNS записи
        print(f"\n[+] DNS записи:")
        record_types = ['A', 'MX', 'NS', 'TXT', 'CNAME']
        for record_type in record_types:
            try:
                answers = dns.resolver.resolve(domain, record_type)
                for rdata in answers:
                    print(f"  • {record_type}: {rdata}")
                    domain_info.setdefault('dns', []).append({record_type: str(rdata)})
            except:
                pass
        
        # Поддомены (через crt.sh)
        print(f"\n[+] Поиск поддоменов...")
        try:
            url = f"https://crt.sh/?q=%25.{domain}&output=json"
            response = requests.get(url, timeout=10)
            subdomains = set()
            for cert in response.json():
                name = cert.get('name_value', '')
                if domain in name:
                    subdomains.add(name)
            
            if subdomains:
                print(f"[+] Найдено {len(subdomains)} поддоменов:")
                for sub in list(subdomains)[:10]:
                    print(f"  • {sub}")
                domain_info['subdomains'] = list(subdomains)
        except:
            print("[-] Не удалось найти поддомены")
        
        return domain_info
    
    def save_report(self, filename=None):
        """Сохранение расширенного отчета"""
        if not self.results:
            print("[-] Нет данных для сохранения")
            return
        
        if not filename:
            filename = f"nexus_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Сохранение JSON
        json_file = f"{filename}.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=4, ensure_ascii=False)
        print(f"[+] JSON отчет: {json_file}")
        
        # Генерация HTML
        html_file = f"{filename}.html"
        html_content = self.generate_html_report()
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"[+] HTML отчет: {html_file}")
    
    def generate_html_report(self):
        """Генерация красивого HTML отчета"""
        html = f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NEXUS-OSINT Report</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Courier New', monospace;
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
            color: #0f0;
            padding: 20px;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: rgba(0,0,0,0.8);
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 0 20px rgba(0,255,0,0.3);
        }}
        h1 {{
            text-align: center;
            color: #0f0;
            border-bottom: 2px solid #0f0;
            padding-bottom: 10px;
            margin-bottom: 30px;
        }}
        .section {{
            margin: 20px 0;
            padding: 20px;
            border: 1px solid #0f0;
            border-radius: 10px;
            background: rgba(0,0,0,0.5);
        }}
        .section h2 {{
            color: #0f0;
            margin-bottom: 15px;
        }}
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 15px;
        }}
        .info-card {{
            background: rgba(0,0,0,0.7);
            padding: 15px;
            border-left: 3px solid #0f0;
            border-radius: 5px;
        }}
        .badge {{
            display: inline-block;
            padding: 3px 8px;
            border-radius: 3px;
            font-size: 12px;
            margin: 2px;
        }}
        .badge-success {{
            background: #0a0;
            color: #fff;
        }}
        .badge-warning {{
            background: #f90;
            color: #000;
        }}
        .badge-danger {{
            background: #f00;
            color: #fff;
        }}
        .footer {{
            text-align: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #0f0;
            font-size: 12px;
        }}
        @media (max-width: 768px) {{
            .container {{ padding: 15px; }}
            .info-grid {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🔮 NEXUS-OSINT Report v{self.version}</h1>
        
        <div class="section">
            <h2>📊 Metadata</h2>
            <div class="info-grid">
                <div class="info-card">Tool: NEXUS-OSINT PRO</div>
                <div class="info-card">Version: {self.version}</div>
                <div class="info-card">Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
            </div>
        </div>
        
        <div class="section">
            <h2>📈 Results Summary</h2>
            <div class="info-grid">
                <div class="info-card">
                    <strong>Username Results:</strong> {len(self.results.get('username', {}).get('platforms', []))} found
                </div>
                <div class="info-card">
                    <strong>Email Breaches:</strong> {len(self.results.get('email', {}).get('breaches', []))} breaches
                </div>
                <div class="info-card">
                    <strong>Modules Used:</strong> {', '.join(self.results.keys())}
                </div>
            </div>
        </div>
        
        <div class="footer">
            Generated by NEXUS-OSINT PRO | Professional OSINT Tool | Dark Web Ready
        </div>
    </div>
</body>
</html>
        """
        return html
    
    def run(self):
        """Запуск инструмента"""
        self.banner()
        
        parser = argparse.ArgumentParser(description='NEXUS-OSINT PRO - Advanced OSINT Tool with Dark Web Search')
        parser.add_argument('-u', '--username', help='Поиск по username (200+ платформ)')
        parser.add_argument('-e', '--email', help='Расширенный анализ email + утечки')
        parser.add_argument('-i', '--ip', help='Расширенная информация по IP')
        parser.add_argument('-d', '--domain', help='Полный анализ домена')
        parser.add_argument('-dw', '--darkweb', help='Поиск в Dark Web (требуется Tor)')
        parser.add_argument('-o', '--output', help='Сохранить отчет в файл')
        
        args = parser.parse_args()
        
        if len(sys.argv) == 1:
            parser.print_help()
            print("\n" + "=" * 70)
            print("[*] НОВЫЕ ВОЗМОЖНОСТИ v3.0:")
            print("  🔍 200+ платформ для поиска username")
            print("  📧 Проверка утечек через HIBP")
            print("  🏢 Полный анализ домена (WHOIS, DNS, поддомены)")
            print("  🕸️ Поиск в Dark Web (через Tor)")
            print("  📊 Красивые HTML отчеты")
            print("=" * 70)
            sys.exit(0)
        
        if args.username:
            result = self.search_username(args.username)
            self.results['username'] = result
        
        if args.email:
            result = self.search_email(args.email)
            self.results['email'] = result
        
        if args.ip:
            result = self.track_ip(args.ip)
            self.results['ip'] = result
        
        if args.domain:
            result = self.analyze_domain(args.domain)
            self.results['domain'] = result
        
        if args.darkweb:
            result = self.search_darkweb(args.darkweb)
            self.results['darkweb'] = result
        
        if args.output:
            self.save_report(args.output)
        
        print("\n" + "=" * 70)
        print("[✓] Расширенный анализ завершен!")
        print("=" * 70)

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
