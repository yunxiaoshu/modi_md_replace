from lib import modi
from lib import getmd
from lib import urlReq
import os
import argparse

#请修改下方token
token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.xxxxxxx.wgV-HRqA'
#使用代理访问待转换md文档里的图床，不用的话请修改为False
#使用代理访问待转换md文档里的图床，需要改端口请自行修改
proxy=True
proxies = {'http': "http://127.0.0.1:7890",
           'https': "https://127.0.0.1:7890"}

#下载图片
def save_url_img(url,req,proxies):
    img=req.req_get(url,proxies=proxies).content
    with open('./exch.png','wb') as f:
        f.write(img)
        f.close()

#输出新的md文档
def export_md(new_md,content):
    with open(new_md,'w') as f:
        for line in content:
            f.writelines(line+'\n')
        f.close()

#主函数
def mainFunc(token,md_path,proxies):
    gmd=getmd.Getmd(md_path)
    imgList=gmd.get_imgList()
    
    md=modi.Modi(token)
    req = urlReq.Request()
    for line in imgList:
        img_title=imgList[line][0]
        img_url=imgList[line][1]
        save_url_img(img_url,req,proxies)
        try:
            new_url='('+md.upload_img(img_title,'./exch.png',req)+')'
            print('[+] url: {0}\n -> {1}'.format(img_url,new_url))
        except Exception as e:
            print('[x] url: {0}'.format(img_url))
            print(e)
            return
        img_title='!['+imgList[line][0]+']'
        new_line={line:img_title+new_url}
        imgList.update(new_line)
    new_md=os.getcwd()+'/result/'+md_path.replace('/','\\').split('\\')[-1]+'_modi.md'
    content=gmd.modify_img(imgList)
    export_md(new_md,content)
    print('[+] 新文件输出路径: {0}'.format(new_md))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description='modi_md_replace 作者：云小书 公众号：恒运安全')
    parser.add_help=True
    parser.add_argument('-f',type=str,required=True,help='需要替换图片的md文件路径')
    args=parser.parse_args()
    md_path=args.f
    if proxy:
        mainFunc(token,md_path,proxies)
    else:
        mainFunc(token,md_path,'')
    