#!/usr/bin/env python3
print('hah')
from sys import argv
table={}
try:
    for i in argv[1:]:
        
        if i.split(':')[0]in table:
            raise ValueError
        table[i.split(':')[0]]=int(i.split(':')[1])
except:
    print("Parameter Error")
insurance={'养老':0.08,'医疗':0.02,'失业':0.005,'工伤':0,'生育':0,'公积金':0.06}
allinsurance=sum(insurance.values())
tablerate=[[1500,0.03,0],[4500,0.1,105],[9000,0.2,555],[35000,0.25,1005],[55000,0.3,2755],[80000,0.35,5505]]
def ratenumber(salary,tablerate):
    for i in tablerate:
        if salary<0:
            rate=0
            break
        if salary>80000:
            rate=salary*0.45-13505
            break
        if salary<i[0]:
            rate=salary*i[1]-i[2]
            break
    return rate

def salarynumber(money,allinsurance,begin=3500):
    return money*(1-allinsurance)-begin

def income(rate,money,allinsurance):
    return money*(1-allinsurance)-rate
if __name__=='__main__':
    
    for key,value in table.items():
        salary=salarynumber(value,allinsurance)
        rate=ratenumber(salary,tablerate)
        come=income(rate,value,allinsurance)
        print("{0}:{1:0.2f}".format(key,come))


