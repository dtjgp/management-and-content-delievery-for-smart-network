#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 17:55:30 2022

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
# LOAD=20
SERVICE = 10.0 # av service time
# ARRIVAL  = SERVICE/LOAD # av inter-arrival time
TYPE1 = 1 
TYPE2 = 2

SIM_TIME = 500000

arrivals=0
users=0
user1 = 0
user2 = 0
BusyServer=False # True: server is currently busy; False: server is currently idle




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
    def __init__(self,type,seq,arrival_time):
        self.type = type
        self.seq = seq
        self.arrival_time = arrival_time
        
# class Client1BS:# for 1BS
#     def __init__(self,type,arrival_time):
#         self.type = type
#         self.arrival_time = arrival_time

# ******************************************************************************
# Server
# ******************************************************************************
class Server(object):

    # constructor
    def __init__(self):

        # whether the server is idle or not
        self.idle = True


# ******************************************************************************
#目标是要实现两个BS with infinite buffer
# arrivals *********************************************************************
def arrival_2dro_inf(time, FES, queue1, queue2):  #2BS, 1channel each, infinite buffer
    global users, user2, user1
    
    #print("Arrival no. ",data.arr+1," at time ",time," with ",users," users" )
    
    # cumulate statistics
    data.arr += 1
    data.ut += users*(time-data.oldT)
    data.oldT = time

    # sample the time until the next event
    inter_arrival = random.expovariate(lambd=1.0/ARRIVAL)
    
    # schedule the next arrival
    FES.put((time + inter_arrival, 0, "arrival"))

    users += 1
    
    #需要判断是进入的哪个队列
    if len(queue1) >= len(queue2):
        seq = 2
        client = Client(TYPE2,seq,time)
    # create a record for the client
        # client = Client(TYPE,time)
        queue2.append(client)
    # insert the record in the queue
        user2 += 1
        if user2==1:
            
            # sample the service time
            service_time = random.expovariate(1.0/SERVICE)
            #service_time = 1 + random.uniform(0, SEVICE_TIME)

            # schedule when the client will finish the server
            FES.put((time + service_time, seq, "departure"))
        
    else:
        seq = 1
        client = Client(TYPE1,seq,time)
        queue1.append(client)
        user1 += 1
        if user1==1:
            
            # sample the service time
            service_time = random.expovariate(1.0/SERVICE)
            #service_time = 1 + random.uniform(0, SEVICE_TIME)

            # schedule when the client will finish the server
            FES.put((time + service_time, seq, "departure"))
        
        
    # client = Client(TYPE,time)
    # queue.append(client)
    # # if the server is idle start the service
    # if users==1:
        
    #     # sample the service time
    #     service_time = random.expovariate(1.0/SERVICE)
    #     #service_time = 1 + random.uniform(0, SEVICE_TIME)

    #     # schedule when the client will finish the server
    #     FES.put((time + service_time, "departure"))

def arrival_2dro_fin(time, FES, queue1, queue2, Buffersize):#2BS,1channel each, finite buffer
    global users, user2, user1
    
    #print("Arrival no. ",data.arr+1," at time ",time," with ",users," users" )
    
    # cumulate statistics
    data.arr += 1
    data.ut += users*(time-data.oldT)
    data.oldT = time

    # sample the time until the next event
    inter_arrival = random.expovariate(lambd=1.0/ARRIVAL)
    
    # schedule the next arrival
    FES.put((time + inter_arrival, 0, "arrival"))

    users += 1
    
    #需要判断是进入的哪个队列
    if len(queue1) >= len(queue2):
        seq = 2
        client = Client(TYPE2,seq,time)
    # create a record for the client
        # client = Client(TYPE,time)
        queue2.append(client)
    # insert the record in the queue
        user2 += 1
        if user2==1:
            
            # sample the service time
            service_time = random.expovariate(1.0/SERVICE)
            #service_time = 1 + random.uniform(0, SEVICE_TIME)

            # schedule when the client will finish the server
            FES.put((time + service_time, seq, "departure"))
        if user2 >= Buffersize:
            user2 -= 1
            queue2.pop()
        
    else:
        seq = 1
        client = Client(TYPE1,seq,time)
        queue1.append(client)
        user1 += 1
        if user1==1:
            
            # sample the service time
            service_time = random.expovariate(1.0/SERVICE)
            #service_time = 1 + random.uniform(0, SEVICE_TIME)

            # schedule when the client will finish the server
            FES.put((time + service_time, seq, "departure"))
        if user1 >= Buffersize:
            user1 -= 1
            queue1.pop()
         
