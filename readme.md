## md文档中的图片——Github图床自动替换墨滴图床

### 程序背景

在学习技术的过程中，不乏需要通过写博文或者发博客的形式来记录成长历程，以及撰写技术文章。通常我们会通过搭建图床配合typora来写md文档，但是在发布博客的过程中，会发现github的域名被社区或微信公众号给屏蔽了，此篇文章通过自研工具将github图床的图片上传至墨滴社区的图床内，然后完美解决该问题。

### 博文发布遇到的问题

首先，我们写了一篇精美的博文（推荐使用jsdelivr+github+typora来写博文，不会配置的可以移步度娘），准备发布的时候发现提示图片无法解析，不少朋友应该都会碰到这个问题，类似如下图所示（**其它社区包括csdn等也会出现类似情况**）：

![image-20230227152731120](https://testingcf.jsdelivr.net/gh/yunxiaoshu/images/image-20230227152731120.png)

但是我们又十分想把这篇精美的博文发布在各个社区里，怎么办呢，这时，我们可以使用本篇文章要叙述的主角来解决这个问题

### modi_md_replace使用方法

今天我们就来食用一下modi_md_replace，看看味道如何，觉得味道不错的希望各位朋友，各位大佬多多支持本公众号，帮忙转载转载，(●ˇ∀ˇ●)

咳咳~扯远了，言归正传：

modi_md_replace是由作者：云小书 开发，公众号：恒运安全 支持

嗯哼~怎么还在扯程序开发介绍，赶紧上正菜！！！

使用方法很简单，一篇通过github图床解析图片的博文被各个社区给屏蔽github域名导致无法解析图片，只能移步搭建其它图床或通过各个社区单独上传图片来发布博文，费时又费力，使用modi_md_replace将完美通过墨滴社区的图床来解决这个问题（我们先看看程序的帮助）：

```
python modi_md_replace.py -h
```

![image-20230227153658417](https://testingcf.jsdelivr.net/gh/yunxiaoshu/images/image-20230227153658417.png)

这里需要注意一点，github图床的图片通过代理加速将会更快获取到图片，所以我们需要考虑是否通过代理来解析在github图床上的图片，程序默认不使用代理，需要使用代理的请打开modi_md_replace.py文件修改proxy为True并修改proxies中的代理地址以及端口号：

![image-20230227154025911](https://testingcf.jsdelivr.net/gh/yunxiaoshu/images/image-20230227154025911.png)

除此之外还需要获取墨滴社区的token，没有账号的朋友可以先去注册一个：https://www.mdnice.com/，通过f12打开浏览器开发者工具，登录后刷新网页抓包如下：

![image-20230227154150403](https://testingcf.jsdelivr.net/gh/yunxiaoshu/images/image-20230227154150403.png)

将token的值取出来在modi_md_replace.py文件中替换即可，接下来我们便可以直接执行如下命令进行图床替换了

```
python modi_md_replace.py -f D:\eyeurl\README.md
```

![image-20230227154559953](https://testingcf.jsdelivr.net/gh/yunxiaoshu/images/image-20230227154559953.png)

可以看到执行完毕并输出了新的文件，新的文件将会输出至本项目文件路径下的result文件夹内，打开查看可以看到图床链接已被完美替换：

![image-20230227154724391](https://testingcf.jsdelivr.net/gh/yunxiaoshu/images/image-20230227154724391.png)

最后，我们便可以直接使用墨滴的插件去订阅号内发表markdown语法的博文了，发布的文章也是十分的精细美丽，真是美滋滋~(●ˇ∀ˇ●)~

效果如下图所示：

![image-20230227154957346](https://testingcf.jsdelivr.net/gh/yunxiaoshu/images/image-20230227154957346.png)