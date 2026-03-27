#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import requests

def analyze(email):
    """Анализ email адреса"""
    
    # Валидация
    if "@" not in email:
        return {"valid": False, "error": "Invalid email format"}
    
    username = email.split("@")[0]
    domain = email.split("@")[1]
    
    # Gravatar
    email_hash = hashlib.md5(email.lower().encode()).hexdigest()
    gravatar_url = f"https://www.gravatar.com/avatar/{email_hash}?d=404"
    
    gravatar_exists = False
    try:
        response = requests.get(gravatar_url, timeout=3)
        gravatar_exists = response.status_code == 200
    except:
        pass
    
    return {
        "valid": True,
        "email": email,
        "username": username,
        "domain": domain,
        "gravatar": {
            "exists": gravatar_exists,
            "url": gravatar_url
        }
    }
