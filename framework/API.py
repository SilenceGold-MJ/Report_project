#!/user/bin/env python3
# -*- coding: utf-8 -*-
import requests,json
from framework.logger import Logger
logger = Logger(logger="API").getlog()

from config.config import *
import configparser,os
proDir = os.getcwd()
configPath = os.path.join(proDir, "config\config.ini")
cf = configparser.ConfigParser()
cf.read(configPath,encoding="utf-8-sig")

address=terminal_server()['host']
port=terminal_server()['port']


class API():

    def APIall(self,connect, dic):
        url = "http://%s:%s/%s"%(address,port,connect)
        payload = json.dumps(dic)
        logger.info( "url:%s"%url )
        logger.info("payload:%s"%payload)
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        data = json.loads(response.text)
        logger.info('return:%s'%data)
        return data
