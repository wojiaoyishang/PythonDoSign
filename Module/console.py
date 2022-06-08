# -*- coding:utf-8 -*-
"""
ESC颜色符定义在此源码中，并提供了一些常用的输出函数
"""
import time

NONE = "\033[m"
RED = "\033[0;32;31m"
LIGHT_RED = "\033[1;31m"
GREEN = "\033[0;32;32m"
LIGHT_GREEN = "\033[1;32m"
BLUE = "\033[0;32;34m"
LIGHT_BLUE = "\033[1;34m"
DARY_GRAY = "\033[1;30m"
CYAN = "\033[0;36m"
LIGHT_CYAN = "\033[1;36m"
PURPLE = "\033[0;35m"
LIGHT_PURPLE = "\033[1;35m"
BROWN = "\033[0;33m"
YELLOW = "\033[1;33m"
LIGHT_GRAY = "\033[0;37m"
WHITE = "\033[1;37m"


def debug(*args):
    print(f'{YELLOW}[{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}](Debug):', *args, f"{NONE}")

def error(*args):
    print(f'{RED}[{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}](Error):', *args, f"{NONE}")

def info(*args):
    print(f'{LIGHT_BLUE}[{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}](Info):', *args, f"{NONE}")

def log(*args):
    print(f'{LIGHT_CYAN}[{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}](Log):', *args, f"{NONE}")

def warn(*args):
    print(f'{YELLOW}[{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}](Warn):', *args, f"{NONE}")

def success(*args):
    print(f'{GREEN}[{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}](Success):', *args, f"{NONE}")

def plain(*args):
    print(f'[{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}](Plain):', *args)
