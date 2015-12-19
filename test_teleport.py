__author__ = 'varribas'

import jderobot
import easyiceconfig as EasyIce

import sys, traceback


ic = EasyIce.initialize(sys.argv)

try:
    posePrx = ic.stringToProxy("Pose3D:default -h localhost -p 9901")
    posePrx = jderobot.Pose3DPrx.checkedCast(posePrx);

    print posePrx.getPose3DData();

    pose = jderobot.Pose3DData(0,0,3, 1,0,0,0)
    posePrx.setPose3DData(pose);

    print posePrx.getPose3DData();

except:
    traceback.print_exc()

ic.shutdown()

