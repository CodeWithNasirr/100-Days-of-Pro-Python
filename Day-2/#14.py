# Calculate the angle between the hour hand and minute hand.
# Note: There can be two angles between hands; we need to print a minimum of two. Also, we need to print the floor of the final result angle. For example, if the final angle is 10.61, we need to print 10.


# Firstyle You Have to calculate the hour & minute Angle 
# Hour = 12(hours)/360=30 Angle
# Minute = 60/360 = 6

# Calculate the Position of Each Hand:
# For the hour hand angle : = (hour%30) * 30 + (minute/60) * 30
# For the minute hand angle : = minute/6 

# Calculate the Difference Between the Two Angles: AngleDiff... = hour_hand angle - minute_hand angle

# Find the Minimum of the Two Possible Angles: minmum_of_two_angle = min(AngleDiff, AngleDiff-360)

import math
def Calculate_Angle(hour,minute):
    # Calculate the Position of Each Hand:
    hour_angle= (hour%30) * 30 + (minute/60)*30
    minute_angle=minute * 6
    # Calculate the Difference Between the Two Angles
    Angle_diff=abs(hour_angle - minute_angle)
    # Find the Minimum of the Two Possible Angles:
    minmum_of_two_angle =min(Angle_diff,360 - Angle_diff)
    return minmum_of_two_angle

hour=int(input('Enter Hour: '))
Minute=int(input('Enter Minute: '))
result=Calculate_Angle(hour,Minute)
print(f"{hour} Hour & {Minute} Angle is: {result}")

