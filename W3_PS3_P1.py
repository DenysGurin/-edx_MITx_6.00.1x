#-*-coding:utf8;-*-
#qpy:2
#qpy:console
import math
#print "This is console module"
def f(x):
    return 10*math.e**(math.log(0.5)/5.27*x)

def radiationExposure(start, stop, step):
    exposure = 0
    time = start
    while time < stop:
        exposure += f(time)*step
        time += step
        #print time, exposure
    return exposure

def radiationExposureRecur(start, stop, step):
    if start == stop:
        return 0
    else:
        return f(start)*step+radiationExposureRecur(start+step, stop, step)

    
print radiationExposure(0,5,1)
#print radiationExposureRecur(0,5,1)
print radiationExposure(5,11,1)
print radiationExposure(0,11,1)

