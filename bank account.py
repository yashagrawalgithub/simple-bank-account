#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ast
file=open('bank.txt','r')
d=ast.literal_eval(file.read())
class bank:
    def __init__(self,i,o,r):
        self.i=i
        self.o=o
        self.r=r
        for k in d.keys():
            if(i==k and o==1):
                self.withdraw(i,r)
            if(i==k and o==2):
                self.deposit(i,r)
            if(i==k and o==3):
                self.transfer(i,r)
    def withdraw(self,i,r):
        print('Before Withdraw: ',d[i])
        if(r>d[i]):
            print("Insufficient Balance!")
        else:
            d[i]=d[i]-r
        self.balance(i)
    def deposit(self,i,r):
        print('Before Deposit: ',d[i])
        d[i]=d[i]+r
        self.balance(i)
    def transfer(self,i,r):
        j=int(input('ID of Receiver: '))
        if(r>d[i]):
            print("Insufficient Balance!")
        else:
            d[j]=d[j]+r
            d[i]=d[i]-r
        self.balance(i)
    def balance(self,i):
        print('Current Balance: ',d[i])
        file=open('bank.txt','w').write(str(d))
i=int(input('Enter The ID: '))
o=int(input('Write 1 for withdraw & 2 for deposit & 3 for transfer: '))
r=int(input('Enter The Amount: '))
b=bank(i,o,r)
file.close()


# In[2]:


import ast
file = open("bank.txt", "r")
contents = file. read()
dictionary = ast.literal_eval(contents)
file. close()
print(dictionary)


# In[ ]:




