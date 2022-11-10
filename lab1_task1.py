#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 10:21:27 2022

@author: dtjgp
"""

#!/usr/bin/python3

import random
from queue import Queue, PriorityQueue
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

# ******************************************************************************
# Constants
# ******************************************************************************

SERVICE = 10.0 # av service time 在无缓冲区的情况下设置为不变

TYPE1 = 1 
arrivals=0

BusyServer=False # True: server is currently busy; False: server is currently idle

MM1=[]


# ******************************************************************************
# To take the measurements
# ******************************************************************************
class Measure:
    def __init__(self,Narr,Ndep,NAveraegUser,OldTimeEvent,AverageDelay):
        self.arr = Narr
        self.dep = Ndep
        self.ut = NAveraegUser
        self.oldT = OldTimeEvent
        self.delay = AverageDelay
        
# ******************************************************************************
# Client
# ******************************************************************************
class Client:
    def __init__(self,type,arrival_time):
        self.type = type
        self.arrival_time = arrival_time

# ******************************************************************************
# Server
# ******************************************************************************
class Server(object):

    # constructor
    def __init__(self):

        # whether the server is idle or not
        self.idle = True


# ******************************************************************************

# arrivals *********************************************************************


def arrival_nobuffer(time, FES, queue): #没有buffer的情况下的arrival
    global users
    
    #print("Arrival no. ",data.arr+1," at time ",time," with ",users," users" )
    
    # cumulate statistics, 用于计算时间相关参数
    data.arr += 1       
    data.ut += users*(time-data.oldT)  
    data.oldT = time

    # sample the time until the next event
    inter_arrival = random.expovariate(lambd=1.0/ARRIVAL)
    
    # schedule the next arrival
    FES.put((time + inter_arrival, "arrival")) # 下一个arrival到来的时间点

    users += 1
    
    # create a record for the client
    client = Client(TYPE1,time)

    # insert the record in the queue
    queue.append(client)
    # print("the number of users before arrival calculation: ", users)

    # if the server is idle start the service
    if users==1:
        
        # sample the service time
        service_time = random.expovariate(1.0/SERVICE)
        # print("service_time is : ", service_time)
        #service_time = 1 + random.uniform(0, SEVICE_TIME)

        # schedule when the client will finish the server
        FES.put((time + service_time, "departure"))#departure的时间
        
    else: #所有的在service过程中到达的包都会被丢弃，所以增加的users应该自动减去1
        users -= 1
        queue.pop()
        
    # print("*******************")
    # print("The number of users after arrival calculation is:", users)
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
# ******************************************************************************

# departures *******************************************************************

def departure_nobuffer(time, FES, queue):
    global users

    #print("Departure no. ",data.dep+1," at time ",time," with ",users," users" )
        
    # cumulate statistics
    data.dep += 1
    data.ut += users*(time-data.oldT)
    data.oldT = time
    
    # get the first element from the queue
    client = queue.pop(0)
    
    # do whatever we need to do when clients go away
    
    data.delay += (time-client.arrival_time)
    # print("The number of users before departure is: ", users)
    users -= 1
    # print("The number of users after departure is: ", users)
    # print("&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&")

    # users只有两个结果：0&1，当users==1时，在执行departure_nobuffer,所以在执行结束的时候，users==0，所以不会出现users继续大于1的情况
    # see whether there are more clients to in the line
    # if users >0:
    #     # sample the service time
    #     service_time = random.expovariate(1.0/SERVICE)

    #     # schedule when the client will finish the server
    #     FES.put((time + service_time, "departure"))       
 
def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m-h, m+h

# ******************************************************************************
# the "main" of the simulation
# ******************************************************************************

def statistical_result(seed, ARRIVAL):
    global users
    global load

    # the simulation time 
    time = 0
    # users=0
    load = SERVICE/ARRIVAL

    # the list of events in the form: (time, type)
    FES = PriorityQueue()


    # schedule the first arrival at t=0
    FES.put((0, "arrival"))
    # arrival_num += 1

    # simulate until the simulated time reaches a constant
    while time < SIM_TIME:
        (time, event_type) = FES.get()

        if event_type == "arrival":
            arrival_nobuffer(time, FES, MM1)
            # arrival_num += 1

        elif event_type == "departure":
            departure_nobuffer(time, FES, MM1)
            # served_num += 1

    # print output data
    # print("MEASUREMENTS \n\nNo. of users in the queue:",users,"\nNo. of arrivals =",
    #       data.arr,"- No. of departures =",data.dep)
    
    # print("Load: ",SERVICE/ARRIVAL)
    # print("\nArrival rate: ",data.arr/time," - Departure rate: ",data.dep/time)

    # print("\nAverage number of users: ",data.ut/time)

    # print("Average delay: ",data.delay/data.dep)
    # print("Actual queue size: ",len(MM1))

    # if len(MM1)>0:
    #     print("Arrival time of the last element in the queue:",MM1[len(MM1)-1].arrival_time)
    #     MM1.pop(0)
    # print("\nThe loss rate is:", (data.arr - data.dep)/data.arr)
    return (data.arr - data.dep)/data.arr, SERVICE/(ARRIVAL+SERVICE), SERVICE/ARRIVAL
  
        
# LOAD=0.85
# ARRIVAL  = SERVICE/LOAD 
'''
investigate the system performance under different arrival rates, 
keeping a fixed value for the average service rate
'''
arrival_list = []
Loss_rate_ave_list = []
theoryloss_ave_list  = []
Load_list=[]
confidence_loss = []


SIM_TIME = 500000
for ARRIVAL in range(1, 21, 1):
    Loss_rate_list = []
    theoryloss_list = []
    load_list = []
    
    for i in range(1,21,1):
        users = 0
        data = Measure(0,0,0,0,0)
        loss_real, loss_theo, load = statistical_result(i, ARRIVAL)
        
        Loss_rate_list.append(loss_real)
        Loss_rate = np.array(Loss_rate_list)
        Loss_rate_mean = np.mean(Loss_rate)
        
        theoryloss_list.append(loss_theo)
        theoryloss = np.array(theoryloss_list)
        theoryloss_mean = np.mean(theoryloss)
        
        load_list.append(load)
        load_array = np.array(load_list)
        load_mean = np.mean(load_array)
    
    Loss_rate_ave_list.append(Loss_rate_mean)
    theoryloss_ave_list.append(theoryloss_mean)
    Load_list.append(load_mean)
    arrival_list.append(ARRIVAL)
    #calculate the loss rate with confidence interval
    confidence_loss.append(mean_confidence_interval(Loss_rate_list))

#calculate the loss rate with confidence interval errorbar
confiloss = np.array(confidence_loss).reshape((20,2))
lossavg = np.array(Loss_rate_ave_list).reshape((20,1))
yerror_range = abs(confiloss - lossavg)
yerror_range_tran = np.transpose(yerror_range)    
   

   
#plot the lossRate
plt.figure(1)
plt.plot(arrival_list,Loss_rate_ave_list,color='red',marker='o',label='simulated loss probability')
plt.plot(arrival_list,theoryloss_ave_list,color='green', label='theoretical loss probability')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("loss probability")
plt.title("M/M/1/1")
plt.xticks(arrival_list)
plt.legend()
plt.grid()
plt.savefig("loss probability vs average inter-arrival time", dpi=300)

#plot the confidence interval    
plt.figure(2)
plt.plot(arrival_list,Load_list,color='red',marker='o')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("load")
plt.title("M/M/1/1")
plt.xticks(arrival_list)
plt.legend()
plt.grid()
plt.savefig("load vs average inter-arrival time", dpi=300)

#plot the confidence interval    
plt.figure(3)
plt.plot(arrival_list,Loss_rate_ave_list,' ',color='red',marker='o')
plt.plot(arrival_list,confidence_loss,' ', marker='x',color='green')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("loss probability with confidence interval")
plt.title("M/M/1/1")
plt.xticks(arrival_list)
plt.legend()
plt.grid()
plt.savefig("loss probability with confidence interval vs average inter-arrival time", dpi=300)

#plot the confidence interval errorbar   
plt.figure(4)
plt.errorbar(arrival_list,Loss_rate_ave_list,yerr=yerror_range_tran, ls=" ",fmt='.',ecolor='g',color='r')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("loss probability with confidence interval errorbar")
plt.title("M/M/1/1")
plt.xticks(arrival_list)
plt.legend()
plt.grid()
plt.savefig("loss probability with confidence interval errorbar vs average inter-arrival time", dpi=300)


'''
当没有缓冲区的时候，BS的工作状态为：
1.没有包的时候与其他保持正常
2.到达一个packet的时候，会进行处理，在处理过程中，直到service结束，当有其他的packet到达的时候，会直接drop

lab1_task1中的要求是：处理速率固定

average waiting delay:考虑到每个真正进入service中的packet都会立刻被进行处理，所以在没有缓冲区的情况下，AVD(average waiting delay)为0
average buffer occupancy:在无缓冲区的情况下，ABO(average buffer occupancy)为0
loss probability: 到达BS但是没有被处理的packets数量占全部packets总数的比例
busy time: packets在serve时所占用的总时间
'''