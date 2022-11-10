# *****************************************************************************
# timeslot1场景：charging与working时间不间断
'''
定义的工作时间段：
1.8:00-11:00 高峰期
2.11:00-14:00 低谷期
3.14:00-17:00 高峰期
4.17:00-20:00 低谷期
'''
# 工况1：工作充电一直进行循环，中间没有任何的间隔
import ClassDrone
import json
import matplotlib.pyplot as plt


workingtime = 25 # in minute 
chargingtime = 60 # in minute
ServiceTime = 10
ArrivalTime1 = 11
ArrivalTime2 = 30
ArrivalTime3 = 11
ArrivalTime4 = 20
Buffersize = 10
channelsize = 2



# drone1 = ClassDrone()
def timeslot1():
    starttime = 8 # in hour
    timeslotperiod = 3 # in hour
    timeperiod = workingtime + chargingtime #work & charging 时间总和 in minute, which is 85min
    totaltime = 8 # in hour 
    time1round = 0
    timepassed1 = 0
    totalround = 0
    num = 0
    timecount = 0

    '''
    简化设置数据列表
    '''
    averageDelayST1 = [0, 0, 0, 0]
    departureNumST1 = [0, 0, 0, 0]
    arrivalNumST1 = [0, 0, 0, 0]
    #第一段时间
    print("round1**********************************************************")
    while timepassed1 <= (timeslotperiod*60): #确定按照一个period来算的话，有几段
        timepassed1 += timeperiod
        time1round += 1
        
    if timepassed1 >= timeslotperiod * 60: 
        if timeperiod-(timepassed1-timeslotperiod*60)<workingtime:
            time1round -= 1
            res1 = timeperiod-(timepassed1-timeslotperiod*60) #
    print("time1round:", time1round)
    num1 = 0
    for i in range(time1round):
        drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime1, Buffersize, workingtime*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageDelayST1[0]+=result1["averageDelay"] #平均延迟
        departureNumST1[0]+=result1["departureNum"] #处理的包的数量
        arrivalNumST1[0] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
        num1 += 1
    drone1.MM1 = []
    drone1.users = 0
    print(res1)
    num1 += 1
    drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime1, Buffersize, res1*60*1000, channelsize)
    resultJson1 = drone1.statistical_result()
    result1 = json.loads(resultJson1)
    print(json.dumps(result1, indent=4))
    averageDelayST1[0]+=result1["averageDelay"] #平均延迟
    departureNumST1[0]+=result1["departureNum"] #处理的包的数量
    arrivalNumST1[0] += result1["arrivalNum"] 
    # averageDelayST1[0] = averageDelayST1[0]/num1
    departureNumST1[0] = departureNumST1[0]
    arrivalNumST1[0] = arrivalNumST1[0]
# *******************************************************************************
    #第二段时间
    print("round2**********************************************************")
    num2 = 0
    timetrans12 = timeperiod - res1
    workingtimetrans12 = timetrans12 - chargingtime
    drone1.MM1 = []
    drone1.users = 0
    drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime2, Buffersize, workingtimetrans12*60*1000, channelsize)
    resultJson1 = drone1.statistical_result()
    result1 = json.loads(resultJson1)
    print(json.dumps(result1, indent=4))
    averageDelayST1[1]+=result1["averageDelay"] #平均延迟
    departureNumST1[1]+=result1["departureNum"] #处理的包的数量
    arrivalNumST1[1] += result1["arrivalNum"] 
    num2 += 1
    
    timeperiodres2 = timeslotperiod * 60 - timetrans12
    timepassed2 = 0
    time2round = 0
    while timepassed2 <= timeperiodres2:
        timepassed2 += timeperiod
        time2round += 1
    if timepassed2 >= timeperiodres2:
        timemore2 = timepassed2 - timeperiodres2
        if timeperiod - timemore2 <= workingtime:
            time2round -= 1
            res2 = timeperiod - timemore2
    print("time2round:", time2round)
    drone1.MM1 = []
    drone1.users = 0
    for i in range(time2round):
        drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime2, Buffersize, workingtime*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageDelayST1[1]+=result1["averageDelay"] #平均延迟
        departureNumST1[1]+=result1["departureNum"] #处理的包的数量
        arrivalNumST1[1] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
        num2 += 1
    drone1.MM1 = []
    drone1.users = 0
    print(res2)
    num2 += 1
    drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime2, Buffersize, res2*60*1000, channelsize)
    resultJson1 = drone1.statistical_result()
    result1 = json.loads(resultJson1)
    print(json.dumps(result1, indent=4))
    averageDelayST1[1]+=result1["averageDelay"] #平均延迟
    departureNumST1[1]+=result1["departureNum"] #处理的包的数量
    arrivalNumST1[1] += result1["arrivalNum"] 
    # averageDelayST1[1] = averageDelayST1[1]/num2
    departureNumST1[1] = departureNumST1[1] + departureNumST1[0]
    arrivalNumST1[1] = arrivalNumST1[1] + arrivalNumST1[0]
