import re
class Getmd:
    def __init__(self,path):
        self.path=path
        self.img_regular=r'\!\[(.*?)\]\((.*?)\)'
        self.img_name_regular=r'\!\[(.*?)\]'
        self.img_url_regular=r'\((.*?)\)'
       
    #获取文章内容
    def get_content(self):
        try:
            with open(self.path,'r',encoding='utf-8') as f:
                content=[]
                while True:
                    line=f.readline()
                    if line:
                        content.append(line.replace('\n',''))
                    else:
                        break
                f.close()
            return content
        except Exception as e:
            print(e)
    
    #匹配图片
    def find_img(self,line):
        if re.search(self.img_regular,line):
            return True
        return False
        
    #外部接口调用获取md文档中的图片列表
    def get_imgList(self):
        self.content=self.get_content()
        imgList={}
        for line in self.content:
            if self.find_img(line):
                img_title=re.search(self.img_name_regular,line).group().replace('!','').replace('[','').replace(']','')
                img_url=re.search(self.img_url_regular,line).group().replace('(','').replace(')','')
                img={self.content.index(line):[img_title,img_url]}
                imgList.update(img)
        return imgList
    
    #外部接口调用图片替换函数
    def modify_img(self,imgList):
        for line in imgList:
            self.content[line]=imgList[line]
        return self.content