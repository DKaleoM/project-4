"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""



#imports for what we need to test
import arrow
from acp_times import open_time, close_time

#helper functions to make test cases shorter to write
def format_time(time):
    return time.format('YYYY-MM-DDTHH:mm')

def assert_equal(actual, expected, msg = "unknown"):
    assert actual == expected, "Expected: " + str(expected) + " but got " + str(actual) + " at " + msg

def assert_time_equal(actual, expected, msg = "unknown"):
    assert_equal(format_time(actual),format_time(expected), msg)

def assert_time_correct(checkpointDist, brevetDist, startTimeStr, correctTimeStr, timeFunc, msg = "unknown"):
    start_time = arrow.get(startTimeStr,"YYYY-MM-DDTHH:mm")

    correct_time = arrow.get(correctTimeStr,"YYYY-MM-DDTHH:mm")

    returned_time = timeFunc(checkpointDist, brevetDist, start_time)

    assert_time_equal(returned_time, correct_time, msg)

import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)



##############
#
#Test Set 1: Basic 300km brevet
# Single brevet with times generated using the online calculator
# Bevet dist: 300, Start Time: 2025-12-12T09:00
#
##############


#test open time of checkpoint 0km (brevet dist: 300km)

def test_0_brevet_300_0_open():
    brevetDist = 300
    startDate = "2025-12-12T09:00"
    dist = 0
    openTime = "2025-12-12T09:00"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 0km (brevet dist: 300km)

def test_1_brevet_300_0_close():
    brevetDist = 300
    startDate = "2025-12-12T09:00"
    dist = 0
    closeTime = "2025-12-12T10:00"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")


#test open time of checkpoint 100km (brevet dist: 300km)

def test_2_brevet_300_100_open():
    brevetDist = 300
    startDate = "2025-12-12T09:00"
    dist = 100
    openTime = "2025-12-12T11:56"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 100km (brevet dist: 300km)

def test_3_brevet_300_100_close():
    brevetDist = 300
    startDate = "2025-12-12T09:00"
    dist = 100
    closeTime = "2025-12-12T15:40"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")


#test open time of checkpoint 150km (brevet dist: 300km)

def test_4_brevet_300_150_open():
    brevetDist = 300
    startDate = "2025-12-12T09:00"
    dist = 150
    openTime = "2025-12-12T13:25"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 150km (brevet dist: 300km)

def test_5_brevet_300_150_close():
    brevetDist = 300
    startDate = "2025-12-12T09:00"
    dist = 150
    closeTime = "2025-12-12T19:00"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")


#test open time of checkpoint 225km (brevet dist: 300km)

def test_6_brevet_300_225_open():
    brevetDist = 300
    startDate = "2025-12-12T09:00"
    dist = 225
    openTime = "2025-12-12T15:40"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 225km (brevet dist: 300km)

def test_7_brevet_300_225_close():
    brevetDist = 300
    startDate = "2025-12-12T09:00"
    dist = 225
    closeTime = "2025-12-13T00:00"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")


#test open time of checkpoint 280km (brevet dist: 300km)

def test_8_brevet_300_280_open():
    brevetDist = 300
    startDate = "2025-12-12T09:00"
    dist = 280
    openTime = "2025-12-12T17:23"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 280km (brevet dist: 300km)

def test_9_brevet_300_280_close():
    brevetDist = 300
    startDate = "2025-12-12T09:00"
    dist = 280
    closeTime = "2025-12-13T03:40"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")


#test open time of checkpoint 330km (brevet dist: 300km)

def test_10_brevet_300_330_open():
    brevetDist = 300
    startDate = "2025-12-12T09:00"
    dist = 330
    openTime = "2025-12-12T18:00"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 330km (brevet dist: 300km)

def test_11_brevet_300_330_close():
    brevetDist = 300
    startDate = "2025-12-12T09:00"
    dist = 330
    closeTime = "2025-12-13T05:00"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")




##############
#
#Test Set 2: Basic 1000km brevet
# Single brevet with times generated using the online calculator
# Bevet dist: 1000, Start Time: 2035-05-06T15:00
#
##############


#test open time of checkpoint 0km (brevet dist: 1000km)

def test_12_brevet_1000_0_open():
    brevetDist = 1000
    startDate = "2035-05-06T15:00"
    dist = 0
    openTime = "2035-05-06T15:00"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 0km (brevet dist: 1000km)

def test_13_brevet_1000_0_close():
    brevetDist = 1000
    startDate = "2035-05-06T15:00"
    dist = 0
    closeTime = "2035-05-06T16:00"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")


#test open time of checkpoint 300km (brevet dist: 1000km)