# *******************************************************************************
    # 第三段时间
    print("round3**********************************************************")
    num3 = 0
    timetrans23 = timeperiod - res2 #65min
    workingtimetrans23 = timetrans23 - chargingtime #5min
    drone1.MM1 = []
    drone1.users = 0
    drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime3, Buffersize, workingtimetrans23*60*1000, channelsize)
    resultJson1 = drone1.statistical_result()
    result1 = json.loads(resultJson1)
    print(json.dumps(result1, indent=4))
    num3 += 1
    averageDelayST1[2]+=result1["averageDelay"] #平均延迟
    departureNumST1[2]+=result1["departureNum"] #处理的包的数量
    arrivalNumST1[2] += result1["arrivalNum"] 
    
    timeperiodres3 = timeslotperiod * 60 - timetrans23 #115min
    timepassed3 = 0
    time3round = 0
    while timepassed3 <= timeperiodres3:
        timepassed3 += timeperiod
        time3round += 1
    if timepassed3 >= timeperiodres3:
        timemore3 = timepassed3 - timeperiodres3
        if timeperiod - timemore3 <= workingtime:
            time2round -= 1
            res3 = timeperiod - timemore3
        elif timeperiod - timemore3 > workingtime:#30min
            time2round -= 0
            res3 = 0
            ischarging = 1 
    print("time3round:", time3round)
    for i in range(time3round):
        drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime3, Buffersize, workingtime*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageDelayST1[2]+=result1["averageDelay"] #平均延迟
        departureNumST1[2]+=result1["departureNum"] #处理的包的数量
        arrivalNumST1[2] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
        num3 += 1
    drone1.MM1 = []
    drone1.users = 0
    print(res3)
    if res3 != 0:
        
        drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime3, Buffersize, res3*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        num3 += 1
        print(json.dumps(result1, indent=4))
        averageDelayST1[2]+=result1["averageDelay"] #平均延迟
        departureNumST1[2]+=result1["departureNum"] #处理的包的数量
        arrivalNumST1[2] += result1["arrivalNum"] 
    else: 
        pass
    # averageDelayST1[2] = averageDelayST1[2]
    departureNumST1[2] = departureNumST1[2] + departureNumST1[1]
    arrivalNumST1[2] = arrivalNumST1[2] + arrivalNumST1[1]
# *******************************************************************************  
    # 第四段时间
    print("round4**********************************************************")
    num4 = 0
    if ischarging == 1:
        timetrans34 = timeperiod - res3
        workingtimetrans34 = 0
    if workingtimetrans34 != 0:
        drone1.MM1 = []
        drone1.users = 0
        drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime4, Buffersize, workingtimetrans34*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageDelayST1[3]+=result1["averageDelay"] #平均延迟
        departureNumST1[3]+=result1["departureNum"] #处理的包的数量
        arrivalNumST1[3] += result1["arrivalNum"] 
        num4 += 1
    else:
        pass
    
    timeperiodres4 = timeslotperiod * 60 - timetrans34
    timepassed4 = 0
    time4round = 0
    while timepassed4 <= timeperiodres4:
        timepassed4 += timeperiod
        time4round += 1
    if timepassed4 >= timeperiodres4:
        timemore4 = timepassed4 - timeperiodres4
        if timeperiod - timemore4 < workingtime:
            time4round -= 1
            res4 = timeperiod - timemore4
        elif timeperiod - timemore4 > workingtime:
            time4round -= 0
            res4 = 0
    print("time4round:", time4round)
    for i in range(time4round):
        drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime4, Buffersize, workingtime*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageDelayST1[3]+=result1["averageDelay"] #平均延迟
        departureNumST1[3]+=result1["departureNum"] #处理的包的数量
        arrivalNumST1[3] += result1["arrivalNum"]    #接受的包的数量
        drone1.MM1 = []
        drone1.users = 0
        num4+=1
    drone1.MM1 = []
    drone1.users = 0
    print(res4)
    if res4 != 0:
        drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime4, Buffersize, res4*60*1000, channelsize)
        resultJson1 = drone1.statistical_result()
        result1 = json.loads(resultJson1)
        print(json.dumps(result1, indent=4))
        averageDelayST1[3]+=result1["averageDelay"] #平均延迟
        departureNumST1[3]+=result1["departureNum"] #处理的包的数量
        arrivalNumST1[3] += result1["arrivalNum"]   
        num4 += 1
        drone1.MM1 = []
        drone1.users = 0
    else:
        pass
    
    # averageDelayST1[3] = averageDelayST1[3]
    departureNumST1[3] = departureNumST1[3] + departureNumST1[2]
    arrivalNumST1[3] = arrivalNumST1[3] + arrivalNumST1[2]
    return averageDelayST1, departureNumST1, arrivalNumST1 
