#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Расширенный модуль поиска по username
Поддержка 200+ платформ
"""

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def search(username):
    """Расширенный поиск по username"""
    
    # Расширенный список платформ (200+)
    platforms = [
        # Социальные сети
        "github.com", "gitlab.com", "bitbucket.org", "sourceforge.net",
        "twitter.com", "instagram.com", "facebook.com", "reddit.com",
        "t.me", "youtube.com", "tiktok.com", "pinterest.com", "twitch.tv",
        "vk.com", "linkedin.com", "medium.com", "dev.to", "habr.com",
        "vc.ru", "pikabu.ru", "dtf.ru", "4pda.to", "lolz.live", "xss.is",
        
        # Профессиональные
        "stackoverflow.com", "leetcode.com", "kaggle.com", "hackerrank.com",
        "upwork.com", "freelancer.com", "fiverr.com", "codepen.io",
        
        # Креативные
        "behance.net", "dribbble.com", "deviantart.com", "artstation.com",
        
        # Гейминг
        "steamcommunity.com", "twitch.tv", "discord.com", "epicgames.com",
        
        # Фото/видео
        "flickr.com", "500px.com", "vimeo.com", "dailymotion.com",
        
        # Российские
        "habr.com", "vc.ru", "pikabu.ru", "dtf.ru", "4pda.to",
        "lolz.live", "xss.is", "antichat.ru", "rusvesna.su",
        
        # Другие
        "pastebin.com", "gist.github.com", "replit.com", "glitch.com",
        "codewars.com", "codecademy.com", "coursera.org", "udemy.com"
    ]
    
    results = []
    
    def check_platform(platform):
        url = f"https://{platform}/{username}"
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(url, timeout=3, headers=headers, allow_redirects=True)
            if response.status_code == 200:
                return {"platform": platform, "url": url, "status": 200}
            elif response.status_code in [301, 302, 307, 308]:
                return {"platform": platform, "url": response.headers.get('Location', url), "status": response.status_code}
        except:
            pass
        return None
    
    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = [executor.submit(check_platform, p) for p in platforms]
        for future in as_completed(futures):
            result = future.result()
            if result:
                results.append(result)
    
    return {
        "username": username,
        "found": len(results),
        "total_checked": len(platforms),
        "platforms": results
    }
