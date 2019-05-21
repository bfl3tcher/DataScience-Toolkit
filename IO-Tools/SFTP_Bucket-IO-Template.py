'''
SFTP Connection using Paramiko

    - Loose collection of code used to connect to SFTP sites

    - in[#] defines each cell, describes what code below it does
            - comments above will describe relevant information
            - including quick definitions, and reference guides

    - Treat the comments above in[#] as a loose set of instructions
            - code is not meant to be run as is
            - parts are meant to be combined to achieve specific tasks

    - This is best used when taking pieces of this to
        connect to SFTP site/client and
        send/recieve/delete files and folders
'''


# coding: utf-8

# ### Documentation References
#
# - http://docs.paramiko.org/en/2.4/
# - http://docs.paramiko.org/en/2.4/api/sftp.html

# ### 1 --- Connect to SFTP ---

# In[1]:


# import libraries
import warnings
warnings.filterwarnings("ignore")

import os
import paramiko

# save log
paramiko.util.log_to_file('/tmp/paramiko.log')

# Open a transport
host = ""
port =
transport = paramiko.Transport((host, port))

# Auth
password = ""
username = ""
transport.connect(username = username, password = password)

# Go!
sftp = paramiko.SFTPClient.from_transport(transport)


# ###  2 --- Directory Management ---

# **Print Current Directory**

# In[2]:


print('SFTP Home Directory:', sftp.listdir())


# **List SFTP folders/files in directory**

# In[12]:


print('\tSFTP -- DIRECTORY')
print('\n-----------------------------------------\n')
for i in sftp.listdir('./incoming'):
    print(str(i))


# **Create Folder in SFTP**

# In[4]:


path = './incoming/BF_Testing'

# sftp.mkdir(path=path)


# **Rename SFTP folder**

# In[5]:


old_name = './incoming/BF_Testing'
new_name = './incoming/BF_Testing1'

# sftp.rename(oldpath=old_name, newpath=new_name)


# **Remove SFTP folder**

# In[6]:


path = './incoming/BF_Testing'

# sftp.rmdir(path=path)


# **Change Working Directory**

# In[7]:


path = './incoming/'

# sftp.chdir(path=path)


# **Print Working Directory**
#
# - Requires changing a directory before this will output anything

# In[8]:


print(sftp.getcwd())


# ### 3 --- File Management for SFTP ---

# **Download Files in SFTP**

# In[9]:


remot_pth = './incoming/BF-test.csv'
local_pth = './DL.csv'

# sftp.get(remotepath=remot_pth, localpath=local_pth)


# **Place Files in SFTP**

# In[10]:


remot_pth = './incoming/BF-test.csv'
local_pth = './DL.csv'

# sftp.put(localpath=str(local_pth), remotepath=str(remot_pth))


# **Removing Files in SFTP**

# In[11]:


path = './incoming/BF-test.csv'

# sftp.remove(path=path)
