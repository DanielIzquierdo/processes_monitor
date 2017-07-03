
# coding: utf-8

# In[131]:
from __future__ import division
import os
import psutil
from operator import methodcaller

MAX_CPU = os.environ.get('MAX_CPU', 15.0)
OK_CPU = os.environ.get('OK_CPU', 50.0)
suspended_pids = []

# In[10]:


def cpu_process_suspender(cpu_users, max_cpu, suspended_pids):
    # print("watching CPU")
    try:
        cpu_users.sort(key=methodcaller('cpu_percent'), reverse=True)
        for i, cpu_user in enumerate(cpu_users):
            cpu_percent = cpu_user.cpu_percent()
            if (cpu_percent >= max_cpu):
                if(cpu_user.name() == "CPU_HUNGRY" and (cpu_user.status() in ["running", "slepping"])):
                    print("suspending CPU_HUNGRY with percent: {}".format(cpu_percent))
                    # print(type(cpu_user.cpu_percent()))
                    suspended_pids.append(cpu_user)
                    cpu_user.suspend()
                    cpu_users[i]
    except:
        pass
    cpu_process_activator(OK_CPU, suspended_pids)
    return 0


# In[2]:

def cpu_process_activator(OK_CPU, suspended_pids):
    # print("watching idled processes")
    cpu_percent_used = psutil.cpu_percent()
    for i, process in enumerate(suspended_pids):
        # print(cpu_percent_used <= OK_CPU and process.name() == "CPU_HUNGRY")
        if (cpu_percent_used <= OK_CPU and process.name() == "CPU_HUNGRY" and process.status() == "stopped"):
            print("###########################\n \
                RESUMING PROCESS CPU HUNGRY##############################")
            process.resume()
            del suspended_pids[i]
        else:
            return 0


# In[135]:

def main():
    processes = [proc for proc in psutil.process_iter() if proc.status() != "stopped"]
    cpu_process_suspender(processes, MAX_CPU, suspended_pids)


while(True):
    main()
