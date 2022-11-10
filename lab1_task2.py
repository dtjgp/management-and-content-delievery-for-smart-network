#!/usr/bin/python3

import random
from queue import Queue, PriorityQueue
import numpy as np
import matplotlib.pyplot as plt
# from lab1_task1 import *

# ******************************************************************************
# Constants
# ******************************************************************************
# LOAD=2
SERVICE = 10.0 # av service time
# ARRIVAL  = SERVICE/LOAD # av inter-arrival time
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
def arrival2(time, FES, queue, Buffersize): # 有两个channels
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
    if users==1 or users==2:
        
        # sample the service time
        service_time = random.expovariate(1.0/SERVICE)
        #service_time = 1 + random.uniform(0, SEVICE_TIME)

        # schedule when the client will finish the server
        FES.put((time + service_time, "departure"))
    
    elif users > Buffersize:
        users -= 1
        queue.pop()
        
def arrival1(time, FES, queue, Buffersize): #只有一个channel
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
        service_time = random.expovariate(1.0/SERVICE)
        #service_time = 1 + random.uniform(0, SEVICE_TIME)

        # schedule when the client will finish the server
        FES.put((time + service_time, "departure"))
    
    elif users >= Buffersize:
        users -= 1
        queue.pop()

# ******************************************************************************

# departures *******************************************************************
def departure2(time, FES, queue): #两个channels
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
    if users >1: #users在等于1的时候，是一定会进行处理的，所以为了保证两个users都会在运行的情况，需要设置为users>1
        # sample the service time
        service_time = random.expovariate(1.0/SERVICE)

        # schedule when the client will finish the server
        FES.put((time + service_time, "departure"))

def departure1(time, FES, queue): # 1个channel
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
        service_time = random.expovariate(1.0/SERVICE)

        # schedule when the client will finish the server
        FES.put((time + service_time, "departure"))
        

def statistical_result(seed, ARRIVAL, Buffersize, channelsize):
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
    
    if channelsize == 1:
        arrival = arrival1
        departure = departure1
    elif channelsize == 2:
        arrival = arrival2
        departure = departure2
    
    # simulate until the simulated time reaches a constant
    while time < SIM_TIME:
        (time, event_type) = FES.get()

        if event_type == "arrival":
            arrival(time, FES, MM1, Buffersize)
            # arrival_num += 1

        elif event_type == "departure":
            departure(time, FES, MM1)
            # served_num += 1

    return (data.arr - data.dep)/data.arr, data.delay/data.dep, data.dep, data.ut/time
# ******************************************************************************
# the "main" of the simulation
# ******************************************************************************

SIM_TIME = 500000
Loss_rate_list1 = []
avgdelay_list1 = []
avgusernum_list1 =[]
arrival_list1 = []
transnum_list1=[]

Loss_rate_list2_3 = []
avgdelay_list2_3 = []
avgusernum_list2_3 = []
arrival_list2_3 = []
transnum_list2_3=[]

Loss_rate_list2_10 = []
avgdelay_list2_10 = []
avgusernum_list2_10 = []
arrival_list2_10 = []
transnum_list2_10 = []


# 1个channel 与两个channel 在相同buffer情况下的性能对比
users = 0 
for ARRIVAL in range(1, 21, 1):
    
    data = Measure(0,0,0,0,0)
    users = 0
    Buffersize = 10
    MM1 = []
    loss1, avgdelay1, transnum1, avgusernum1 = statistical_result(42, ARRIVAL, Buffersize, 1)
    
    Loss_rate_list1.append(loss1)
    avgdelay_list1.append(avgdelay1)
    avgusernum_list1.append(avgusernum1)
    arrival_list1.append(ARRIVAL)
    transnum_list1.append(transnum1)


# 2个channel：比较不同有限buffer下的性能
users = 0   
for ARRIVAL in range(1, 21, 1):
    
    data = Measure(0,0,0,0,0)
    # users = 0
    # Buffersize3 = 3
    # MM1 = []    

    # loss2_3, avgdelay2_3, transnum2_3, avgusernum2_3 = statistical_result(42, ARRIVAL, Buffersize3, 2)
    # Loss_rate_list2_3.append(loss2_3)
    # avgdelay_list2_3.append(avgdelay2_3)
    # avgusernum_list2_3.append(avgusernum2_3)
    # arrival_list2_3.append(ARRIVAL)
    # transnum_list2_3.append(transnum2_3)
    
    users = 0
    Buffersize10 = 10
    MM1 = []    
    
    loss2_10, avgdelay2_10, transnum2_10, avgusernum2_10 = statistical_result(42, ARRIVAL, Buffersize10, 2)
    Loss_rate_list2_10.append(loss2_10)
    avgdelay_list2_10.append(avgdelay2_10)
    avgusernum_list2_10.append(avgusernum2_10)
    arrival_list2_10.append(ARRIVAL)
    transnum_list2_10.append(transnum2_10)