def arrival_1dro_2ch_fin(time, FES, queue, Buffersize): # 1BS有两个channels, finite buffer
    global users
    
    #print("Arrival no. ",data.arr+1," at time ",time," with ",users," users" )
    seq = 0
    # cumulate statistics
    data.arr += 1
    data.ut += users*(time-data.oldT)
    data.oldT = time

    # sample the time until the next event
    inter_arrival = random.expovariate(lambd=1.0/ARRIVAL)
    
    # schedule the next arrival
    FES.put((time + inter_arrival,seq, "arrival"))

    users += 1
    
    # create a record for the client
    client = Client(TYPE1,seq, time)

    # insert the record in the queue
    queue.append(client)

    # if the server is idle start the service
    if users==1 or users==2:
        
        # sample the service time
        service_time = random.expovariate(1.0/SERVICE)
        #service_time = 1 + random.uniform(0, SEVICE_TIME)

        # schedule when the client will finish the server
        FES.put((time + service_time,seq, "departure"))
    
    elif users >= Buffersize:
        users -= 1
        queue.pop()
        
def arrival_1dro_2ch_inf(time, FES, queue): # 1BS有两个channels,infinite buffer
    global users
    
    #print("Arrival no. ",data.arr+1," at time ",time," with ",users," users" )
    seq = 0
    # cumulate statistics
    data.arr += 1
    data.ut += users*(time-data.oldT)
    data.oldT = time

    # sample the time until the next event
    inter_arrival = random.expovariate(lambd=1.0/ARRIVAL)
    
    # schedule the next arrival
    FES.put((time + inter_arrival,seq, "arrival"))

    users += 1
    
    # create a record for the client
    client = Client(TYPE1,seq, time)

    # insert the record in the queue
    queue.append(client)

    # if the server is idle start the service
    if users==1 or users==2:
        
        # sample the service time
        service_time = random.expovariate(1.0/SERVICE)
        #service_time = 1 + random.uniform(0, SEVICE_TIME)

        # schedule when the client will finish the server
        FES.put((time + service_time,seq, "departure"))
    
    # elif users >= Buffersize:
    #     users -= 1

# ******************************************************************************

# departures *******************************************************************
def departure_2dro(time, FES, queue):#2个无人机
    global users, user1, user2

    #print("Departure no. ",data.dep+1," at time ",time," with ",users," users" )
        
    # cumulate statistics
    data.dep += 1
    data.ut += users*(time-data.oldT)
    data.oldT = time
    users -= 1
    
        
    # get the first element from the queue
    client = queue.pop(0)
    seq = client.seq
    
    if seq == 1:
    # do whatever we need to do when clients go away
    
        data.delay += (time-client.arrival_time)
        user1 -= 1
    
    # see whether there are more clients to in the line
        if user1 >0:
            # sample the service time
            service_time = random.expovariate(1.0/SERVICE)
    
            # schedule when the client will finish the server
            FES.put((time + service_time, seq, "departure"))
    elif seq == 2:
    
    # do whatever we need to do when clients go away
    
        data.delay += (time-client.arrival_time)
        user2 -= 1
    
    # see whether there are more clients to in the line
        if user2 >0:
            # sample the service time
            service_time = random.expovariate(1.0/SERVICE)
    
            # schedule when the client will finish the server
            FES.put((time + service_time, seq, "departure"))

def departure_1dro_2ch(time, FES, queue): #1 个无人机两个channels
    global users

    #print("Departure no. ",data.dep+1," at time ",time," with ",users," users" )
    seq = 0    
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
        FES.put((time + service_time,seq, "departure"))  

# ******************************************************************************
# the "main" of the simulation
# ******************************************************************************
def statistical_result_2dro_inf(seed, ARRIVAL): #2个无人机，无限buffer
    global users, user1, user2
    global load
    
    time = 0
    # users=0
    load = SERVICE/ARRIVAL
    # the list of events in the form: (time, type)
    FES = PriorityQueue()  

# schedule the first arrival at t=0
    FES.put((0, 0, "arrival"))

# simulate until the simulated time reaches a constant
    while time < SIM_TIME:
        (time, seq, event_type) = FES.get()
        
        if event_type == "arrival":
            arrival_2dro_inf(time, FES, MM1, MM2)
    
        elif event_type == "departure":
    
            if seq == 1:
                
                departure_2dro(time, FES, MM1)
            elif seq == 2:
                departure_2dro(time, FES, MM2)

    return (data.arr - data.dep)/data.arr, data.delay/data.dep, data.dep, data.ut/time

