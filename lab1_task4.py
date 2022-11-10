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


def arrival_gauss1(time, FES, queue, Buffersize): #只有一个channel
    global users
    
    #print("Arrival no. ",data.arr+1," at time ",time," with ",users," users" )
    
    # cumulate statistics
    data.arr += 1
    data.ut += users*(time-data.oldT)
    data.oldT = time

    # sample the time until the next event
    inter_arrival = random.expovariate(lambd=1.0/ARRIVAL)
    
    # schedule the next arrival
    FES.put((time + inter_arrival, "arrival"))

    users += 1
    
    # create a record for the client
    client = Client(TYPE1,time)

    # insert the record in the queue
    queue.append(client)

    # if the server is idle start the service
    if users==1:
        
        # sample the service time
        service_time = random.gauss(SERVICE, 1)
        #service_time = 1 + random.uniform(0, SEVICE_TIME)

        # schedule when the client will finish the server
        FES.put((time + service_time, "departure"))
    
    elif users >= Buffersize:
        users -= 1
        queue.pop()

def arrival_gauss5(time, FES, queue, Buffersize): #只有一个channel
    global users
    
    #print("Arrival no. ",data.arr+1," at time ",time," with ",users," users" )
    
    # cumulate statistics
    data.arr += 1
    data.ut += users*(time-data.oldT)
    data.oldT = time

    # sample the time until the next event
    inter_arrival = random.expovariate(lambd=1.0/ARRIVAL)
    
    # schedule the next arrival
    FES.put((time + inter_arrival, "arrival"))

    users += 1
    
    # create a record for the client
    client = Client(TYPE1,time)

    # insert the record in the queue
    queue.append(client)

    # if the server is idle start the service
    if users==1:
        
        # sample the service time
        service_time = random.gauss(SERVICE, 5)
        #service_time = 1 + random.uniform(0, SEVICE_TIME)

        # schedule when the client will finish the server
        FES.put((time + service_time, "departure"))
    
    elif users >= Buffersize:
        users -= 1
        queue.pop()

def arrival_gauss10(time, FES, queue, Buffersize): #只有一个channel
    global users
    
    #print("Arrival no. ",data.arr+1," at time ",time," with ",users," users" )
    
    # cumulate statistics
    data.arr += 1
    data.ut += users*(time-data.oldT)
    data.oldT = time

    # sample the time until the next event
    inter_arrival = random.expovariate(lambd=1.0/ARRIVAL)
    
    # schedule the next arrival
    FES.put((time + inter_arrival, "arrival"))

    users += 1
    
    # create a record for the client
    client = Client(TYPE1,time)

    # insert the record in the queue
    queue.append(client)

    # if the server is idle start the service
    if users==1:
        
        # sample the service time
        service_time = random.gauss(SERVICE, 10)
        #service_time = 1 + random.uniform(0, SEVICE_TIME)

        # schedule when the client will finish the server
        FES.put((time + service_time, "departure"))
    
    elif users >= Buffersize:
        users -= 1
        queue.pop()
        
def arrival_uni(time, FES, queue, Buffersize): #只有一个channel
    global users
    
    #print("Arrival no. ",data.arr+1," at time ",time," with ",users," users" )
    
    # cumulate statistics
    data.arr += 1
    data.ut += users*(time-data.oldT)
    data.oldT = time

    # sample the time until the next event
    inter_arrival = random.expovariate(lambd=1.0/ARRIVAL)
    
    # schedule the next arrival
    FES.put((time + inter_arrival, "arrival"))

    users += 1
    
    # create a record for the client
    client = Client(TYPE1,time)

    # insert the record in the queue
    queue.append(client)

    # if the server is idle start the service
    if users==1:
        
        # sample the service time
        service_time = random.uniform(SERVICE-3, SERVICE+3)
        #service_time = 1 + random.uniform(0, SEVICE_TIME)

        # schedule when the client will finish the server
        FES.put((time + service_time, "departure"))
    
    elif users >= Buffersize:
        users -= 1
        queue.pop()
        
    # print("*******************")
    # print("The number of users after arrival calculation is:", users)
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
# ******************************************************************************

