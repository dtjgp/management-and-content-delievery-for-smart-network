#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 14:40:54 2022

@author: jingsichen
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 22:13:08 2022

@author: dtjgp
"""

import math
import random
from queue import Queue, PriorityQueue
import json

'''
在该试验中，设定的三种无人机的模式是按照lab2-task4种提供的三种模式来进行设定：

• Type A: the drone is powered by a battery only; its BS is equipped with 2
antennas featuring the same service rate μ, and the bu↵er size is equal to sA;
天线数量2，服务速率μ，缓冲区大小sA,(μ,sA均需要用户自定义)
• Type B: the drone is powered by a battery and a PV panel with small capacity;
its BS is equipped with 1 antenna featuring service rate 2μ, and the bu↵er size is
equal to sA;
天线数量1，服务速率2μ，缓冲区大小sA,(μ,sA均需要用户自定义)
• Type C: the drone is powered by a battery and a PV panel with larger capacity;
its BS is equipped with 1 antenna featuring service rate μ, and the bu↵er size is
equal to 2sA.
天线数量1，服务速率μ，缓冲区大小2sA,(μ,sA均需要用户自定义)
'''
class Client:
    def __init__(self,type, seq, arrival_time):
        self.type = type
        self.seq = seq
        self.arrival_time = arrival_time
        
class Drone3:
    def __init__(self, SERVICE, ARRIVAL, Buffersize, Simtime, channelsize):
        #根据不同的无人机可以进行不同的设定
        self.SERVICE = SERVICE   # av service time
        self.ARRIVAL = ARRIVAL   # av inter-arrival time
        self.Buffersize = Buffersize # buffer size
        self.Simtime = Simtime #total simulation time
        self.channelsize = channelsize #channel size 定义每一个无人机上的channel的数量
        #通过统一设定来进行下列函数定义
        self.arr = 0
        self.dep = 0
        self.ut = 0
        self.oldT = 0
        self.delay = 0
        self.users = 0  # users
        self.TYPE1 =1 #type of client
        self.TYPE2 = 2
        self.TYPE3 = 3
        self.MM1 = []
        self.MM2 = []
        self.MM3 = []
        self.user1 = 0
        self.user2 = 0
        self.user3 = 0
        
                
    def arrival(self, time, FES, queue1, queue2, queue3): #没有buffer的情况下的arrival
        
        #print("Arrival no. ",data.arr+1," at time ",time," with ",users," users" )
        # cumulate statistics, 用于计算时间相关参数
        self.arr += 1       
        self.ut += self.users*(time-self.oldT)  
        self.oldT = time

        # sample the time until the next event
        inter_arrival = random.expovariate(lambd=1.0/self.ARRIVAL)
        
        # schedule the next arrival
        FES.put((time + inter_arrival,0, "arrival")) # 下一个arrival到来的时间点

        self.users += 1 #用户数量加一
        
        a = len(queue1)
        b = len(queue2)
        c = len(queue3)
        listqueue = [a,b,c]
        minque = listqueue.index(min(listqueue))
        if minque == 0:
            seq = 1
            seq = 1
            client = Client(self.TYPE1,seq,time)
            queue1.append(client)
            self.user1 += 1
            if self.user1==1:
                
                # sample the service time
                service_time = random.expovariate(1.0/self.SERVICE)
                #service_time = 1 + random.uniform(0, SEVICE_TIME)
    
                # schedule when the client will finish the server
                FES.put((time + service_time, seq, "departure"))
            if self.user1 >= self.Buffersize:
                self.user1 -= 1
                queue1.pop() 
        elif minque == 1:
            seq = 2
            client = Client(self.TYPE2,seq,time)
            queue2.append(client)
            self.user2 += 1
            if self.user2==1:
                
                # sample the service time
                service_time = random.expovariate(1.0/self.SERVICE)
                #service_time = 1 + random.uniform(0, SEVICE_TIME)
    
                # schedule when the client will finish the server
                FES.put((time + service_time, seq, "departure"))
            if self.user2 >= self.Buffersize:
                self.user2 -= 1
                queue2.pop()
        elif minque == 2:
            seq = 3
            client = Client(self.TYPE3,seq,time)
            queue3.append(client)
            self.user3 += 1
            if self.user3==1:
                
                # sample the service time
                service_time = random.expovariate(1.0/self.SERVICE)
                #service_time = 1 + random.uniform(0, SEVICE_TIME)
    
                # schedule when the client will finish the server
                FES.put((time + service_time, seq, "departure"))
            if self.user3 >= self.Buffersize:
                self.user3 -= 1
                queue3.pop()

        
  
                
    def departure(self, time, FES, queue):

        #print("Departure no. ",data.dep+1," at time ",time," with ",users," users" )
            
        # cumulate statistics
        self.dep += 1
        self.ut += self.users*(time-self.oldT)
        self.oldT = time
        
        # get the first element from the queue
        client = queue.pop(0)
        seq = client.seq
        # do whatever we need to do when clients go away
        
        # self.delay += (time-client.arrival_time)
        self.users -= 1
        
        # see whether there are more clients to in the line
        # if self.users > (self.channelsize -1):
        #     # sample the service time
        #     service_time = random.expovariate(1.0/self.SERVICE)

        #     # schedule when the client will finish the server
        #     FES.put((time + service_time, seq, "departure"))
            
        if seq == 1:
            
         # do whatever we need to do when clients go away
         
            self.delay += (time-client.arrival_time)
            self.user1 -= 1
         
         # see whether there are more clients to in the line
            if self.user1 >(self.channelsize -1):
                 # sample the service time
                 service_time = random.expovariate(1.0/self.SERVICE)
         
                 # schedule when the client will finish the server
                 FES.put((time + service_time, seq, "departure"))
        elif seq == 2:
         
         # do whatever we need to do when clients go away
         
             self.delay += (time-client.arrival_time)
             self.user2 -= 1
         
         # see whether there are more clients to in the line
             if self.user2 >(self.channelsize -1):
                 # sample the service time
                 service_time = random.expovariate(1.0/self.SERVICE)
         
                 # schedule when the client will finish the server
                 FES.put((time + service_time, seq, "departure"))
                 
        elif seq == 3:
         
         # do whatever we need to do when clients go away
         
             self.delay += (time-client.arrival_time)
             self.user3 -= 1
         
         # see whether there are more clients to in the line
             if self.user3 >(self.channelsize -1):
                 # sample the service time
                 service_time = random.expovariate(1.0/self.SERVICE)
         
                 # schedule when the client will finish the server
                 FES.put((time + service_time, seq, "departure"))
    
    def statistical_result(self):
        random.seed(42)
        # initiate the simulation time 
        time = 0
        
        # the list of events in the form: (time, type)
        self.FES = PriorityQueue()
        
        
        # schedule the first arrival at t=0
        self.FES.put((0, 0, "arrival"))
         # simulate until the simulated time reaches a constant
        while time < self.Simtime:
            (time, seq, event_type) = self.FES.get()
        
            if event_type == "arrival":
                self.arrival(time, self.FES, self.MM1, self.MM2,self.MM3)
        
            elif event_type == "departure":
                
                if seq == 1:
                    
                    self.departure(time, self.FES, self.MM1)
                    
                elif seq == 2:
                    self.departure(time, self.FES, self.MM2) 
                    
                elif seq == 3:
                    self.departure(time, self.FES, self.MM3)
                    
                    
        
                
                
        load = self.SERVICE/self.ARRIVAL
        arrivalRate = self.arr/time
        departureRate = self.dep/time
        lossRate = (self.arr-self.dep)/self.arr
        successRate = self.dep/self.arr
        averageUser = self.ut/time
        averageDelay = self.delay/self.dep
        queueSize1 = len(self.MM1) 
        queueSize2 = len(self.MM2) 
        queueSize3 = len(self.MM3) 
        payload = {
            "usersInQueue": self.users,
            "arrivalNum": self.arr,
            "departureNum": self.dep,
            "load": load,
            "arrivalRate": arrivalRate,
            "departureRate": departureRate,
            "lossRate": lossRate,
            "successRate": successRate,
            "averageUser": averageUser,
            "averageDelay": averageDelay,
            "queueSize1": queueSize1,
            "queueSize2": queueSize2,
            "queueSize3": queueSize3,
            }
        return json.dumps(payload)

    