def statistical_result_2dro_fin(seed, ARRIVAL, Buffersize): #2个无人机，有限buffer
    global users, user1, user2
    global load
  
    time = 0
    # users=0
    load = SERVICE/ARRIVAL
    # the list of events in the form: (time, type)
    FES = PriorityQueue()  

# schedule the first arrival at t=0
    FES.put((0, 0, "arrival"))

# simulate until the simulated time reaches a constant
    while time < SIM_TIME:
        (time, seq, event_type) = FES.get()
        
        if event_type == "arrival":
            arrival_2dro_fin(time, FES, MM1, MM2, Buffersize)
    
        elif event_type == "departure":
    
            if seq == 1:
                
                departure_2dro(time, FES, MM1)
            elif seq == 2:
                departure_2dro(time, FES, MM2)
     
    return (data.arr - data.dep)/data.arr, data.delay/data.dep, data.dep, data.ut/time

def statistical_result_1dro_2ch_fin(seed, ARRIVAL, Buffersize): #1个无人机，2channels,有限buffer
    global users
    global load

    # the simulation time 
    time = 0
    # users=0
    load = SERVICE/ARRIVAL
    # the list of events in the form: (time, type)
    FES = PriorityQueue()     
        
    # schedule the first arrival at t=0
    FES.put((0, 0,"arrival"))
    # arrival_num += 1
    
    # simulate until the simulated time reaches a constant
    while time < SIM_TIME:
        (time, seq, event_type) = FES.get()

        if event_type == "arrival":
            arrival_1dro_2ch_fin(time, FES, MM1, Buffersize)
            # arrival_num += 1

        elif event_type == "departure":
            departure_1dro_2ch(time, FES, MM1)
            # served_num += 1
    
    return (data.arr - data.dep)/data.arr, data.delay/data.dep, data.dep, data.ut/time

def statistical_result_1dro_2ch_inf(seed, ARRIVAL): #1个无人机，2channels，无限buffer
    global users
    global load

    # the simulation time 
    time = 0
    # users=0
    load = SERVICE/ARRIVAL
    # the list of events in the form: (time, type)
    FES = PriorityQueue()     
        
    # schedule the first arrival at t=0
    FES.put((0, 0,"arrival"))
    # arrival_num += 1
   
    # simulate until the simulated time reaches a constant
    while time < SIM_TIME:
        (time, seq, event_type) = FES.get()

        if event_type == "arrival":
            arrival_1dro_2ch_inf(time, FES, MM1)
            # arrival_num += 1

        elif event_type == "departure":
            departure_1dro_2ch(time, FES, MM1)
            # served_num += 1
    
    return (data.arr - data.dep)/data.arr, data.delay/data.dep, data.dep, data.ut/time
data = Measure(0,0,0,0,0)
MM1=[]
MM2=[]

# ******************************************************************************
# ******************************************************************************

#************************
# 1 drone 2 servers infinite buffer
Loss_rate_list1_inf = []
avgdelay_list1_inf = []
avgusernum_list1_inf =[]
arrival_list1_inf = []
transnum_list1_inf=[]

for ARRIVAL in range(1, 21, 1):

    data = Measure(0,0,0,0,0)
    users = 0
    # user1 = 0
    # user2 = 0
    # Buffersize = 10
    MM1=[]
    # MM2=[]
    Buffersize = 10
    loss1_inf, avgdelay1_inf, transnum1_inf, avgusernum1_inf = statistical_result_1dro_2ch_inf(42, ARRIVAL)

    Loss_rate_list1_inf.append(loss1_inf)
    avgdelay_list1_inf.append(avgdelay1_inf)
    avgusernum_list1_inf.append(avgusernum1_inf)
    arrival_list1_inf.append(ARRIVAL)
    transnum_list1_inf.append(transnum1_inf) 

         
#************************
# 2 drone 各1 server infinite buffer
Loss_rate_list2_inf = []
avgdelay_list2_inf = []
avgusernum_list2_inf = []
arrival_list2_inf = []
transnum_list2_inf=[]

for ARRIVAL in range(1, 21, 1):
    data = Measure(0,0,0,0,0)
    users = 0
    user1 = 0
    user2 = 0

    MM1=[]
    MM2=[]
    loss2_inf, avgdelay2_inf, transnum2_inf, avgusernum2_inf = statistical_result_2dro_inf(42, ARRIVAL)

    Loss_rate_list2_inf.append(loss2_inf)
    avgdelay_list2_inf.append(avgdelay2_inf)
    avgusernum_list2_inf.append(avgusernum2_inf)
    arrival_list2_inf.append(ARRIVAL)
    transnum_list2_inf.append(transnum2_inf) 
    