def test_14_brevet_1000_300_open():
    brevetDist = 1000
    startDate = "2035-05-06T15:00"
    dist = 300
    openTime = "2035-05-07T00:00"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 300km (brevet dist: 1000km)

def test_15_brevet_1000_300_close():
    brevetDist = 1000
    startDate = "2035-05-06T15:00"
    dist = 300
    closeTime = "2035-05-07T11:00"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")


#test open time of checkpoint 600km (brevet dist: 1000km)

def test_16_brevet_1000_600_open():
    brevetDist = 1000
    startDate = "2035-05-06T15:00"
    dist = 600
    openTime = "2035-05-07T09:48"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 600km (brevet dist: 1000km)

def test_17_brevet_1000_600_close():
    brevetDist = 1000
    startDate = "2035-05-06T15:00"
    dist = 600
    closeTime = "2035-05-08T07:00"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")


#test open time of checkpoint 900km (brevet dist: 1000km)

def test_18_brevet_1000_900_open():
    brevetDist = 1000
    startDate = "2035-05-06T15:00"
    dist = 900
    openTime = "2035-05-07T20:31"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 900km (brevet dist: 1000km)

def test_19_brevet_1000_900_close():
    brevetDist = 1000
    startDate = "2035-05-06T15:00"
    dist = 900
    closeTime = "2035-05-09T09:15"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")


#test open time of checkpoint 1100km (brevet dist: 1000km)

def test_20_brevet_1000_1100_open():
    brevetDist = 1000
    startDate = "2035-05-06T15:00"
    dist = 1100
    openTime = "2035-05-08T00:05"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 1100km (brevet dist: 1000km)

def test_21_brevet_1000_1100_close():
    brevetDist = 1000
    startDate = "2035-05-06T15:00"
    dist = 1100
    closeTime = "2035-05-09T18:00"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")




##############
#
#Test Set 3: short times
# Generated using the online calculator, to test the edge cases under 60km.
# Bevet dist: 200, Start Time: 2035-07-06T12:00
#
##############


#test open time of checkpoint 0km (brevet dist: 200km)

def test_22_brevet_200_0_open():
    brevetDist = 200
    startDate = "2035-07-06T12:00"
    dist = 0
    openTime = "2035-07-06T12:00"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 0km (brevet dist: 200km)

def test_23_brevet_200_0_close():
    brevetDist = 200
    startDate = "2035-07-06T12:00"
    dist = 0
    closeTime = "2035-07-06T13:00"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")


#test open time of checkpoint 20km (brevet dist: 200km)

def test_24_brevet_200_20_open():
    brevetDist = 200
    startDate = "2035-07-06T12:00"
    dist = 20
    openTime = "2035-07-06T12:35"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 20km (brevet dist: 200km)

def test_25_brevet_200_20_close():
    brevetDist = 200
    startDate = "2035-07-06T12:00"
    dist = 20
    closeTime = "2035-07-06T14:00"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")


#test open time of checkpoint 40km (brevet dist: 200km)

def test_26_brevet_200_40_open():
    brevetDist = 200
    startDate = "2035-07-06T12:00"
    dist = 40
    openTime = "2035-07-06T13:11"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 40km (brevet dist: 200km)

def test_27_brevet_200_40_close():
    brevetDist = 200
    startDate = "2035-07-06T12:00"
    dist = 40
    closeTime = "2035-07-06T15:00"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")


#test open time of checkpoint 50km (brevet dist: 200km)

def test_28_brevet_200_50_open():
    brevetDist = 200
    startDate = "2035-07-06T12:00"
    dist = 50
    openTime = "2035-07-06T13:28"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 50km (brevet dist: 200km)

def test_29_brevet_200_50_close():
    brevetDist = 200
    startDate = "2035-07-06T12:00"
    dist = 50
    closeTime = "2035-07-06T15:30"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")


#test open time of checkpoint 60km (brevet dist: 200km)

def test_30_brevet_200_60_open():
    brevetDist = 200
    startDate = "2035-07-06T12:00"
    dist = 60
    openTime = "2035-07-06T13:46"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 60km (brevet dist: 200km)

def test_31_brevet_200_60_close():
    brevetDist = 200
    startDate = "2035-07-06T12:00"
    dist = 60
    closeTime = "2035-07-06T16:00"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")


#test open time of checkpoint 70km (brevet dist: 200km)

def test_32_brevet_200_70_open():
    brevetDist = 200
    startDate = "2035-07-06T12:00"
    dist = 70
    openTime = "2035-07-06T14:04"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 70km (brevet dist: 200km)

