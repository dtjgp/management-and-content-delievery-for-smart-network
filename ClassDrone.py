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
    def __init__(self,type,arrival_time):
        self.type = type
        self.arrival_time = arrival_time
        
class Drone:
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
        self.MM1 = []
        
                
    def arrival(self, time, FES, queue): #没有buffer的情况下的arrival
        
        #print("Arrival no. ",data.arr+1," at time ",time," with ",users," users" )
        
        # cumulate statistics, 用于计算时间相关参数
        self.arr += 1       
        self.ut += self.users*(time-self.oldT)  
        self.oldT = time

        # sample the time until the next event
        inter_arrival = random.expovariate(lambd=1.0/self.ARRIVAL)
        
        # schedule the next arrival
        FES.put((time + inter_arrival, "arrival")) # 下一个arrival到来的时间点

        self.users += 1 #用户数量加一
        
        # create a record for the client
        client = Client(self.TYPE1,time) #定义client的类型为TYPE1

        # insert the record in the queue
        queue.append(client)
        # print("the number of users before arrival calculation: ", users)

        '''目标是能够实现，当channel的数量大于等于1的时候，能够进行判定users的数量在channelsize
        的数量限定范围之内，能够直接进行调用服务，否则的话，需要进行排队'''
        
        # make sure if the channelsize is equal to 1
        # if the server is idle start the service
        if self.users <= self.channelsize:
            
            # sample the service time
            service_time = random.expovariate(1.0/self.SERVICE)
            # print("service_time is : ", service_time)
            #service_time = 1 + random.uniform(0, SEVICE_TIME)

            # schedule when the client will finish the server
            FES.put((time + service_time, "departure"))#departure的时间
            
        elif self.users > self.Buffersize: #所有的在service过程中到达的包都会被丢弃，所以增加的users应该自动减去1
            self.users -= 1
            queue.pop()
            
    def departure(self, time, FES, queue):

        #print("Departure no. ",data.dep+1," at time ",time," with ",users," users" )
            
        # cumulate statistics
        self.dep += 1
        self.ut += self.users*(time-self.oldT)
        self.oldT = time
        
        # get the first element from the queue
        client = queue.pop(0)
        
        # do whatever we need to do when clients go away
        
        self.delay += (time-client.arrival_time)
        self.users -= 1
        
        # see whether there are more clients to in the line
        if self.users > (self.channelsize -1):
            # sample the service time
            service_time = random.expovariate(1.0/self.SERVICE)

            # schedule when the client will finish the server
            FES.put((time + service_time, "departure"))
    
    def statistical_result(self):
        random.seed(42)
        # initiate the simulation time 
        time = 0
        
        # the list of events in the form: (time, type)
        self.FES = PriorityQueue()
        
        
        # schedule the first arrival at t=0
        self.FES.put((0, "arrival"))
         # simulate until the simulated time reaches a constant
        while time < self.Simtime:
            (time, event_type) = self.FES.get()
        
            if event_type == "arrival":
                self.arrival(time, self.FES, self.MM1)
        
            elif event_type == "departure":
                self.departure(time, self.FES, self.MM1)
                
        load = self.SERVICE/self.ARRIVAL
        arrivalRate = self.arr/time
        departureRate = self.dep/time
        lossRate = (self.arr-self.dep)/self.arr
        successRate = self.dep/self.arr
        averageUser = self.ut/time
        averageDelay = self.delay/self.dep
        queueSize = len(self.MM1)
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
            "queueSize": queueSize,
            }
        return json.dumps(payload)

    