'''
# ******************************************************************************
# 对比2channel情况下，不同的buffer值
#plot the lossRate
plt.figure(1)
plt.plot(arrival_list2_3,Loss_rate_list2_3,color='red',marker='o',label='two antennas with buffersize 3')
plt.plot(arrival_list2_10,Loss_rate_list2_10,color='green',marker='o', label='two antennas with buffersize 10')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("loss probability")
# plt.title("M/M/1/1")
plt.xticks(arrival_list2_3)
plt.legend()
plt.grid()
plt.savefig("task2a-loss probability vs average inter-arrival time", dpi=300)

#plot the average queuing delay
plt.figure(2)
plt.plot(arrival_list2_3,avgdelay_list2_3,color='red',marker='o',label='two antennas with buffersize 3')
plt.plot(arrival_list2_10,avgdelay_list2_10,color='green',marker='o', label='two antennas with buffersize 10')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("average queuing delay [ms]")
# plt.title("M/M/1/1")
plt.xticks(arrival_list2_3)
plt.legend()
plt.grid()
plt.savefig("task2a-average queuing delay vs average inter-arrival time", dpi=300)

#plot the average user number
plt.figure(3)
plt.plot(arrival_list2_3,avgusernum_list2_3,color='red',marker='o',label='two antennas with buffersize 3')
plt.plot(arrival_list2_10,avgusernum_list2_10,color='green',marker='o', label='two antennas with buffersize 10')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("average user number")
# plt.title("M/M/1/1")
plt.xticks(arrival_list2_3)
plt.legend()
plt.grid()
plt.savefig("task2a-average user number vs average inter-arrival time", dpi=300)     

#plot the transmitted packets number
plt.figure(4)
plt.plot(arrival_list2_3,transnum_list2_3,color='red',marker='o',label='two antennas with buffersize 3')
plt.plot(arrival_list2_10,transnum_list2_10,color='green',marker='o',label='two antennas with buffersize 10')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("number of transmitted packets")
# plt.title("M/M/1/1")
plt.xticks(arrival_list2_3)
plt.legend()
plt.grid()
plt.savefig("task2a-number of transmitted packets vs average inter-arrival time", dpi=300)
   ''' 

# ******************************************************************************
# 相同buffer值，对比1channel and 2channel
#plot the lossRate
plt.figure(1)
plt.plot(arrival_list1,Loss_rate_list1,color='red',marker='o',label='one antenna with buffersize 10')
plt.plot(arrival_list2_10,Loss_rate_list2_10,color='green',marker='o', label='two antennas with buffersize 10')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("loss probability")
# plt.title("M/M/1/1")
plt.xticks(arrival_list1)
plt.legend()
plt.grid()
plt.savefig("task2c-loss probability vs average inter-arrival time", dpi=300)

#plot the average queuing delay
plt.figure(2)
plt.plot(arrival_list1,avgdelay_list1,color='red',marker='o',label='one antenna with buffersize 10')
plt.plot(arrival_list2_10,avgdelay_list2_10,color='green',marker='o', label='two antennas with buffersize 10')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("average queuing delay [ms]")
# plt.title("M/M/1/1")
plt.xticks(arrival_list1)
plt.legend()
plt.grid()
plt.savefig("task2c-average queuing delay vs average inter-arrival time", dpi=300)

#plot the average user number
plt.figure(3)
plt.plot(arrival_list1,avgusernum_list1,color='red',marker='o',label='one antenna with buffersize 10')
plt.plot(arrival_list2_10,avgusernum_list2_10,color='green',marker='o', label='two antennas with buffersize 10')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("average user number")
# plt.title("M/M/1/1")
plt.xticks(arrival_list1)
plt.legend()
plt.grid()
plt.savefig("task2c-average user number vs average inter-arrival time", dpi=300)     

#plot the transmitted packets number
plt.figure(4)
plt.plot(arrival_list1,transnum_list1,color='red',marker='o',label='one antenna with buffersize 10')
plt.plot(arrival_list2_10,transnum_list2_10,color='green',marker='o',label='two antennas with buffersize 10')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("number of transmitted packets")
# plt.title("M/M/1/1")
plt.xticks(arrival_list1)
plt.legend()
plt.grid()
plt.savefig("task2c-number of transmitted packets vs average inter-arrival time", dpi=300)
   
'''
搭建双通道有限buffer步骤：
1.搭建一个双通道
2.限制buffer数量
'''