#************************
# 1 drone 2 servers buffer3
Loss_rate_list1_3 = []
avgdelay_list1_3 = []
avgusernum_list1_3 = []
arrival_list1_3 = []
transnum_list1_3 = []

   
for ARRIVAL in range(1, 21, 1):
    data = Measure(0,0,0,0,0)
    users = 0
    MM1=[]
    Buffersize = 3
    loss1_3, avgdelay1_3, transnum1_3, avgusernum1_3 = statistical_result_1dro_2ch_fin(42, ARRIVAL, Buffersize)

    Loss_rate_list1_3.append(loss1_3)
    avgdelay_list1_3.append(avgdelay1_3)
    avgusernum_list1_3.append(avgusernum1_3)
    arrival_list1_3.append(ARRIVAL)
    transnum_list1_3.append(transnum1_3)  



#************************
# 1 drone 2 servers buffer10
Loss_rate_list1_10 = []
avgdelay_list1_10 = []
avgusernum_list1_10 = []
arrival_list1_10 = []
transnum_list1_10 = []

for ARRIVAL in range(1, 21, 1):
    data = Measure(0,0,0,0,0)
    users = 0
    Buffersize = 10
    MM1=[]
    loss1_10, avgdelay1_10, transnum1_10, avgusernum1_10 = statistical_result_1dro_2ch_fin(42, ARRIVAL, Buffersize)

    Loss_rate_list1_10.append(loss1_10)
    avgdelay_list1_10.append(avgdelay1_10)
    avgusernum_list1_10.append(avgusernum1_10)
    arrival_list1_10.append(ARRIVAL)
    transnum_list1_10.append(transnum1_10)  

#************************
# 2 drone 各1 server buffer3
Loss_rate_list2_3 = []
avgdelay_list2_3 = []
avgusernum_list2_3 = []
arrival_list2_3 = []
transnum_list2_3 = []

for ARRIVAL in range(1, 21, 1):

    data = Measure(0,0,0,0,0)
    users = 0
    user1 = 0
    user2 = 0
    # Buffersize = 10
    MM1=[]
    MM2=[]
    Buffersize = 3
    loss2_3, avgdelay2_3, transnum2_3, avgusernum2_3 = statistical_result_2dro_fin(42, ARRIVAL, Buffersize)

    Loss_rate_list2_3.append(loss2_3)
    avgdelay_list2_3.append(avgdelay2_3)
    avgusernum_list2_3.append(avgusernum2_3)
    arrival_list2_3.append(ARRIVAL)
    transnum_list2_3.append(transnum2_3) 
    
#************************   
# 2 drone 各1 server buffer10
Loss_rate_list2_10 = []
avgdelay_list2_10 = []
avgusernum_list2_10 = []
arrival_list2_10 = []
transnum_list2_10 = []

for ARRIVAL in range(1, 21, 1):
    data = Measure(0,0,0,0,0)
    users = 0
    user1 = 0
    user2 = 0
    # Buffersize = 10
    MM1=[]
    MM2=[]
    Buffersize = 10
    loss2_10, avgdelay2_10, transnum2_10, avgusernum2_10 = statistical_result_2dro_fin(42, ARRIVAL, Buffersize)

    Loss_rate_list2_10.append(loss2_10)
    avgdelay_list2_10.append(avgdelay2_10)
    avgusernum_list2_10.append(avgusernum2_10)
    arrival_list2_10.append(ARRIVAL)
    transnum_list2_10.append(transnum2_10) 

