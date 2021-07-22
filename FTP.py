#!/usr/bin/env python
# coding: utf-8

# In[101]:


from ftplib import FTP
from io import BytesIO


# In[102]:


ftp = FTP()
ftp.connect('ftp.cet-rio.ddns.com.br',20121)
ftp.login('ftp_ufrj','ng*LxVnc$R')


# In[103]:


data = []
ftp.dir(data.append)
for line in data:
    print('-', line)


# In[105]:


data[0].split(" ")[-1]


# In[106]:


def getFile(ftp, filename):
    try:
        ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
    except:
        print("Error")


# In[ ]:


for file in data:
    getFile(ftp, file.split(" ")[-1])

