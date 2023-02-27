import os
import json
from . import getmd

class Modi:
    def __init__(self,auth):
        path=os.getcwd()+'/result'
        if os.path.exists(path):
            if not os.path.isdir(path):
                os.mkdir(path)
        else:
            os.mkdir(path)
        #导入墨滴社区token
        self.auth=auth
        
    def upload_img(self,img_title,img_path,req):
        url = "https://api.mdnice.com:443/file/user/upload"
        headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"", "Accept": "application/json, text/plain, */*", "Sec-Ch-Ua-Mobile": "?0", "Authorization": "Bearer "+self.auth, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://editor.mdnice.com", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://editor.mdnice.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7", "Connection": "close"}
        with open(img_path,'rb') as f:
            img=f.read()
            f.close()
        if img_title=='':
            img_title='exch.png'
        files=[('file',(img_title+'.png',img,'image/png'))]
        res_url=json.loads(req.req_post(url, header=headers, data={},files=files).content)["data"]
        return res_url