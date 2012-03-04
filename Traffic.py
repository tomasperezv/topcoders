# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=586
'''
import math

class Traffic():
    
    DIV_LENGTH = 150
    
    def getTimeToDest(self, speed):
        return float(float(self.DIV_LENGTH) / float(speed))

    def isRed(self, time, lightTime):
        return (time/lightTime) % 2 <> 0
    
    def time(self, lights, speed):
        totalTime = 0
        at = 0
        pendingDistance = 0
        while( len(lights) > 0 ):
            currentLightTime = lights[0]
            timeToDest = self.getTimeToDest(speed)
            if timeToDest+at == currentLightTime:
                at = 0
                totalTime+=currentLightTime
            elif timeToDest+at > currentLightTime:
                if self.isRed(timeToDest+at, currentLightTime):
                    if (timeToDest+at)%currentLightTime == 0:
                        totalTime+=currentLightTime
                    else:
                        totalTime+=(timeToDest+at)%currentLightTime
                at = 0
            else:
                at+=timeToDest
            totalTime+= timeToDest
            lights.pop(0)
        totalTime+=self.getTimeToDest(speed)
        return int(math.ceil(totalTime))

def main():
    traffic = Traffic()
    print traffic.time([10,10,10], 30)
    print traffic.time([10,10,10], 20)
    print traffic.time([10,20,30], 20)
    print traffic.time([10,11,12,13,14,15], 5)
    
if __name__ == '__main__':
    main()
