#!/usr/bin/env python3
from sys import argv
filetable=[]
ratetable=[[1500,0.03,0],[4500,0.1,105],[9000,0.2,555],[35000,0.25,1005],[55000,0.3,2755],[80000,0.35,5505]]
try:
    for i in ['-c','-d','-o']:
        index=argv.index(i)
        filetable.append(argv[index+1])
       
        with open(filetable[-1]) as file:
            pass
except:
    print('文件读取有错误')
class config(object):
#配置类
    def __init__(self,filename):
        self._config={}
        self.filename=filename

#获取配置信息
    def Getconfig(self):
        with open(self.filename,'r') as file:
            config=file.readlines()
        for i in config:
            z=i.strip('\n').split('=')
            self._config[z[0]]=float(z[1])

#通过配置信息计算社保
    def Shebao(self,money):
        rate=sum(self._config.values())-self._config['Jishul']-self._config['Jishuh']
        if money<self._config['Jishul']:
            shebao=self._config['Jishul']*rate
        elif money>self._config['Jishuh']:
            shebao=self._config['Jishuh']*rate
        else:
            shebao=rate*money
        return shebao
class user(object):
#员工类
    def __init__(self,filename):
        self.filename=filename
        self._user={}

#获取员工信息
    def Getuser(self):
        with open(self.filename,'r') as file:
            usertable=file.readlines()
        for i in usertable:
            z=i.strip('\n').split(',')
            self._user[z[0]]=float(z[1])

#计算个税并返回
    def Taxe(self,taxetable,shebao,begin=3500):
        userdict={}
        for key,value in self._user.items():
            userdict[key]=[value]
            shebaofei=shebao(value)
            ratenumber=value-begin-shebaofei
            userdict[key].append(shebaofei)
            for i in taxetable:
                if ratenumber<0:
                    rate=0
                    break
                if ratenumber >80000:
                    rate=ratenumber*0.45-13505
                    break
                elif ratenumber<i[0]:
                    rate=ratenumber*i[1]-i[2]
                    break
            userdict[key].append(rate)
        return userdict
if __name__=='__main__':
    Config=config(filetable[0])
    User=user(filetable[1])
    filename=filetable[2]
    file=open(filename,'w')
    Config.Getconfig()
    User.Getuser()
    usertable=User.Taxe(ratetable,Config.Shebao)
    for key,value in usertable.items():
        income=value[0]-value[2]-value[1]       
        string="{0},{1},{2:0.2f},{3:0.2f},{4:0.2f}\n".format(key,int(value[0]),value[1],value[2],income)
        file.write(string)
    file.close()
