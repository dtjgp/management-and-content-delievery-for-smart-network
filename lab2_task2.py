#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:24:51 2022

@author: dtjgp
"""

#设定不同无人机运行次数下的状态
#version A有两个高峰运行阶段

import ClassDrone
import json
import matplotlib.pyplot as plt

'''
8:00-11:00高峰期
11:00-14:00低谷期
14:00-17:00高峰期
17:00-20:00低谷期
'''
#**********************************************************************************
#情景1 ：只有一次飞行机会
workingtime = 25 # in minute
chargingtime = 60 # in minute
Service = 10 # av service time
Arrival1 = 10 # av arrival time in period 1
Arrival2 = 30 # av arrival time in period 2
Arrival3 = 11 # av arrival time in period 3
Arrival4 = 20 # av arrival time in period 4
Buffersize = 10
channelsize = 2
def timeslot1_1():
    successRateST11 = [0, 0, 0, 0]
    departureNumST11 = [0, 0, 0, 0]
    arrivalNumST11 = [0, 0, 0, 0]
    drone1 = ClassDrone.Drone(Service, Arrival1, Buffersize, workingtime*60*1000, channelsize)
    resultJson1 = drone1.statistical_result()
    result1 = json.loads(resultJson1)
    print(json.dumps(result1, indent=4))
    successRateST11[0]+=result1["averageDelay"] #成功到达率
    departureNumST11[0]+=result1["departureNum"] #处理的包的数量
    arrivalNumST11[0] += result1["arrivalNum"] 
    drone1.MM1 = []
    drone1.users = 0
    
    return successRateST11, departureNumST11, arrivalNumST11 

def timeslot1_2():
    successRateST12 = [0, 0, 0, 0]
    departureNumST12 = [0, 0, 0, 0]
    arrivalNumST12 = [0, 0, 0, 0]
    drone1 = ClassDrone.Drone(Service, Arrival1, Buffersize, workingtime*60*1000, channelsize)
    resultJson1 = drone1.statistical_result()
    result1 = json.loads(resultJson1)
    print(json.dumps(result1, indent=4))
    successRateST12[2]+=result1["averageDelay"] #成功到达率
    departureNumST12[2]+=result1["departureNum"] #处理的包的数量
    arrivalNumST12[2] += result1["arrivalNum"] 
    drone1.MM1 = []
    drone1.users = 0
    
    return successRateST12, departureNumST12, arrivalNumST12


#**********************************************************************************
#情景2:两次飞行机会
def timeslot2_1():
    successRateST21 = [0, 0, 0, 0]
    departureNumST21 = [0, 0, 0, 0]
    arrivalNumST21 = [0, 0, 0, 0]
    for i in range(2):
        drone1 = ClassDrone.Drone(Service, Arrival1, Buffersize, workingtime*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        successRateST21[0]+=result1["averageDelay"] #平均延迟
        departureNumST21[0]+=result1["departureNum"] #处理的包的数量
        arrivalNumST21[0] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
    
    return successRateST21, departureNumST21, arrivalNumST21

def timeslot2_2():
    successRateST22 = [0, 0, 0, 0]
    departureNumST22 = [0, 0, 0, 0]
    arrivalNumST22 = [0, 0, 0, 0]

    drone1 = ClassDrone.Drone(Service, Arrival1, Buffersize, workingtime*60*1000, channelsize)
    resultJson1 = drone1.statistical_result()
    result1 = json.loads(resultJson1)
    print(json.dumps(result1, indent=4))
    successRateST22[0]+=result1["averageDelay"] #平均延迟
    departureNumST22[0]+=result1["departureNum"] #处理的包的数量
    arrivalNumST22[0] += result1["arrivalNum"]    #接受的包的数量
    drone1.MM1 = []
    drone1.users = 0
    
    drone1 = ClassDrone.Drone(Service, Arrival3, Buffersize, workingtime*60*1000, channelsize)
    resultJson1 = drone1.statistical_result()
    result1 = json.loads(resultJson1)
    print(json.dumps(result1, indent=4))
    successRateST22[2]+=result1["averageDelay"] #平均延迟
    departureNumST22[2]+=result1["departureNum"] #处理的包的数量
    arrivalNumST22[2] += result1["arrivalNum"]    #接受的包的数量
    drone1.MM1 = []
    drone1.users = 0
    
    return successRateST22, departureNumST22, arrivalNumST22

def timeslot2_3():
    successRateST23 = [0, 0, 0, 0]
    departureNumST23 = [0, 0, 0, 0]
    arrivalNumST23 = [0, 0, 0, 0]
    for i in range(2):
        drone1 = ClassDrone.Drone(Service, Arrival3, Buffersize, workingtime*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        successRateST23[2]+=result1["averageDelay"] #平均延迟
        departureNumST23[2]+=result1["departureNum"] #处理的包的数量
        arrivalNumST23[2] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
    
    return successRateST23, departureNumST23, arrivalNumST23


#**********************************************************************************
#情景3:三次飞行机会
def timeslot3_1():
    successRateST31 = [0, 0, 0, 0]
    departureNumST31 = [0, 0, 0, 0]
    arrivalNumST31 = [0, 0, 0, 0]
    for i in range(2):
        drone1 = ClassDrone.Drone(Service, Arrival1, Buffersize, workingtime*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        successRateST31[0]+=result1["averageDelay"] #平均延迟
        departureNumST31[0]+=result1["departureNum"] #处理的包的数量
        arrivalNumST31[0] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
    drone1 = ClassDrone.Drone(Service, Arrival3, Buffersize, workingtime*60*1000, channelsize)
    resultJson1 = drone1.statistical_result()
    result1 = json.loads(resultJson1)
    print(json.dumps(result1, indent=4))
    successRateST31[2]+=result1["averageDelay"] #平均延迟
    departureNumST31[2]+=result1["departureNum"] #处理的包的数量
    arrivalNumST31[2] += result1["arrivalNum"]    #接受的包的数量
    drone1.MM1 = []
    drone1.users = 0
    
    return successRateST31, departureNumST31, arrivalNumST31

def timeslot3_2():
    successRateST32 = [0, 0, 0, 0]
    departureNumST32 = [0, 0, 0, 0]
    arrivalNumST32 = [0, 0, 0, 0]
    
    drone1 = ClassDrone.Drone(Service, Arrival1, Buffersize, workingtime*60*1000, channelsize)
    resultJson1 = drone1.statistical_result()
    result1 = json.loads(resultJson1)
    print(json.dumps(result1, indent=4))
    successRateST32[0]+=result1["averageDelay"] #平均延迟
    departureNumST32[0]+=result1["departureNum"] #处理的包的数量
    arrivalNumST32[0] += result1["arrivalNum"]    #接受的包的数量
    drone1.MM1 = []
    drone1.users = 0
    
    for i in range(2):
        drone1 = ClassDrone.Drone(Service, Arrival3, Buffersize, workingtime*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        successRateST32[2]+=result1["averageDelay"] #平均延迟
        departureNumST32[2]+=result1["departureNum"] #处理的包的数量
        arrivalNumST32[2] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
    
    
    return successRateST32, departureNumST32, arrivalNumST32

#**********************************************************************************
def timeslot4():
    successRateST4 = [0, 0, 0, 0]
    departureNumST4 = [0, 0, 0, 0]
    arrivalNumST4 = [0, 0, 0, 0]
    
    for i in range(2):
        drone1 = ClassDrone.Drone(Service, Arrival1, Buffersize, workingtime*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        successRateST4[0]+=result1["averageDelay"] #平均延迟
        departureNumST4[0]+=result1["departureNum"] #处理的包的数量
        arrivalNumST4[0] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
    
    for i in range(2):
        drone1 = ClassDrone.Drone(Service, Arrival3, Buffersize, workingtime*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        successRateST4[2]+=result1["averageDelay"] #平均延迟
        departureNumST4[2]+=result1["departureNum"] #处理的包的数量
        arrivalNumST4[2] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
    
    
    return successRateST4, departureNumST4, arrivalNumST4







successRateST11, departureNumST11, arrivalNumST11 = timeslot1_1()
successRateST12, departureNumST12, arrivalNumST12 = timeslot1_2()
successRateST21, departureNumST21, arrivalNumST21 = timeslot2_1()
successRateST22, departureNumST22, arrivalNumST22 = timeslot2_2()
successRateST23, departureNumST23, arrivalNumST23 = timeslot2_3()
successRateST31, departureNumST31, arrivalNumST31 = timeslot3_1()
successRateST32, departureNumST32, arrivalNumST32 = timeslot3_2()
successRateST4, departureNumST4, arrivalNumST4 = timeslot4()

#plot the Success Rate
plt.figure(dpi=700)
timeslot = ['8:00-11:00','11:00-14:00','14:00-17:00','17:00-20:00']
#plt.plot(arrivalNo,departures, " ",marker='.', label = 'No. of departures')
plt.plot(timeslot,successRateST11, linestyle='-', marker='.', label = 'averageDelay(Strategy 12)')
plt.plot(timeslot,successRateST12, linestyle='-', marker='.', label = 'averageDelay(Strategy 12)')
plt.plot(timeslot,successRateST21, linestyle='-', marker='.', label = 'averageDelay(Strategy 21)')
plt.plot(timeslot,successRateST22, linestyle='-', marker='.', label = 'averageDelay(Strategy 22)')
plt.plot(timeslot,successRateST23, linestyle='-', marker='.', label = 'averageDelay(Strategy 23)')
plt.plot(timeslot,successRateST31, linestyle='-', marker='.', label = 'averageDelay(Strategy 31)')
plt.plot(timeslot,successRateST32, linestyle='-', marker='.', label = 'averageDelay(Strategy 32)')
plt.plot(timeslot,successRateST4, linestyle='-', marker='.', label = 'averageDelay(Strategy 4)')


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
plt.plot(timeslot, arrivalNumST11, linestyle='-', marker='.', label = 'Arrival Number(Strategy 11)')
plt.plot(timeslot, arrivalNumST12, linestyle='-', marker='.', label = 'Arrival Number(Strategy 12)')
plt.plot(timeslot, arrivalNumST21, linestyle='-', marker='.', label = 'Arrival Number(Strategy 21)')
plt.plot(timeslot, arrivalNumST22, linestyle='-', marker='.', label = 'Arrival Number(Strategy 22)')
plt.plot(timeslot, arrivalNumST23, linestyle='-', marker='.', label = 'Arrival Number(Strategy 23)')
plt.plot(timeslot, arrivalNumST31, linestyle='-', marker='.', label = 'Arrival Number(Strategy 31)')
plt.plot(timeslot, arrivalNumST32, linestyle='-', marker='.', label = 'Arrival Number(Strategy 32)')
plt.plot(timeslot, arrivalNumST4, linestyle='-', marker='.', label = 'Arrival Number(Strategy 4)')


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
plt.plot(timeslot, departureNumST11, linestyle='-', marker='.', label = 'Departure Number(Strategy 11)')
plt.plot(timeslot, departureNumST12, linestyle='-', marker='.', label = 'Departure Number(Strategy 12)')
plt.plot(timeslot, departureNumST21, linestyle='-', marker='.', label = 'Departure Number(Strategy 21)')
plt.plot(timeslot, departureNumST22, linestyle='-', marker='.', label = 'Departure Number(Strategy 22)')
plt.plot(timeslot, departureNumST23, linestyle='-', marker='.', label = 'Departure Number(Strategy 23)')
plt.plot(timeslot, departureNumST31, linestyle='-', marker='.', label = 'Departure Number(Strategy 31)')
plt.plot(timeslot, departureNumST32, linestyle='-', marker='.', label = 'Departure Number(Strategy 32)')
plt.plot(timeslot, departureNumST4, linestyle='-', marker='.', label = 'Departure Number(Strategy 4)')



plt.xlabel('Time Slots')
plt.ylabel('Departure Number')
plt.title('Departure Number vs Time Slots')
plt.grid(linestyle=':')
plt.legend()
#plt.savefig("Departure Number.png", dpi=300)
plt.show()  