# ******************************************************************************* 
# ******************************************************************************* 
# *******************************************************************************
#工况2:以1.5h作为一个运行时间段


averageDelayST2= [0, 0, 0, 0]
departureNumST2 = [0, 0, 0, 0]
arrivalNumST2 = [0, 0, 0, 0]

def timeslot2():
    starttime = 8 # in hour
    timeslotperiod = 3 # in hour
    timeperiod = 90 #in minute
    totaltime = 8 # in hour 
    timeround = 2
    for i in range(timeround):
        drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime1, Buffersize, workingtime*60*1000, channelsize)
        resultJson2 = drone1.statistical_result()
        result2 = json.loads(resultJson2)
        print(json.dumps(result2, indent=4))
        averageDelayST2[0]+=result2["averageDelay"] #平均延迟
        departureNumST2[0]+=result2["departureNum"] #处理的包的数量
        arrivalNumST2[0] += result2["arrivalNum"]  
        drone1.MM1 = []
        drone1.users = 0
        
        
    for i in range(timeround):
        drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime2, Buffersize, workingtime*60*1000, channelsize)
        resultJson2 = drone1.statistical_result()
        result2 = json.loads(resultJson2)
        print(json.dumps(result2, indent=4))
        averageDelayST2[1]+=result2["averageDelay"] #平均延迟
        departureNumST2[1]+=result2["departureNum"] #处理的包的数量
        arrivalNumST2[1] += result2["arrivalNum"]  
        drone1.MM1 = []
        drone1.users = 0
        
    departureNumST2[1] = departureNumST2[1]+departureNumST2[0]
    arrivalNumST2[1] = arrivalNumST2[1]+arrivalNumST2[0]
        
    for i in range(timeround):
        drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime3, Buffersize, workingtime*60*1000, channelsize)
        resultJson2 = drone1.statistical_result()
        result2 = json.loads(resultJson2)
        print(json.dumps(result2, indent=4))
        averageDelayST2[2]+=result2["averageDelay"] #平均延迟
        departureNumST2[2]+=result2["departureNum"] #处理的包的数量
        arrivalNumST2[2] += result2["arrivalNum"]  
        drone1.MM1 = []
        drone1.users = 0
        
    departureNumST2[2] = departureNumST2[1]+departureNumST2[2]
    arrivalNumST2[2] = arrivalNumST2[1]+arrivalNumST2[2]
        
    for i in range(timeround):
        drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime4, Buffersize, workingtime*60*1000, channelsize)
        resultJson2 = drone1.statistical_result()
        result2 = json.loads(resultJson2)
        print(json.dumps(result2, indent=4))
        averageDelayST2[3]+=result2["averageDelay"] #平均延迟
        departureNumST2[3]+=result2["departureNum"] #处理的包的数量
        arrivalNumST2[3] += result2["arrivalNum"]  
        drone1.MM1 = []
        drone1.users = 0
        
    departureNumST2[3] = departureNumST2[3]+departureNumST2[2]
    arrivalNumST2[3] = arrivalNumST2[3]+arrivalNumST2[2]
    
    # for i in averageDelayST2:
    #     i = i/timeround
        
        
    return averageDelayST2, departureNumST2, arrivalNumST2         
       
# ******************************************************************************* 
# ******************************************************************************* 
# *******************************************************************************

averageDelayST3= [0, 0, 0, 0]
departureNumST3 = [0, 0, 0, 0]
arrivalNumST3 = [0, 0, 0, 0]

