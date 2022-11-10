#task1中具体要求如下：
#  单个无人机，单个BS，电源为电池供电，不带太阳能板

'''
version A:
in this area the traffic typically features two peakperiods:
one in the morning 
one in the afternoon after lunchtime,
whereasas the evening approaches the traffic rate tends to decrease.
'''
'''
返回值包括：
1.通过无人机接受到的包的总数
2.无人机处理的包的总数
3.无人机处理的包的平均延迟
'''
import json
import ClassDrone
import matplotlib.pyplot as plt
from timeslot_task1 import timeslot1, timeslot2, timeslot3

Buffersize = 10
channelsize = 1
SimTime = 25*60*1000 #drone can only work 25min
'''
考虑version A的工况：
1.早上有高峰期 8:00-12:00
2.午饭之后有高峰期 12:00-16:00
3.晚上有低谷期 16:00-20:00
'''
#for different time slot:
# 1. morning : 8:00-12:00
# 2. afternoon : 12:00-16:00
# 3. evening : 16:00-20:00

averageDelayST1= []
departureNumST1 = []
arrivalNumST1 = []

'''
strategy 1:
work for 25min,and charge for 60min, even for low load
strategy 2:
set 120min as a time slot,work for 25min,and charge for 60min
strategy 3:
work for 25min,and charge for 60min during high load only
8:00-8:25,8:25-9:25,9:25-9:50,9:50-10:50,10:50-11:15,11:15-12:15,12:15-12:40,12:40-13:40,13:40-14:05,14:05-15:05,15:05-15:30,15:30-16:30,16:30-16:55,16:55-17:55,17:55-18:20,18:20-19:20,19:20-19:45,19:45-20:45
'''

#strategy 1
ServiceTime = 10
ArrivalTime = 11
Buffersize = 10
channelsize = 2
timeworkinghigh, timeworkinglow = timeslot1()
drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime, Buffersize, timeworkinghigh/6, channelsize)
drone1.users = 0
drone1.MM1 = []
resultJson1 = drone1.statistical_result()
result1 = json.loads(resultJson1)
print(json.dumps(result1, indent=4))
averageDelayST1.append(result1["averageDelay"]) #平均延迟
departureNumST1.append(result1["departureNum"]) #处理的包的数量
arrivalNumST1.append(result1["arrivalNum"])     #接受的包的数量

ServiceTime = 10
ArrivalTime = 10
drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime, Buffersize, timeworkinghigh/2, channelsize)
drone1.users = 0
drone1.MM1 = []
resultJson2 = drone1.statistical_result()
result2 = json.loads(resultJson2)
print(json.dumps(result2, indent=4))
averageDelayST1.append(result2["averageDelay"]) #平均延迟
departureNumST1.append(result2["departureNum"]) #处理的包的数量
arrivalNumST1.append(result2["arrivalNum"])     #接受的包的数量

ServiceTime = 10
ArrivalTime = 20
drone1 = ClassDrone.Drone(ServiceTime, ArrivalTime,  Buffersize, timeworkinglow, channelsize)
drone1.users = 0
drone1.MM1 = []
resultJson3 = drone1.statistical_result()
result3 = json.loads(resultJson3)
print(json.dumps(result3, indent=4))
averageDelayST1.append(result3["averageDelay"]) #平均延迟
departureNumST1.append(result3["departureNum"]) #处理的包的数量
arrivalNumST1.append(result3["arrivalNum"])     #接受的包的数量

timeslot = ['high load1','high load2','low load']

#plot the Success Rate
plt.figure(dpi=300)
#plt.plot(arrivalNo,departures, " ",marker='.', label = 'No. of departures')
plt.plot(timeslot,averageDelayST1, linestyle='-', marker='.', label = 'averageDelay(Strategy 1)')
# plt.plot(timeSlot, successRateST2, linestyle=':', marker='o', label = 'Success Rate(Strategy 2)')
# plt.plot(timeSlot, successRateST3, linestyle='-.', marker='s', label = 'Success Rate(Strategy 3')
plt.xlabel('Time Slots')
plt.ylabel('Average Delay')
plt.title('Average Delay vs Time Slots')
plt.grid(linestyle=':')
plt.legend()
#plt.savefig("successRate.png", dpi=300)
plt.show()

#plot the No. of arrivals
plt.figure(dpi=300)
#plt.plot(arrivalNo,departures, " ",marker='.', label = 'No. of departures')
plt.plot(timeslot, arrivalNumST1, linestyle='-', marker='.', label = 'Arrival Number(Strategy 1)')
# plt.plot(timeSlot, arrivalNumST2, linestyle=':', marker='o', label = 'Arrival Number(Strategy 2)')
# plt.plot(timeSlot, arrivalNumST3, linestyle='-.', marker='s', label = 'Arrival Number(Strategy 3')
plt.xlabel('Time Slots')
plt.ylabel('Arrival Number')
plt.title('Arrival Number vs Time Slots')
plt.grid(linestyle=':')
plt.legend()
#plt.savefig("Arrival Number.png", dpi=300)
plt.show()











