# Title: wechat push CVE-2020
# Date: 2020-5-9
# Exploit Author: weixiao9188
# Version: 4.0
# Tested on: Linux,windows
# coding:UTF-8
import requests
import json
import time
import os
import pandas as pd
time_sleep = 20 #每隔20秒爬取一次
while(True):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"}
    #判断文件是否存在
    datas = []
    response1=None
    response2=None
    if os.path.exists("olddata.csv"):
        #如果文件存在则每次爬取10个
        df = pd.read_csv("olddata.csv", header=None)
        datas = df.where(df.notnull(),None).values.tolist()#将提取出来的数据中的nan转化为None
        response1 = requests.get(url="https://api.github.com/search/repositories?q=CVE-2020&sort=updated&per_page=10",
                                 headers=headers)
        response2 = requests.get(url="https://api.github.com/search/repositories?q=RCE&ssort=updated&per_page=10",
                                 headers=headers)

    else:
        #不存在爬取全部
        datas = []
        response1 = requests.get(url="https://api.github.com/search/repositories?q=CVE-2020&sort=updated&order=desc",headers=headers)
        response2 = requests.get(url="https://api.github.com/search/repositories?q=RCE&ssort=updated&order=desc",headers=headers)

    data1 = json.loads(response1.text)
    data2 = json.loads(response2.text)
    for j in [data1["items"],data2["items"]]:
        for i in j:
            s = {"name":i['name'],"html":i['html_url'],"description":i['description']}
            s1 =[i['name'],i['html_url'],i['description']]
            if s1 not in datas:
                #print(s1)
                #print(datas)
                params = {
                     "text":s["name"],
                    "desp":" 链接:"+str(s["html"])+"\n简介"+str(s["description"])
                }
                print("当前推送为"+str(s)+"\n")
                print(params)
                requests.get("https://sc.ftqq.com/XXXX.send",params=params,timeout=10,verify=False)
                #time.sleep(1)#以防推送太猛
                print("推送完成!")
                datas.append(s1)
            else:
                pass
                #print("数据已处在!")
    pd.DataFrame(datas).to_csv("olddata.csv",header=None,index=None)
    time.sleep(time_sleep)
"""
#利用微信推送通用漏洞4.0
#XXX表示通过server酱获取的微信推送接口
#数据保存在当前路径下的olddata.csv
#当前代码运行需要预先安装numpy pandas requests库，一般anaconda的环境就行
#可以通过更改time_sleep设置爬取间隔时间
注：github哪个api需要翻墙
如果一直什么都不输出说明是遇到重复数据了
代码运行的时候不要打开olddata.csv文件，否则会报错
"""