#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from datetime import datetime

def generate_html_report(results):
    """Генерация HTML отчета"""
    
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>NEXUS-OSINT Report</title>
        <style>
            body { font-family: Arial; margin: 40px; background: #0a0a0a; color: #0f0; }
            .container { max-width: 1200px; margin: 0 auto; }
            .section { margin: 20px 0; padding: 20px; border: 1px solid #0f0; }
            h1 { color: #0f0; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>NEXUS-OSINT Report</h1>
            <div class="section">
                <h2>Results</h2>
                <pre>{}</pre>
            </div>
        </div>
    </body>
    </html>
    """.format(json.dumps(results, indent=2))
    
    return html