def test_33_brevet_200_70_close():
    brevetDist = 200
    startDate = "2035-07-06T12:00"
    dist = 70
    closeTime = "2035-07-06T16:40"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")




##############
#
#Test Set 4: times over brevet dist
# Tests to make sure times for distances over the brevet dist are same as at the brevet dist.
# Bevet dist: 200, Start Time: 2035-07-06T12:00
#
##############


#test open time of checkpoint 200km (brevet dist: 200km)

def test_34_brevet_200_200_open():
    brevetDist = 200
    startDate = "2035-07-06T12:00"
    dist = 200
    openTime = "2035-07-06T17:53"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 200km (brevet dist: 200km)

def test_35_brevet_200_200_close():
    brevetDist = 200
    startDate = "2035-07-06T12:00"
    dist = 200
    closeTime = "2035-07-07T01:30"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")


#test open time of checkpoint 205km (brevet dist: 200km)

def test_36_brevet_200_205_open():
    brevetDist = 200
    startDate = "2035-07-06T12:00"
    dist = 205
    openTime = "2035-07-06T17:53"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 205km (brevet dist: 200km)

def test_37_brevet_200_205_close():
    brevetDist = 200
    startDate = "2035-07-06T12:00"
    dist = 205
    closeTime = "2035-07-07T01:30"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")


#test open time of checkpoint 212km (brevet dist: 200km)

def test_38_brevet_200_212_open():
    brevetDist = 200
    startDate = "2035-07-06T12:00"
    dist = 212
    openTime = "2035-07-06T17:53"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 212km (brevet dist: 200km)

def test_39_brevet_200_212_close():
    brevetDist = 200
    startDate = "2035-07-06T12:00"
    dist = 212
    closeTime = "2035-07-07T01:30"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")


#test open time of checkpoint 222km (brevet dist: 200km)

def test_40_brevet_200_222_open():
    brevetDist = 200
    startDate = "2035-07-06T12:00"
    dist = 222
    openTime = "2035-07-06T17:53"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 222km (brevet dist: 200km)

def test_41_brevet_200_222_close():
    brevetDist = 200
    startDate = "2035-07-06T12:00"
    dist = 222
    closeTime = "2035-07-07T01:30"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")




##############
#
#Test Set 5: decimal distances
# Tests to make sure distances are rounded the same as the online calculator https://rusa.org/octime_acp.html
# Bevet dist: 200, Start Time: 2050-01-01T00:00
#
##############


#test open time of checkpoint 99km (brevet dist: 200km)

def test_42_brevet_200_99_open():
    brevetDist = 200
    startDate = "2050-01-01T00:00"
    dist = 99
    openTime = "2050-01-01T02:55"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 99km (brevet dist: 200km)

def test_43_brevet_200_99_close():
    brevetDist = 200
    startDate = "2050-01-01T00:00"
    dist = 99
    closeTime = "2050-01-01T06:36"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")


#test open time of checkpoint 99.4km (brevet dist: 200km)

def test_44_brevet_200_99_4_open():
    brevetDist = 200
    startDate = "2050-01-01T00:00"
    dist = 99.4
    openTime = "2050-01-01T02:55"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 99.4km (brevet dist: 200km)

def test_45_brevet_200_99_4_close():
    brevetDist = 200
    startDate = "2050-01-01T00:00"
    dist = 99.4
    closeTime = "2050-01-01T06:36"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")


#test open time of checkpoint 99.6km (brevet dist: 200km)

def test_46_brevet_200_99_6_open():
    brevetDist = 200
    startDate = "2050-01-01T00:00"
    dist = 99.6
    openTime = "2050-01-01T02:56"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 99.6km (brevet dist: 200km)

def test_47_brevet_200_99_6_close():
    brevetDist = 200
    startDate = "2050-01-01T00:00"
    dist = 99.6
    closeTime = "2050-01-01T06:40"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")


#test open time of checkpoint 100km (brevet dist: 200km)

def test_48_brevet_200_100_open():
    brevetDist = 200
    startDate = "2050-01-01T00:00"
    dist = 100
    openTime = "2050-01-01T02:56"

    return assert_time_correct(dist, brevetDist, startDate, openTime, open_time, "open time of checkpoint: "+str(dist)+"km")


#test close time of checkpoint 100km (brevet dist: 200km)

def test_49_brevet_200_100_close():
    brevetDist = 200
    startDate = "2050-01-01T00:00"
    dist = 100
    closeTime = "2050-01-01T06:40"

    return assert_time_correct(dist, brevetDist, startDate, closeTime, close_time, "close time of checkpoint: "+str(dist)+"km")

