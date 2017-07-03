
# coding: utf-8

# In[131]:
from __future__ import division
import os
import psutil
from operator import methodcaller

MAX_MEM = os.environ.get('MAX_MEM', 60)

# In[136]:


def mem_process_term(mem_users, MAX_MEM):
    print("watching memory...")
    mem_percent_used = psutil.virtual_memory().percent
    try:
        mem_users.sort(key=methodcaller('memory_percent'), reverse=True)
    except:
        pass
    # print(mem_users)

    while(mem_percent_used >= MAX_MEM):
        # print("terminating processess...")
        sigterm_(mem_users)
        mem_percent_used = psutil.virtual_memory().percent
    print("continuing processes...")
    return 0


def sigterm_(mem_users):
    if len(mem_users) > 0:
        process = mem_users[0]
        # if(process.name() != "root"):
        if(process.name() == "MEM_HUNGRY"):
            process.terminate()
        del mem_users[0]
    return 0


# In[135]:

def main():
    processes = [proc for proc in psutil.process_iter()]
    mem_process_term(processes, MAX_MEM)


while(True):
    main()
