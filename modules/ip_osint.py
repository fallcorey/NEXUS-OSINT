#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

def track(ip):
    """Получение информации по IP"""
    
    try:
        # IP-API
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = response.json()
        
        if data["status"] == "success":
            return {
                "ip": ip,
                "country": data.get("country"),
                "country_code": data.get("countryCode"),
                "region": data.get("regionName"),
                "city": data.get("city"),
                "zip": data.get("zip"),
                "lat": data.get("lat"),
                "lon": data.get("lon"),
                "isp": data.get("isp"),
                "org": data.get("org"),
                "as": data.get("as")
            }
        else:
            return {"error": "IP not found"}
            
    except Exception as e:
        return {"error": str(e)}
