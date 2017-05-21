#!/usr/bin/env python
# -*- coding=utf-8 -*-
# author: hackqiang
# version 0.1
# requirement: python2.7
# pip install aliyun-python-sdk-alidns

import time
import json
import logging
import logging.handlers

from aliyunsdkcore import client
from aliyunsdkalidns.request.v20150109 import UpdateDomainRecordRequest, DescribeDomainRecordsRequest

from myutils import *


class aliDomainAUpdate(object):
    def __init__(self):
        self.pre_ip = ''
        with open('config/domains.json') as f:
            self.domains = json.load(f)
        with open('config/key.json') as f:
            keys = json.load(f)
            access_key_id = str(keys['access_key_id'])
            access_key_secret = str(keys['access_key_secret'])
        self.clt = client.AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')

    def get_A_records(self, domain):
        records = list()
        try:
            request = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
            request.set_DomainName(domain)
            request.set_accept_format('json')
            result = self.clt.do_action_with_exception(request)
            logging.debug(result)
            for record in json.loads(result)['DomainRecords']['Record']:
                if 'Type' in record and record['Type'] == 'A':
                    records.append(record)
        except Exception as e:
            logging.error(e)

        return records

    def update_A_records(self, ip, domain):
        for record in self.get_A_records(domain):
            try:
                request = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
                request.set_RR(record['RR'])
                request.set_Type(record['Type'])
                request.set_Value(ip)
                request.set_RecordId(record['RecordId'])
                request.set_TTL(record['TTL'])
                request.set_accept_format('json')
                logging.info('update %s.%s with %s' % (record['RR'], record['DomainName'], ip))
                result = self.clt.do_action_with_exception(request)
                logging.debug(result)
            except Exception as e:
                logging.error(e)

    def loop(self):
        while True:
            ip = my_ip()
            if ip:
                if self.pre_ip != ip:
                    self.pre_ip = ip
                    for domain in self.domains:
                        self.update_A_records(ip, domain)
                    logging.info('update finish')
                else:
                    logging.info('same ip %s, skip' % ip)
            time.sleep(600)


if __name__ == "__main__":
    if not os.path.exists('log'):
        os.mkdir('log')

    logging.basicConfig(level=logging.DEBUG)
    handler = logging.handlers.RotatingFileHandler('log/main.log', maxBytes=1024*1024*10, backupCount=0)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)-8s %(message)s'))
    logging.getLogger('').addHandler(handler)

    domup = aliDomainAUpdate()
    domup.loop()
