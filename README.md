# Aerial Survey Planning  

This repository is a collection of Python scripts used to properly prepare/plan an aerial imaging survey.  

The scripts help to select the proper camera parameters, flight speed, flight elevation above the ground, ground sampling distance, etc., based on the characteristics of the equipment used and the constraints of the field survey.   

### Scripts currently available:
- **UAS_footprint_and_GSD_Table_v100.py:** Script used to calculate the image footprint, ground sampling distance and expected max. DEM resolution, based on the flight elevattion.  

- **UAS_min_ShutterSpeed_calculation_v100.py:** Script allowing the calculation of the minimum and ideal (security threshold) shutter speed for a given flight speed, in order to avoid image blurring.

### Licence and citation:
These scripts are open-source and under a GPL-3.0 licence.
If you use these scripts or a tuned version of them in your work, please cite them according to the citation information provided within the script. Thank you!
  
### Author(s):  
***Benoît Smets***
  Natural Hazards Service (GeoRiskA), Dpt. of Earth Sciences, ROYAL MUSEUM FOR CENTRAL AFRICA (Belgium)
  Cartography and GIS Research Group, Dpt. of Geography, VRIJE UNIVERSITEIT BRUSSEL (Belgium)
  *E-MAIL:* benoit (at) africamuseum.be
  *WEBSITES:* https://georiska.africamuseum.be/ | https://we.vub.ac.be/en/cartography-and-gis | https://bsmets.net/
  
