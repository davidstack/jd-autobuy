# -*- coding: utf-8 -*-
import threading
import bs4
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import time

import sys

reload(sys)
sys.setdefaultencoding('utf-8')



class MiaoShaThread(threading.Thread):
    def __init__(self, threadID, jd,options, stock_id):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.jd = jd
        self.options=options
        self.stock_id = stock_id
    def run(self):
        print u'添加到购物车失败'+ self.stock_id
        while not self.jd.buy(self.options, self.stock_id) and self.options.flush:
            print u'暂时无货，刷新中...'+ self.stock_id
            time.sleep(self.options.wait / 1000.0)
        print "Exiting " + self.name
