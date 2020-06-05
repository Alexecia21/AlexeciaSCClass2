#class libraries for bluetooth application

import time #<-- 1st party class library

from bluetooth.ble import BeaconService #<-- 3rd party module (someone from the internet who created class library)

#instantiate the object 
service = BeaconService() #<-- create an instance object of class library

service.start_advertising("1, 1, 200") #<-- advertise the UUID and different ports for spoofing devices

time.sleep(15) #<--every fifteen seconds 
service.stop_advertise() #<-- stop service 

print("Done ") #<--print when done 