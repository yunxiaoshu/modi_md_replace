import requests as rq
from requests.packages import urllib3

class Request:
    def __init__(self):
        urllib3.disable_warnings()
        self.s=rq.Session()
    def req_get(self,url,header='',verify=False,proxies=''):
        resp=self.s.get(url,headers=header,verify=verify,proxies=proxies)
        self.s.close()
        return resp
    def req_post(self,url,header='',data='',verify=False,files='',proxies=''):
        resp = self.s.post(url, headers=header,data=data,verify=verify,files=files,proxies=proxies)
        self.s.close()
        return resp