def timeslot3():
    starttime = 8 # in hour
    timeslotperiod = 3 # in hour
    timeperiod = 90 #in minute
    totaltime = 8 # in hour 
    timeround = 2
    for i in range(timeround):
        drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime1, Buffersize, workingtime*60*1000, channelsize)
        resultJson3 = drone1.statistical_result()
        result3 = json.loads(resultJson3)
        print(json.dumps(result3, indent=4))
        averageDelayST3[0]+=result3["averageDelay"] #平均延迟
        departureNumST3[0]+=result3["departureNum"] #处理的包的数量
        arrivalNumST3[0] += result3["arrivalNum"]  
        drone1.MM1 = []
        drone1.users = 0
        
        
    for i in range(timeround):
        drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime2, Buffersize, workingtime*60*1000, channelsize)
        resultJson3 = drone1.statistical_result()
        result3 = json.loads(resultJson3)
        print(json.dumps(result3, indent=4))
        averageDelayST3[1]+=result3["averageDelay"] #平均延迟
        departureNumST3[1]+=result3["departureNum"] #处理的包的数量
        arrivalNumST3[1] += result3["arrivalNum"]  
        drone1.MM1 = []
        drone1.users = 0
        
    departureNumST3[1] = departureNumST3[1]+departureNumST3[0]
    arrivalNumST3[1] = arrivalNumST3[1]+arrivalNumST3[0]
        
    for i in range(timeround):
        drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime3, Buffersize, workingtime*60*1000, channelsize)
        resultJson3 = drone1.statistical_result()
        result3 = json.loads(resultJson3)
        print(json.dumps(result3, indent=4))
        averageDelayST3[2]+=result3["averageDelay"] #平均延迟
        departureNumST3[2]+=result3["departureNum"] #处理的包的数量
        arrivalNumST3[2] += result3["arrivalNum"]  
        drone1.MM1 = []
        drone1.users = 0
        
    departureNumST3[2] = departureNumST3[1]+departureNumST3[2]
    arrivalNumST3[2] = arrivalNumST3[1]+arrivalNumST3[2]
        
    for i in range(1):
        drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime4, Buffersize, workingtime*60*1000, channelsize)
        resultJson3 = drone1.statistical_result()
        result3 = json.loads(resultJson3)
        print(json.dumps(result3, indent=4))
        averageDelayST3[3]+=result3["averageDelay"] #平均延迟
        departureNumST3[3]+=result3["departureNum"] #处理的包的数量
        arrivalNumST3[3] += result3["arrivalNum"]  
        drone1.MM1 = []
        drone1.users = 0
        
    departureNumST3[3] = departureNumST3[3]+departureNumST3[2]
    arrivalNumST3[3] = arrivalNumST3[3]+arrivalNumST3[2]
    
    # for i in averageDelayST2:
    #     i = i/timeround
        
        
    return averageDelayST3, departureNumST3, arrivalNumST3      




      

averageDelayST1, departureNumST1, arrivalNumST1  = timeslot1()
averageDelayST2, departureNumST2, arrivalNumST2  = timeslot2()
averageDelayST3, departureNumST3, arrivalNumST3   = timeslot3()
#plot the Success Rate
plt.figure(dpi=700)
timeslot = ['8:00-11:00','11:00-14:00','14:00-17:00','17:00-20:00']
#plt.plot(arrivalNo,departures, " ",marker='.', label = 'No. of departures')
plt.plot(timeslot,averageDelayST1, linestyle='-', marker='.', label = 'averageDelay(Strategy 1)')
plt.plot(timeslot, averageDelayST2, linestyle=':', marker='o', label = 'averageDelay(Strategy 2)')
plt.plot(timeslot, averageDelayST3, linestyle='-.', marker='s', label = 'Success Rate(Strategy 3')
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
plt.plot(timeslot, arrivalNumST1, linestyle='-', marker='.', label = 'Arrival Number(Strategy 1)')
plt.plot(timeslot, arrivalNumST2, linestyle=':', marker='o', label = 'Arrival Number(Strategy 2)')
plt.plot(timeslot, arrivalNumST3, linestyle='-.', marker='s', label = 'Arrival Number(Strategy 3')
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
plt.plot(timeslot, departureNumST1, linestyle='-', marker='.', label = 'Departure Number(Strategy 1)')
plt.plot(timeslot, departureNumST2, linestyle=':', marker='o', label = 'Departure Number(Strategy 2)')
plt.plot(timeslot, departureNumST3, linestyle='-.', marker='s', label = 'Departure Number(Strategy 3')
plt.xlabel('Time Slots')
plt.ylabel('Departure Number')
plt.title('Departure Number vs Time Slots')
plt.grid(linestyle=':')
plt.legend()
#plt.savefig("Departure Number.png", dpi=300)
plt.show()      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    