# ******************************************************************************
'''
# 无限buffer值，对比1drone and 2drone
#plot the average queuing delay
plt.figure(1)
plt.plot(arrival_list1_inf,avgdelay_list1_inf,color='r',marker='o',label='1 drone with infinite buffersize')
plt.plot(arrival_list2_inf,avgdelay_list2_inf,color='g',marker='o',label='2 drones with infinite buffersize')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("average queuing delay [ms]")
# plt.title("M/M/1/1")
plt.xticks(arrival_list1_inf)
plt.legend()
plt.grid()
plt.savefig("task3a-average queuing delay", dpi=300)

#plot the average user number
plt.figure(2)
plt.plot(arrival_list1_inf,avgusernum_list1_inf,color='r',marker='o',label='1 drone with infinite buffersize')
plt.plot(arrival_list2_inf,avgusernum_list2_inf,color='g',marker='o',label='2 drones with infinite buffersize')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("average user number")
# plt.title("M/M/1/1")
plt.xticks(arrival_list1_inf)
plt.legend()
plt.grid()
plt.savefig("task3a-average user number", dpi=300)     

#plot the transmitted packets number
plt.figure(3)
plt.plot(arrival_list1_inf,transnum_list1_inf,color='r',marker='o',label='1 drone with infinite buffersize')
plt.plot(arrival_list2_inf,transnum_list2_inf,color='g',marker='o',label='2 drones with infinite buffersize')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("number of transmitted packets")
# plt.title("M/M/1/1")
plt.xticks(arrival_list1_inf)
plt.legend()
plt.grid()
plt.savefig("task3a-number of transmitted packets", dpi=300)    
'''
# 不同有限buffer值，对比1drone and 2drone
plt.figure(4)
# plt.plot(arrival_list1_inf,Loss_rate_list1_inf,color='r',marker='o',label='1 drone with infinite buffersize')
plt.plot(arrival_list1_3,Loss_rate_list1_3,color='r',marker='x', label='1 drone with buffersize 3')
plt.plot(arrival_list1_10,Loss_rate_list1_10,color='r',marker='^', label='1 drone with buffersize 10')
# plt.plot(arrival_list2_inf,Loss_rate_list2_inf,color='g',marker='o',label='2 drones with infinite buffersize')
plt.plot(arrival_list2_3,Loss_rate_list2_3,color='g',marker='x', label='2 drones with buffersize 3')
plt.plot(arrival_list2_10,Loss_rate_list2_10,color='g',marker='^', label='2 drones with buffersize 10')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("loss probability")
plt.xticks(arrival_list1_inf)
plt.legend()
plt.grid()
plt.savefig("task3b-loss probability", dpi=300)


#plot the average queuing delay
plt.figure(5)
# plt.plot(arrival_list1_inf,avgdelay_list1_inf,color='r',marker='o',label='1 drone with infinite buffersize')
plt.plot(arrival_list1_3,avgdelay_list1_3,color='r',marker='x', label='1 drone with buffersize 3')
plt.plot(arrival_list1_10,avgdelay_list1_10,color='r',marker='^', label='1 drone with buffersize 10')
# plt.plot(arrival_list2_inf,avgdelay_list2_inf,color='g',marker='o',label='2 drones with infinite buffersize')
plt.plot(arrival_list2_3,avgdelay_list2_3,color='g',marker='x', label='2 drones with buffersize 3')
plt.plot(arrival_list2_10,avgdelay_list2_10,color='g',marker='^', label='2 drones with buffersize 10')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("average queuing delay [ms]")
# plt.title("M/M/1/1")
plt.xticks(arrival_list1_inf)
plt.legend()
plt.grid()
plt.savefig("task3b-average queuing delay", dpi=300)

#plot the average user number
plt.figure(6)
# plt.plot(arrival_list1_inf,avgusernum_list1_inf,color='r',marker='o',label='1 drone with infinite buffersize')
plt.plot(arrival_list1_3,avgusernum_list1_3,color='r',marker='x', label='1 drone with buffersize 3')
plt.plot(arrival_list1_10,avgusernum_list1_10,color='r',marker='^', label='1 drone with buffersize 10')
# plt.plot(arrival_list2_inf,avgusernum_list2_inf,color='g',marker='o',label='2 drones with infinite buffersize')
plt.plot(arrival_list2_3,avgusernum_list2_3,color='g',marker='x', label='2 drones with buffersize 3')
plt.plot(arrival_list2_10,avgusernum_list2_10,color='g',marker='^', label='2 drones with buffersize 10')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("average user number")
# plt.title("M/M/1/1")
plt.xticks(arrival_list1_inf)
plt.legend()
plt.grid()
plt.savefig("task3b-average user number", dpi=300)     

#plot the transmitted packets number
plt.figure(7)
# plt.plot(arrival_list1_inf,transnum_list1_inf,color='r',marker='o',label='1 drone with infinite buffersize')
plt.plot(arrival_list1_3,transnum_list1_3,color='r',marker='x', label='1 drone with buffersize 3')
plt.plot(arrival_list1_10,transnum_list1_10,color='r',marker='^', label='1 drone with buffersize 10')
# plt.plot(arrival_list2_inf,transnum_list2_inf,color='g',marker='o',label='2 drones with infinite buffersize')
plt.plot(arrival_list2_3,transnum_list2_3,color='g',marker='x', label='2 drones with buffersize 3')
plt.plot(arrival_list2_10,transnum_list2_10,color='g',marker='^', label='2 drones with buffersize 10')
plt.xlabel("average inter-arrival time [ms]")
plt.ylabel("number of transmitted packets")
# plt.title("M/M/1/1")
plt.xticks(arrival_list1_inf)
plt.legend()
plt.grid()
plt.savefig("task3b-number of transmitted packets", dpi=300)    



 