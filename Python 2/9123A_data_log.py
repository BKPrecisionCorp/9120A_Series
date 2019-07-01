# BK PRECISION
# Sample how to log data to a text document

import visa
from datetime import datetime


try:
    resourceM = visa.ResourceManager()
    resourceM.list_resources()
    
    power_supply = resourceM.open_resource('ASRL1::INSTR')
    power_supply.baud_rate = 9600
    
    power_supply.timeout =  5000

    print power_supply.ask('*IDN?')
 
    filename = 'C:\Users\eamezquita\Documents\Current Projects\python data\9123A_data.txt'
    
    my_log = open(filename, 'w')
    my_log.truncate()
    
    my_log.write(power_supply.ask('*IDN?'))
    my_log.write('\n')
    count = 0
    while (count < 9):
        
            my_log.write(str(datetime.now()))
            my_log.write('\n')
            
            my_log.write('VOLTAGE='+ power_supply.ask('VOLT?') )
            my_log.write('CURRENT='+ power_supply.ask('CURR?'))
            my_log.write('\n')
       
        
            count = count + 1
           
    print 'close instrument connection'

 
finally:
    my_log.close()
    #perforesourceM clean up operations
    print 'complete'
