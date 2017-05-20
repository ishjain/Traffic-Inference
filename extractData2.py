from pandas import read_csv
import numpy as np
import array
from math import sin, cos, sqrt, atan2, radians
import datetime as dt

busData = read_csv('MTA-Bus-Time_.2014-09-04.txt', delimiter='\t')
print busData.shape

M15D = [[40.731984, -73.987630, 40.728659, -73.985313],[40.728610, -73.990015, 40.725402, -73.988037]]#2 segments
M8R = [[40.730960, -73.992909, 40.728553, -73.987824],[40.728634, -73.987545, 40.726658, -73.983253]] 
'''
# syntex [TL-lat,TL-lon, BR-lat, BR-lon] TopLeft, BottomRight lattitude longitude 
# Syntex M15D = bus # M15 going down on 2nd ave
'''
def extractbus(route_id, loc, name):
	for segment in range(len(loc)):#loc=location list
		if loc[segment][2]<lat and lat<loc[segment][0] and  loc[segment][1]<lon and lon<loc[segment][3]:
			dataPoint = [busData.time_received[i], busData.latitude[i],busData.longitude[i],name,segment]
			return datapoint

def Speed(LatLonData):
	lat1 = radians(LatLonData[0][0])
	lon1 = radians(LatLonData[0][1])
	lat2 = radians(LatLonData[1][0])
	lon2 = radians(LatLonData[1][1])
	time1 = LatLonData[2][11:19]
	time2 = LatLonData[3][11:19]
	dlon = lon2-lon1
	dlat = lat2-lat1
	R = 6373.0
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	distance = R * c*1000 #meters
	
	start = dt.datetime.strptime(time1, '%H:%M:%S')
	end = dt.datetime.strptime(time2, '%H:%M:%S')
	diff = end-start
	time = diff.seconds #seconds
	speed = distance/time *2.23694 #mph
	return speed
	#return distance


data=[];
index=0
state = 0
speed1=0

speed2=0
count1=0
count2=0
bus_id = 0
#time0 = busData.time_received[551][11:19] #703 is special number for bus M15
#print time0
time0 = dt.datetime.strptime('04:00:00', '%H:%M:%S') # Set initial time for reference.
#time00 = busData.time_received[30][11:19]
#print time00
#time1 = dt.datetime.strptime(time00, '%H:%M:%S')
#time0=time1-time0

print time0#.seconds

for i in range(2000000):#busData.size):
	lat = busData.latitude[i]
	lon =  busData.longitude[i]
	if busData.inferred_route_id[i]== 'MTA NYCT_M15': #Change Bus ID here(need to comment/uncom one more place)
		
		#data.append(extractbus('MTA NYCT_M15',M15D,'M15D'))
		#data.append(extractbus('MTA NYCT_M15',M15D,'M15D'))
		#datapoint = extractbus('MTA NYCT_M15',M15D,'M15D')
		#print datapoint
		
		#bus15[index] = i
		index=index+1		
		if busData.inferred_direction_id[i] ==1.0: #Down
			#print lat
			#print lon
			#print busData.time_received[i]
			for segment in range(2):
				if M15D[segment][0]>lat and lat>M15D[segment][2] and M15D[segment][1]<lon and lon<M15D[segment][3]:
				#if M8R[segment][0]>lat and lat>M8R[segment][2] and M8R[segment][1]<lon and lon<M8R[segment][3]:	
					#data.append([busData.time_received[i], busData.latitude[i],busData.longitude[i],'M15D',segment])
					#print segment, busData.time_received[i], busData.vehicle_id[i], busData.latitude[i],busData.longitude[i]
					#print lat, ",", lon
					
					
					if busData.vehicle_id[i] == bus_id:
						state = 1
						LatLon2 = [busData.latitude[i],busData.longitude[i]]
						time2 = busData.time_received[i]
						speedData = Speed([LatLon1,LatLon2,time1,time2])
						if speedData<5:
							speedData=0 #Filter small or close to zero speeds
						if segment==0:
							speed1 = speed1+ speedData
							count1=count1+1
						if segment==1:
							speed2 = speed2+ speedData
							count2=count2+1
						#print segment, busData.time_received[i], busData.vehicle_id[i], speed
						LatLon1 = LatLon2
						time1 = time2
						
					else :
						bus_id = busData.vehicle_id[i]
						
						LatLon1 = [busData.latitude[i],busData.longitude[i]]
						time1 = busData.time_received[i]
						time1temp = time1[11:19]
						#print time1, 'at index', i
						time1temp = dt.datetime.strptime(time1temp, '%H:%M:%S')
						#print time1temp
						time = time1temp-time0
						#print time
						time=int(time.seconds/60)
						if state==1:
							if count1!=0: 
								speed1=speed1/count1 #Calculate average speed
							if count2!=0:
								speed2=speed2/count2
							#print '0',  busData.time_received[i], busData.vehicle_id[i], time, speed1
							#print '1',  busData.time_received[i], busData.vehicle_id[i], time, speed2
							print '0',  time, speed1 ''' Finally printing the average speed of segments'''
							print '1', time, speed2
						count1=0
						count2=0
						speed1=0
						speed2=0 # speed of segment 2
						state = 0;
						#print 'yeah',i
					
		'''			
		elif busData.inferred_direction_id[i] ==0.0: #UP
			for segment in range(3):
				if M15U[segment][0]>lat and lat>M15U[segment][2] and M15U[segment][1]<lon and lon<M15U[segment][3]:	
					print segment, busData.time_received[i], busData.vehicle_id[i]
					data.append([busData.time_received[i], busData.latitude[i],busData.longitude[i],'M15U',segment])
		'''
#print data
		




