# -*- coding: utf-8 -*-
import pickle
def p():#将字典转换为pickle存储
    sss = {'1':'a','2':'b','3':'c'}
    #使用dump()将数据序列化到文件中  
    fw = open('dataFile.txt','wb')  
    pickle.dump(sss,fw)
    fw.close()
def ss():#将pickle文件中存储的数据还原出来
    fr = open('dataFile.txt','rb')
    data = pickle.load(fr)
    print(data)

if __name__ == "__main__":
    p() #pickel 化
    ss() #逆 pickle 化