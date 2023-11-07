"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

def shift_time_nearest_min(time, hours):
    #round to nearest minute
    total_minutes = round(hours*60)


    #copy time
    newTime = arrow.get(time)

    #add minutes to the time
    newTime = newTime.shift(minutes=total_minutes)
    
    return newTime

#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """

    """
    Any checkpoints after the brevet distance are calculated differently:
    opening time is calculated based on nominal brevit distance in the calculation table
    """
    #online calculator that we are trying to replicate rounds km values
    #so we will as well.
    current_dist = round(control_dist_km)

    
    #this is the opening time, so we must treat distances over the brevit distance as equal
    current_dist = min(current_dist, brevet_dist_km)

    #initialize hours at zero
    current_time_hours = 0
    
    #the ordered pairs are of min distance and max speed in class (since opening timeS)
    #note that min distance is EXCLUSIVE as it belongs to the next class over
    #so for example, 1000 is the over 1000 class in the table from the page (listed as 1000-1300) 
    openingTimeSpeeds = [(1000, 26), (600, 28), (400, 30), (200, 32), (0, 34)]
        
    #iterate through each speed, and calculate the time added by that portion
    for speed in openingTimeSpeeds:
        minDist = speed[0]
        maxSpeed = speed[1]
        
        
        distOverNext = current_dist - minDist 
        #if not, this category doesn't apply and just do the next one
        if distOverNext > 0:
            #update current dist so it only has the stuff left
            #to account for when entering the next item
            current_dist -= distOverNext

            #units work out, km and km/hr
            #add it to the current running total of time
            current_time_hours += distOverNext / maxSpeed

    
    return shift_time_nearest_min(brevet_start_time,current_time_hours)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """

    """
    Rules: first checkpoint closes an hour after the race starts.
    Closing time control for checkpoints in the first 60km is based on 20km/hr, plus one hour

    Any checkpoints after the brevet distance are calculated differently:
    closing time is fixed based on the nominal brevet distance
    
    """

    #the ordered pairs are of min distance and min speed
    #note that min distance is EXCLUSIVE as it belongs to the next class over
    #so for example, 1000 is the over 1000 class in the table from the page (listed as 1000-1300) 
    closingTimeSpeeds = [(1000, 13.333), (600, 11.428), (400, 15), (200, 15), (0, 15)]

    #closing times are in hours
    #taken from wikipedia: https://en.wikipedia.org/wiki/Randonneuring#Time_limits
    #unlike the above table, this is obviously inclusive as the values are always exact
    raceClosingTimes = {1000: 75, 600:40, 400:27, 300:20, 200:13.5}

    #TODO: round or truncate here?
    #specs say to truncate but the online calculator is rounding... 
    current_dist = round(control_dist_km)

    current_time_hours = 0

    #special case where this is closing checkpoint
    #so we use race time limit for the time it closes
    if current_dist >= brevet_dist_km:
        current_time_hours = raceClosingTimes[brevet_dist_km]

    #special case for first 60km, to ensure checkpoint doesn't close before the race start closes
    elif current_dist <= 60:
        #use 20km/hr as defined in specs
        current_time_hours = current_dist/20

        #extra hour as defined in specs
        current_time_hours += 1

    #normal case, where we use the different speeds for each amount over the previous dist
    #as described in the specs
    else:
        #iterate through each speed, and calculate the time added by that portion
        for speed in closingTimeSpeeds:
            minDist = speed[0]
            minSpeed = speed[1]
            
            distOverNext = current_dist - minDist 
            #if not, this category doesn't apply and just do the next one
            if distOverNext > 0:
                #update current dist so it only has the stuff left
                #to account for when entering the next item
                current_dist -= distOverNext

                #units work out, km and km/hr
                #add it to the current running total of time
                current_time_hours += distOverNext / minSpeed
    
    
    return shift_time_nearest_min(brevet_start_time,current_time_hours)
