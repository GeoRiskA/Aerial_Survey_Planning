#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------------------------------------
SCRIPT TO CALCULATE THE FOOTPRINT AND THE GROUND PIXEL RESOLUTION OF IMAGES
FOR THE PLANNING Of AN AERIAL SURVEY (UAS, HELICOPTER, ETC.)
----------------------------------------------------------------------------

Version: 1.0.0 (14/05/2021)
Author: Benoît SMETS
       (Royal Museum for Central Africa / Vrije Universiteit Brussel)

Citation:
    Smets, B., 2021.
    Aerial Survey Planning [UAS_footprint_and_GSD_Table_v100.py].
    Version 1.0
    https://github.com/GeoRiskA/Aerial_Survey_Planning.
    DOI: 10.5281/zenodo.4762100

Camera models currently available:
    - FC330 (DJI Phantom 4 - 12MPix)

Note:
    - Elevations and footprints are provided in metre
    - Ground sampling resolutions are provided in centimetre
    
"""

import math
import pandas as pd

################################    SETUP     ################################

### CAMERA USED
#---------------
camera = "P4"
# Available cameras= "P4"; 

### ELEVATION RANGE
#-------------------
z_min = 50   # Minimum elevation in m
z_max = 200   # Maximum elevation in m
z_step = 5    # Elevation steps withing the range, in m

### SAVING OPTION
#-----------------
save_results = True
output_folder = '/Users/benoitsmets/Desktop/'  # with '/' at the end
output_table_name = 'table_test_Phantom4'

################################ END OF SETUP ################################

### PRE-CONFIGURED CAMERAS
#--------------------------

if camera == "P4":
    cam_type = "Camera of the DJI Phantom 4 quadcopter"
    model = "FC330"
    sensor_L = 6.24768 # in mm
    sensor_l = 4.68576 # in mm
    focal_length = 3.61 # in mm
    width = 4000 # in pixel
    height = 3000 # in pixel

### CALCULATE FIELDS OF VIEW
#----------------------------

hfov = 2 * math.atan((sensor_L/2)/focal_length)
vfov = 2 * math.atan((sensor_l/2)/focal_length)

### CREATE TABLE WITH FOOTPRINT AND SPATIAL RESOLUTION
#------------------------------------------------------

## First, create the elevation range

z_max_python = z_max + z_step  # to include z_max value in the list
z_range = [*range(z_min, z_max_python, z_step)]
df = pd.DataFrame(z_range, columns=['Elevation'])
df = df.set_index('Elevation')

## Second calculate the columns of the dataframe

h_footprint = [] # empty list to store horizontal footprints
v_footprint = [] # empty list to store vertical footprints
resolution = [] # empty list to store (vertical, here) resolution
dem_resolution = [] # empty list to store DEM resolution

for z in z_range:
    h_fp = z*hfov
    h_footprint.append(round(h_fp,2))
    v_fp = z*vfov
    v_footprint.append(round(v_fp,2))

    resol = v_fp/height*100
    resolution.append(round(resol,1))
    dem_resol = 2*resol
    dem_resolution.append(round(dem_resol, 1))

df['h_footprint'] = h_footprint
df['v_footprint'] = v_footprint
df['GSD'] = resolution
df['DEM_GSD'] = dem_resolution

### PRINT THE RESULTS IN THE CONSOLE
#------------------------------------

print(' ')
print('==================================================================================')
print('=   Table of footprint and ground sampling distance for aerial survey planning   =')
print('==================================================================================')
print('    (c) Benoît Smets - RMCA/VUB  (v. 1.0.0, 14 May 2021)')
print(' ')
print(' ')
print('CAMERA USED: ' + cam_type)
print('CAMERA MODEL: ' + model)
print('IMAGE SIZE: ' + str(width) + 'x' + str(height) + ' pixels')
print('FOCAL LENGTH: ' + str(focal_length) + ' mm')
print(' ')
print('Calculated horizontal field of view: ')
print('   ' + str(round(hfov, 3)) + ' rad')
print('Calculated vertical field of view: ')
print('   ' + str(round(vfov, 3)) + ' rad')
print(' ')
print(' ')
print('CALCULATED TABLE')
print('-----------------')
print(' ')
print(df)
print(' ')
print('TABLE LEGEND:')
print('--> \'Elevation\' is the distance from the camera to the ground (in m)')
print('--> \'h_footprint\' is the horizontal footprint (in m)')
print('--> \'v_footprint\' is the vertical footprint (in m)')
print('--> \'GSD\' is the ground sampling distance or image pixel resolution (in cm)')
print('--> \'DEM_GSD\' is the expected maximum resolution of a derived DEM (in cm)')
print(' ')
print(' ')

### SAVING THE CALCULATED TABLE INTO A CSV FILE
#-----------------------------------------------

if save_results == True:
    df.to_csv(output_folder + output_table_name + '.csv')
    print('TABLE SAVED IN CSV FORMAT')
    print('-------------------------')
    print('LOCATION: ' + output_folder)
    print('TABLE NAME: ' + output_table_name + '.csv')

### END OF SCRIPT
#-----------------
print(' ')
print(' ')
print(' ')
print('#####   PROCESSING COMPLETED   #####')