# departures *******************************************************************

def departure_gauss1(time, FES, queue): # 1个channel
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
    users -= 1
    
    # see whether there are more clients to in the line
    if users >0: #users在等于1的时候，是一定会进行处理的，所以为了保证两个users都会在运行的情况，需要设置为users>1
        # sample the service time
        service_time = random.gauss(SERVICE, 1)

        # schedule when the client will finish the server
        FES.put((time + service_time, "departure"))  

def departure_gauss5(time, FES, queue): # 1个channel
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
    users -= 1
    
    # see whether there are more clients to in the line
    if users >0: #users在等于1的时候，是一定会进行处理的，所以为了保证两个users都会在运行的情况，需要设置为users>1
        # sample the service time
        service_time = random.gauss(SERVICE, 5)

        # schedule when the client will finish the server
        FES.put((time + service_time, "departure"))   
        
def departure_gauss10(time, FES, queue): # 1个channel
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
    users -= 1
    
    # see whether there are more clients to in the line
    if users >0: #users在等于1的时候，是一定会进行处理的，所以为了保证两个users都会在运行的情况，需要设置为users>1
        # sample the service time
        service_time = random.gauss(SERVICE, 10)

        # schedule when the client will finish the server
        FES.put((time + service_time, "departure"))  
        
def departure_uni(time, FES, queue): # 1个channel
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
    users -= 1
    
    # see whether there are more clients to in the line
    if users >0: #users在等于1的时候，是一定会进行处理的，所以为了保证两个users都会在运行的情况，需要设置为users>1
        # sample the service time
        service_time = random.uniform(SERVICE-3, SERVICE+3)

        # schedule when the client will finish the server
        FES.put((time + service_time, "departure"))  
 
# ******************************************************************************
# the "main" of the simulation
# ******************************************************************************

def statistical_result_gauss1(seed, ARRIVAL):
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
            arrival_gauss1(time, FES, MM1,Buffersize)
            # arrival_num += 1

        elif event_type == "departure":
            departure_gauss1(time, FES, MM1)
            # served_num += 1
    return (data.arr - data.dep)/data.arr, data.delay/data.dep, data.dep

def statistical_result_gauss5(seed, ARRIVAL):
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
            arrival_gauss1(time, FES, MM1,Buffersize)
            # arrival_num += 1

        elif event_type == "departure":
            departure_gauss5(time, FES, MM1)
            # served_num += 1
    return (data.arr - data.dep)/data.arr, data.delay/data.dep, data.dep

def statistical_result_gauss10(seed, ARRIVAL):
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
            arrival_gauss10(time, FES, MM1,Buffersize)
            # arrival_num += 1

        elif event_type == "departure":
            departure_gauss10(time, FES, MM1)
            # served_num += 1
    return (data.arr - data.dep)/data.arr, data.delay/data.dep, data.dep


def statistical_result_uni(seed, ARRIVAL):
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
            arrival_uni(time, FES, MM1,Buffersize)
            # arrival_num += 1

        elif event_type == "departure":
            departure_uni(time, FES, MM1)
            # served_num += 1

    return (data.arr - data.dep)/data.arr,data.delay/data.dep, data.dep
        
# LOAD=0.85
# ARRIVAL  = SERVICE/LOAD 
'''
investigate the system performance under different arrival rates, 
keeping a fixed value for the average service rate
'''
# data = Measure(0,0,0,0,0)   

arrival_list_gau1 = []
avgdelay_list_gau1 = []
transnum_list_gau1=[]

arrival_list_gau5 = []
avgdelay_list_gau5 = []
transnum_list_gau5=[]

arrival_list_gau10 = []
avgdelay_list_gau10 = []
transnum_list_gau10=[]

