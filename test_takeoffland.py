__author__ = 'varribas'

import jderobot
import easyiceconfig as EasyIce

import sys, traceback, time


ic = EasyIce.initialize(sys.argv)

try:
    advPrx = ic.stringToProxy("Extra:default -h localhost -p 9000")
    advPrx = jderobot.ArDroneExtraPrx.checkedCast(advPrx);

    print "Take off!"
    advPrx.takeoff()

    time.sleep(5)

    print "Land!"
    advPrx.land()

except:
    traceback.print_exc()

ic.shutdown()

