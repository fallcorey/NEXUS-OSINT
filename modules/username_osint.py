#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from concurrent.futures import ThreadPoolExecutor

def search(username):
    """Расширенный поиск по username"""
    
    platforms = [
        "github.com",
        "twitter.com", 
        "instagram.com",
        "reddit.com",
        "t.me",
        "youtube.com",
        "twitch.tv",
        "pinterest.com",
        "tumblr.com",
        "medium.com",
        "patreon.com",
        "spotify.com",
        "facebook.com",
        "linkedin.com",
        "vk.com"
    ]
    
    results = []
    
    def check_platform(platform):
        url = f"https://{platform}/{username}"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                return {"platform": platform, "url": url}
        except:
            pass
        return None
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_platform, p) for p in platforms]
        for future in futures:
            result = future.result()
            if result:
                results.append(result)
    
    return {
        "username": username,
        "found": len(results),
        "platforms": results
    }
