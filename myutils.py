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
    try:
        ip = html.readlines()[0]
        if check_ip(ip):
            return ip
    except:
        pass
    return None
    

def get_root_domain(domain):
    s = domain.split('.')
    return s[-2] + '.' + s[-1]
    

if __name__ == "__main__":
    print get_root_domain('x.y.baidu.com')
    print get_root_domain('x.baidu.com')
    print get_root_domain('baidu.com')
