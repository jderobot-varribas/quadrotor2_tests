__author__ = 'varribas'

import jderobot
import easyiceconfig as EasyIce

import sys, traceback, time


ic = EasyIce.initialize(sys.argv)

try:
    advPrx = ic.stringToProxy("Extra:default -h localhost -p 9901")
    advPrx = jderobot.ArDroneExtraPrx.checkedCast(advPrx);

    advPrx.takeoff()
    time.sleep(3)

    posePrx = ic.stringToProxy("Pose3D:default -h localhost -p 9901")
    posePrx = jderobot.Pose3DPrx.checkedCast(posePrx);

    pose_altPrx = ic.stringToProxy("Pose3D_altitude:default -h localhost -p 9901")
    pose_altPrx = jderobot.Pose3DPrx.checkedCast(pose_altPrx);

    print posePrx.getPose3DData()

    pose = jderobot.Pose3DData(0,0,5,1, 1,0,0,0)
    posePrx.setPose3DData(pose)
    time.sleep(1)

    print "real:", posePrx.getPose3DData().z
    print "sonar:", pose_altPrx.getPose3DData().z

    advPrx.land()

except:
    traceback.print_exc()

ic.shutdown()