arrival_list_uni = []
avgdelay_list_uni = []
transnum_list_uni=[]

SIM_TIME = 500000
for ARRIVAL in range(12, 21, 1):
    MM1 = []
    Buffersize = 10
    users = 0
    data = Measure(0,0,0,0,0)
    loss_gau1, avgdelay_gau1,transnum_gau1 = statistical_result_gauss1(42, ARRIVAL)
    avgdelay_list_gau1.append(avgdelay_gau1)
    transnum_list_gau1.append(transnum_gau1)
    arrival_list_gau1.append(ARRIVAL)

for ARRIVAL in range(12, 21, 1):
    MM1 = []
    Buffersize = 10
    users = 0
    data = Measure(0,0,0,0,0)
    loss_gau5, avgdelay_gau5,transnum_gau5 = statistical_result_gauss5(42, ARRIVAL)
    avgdelay_list_gau5.append(avgdelay_gau5)
    transnum_list_gau5.append(transnum_gau5)
    arrival_list_gau5.append(ARRIVAL)

for ARRIVAL in range(12, 21, 1):
    MM1 = []
    Buffersize = 10
    users = 0
    data = Measure(0,0,0,0,0)
    loss_gau10, avgdelay_gau10,transnum_gau10 = statistical_result_gauss10(42, ARRIVAL)
    avgdelay_list_gau10.append(avgdelay_gau10)
    transnum_list_gau10.append(transnum_gau10)
    arrival_list_gau10.append(ARRIVAL)
    
for ARRIVAL in range(12, 21, 1):
    MM1 = []
    Buffersize = 10
    users = 0
    data = Measure(0,0,0,0,0)
    loss_uni, avgdelay_uni,transnum_uni = statistical_result_uni(42, ARRIVAL)
    avgdelay_list_uni.append(avgdelay_uni)
    transnum_list_uni.append(transnum_uni)
    arrival_list_uni.append(ARRIVAL)

# plt.figure()
# x = np.arange(0.05, 2.1, 0.05)
# y1 = Loss_rate_list
# y2 = theoryloss_list
# plt.xlabel("load rate")
# plt.ylabel("loss rate")
# plt.title("actual relation between loss rate and load rate")
# plt.plot(x,y1,color='red', linestyle='-',label='actual')
# plt.plot(x,y2,color='green', linewidth=5, linestyle='dotted',label='theory')
# plt.legend(loc='lower right')
# plt.savefig("loss analysis", dpi=300)

# 相同有限buffer值，对比gauss and uniform 下的平均排队延时
plt.figure(1)
plt.plot(arrival_list_uni,avgdelay_list_uni,color='r',marker='o',label='constant')
plt.plot(arrival_list_gau1,avgdelay_list_gau1,color='g',marker='*', label='gauss with sigma 1')
plt.plot(arrival_list_gau5,avgdelay_list_gau5,color='b',marker='^', label='gauss with sigma 5')
plt.plot(arrival_list_gau10,avgdelay_list_gau10,color='y',marker='s', label='gauss with sigma 10')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("average queuing delay [ms]")
plt.xticks(arrival_list_uni)
plt.legend()
plt.grid()
plt.savefig("task4a-average queuing delay", dpi=300)   


# 相同有限buffer值，对比gauss and uniform 下的传输包数量
plt.figure(2)
plt.plot(arrival_list_uni,transnum_list_uni,color='r',marker='o',label='constant')
plt.plot(arrival_list_gau1,transnum_list_gau1,color='g',marker='*', label='gauss with sigma 1')
plt.plot(arrival_list_gau5,transnum_list_gau5,color='b',marker='^', label='gauss with sigma 5')
plt.plot(arrival_list_gau10,transnum_list_gau10,color='y',marker='s', label='gauss with sigma 10')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("transmitted packets number")
plt.xticks(arrival_list_uni)
plt.legend()
plt.grid()
plt.savefig("task4a-transmitted packets number", dpi=300)   

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