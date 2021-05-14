#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---------------------------------------------------------------------
SCRIPT TO CALCULATE THE MINIMUM AND IDEAL SHUTTER SPEEDS, AT A GIVEN
FLIGHT SPEED, FOR THE PLANNING OF AN AERIAL IMAGING SURVEY
---------------------------------------------------------------------

Version: 1.0.0 (13/05/2021)

Author: Benoît SMETS
       (Royal Museum for Central Africa / Vrije Universiteit Brussel)

Citation:
    Smets, B., 2021. Script to calculate the minimum and ideal shutter
    speeds, at a given flight speed, for the planning of an aerial
    imaging survey. Version 1.0.0,
    https://github.com/GeoRiskA/Aerial_Survey_Planning

"""

from fractions import Fraction
from decimal import Decimal

################################    SETUP     ################################

flight_speed = 10.0 # in m/s, with decimal

pixel_size = 0.05 # in m, with decimals

safety_threshold = 60 # in percentage (%)

################################ END OF SETUP ################################

max_speed_dec = pixel_size / flight_speed

max_shutter_speed = Fraction(Decimal(str(max_speed_dec)))
max_num = int(round(max_shutter_speed.numerator/max_shutter_speed.numerator,0))
max_den = int(round(max_shutter_speed.denominator/max_shutter_speed.numerator,0))

threshold = (100 - safety_threshold)/100
ideal_speed_dec = (threshold * pixel_size) / flight_speed
ideal_speed = Fraction(Decimal(str(ideal_speed_dec))).limit_denominator()
ideal_num = int(round(ideal_speed.numerator/ideal_speed.numerator,0))
idal_den = int(round(ideal_speed.denominator/ideal_speed.numerator,0))

print(' ')
print('=======================================================')
print('=     MINIMUM AND IDEAL SHUTTER SPEED CALCULATION     =')
print('=======================================================')
print('     (c) B. Smets - RMCA/VUB (v. 1.0.0, 13 May 2021)')
print(' ')
print('For a flight speed of ' + str(flight_speed) + ' m/s')
print('with a ground sampling distance of ' + str(pixel_size) + ' m,')
print('the minimum shutter speed is ' + str(max_speed_dec) + ' seconds')
print(' ')
print('-->  ' + str(max_num)+'/'+str(max_den))
print(' ')
print('-->  ' + str(ideal_num)+'/'+str(idal_den) + ' ideally')

