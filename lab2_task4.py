#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 00:15:27 2022

@author: dtjgp
"""

'''
设定：
1.无人机数量
N = 2
service_rate:10
buffersize = 10
Arrival1 = 10 # av arrival time in period 1
Arrival2 = 30 # av arrival time in period 2
Arrival3 = 11 # av arrival time in period 3
Arrival4 = 20 # av arrival time in period 4

A型无人机：
workingtime = 25 # in minute
chargingtime = 60 # in minute
serviceA = 10
buffersize = 10
channelsize = 1
Drone2

B型无人机：
workingtime = 30 # in minute
chargingtime = 60 # in minute
serviceB = 5
buffersize = 10
channelsize = 1
Drone

C型无人机：
workingtime = 40 # in minute
chargingtime = 60 # in minute
serviceC = 10
buffersize = 20
channelsize = 1
Drone


configuration I:
    1*A & 1*C
configuration II:
    2*B
configuration III:
    1*A & 1*B
configuration IV:
    1*B & 1*C
'''


import ClassDrone
import json
import matplotlib.pyplot as plt
import Drone2


Arrival1 = 10 # av arrival time in period 1
Arrival2 = 30 # av arrival time in period 2
Arrival3 = 11 # av arrival time in period 3
Arrival4 = 20 # av arrival time in period 4

channelsize = 1
chargingtime = 60

workingA = 25
serviceA = 10
buffersizeA = 10

workingB = 30
serviceB = 5
buffersizeB = 10

workingC = 40
serviceC = 10
buffersizeC = 20

#set the maximum cycle is 4
'''
每个period运行两次，工作两次充电两次
'''
#********************************************************************************
#********************************************************************************
#configuration I：A&C
def timeslot1():
    
    averageUserSTA = [0, 0, 0, 0]
    departureNumSTA = [0, 0, 0, 0]
    arrivalNumSTA = [0, 0, 0, 0]
    
    averageUserSTC = [0, 0, 0, 0]
    departureNumSTC = [0, 0, 0, 0]
    arrivalNumSTC = [0, 0, 0, 0]
    
    averageUserST1 = [0, 0, 0, 0]
    departureNumST1 = [0, 0, 0, 0]
    arrivalNumST1 = [0, 0, 0, 0]
    
    for i in range(2):
        drone1 = Drone2.Drone2(serviceA, Arrival1, buffersizeA, workingA*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageUserSTA[0]+=result1["averageUser"] #平均延迟
        departureNumSTA[0]+=result1["departureNum"] #处理的包的数量
        arrivalNumSTA[0] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
    for i in range(2):
        drone1 = ClassDrone.Drone(serviceC, Arrival1, buffersizeC, workingC*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageUserSTC[0]+=result1["averageUser"] #平均延迟
        departureNumSTC[0]+=result1["departureNum"] #处理的包的数量
        arrivalNumSTC[0] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
        
    averageUserST1[0] = averageUserSTA[0] + averageUserSTC[0]
    departureNumST1[0] = departureNumSTA[0] + departureNumSTC[0]
    arrivalNumST1[0] = arrivalNumSTA[0] + arrivalNumSTC[0]
    
    departureNumST1[1] = departureNumST1[0] + departureNumST1[1]
    arrivalNumST1[1] = arrivalNumST1[0] + arrivalNumST1[1]
    
    for i in range(2):
        drone1 = Drone2.Drone2(serviceA, Arrival3, buffersizeA, workingA*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageUserSTA[2]+=result1["averageUser"] #平均延迟
        departureNumSTA[2]+=result1["departureNum"] #处理的包的数量
        arrivalNumSTA[2] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
    for i in range(2):
        drone1 = ClassDrone.Drone(serviceC, Arrival3, buffersizeC, workingC*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageUserSTC[2]+=result1["averageUser"] #平均延迟
        departureNumSTC[2]+=result1["departureNum"] #处理的包的数量
        arrivalNumSTC[2] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
    
    averageUserST1[2] = averageUserSTA[2] + averageUserSTC[2]
    departureNumST1[2] = departureNumSTA[2] + departureNumSTC[2]
    arrivalNumST1[2] = arrivalNumSTA[2] + arrivalNumSTC[2]
    
    departureNumST1[2] = departureNumST1[2] + departureNumST1[1]
    arrivalNumST1[2] = arrivalNumST1[2] + arrivalNumST1[1]
    
    departureNumST1[3] = departureNumST1[2] + departureNumST1[3]
    arrivalNumST1[3] = arrivalNumST1[2] + arrivalNumST1[3]
    
    return averageUserST1, departureNumST1, arrivalNumST1

#********************************************************************************
#configuration II: 2*B
def timeslot2():
    averageUserSTB1 = [0, 0, 0, 0]
    departureNumSTB1 = [0, 0, 0, 0]
    arrivalNumSTB1 = [0, 0, 0, 0]
    
    averageUserSTB2 = [0, 0, 0, 0]
    departureNumSTB2 = [0, 0, 0, 0]
    arrivalNumSTB2 = [0, 0, 0, 0]
    
    averageUserST2 = [0, 0, 0, 0]
    departureNumST2 = [0, 0, 0, 0]
    arrivalNumST2 = [0, 0, 0, 0]
    
    for i in range(2):
        drone1 = ClassDrone.Drone(serviceB, Arrival1, buffersizeB, workingB*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageUserSTB1[0]+=result1["averageUser"] #平均延迟
        departureNumSTB1[0]+=result1["departureNum"] #处理的包的数量
        arrivalNumSTB1[0] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
    for i in range(2):
        drone1 = ClassDrone.Drone(serviceB, Arrival1, buffersizeB, workingB*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageUserSTB2[0]+=result1["averageUser"] #平均延迟
        departureNumSTB2[0]+=result1["departureNum"] #处理的包的数量
        arrivalNumSTB2[0] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
        
    averageUserST2[0] = averageUserSTB1[0] + averageUserSTB2[0]
    departureNumST2[0] = departureNumSTB1[0] + departureNumSTB2[0]
    arrivalNumST2[0] = arrivalNumSTB1[0] + arrivalNumSTB2[0]
    
    departureNumST2[1] = departureNumST2[0] + departureNumST2[1]
    arrivalNumST2[1] = arrivalNumST2[0] + arrivalNumST2[1]
    
    for i in range(2):
        drone1 = ClassDrone.Drone(serviceB, Arrival3, buffersizeB, workingB*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageUserSTB1[2]+=result1["averageUser"] #平均延迟
        departureNumSTB1[2]+=result1["departureNum"] #处理的包的数量
        arrivalNumSTB1[2] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
    for i in range(2):
        drone1 = ClassDrone.Drone(serviceB, Arrival3, buffersizeB, workingB*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageUserSTB2[2]+=result1["averageUser"] #平均延迟
        departureNumSTB2[2]+=result1["departureNum"] #处理的包的数量
        arrivalNumSTB2[2] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
        
    averageUserST2[2] = averageUserSTB1[2] + averageUserSTB2[2]
    departureNumST2[2] = departureNumSTB1[2] + departureNumSTB2[2]
    arrivalNumST2[2] = arrivalNumSTB1[2] + arrivalNumSTB2[2]
    
    departureNumST2[2] = departureNumST2[2] + departureNumST2[1]
    arrivalNumST2[2] = arrivalNumST2[2] + arrivalNumST2[1]
    
    departureNumST2[3] = departureNumST2[2] + departureNumST2[3]
    arrivalNumST2[3] = arrivalNumST2[2] + arrivalNumST2[3]
    
    return averageUserST2, departureNumST2, arrivalNumST2

#********************************************************************************
#configuration III: A&B
def timeslot3():
    
    averageUserSTA = [0, 0, 0, 0]
    departureNumSTA = [0, 0, 0, 0]
    arrivalNumSTA = [0, 0, 0, 0]
    
    averageUserSTB = [0, 0, 0, 0]
    departureNumSTB = [0, 0, 0, 0]
    arrivalNumSTB = [0, 0, 0, 0]
    
    averageUserST3 = [0, 0, 0, 0]
    departureNumST3 = [0, 0, 0, 0]
    arrivalNumST3 = [0, 0, 0, 0]
    
    for i in range(2):
        drone1 = Drone2.Drone2(serviceA, Arrival1, buffersizeA, workingA*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageUserSTA[0]+=result1["averageUser"] #平均延迟
        departureNumSTA[0]+=result1["departureNum"] #处理的包的数量
        arrivalNumSTA[0] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
    for i in range(2):
        drone1 = ClassDrone.Drone(serviceB, Arrival1, buffersizeB, workingB*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageUserSTB[0]+=result1["averageUser"] #平均延迟
        departureNumSTB[0]+=result1["departureNum"] #处理的包的数量
        arrivalNumSTB[0] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
        
    averageUserST3[0] = averageUserSTA[0] + averageUserSTB[0]
    departureNumST3[0] = departureNumSTA[0] + departureNumSTB[0]
    arrivalNumST3[0] = arrivalNumSTA[0] + arrivalNumSTB[0]
    
    departureNumST3[1] = departureNumST3[0] + departureNumST3[1]
    arrivalNumST3[1] = arrivalNumST3[0] + arrivalNumST3[1]
    
    for i in range(2):
        drone1 = Drone2.Drone2(serviceA, Arrival3, buffersizeA, workingA*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageUserSTA[2]+=result1["averageUser"] #平均延迟
        departureNumSTA[2]+=result1["departureNum"] #处理的包的数量
        arrivalNumSTA[2] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
    for i in range(2):
        drone1 = ClassDrone.Drone(serviceB, Arrival3, buffersizeB, workingB*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageUserSTB[2]+=result1["averageUser"] #平均延迟
        departureNumSTB[2]+=result1["departureNum"] #处理的包的数量
        arrivalNumSTB[2] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
    
    averageUserST3[2] = averageUserSTA[2] + averageUserSTB[2]
    departureNumST3[2] = departureNumSTA[2] + departureNumSTB[2]
    arrivalNumST3[2] = arrivalNumSTA[2] + arrivalNumSTB[2]
    
    departureNumST3[2] = departureNumST3[2] + departureNumST3[1]
    arrivalNumST3[2] = arrivalNumST3[2] + arrivalNumST3[1]
    
    departureNumST3[3] = departureNumST3[2] + departureNumST3[3]
    arrivalNumST3[3] = arrivalNumST3[2] + arrivalNumST3[3]
    
    return averageUserST3, departureNumST3, arrivalNumST3

#********************************************************************************
#configuration IV: C&B
def timeslot4():
    
    averageUserSTC = [0, 0, 0, 0]
    departureNumSTC = [0, 0, 0, 0]
    arrivalNumSTC = [0, 0, 0, 0]
    
    averageUserSTB = [0, 0, 0, 0]
    departureNumSTB = [0, 0, 0, 0]
    arrivalNumSTB = [0, 0, 0, 0]
    
    averageUserST4 = [0, 0, 0, 0]
    departureNumST4 = [0, 0, 0, 0]
    arrivalNumST4 = [0, 0, 0, 0]
    
    for i in range(2):
        drone1 = ClassDrone.Drone(serviceC, Arrival1, buffersizeC, workingC*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageUserSTC[0]+=result1["averageUser"] #平均延迟
        departureNumSTC[0]+=result1["departureNum"] #处理的包的数量
        arrivalNumSTC[0] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
    for i in range(2):
        drone1 = ClassDrone.Drone(serviceB, Arrival1, buffersizeB, workingB*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageUserSTB[0]+=result1["averageUser"] #平均延迟
        departureNumSTB[0]+=result1["departureNum"] #处理的包的数量
        arrivalNumSTB[0] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
        
    averageUserST4[0] = averageUserSTC[0] + averageUserSTB[0]
    departureNumST4[0] = departureNumSTC[0] + departureNumSTB[0]
    arrivalNumST4[0] = arrivalNumSTC[0] + arrivalNumSTB[0]
    
    departureNumST4[1] = departureNumST4[0] + departureNumST4[1]
    arrivalNumST4[1] = arrivalNumST4[0] + arrivalNumST4[1]
    
    for i in range(2):
        drone1 = ClassDrone.Drone(serviceC, Arrival3, buffersizeC, workingC*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageUserSTC[2]+=result1["averageUser"] #平均延迟
        departureNumSTC[2]+=result1["departureNum"] #处理的包的数量
        arrivalNumSTC[2] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
    for i in range(2):
        drone1 = ClassDrone.Drone(serviceB, Arrival3, buffersizeB, workingB*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageUserSTB[2]+=result1["averageUser"] #平均延迟
        departureNumSTB[2]+=result1["departureNum"] #处理的包的数量
        arrivalNumSTB[2] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
    
    averageUserST4[2] = averageUserSTC[2] + averageUserSTB[2]
    departureNumST4[2] = departureNumSTC[2] + departureNumSTB[2]
    arrivalNumST4[2] = arrivalNumSTC[2] + arrivalNumSTB[2]
    
    departureNumST4[2] = departureNumST4[2] + departureNumST4[1]
    arrivalNumST4[2] = arrivalNumST4[2] + arrivalNumST4[1]
    
    departureNumST4[3] = departureNumST4[2] + departureNumST4[3]
    arrivalNumST4[3] = arrivalNumST4[2] + arrivalNumST4[3]
    
    return averageUserST4, departureNumST4, arrivalNumST4

#********************************************************************************
averageUserST1, departureNumST1, arrivalNumST1 = timeslot1()
averageUserST2, departureNumST2, arrivalNumST2 = timeslot2()
averageUserST3, departureNumST3, arrivalNumST3 = timeslot3()
averageUserST4, departureNumST4, arrivalNumST4 = timeslot4()

#********************************************************************************
#plot the Success Rate
plt.figure(dpi=700)
timeslot = ['8:00-11:00','11:00-14:00','14:00-17:00','17:00-20:00']
#plt.plot(arrivalNo,departures, " ",marker='.', label = 'No. of departures')
plt.plot(timeslot,averageUserST1, linestyle='-', marker='.', label = 'averageUser(configuration 1)')
plt.plot(timeslot,averageUserST2, linestyle='-', marker='.', label = 'averageUser(configuration 2)')
plt.plot(timeslot,averageUserST3, linestyle='-', marker='.', label = 'averageUser(configuration 3)')
plt.plot(timeslot,averageUserST4, linestyle='-', marker='.', label = 'averageUser(configuration 4)')

plt.xlabel('Time Slots')
plt.ylabel('Average Delay')
plt.title('Average Delay vs Time Slots')
plt.grid(linestyle=':')
plt.legend()
#plt.savefig("successRate.png", dpi=300)
plt.show()


#plot the No. of arrivals
plt.figure(dpi=300)
# plt.plot(arrivalNo,departures, " ",marker='.', label = 'No. of departures')
plt.plot(timeslot, arrivalNumST1, linestyle='-', marker='.', label = 'Arrival Number(configuration 1)')
plt.plot(timeslot, arrivalNumST2, linestyle='-', marker='.', label = 'Arrival Number(configuration 2)')
plt.plot(timeslot, arrivalNumST3, linestyle='-', marker='.', label = 'Arrival Number(configuration 3)')
plt.plot(timeslot, arrivalNumST4, linestyle='-', marker='.', label = 'Arrival Number(configuration 4)')

plt.xlabel('Time Slots')
plt.ylabel('Arrival Number')
plt.title('Arrival Number vs Time Slots')
plt.grid(linestyle=':')
plt.legend()
#plt.savefig("Arrival Number.png", dpi=300)
plt.show()
    

#plot the No. of departures
plt.figure(dpi=300)
#plt.plot(arrivalNo,departures, " ",marker='.', label = 'No. of departures')
plt.plot(timeslot, departureNumST1, linestyle='-', marker='.', label = 'Departure Number(configuration 1)')
plt.plot(timeslot, departureNumST2, linestyle='-', marker='.', label = 'Departure Number(configuration 2)')
plt.plot(timeslot, departureNumST3, linestyle='-', marker='.', label = 'Departure Number(configuration 3)')
plt.plot(timeslot, departureNumST4, linestyle='-', marker='.', label = 'Departure Number(configuration 4)')

plt.xlabel('Time Slots')
plt.ylabel('Departure Number')
plt.title('Departure Number vs Time Slots')
plt.grid(linestyle=':')
plt.legend()
#plt.savefig("Departure Number.png", dpi=300)
plt.show()  