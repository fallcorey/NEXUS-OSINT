#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dark Web Search Module for NEXUS-OSINT
Поиск информации в Tor сети и даркнете
"""

import requests
import json
from urllib.parse import quote

class DarkWebSearch:
    def __init__(self):
        self.tor_proxy = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        self.onion_engines = {
            'ahmia': 'http://ahmia.fi/search/?q={}',
            'tor66': 'http://tor66searchengine.com/search?q={}',
            'haystack': 'http://haystakvxad7wbk5.onion/?q={}',
            'darksearch': 'http://darksearch.onion/search?q={}'
        }
        
    def check_tor_connection(self):
        """Проверка доступности Tor"""
        try:
            # Проверка через обычный интернет
            response = requests.get('http://check.torproject.org', timeout=5)
            return 'Congratulations' in response.text
        except:
            return False
    
    def search_onion_sites(self, query, use_tor=False):
        """Поиск по onion-сайтам"""
        results = []
        
        if use_tor and self.check_tor_connection():
            print("[+] Tor подключен, выполняется поиск...")
            for engine, url in self.onion_engines.items():
                try:
                    search_url = url.format(quote(query))
                    response = requests.get(search_url, proxies=self.tor_proxy, timeout=15)
                    if response.status_code == 200:
                        results.append({
                            'engine': engine,
                            'url': search_url,
                            'found': True
                        })
                except:
                    results.append({
                        'engine': engine,
                        'url': search_url,
                        'found': False,
                        'error': 'Tor connection failed'
                    })
        else:
            print("[!] Tor не обнаружен. Результаты будут ограничены.")
            # Поиск через общедоступные зеркала
            for engine, url in self.onion_engines.items():
                if engine in ['ahmia', 'tor66']:
                    results.append({
                        'engine': engine,
                        'url': url.format(quote(query)),
                        'available_via': 'clearnet mirror',
                        'note': 'Откройте в обычном браузере'
                    })
        
        return results
    
    def search_breaches(self, username):
        """Поиск в утечках баз данных"""
        breaches = []
        
        # Известные утечки
        known_breaches = {
            'collection1': 'Collection #1 (773M emails)',
            'antipublic': 'AntiPublic (458M records)',
            'breachcompilation': 'Breach Compilation (3B records)'
        }
        
        for breach_name, breach_desc in known_breaches.items():
            breaches.append({
                'name': breach_name,
                'description': breach_desc,
                'search_query': f"https://haveibeenpwned.com/account/{username}"
            })
        
        return breaches
    
    def search_forums(self, username):
        """Поиск по даркнет форумам"""
        forums = [
            {'name': 'Dread', 'url': 'http://dreadytofatroptsdj6io7l3xptbetj2rf3dvmv4lizg7c3v7ss4jq4yd.onion', 'type': 'darknet'},
            {'name': 'Dark0de', 'url': 'http://darkodew6hxcb36k.onion', 'type': 'darknet'},
            {'name': 'RuTor', 'url': 'http://rutor2tljxf2gvty.onion', 'type': 'darknet'},
            {'name': 'XSS.is', 'url': 'https://xss.is', 'type': 'clearnet'}
        ]
        
        results = []
        for forum in forums:
            results.append({
                'forum': forum['name'],
                'url': forum['url'],
                'type': forum['type'],
                'search_suggestion': f"Поиск пользователя {username} на {forum['name']}"
            })
        
        return results
    
    def get_darkweb_stats(self):
        """Получение статистики по даркнету"""
        return {
            'onion_sites': '~70,000 активных onion-сайтов',
            'marketplaces': '~50 активных маркетплейсов',
            'forums': '~100 форумов на русском и английском',
            'search_engines': ['Ahmia', 'Tor66', 'Haystack', 'DarkSearch']
        }

# Функция для использования в main.py
def search(query):
    searcher = DarkWebSearch()
    return {
        'query': query,
        'tor_available': searcher.check_tor_connection(),
        'onion_results': searcher.search_onion_sites(query, searcher.check_tor_connection()),
        'breaches': searcher.search_breaches(query),
        'forums': searcher.search_forums(query),
        'stats': searcher.get_darkweb_stats(),
        'setup_guide': {
            'install_tor': 'sudo apt install tor -y',
            'start_tor': 'sudo systemctl start tor',
            'use_proxy': 'Настройте прокси 127.0.0.1:9050'
        }
    }
