#!/usr/bin/env python
# -*- coding=utf-8 -*-
# author: hackqiang
# version 0.1
# requirement: python2.7

import os


def check_ip(ip):
    addrs = ip.strip().split('.')
    if len(addrs) != 4:
        return False

    for addr in addrs:
        try:
            addr = int(addr)
        except:
            return False
        if addr > 255 or addr < 0:
            return False

    return True


def my_ip():
    html = os.popen('curl -s http://myip.dnsomatic.com/')
    ip = html.readlines()[0]
    if check_ip(ip):
        return ip
    return None
