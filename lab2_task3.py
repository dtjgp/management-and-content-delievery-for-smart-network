#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 13:15:54 2022

@author: dtjgp
"""

'''
set the maximum charging clcles is 4
'''
import ClassDrone
import json
import matplotlib.pyplot as plt
import Drone2
import Drone3
 
workingtime = 25 # in minute
chargingtime = 60 # in minute
Service = 10 # av service time
Arrival1 = 5 # av arrival time in period 1
Arrival2 = 20 # av arrival time in period 2
Arrival3 = 5 # av arrival time in period 3
Arrival4 = 10 # av arrival time in period 4
Buffersize = 10
channelsize = 1


#******************************************************************************
#one drone
def timeslot1():
    successRateST1 = [0, 0, 0, 0]
    departureNumST1 = [0, 0, 0, 0]
    arrivalNumST1 = [0, 0, 0, 0]
    
    for i in range(2):
        drone1 = ClassDrone.Drone(Service, Arrival1, Buffersize, workingtime*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        successRateST1[0]+=result1["successRate"] #平均延迟
        departureNumST1[0]+=result1["departureNum"] #处理的包的数量
        arrivalNumST1[0] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0

    
    for i in range(2):
        drone1 = ClassDrone.Drone(Service, Arrival3, Buffersize, workingtime*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        successRateST1[2]+=result1["successRate"] #平均延迟
        departureNumST1[2]+=result1["departureNum"] #处理的包的数量
        arrivalNumST1[2] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0

    successRateST1[0] = successRateST1[0]/2
    successRateST1[2] = successRateST1[2]/2
    
    return successRateST1, departureNumST1, arrivalNumST1

#******************************************************************************
#two drones
def timeslot2():
    successRateST21 = [0, 0, 0, 0]
    departureNumST21 = [0, 0, 0, 0]
    arrivalNumST21 = [0, 0, 0, 0]
    successRateST22 = [0, 0, 0, 0]
    departureNumST22 = [0, 0, 0, 0]
    arrivalNumST22 = [0, 0, 0, 0]
    successRateST2 = [0, 0, 0, 0]
    departureNumST2 = [0, 0, 0, 0]
    arrivalNumST2 = [0, 0, 0, 0]
    
    for i in range(2):
        drone1 = Drone2.Drone2(Service, Arrival1/2, Buffersize, workingtime*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        successRateST21[0]+=result1["successRate"] #平均延迟
        departureNumST21[0]+=result1["departureNum"] #处理的包的数量
        arrivalNumST21[0] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
    
        
    successRateST2[0] = (successRateST21[0] + successRateST22[0]) /2
    departureNumST2[0] = departureNumST21[0] + departureNumST22[0]
    arrivalNumST2[0] = arrivalNumST21[0] + arrivalNumST22[0]

        
    for i in range(2):
        drone1 = Drone2.Drone2(Service, Arrival3/2, Buffersize, workingtime*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        successRateST22[2]+=result1["successRate"] #平均延迟
        departureNumST22[2]+=result1["departureNum"] #处理的包的数量
        arrivalNumST22[2] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
        
    successRateST2[2] = (successRateST21[2] + successRateST22[2]) /2
    departureNumST2[2] = departureNumST21[2] + departureNumST22[2]
    arrivalNumST2[2] = arrivalNumST21[2] + arrivalNumST22[2]
    
    
    return successRateST2, departureNumST2, arrivalNumST2


#******************************************************************************
#three drones
def timeslot3():
    successRateST31 = [0, 0, 0, 0]
    departureNumST31 = [0, 0, 0, 0]
    arrivalNumST31 = [0, 0, 0, 0]
    successRateST32 = [0, 0, 0, 0]
    departureNumST32 = [0, 0, 0, 0]
    arrivalNumST32 = [0, 0, 0, 0]
    successRateST33 = [0, 0, 0, 0]
    departureNumST33 = [0, 0, 0, 0]
    arrivalNumST33 = [0, 0, 0, 0]
    successRateST3 = [0, 0, 0, 0]
    departureNumST3 = [0, 0, 0, 0]
    arrivalNumST3 = [0, 0, 0, 0]
    
    for i in range(2):
        drone1 = Drone3.Drone3(Service, Arrival1/3, Buffersize, workingtime*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        successRateST31[0]+=result1["successRate"] #平均延迟
        departureNumST31[0]+=result1["departureNum"] #处理的包的数量
        arrivalNumST31[0] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
        
        
    successRateST3[0] = (successRateST31[0] + successRateST32[0] + successRateST33[0]) /2
    departureNumST3[0] = departureNumST31[0] + departureNumST32[0] + departureNumST33[0]
    arrivalNumST3[0] = arrivalNumST31[0] + arrivalNumST32[0] + arrivalNumST33[0]
    
    for i in range(2):
        drone1 = Drone3.Drone3(Service, Arrival3/3, Buffersize, workingtime*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        successRateST31[2]+=result1["successRate"] #平均延迟
        departureNumST31[2]+=result1["departureNum"] #处理的包的数量
        arrivalNumST31[2] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
        

        
    successRateST3[2] = (successRateST31[2] + successRateST32[2] + successRateST33[2]) /2
    departureNumST3[2] = departureNumST31[2] + departureNumST32[2] + departureNumST33[2]
    arrivalNumST3[2] = arrivalNumST31[2] + arrivalNumST32[2] + arrivalNumST33[2]
    
    return successRateST3, departureNumST3, arrivalNumST3


successRateST1, departureNumST1, arrivalNumST1 = timeslot1()
successRateST2, departureNumST2, arrivalNumST2 = timeslot2()
successRateST3, departureNumST3, arrivalNumST3 = timeslot3()

#plot the Success Rate
plt.figure(dpi=700)
timeslot = ['8:00-11:00','11:00-14:00','14:00-17:00','17:00-20:00']
#plt.plot(arrivalNo,departures, " ",marker='.', label = 'No. of departures')
plt.plot(timeslot,successRateST1, linestyle='-', marker='.', label = 'Case 1')
plt.plot(timeslot,successRateST2, linestyle='-', marker='.', label = 'Case 2')
plt.plot(timeslot,successRateST3, linestyle='-', marker='.', label = 'Case 3')


plt.xlabel('Time Slots')
plt.ylabel('SuccessRate')
plt.title('SuccessRate vs Time Slots')
plt.grid(linestyle=':')
plt.legend()
#plt.savefig("successRate.png", dpi=300)
plt.show()


#plot the No. of arrivals
plt.figure(dpi=300)
# plt.plot(arrivalNo,departures, " ",marker='.', label = 'No. of departures')
plt.plot(timeslot, arrivalNumST1, linestyle='-', marker='.', label = 'Case 1)')
plt.plot(timeslot, arrivalNumST2, linestyle='-', marker='.', label = 'Case 2)')
plt.plot(timeslot, arrivalNumST3, linestyle='-', marker='.', label = 'Case 3)')



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
plt.plot(timeslot, departureNumST1, linestyle='-', marker='.', label = 'Case 1')
plt.plot(timeslot, departureNumST2, linestyle='-', marker='.', label = 'Case 2')
plt.plot(timeslot, departureNumST3, linestyle='-', marker='.', label = 'Case 3')




plt.xlabel('Time Slots')
plt.ylabel('Departure Number')
plt.title('Departure Number vs Time Slots')
plt.grid(linestyle=':')
plt.legend()
#plt.savefig("Departure Number.png", dpi=300)
plt.show()  