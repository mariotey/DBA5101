# server_pull.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:53:41 2020

@author: iora
"""

import requests

def pull(user_group, secret_key, arm):
    url = 'https://appiora.nus.edu.sg/pull_arm/%s/%s/%s' % (user_group, secret_key, str(arm))
    try:
        r = requests.get(url, timeout=10)  # Set a timeout (e.g., 10 seconds)
        r.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)

        output = r.json()['result']
        return output
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None