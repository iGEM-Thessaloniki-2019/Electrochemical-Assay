import serial
import numpy
import matplotlib.pyplot as plt
import pandas as pd
from drawnow import *

Voltage= []
Time=[]
cnt=0
f=1
com=input("Please enter com port number: ")
while f==1:
    try:
        ser = serial.Serial('COM'+com,115200)
        f=0
    except:
        com=input("Please enter com port number only: ")
        f=1
plt.ion()

def makeFig():
    plt.title('Sensor Voltage')
    plt.xlabel('Time(s)')
    plt.ylabel('Voltage(V)')
    plt.plot(Time,Voltage, 'ro-',label=' ')
    plt.legend().remove()

while True:
    while (ser.inWaiting()==0):
        pass
    Voltage.append(float(int(1000*float(str(ser.readline()).split('\\')[0].split('\'')[1])/310))/1000)
    Time.append(cnt*2)
    if plt.fignum_exists(1) or cnt==0:
        drawnow(makeFig)
    else:
        break
    plt.pause(.01)
    cnt=cnt+1
print (Voltage)
a=pd.DataFrame(list(zip(Time,Voltage)))
path=input("Please enter file name to save data: ")+".csv"
a.to_csv(path,index=False,header=False)
