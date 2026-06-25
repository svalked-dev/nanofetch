#!/usr/bin/env python3
import os, subprocess

try:
    with open('art.txt', 'r') as f:
        print(f.read())
except:
    print('noasciiyet')

print(f"OS: {os.uname().sysname}")
print(f"Kernel: {os.uname().release}")
print(f"Uptime: {subprocess.getoutput('uptime -p').replace('up ', '')}")
print(f"Shell: {os.environ.get('SHELL', 'unknown')}")
print(f"User: {os.environ.get('USER', 'unknown')}@{os.uname().nodename}")
