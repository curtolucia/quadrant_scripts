---
# Contact information

Author: Lucia Curto

email: lcurto@at.fcen.uba.ar


---
## Description
1. Select data according quality control of turbulent fluxes/covariances.

2. Performs quadrant analysis of high-frequancy micrometeorological and eddy-covariance data. 
    1. Separate instantaneous turbulent covariances according quadrant contribution 
    2. Calculation of contribution of each quadrant to total turbulent covariances
    3. Applied to momentum, temperature, CO2 and q turbulent covariances (can be extended to any scalar c)

---
## Available files

The following files are available:

 1. **main_cuad.py** contains the necessary to implement quadrant analysis.
    - It has a for, for read each file, and makes all calculation for each file (half-hour data). If you have only one file, remove this part.
    - Select data according quality control (less than 30\% missing data, less than 250 for stationary test).
    - Makes all calculation for all vertical levels with information.
    - Also it saves results from 2.i (in "cuadrantes") and 2.ii  (in "Sih/Si0").
    - All the auxiliar calculations are un auxiliar functions.

 2. **func_aux.py** contains auxiliar functions to compute 2.i and 2.ii.
    - calc_cuad: defines function for separating covariance contribution according their quadrant.
    - calc_S: defines function for calculate contribution of each quadrant to total turbulent covariances.
      
 3. **func_uw_cuad.py** contains auxiliar functions to compute 2.i for momentum covariance.
    - flujo_uw_cuad: separates instantaneous turbulent covariances according quadrant contribution for momentum covariance for all vertical levels.  

 4. **func_uw_S.py** contains auxiliar functions to compute 2.ii for momentum covariance.
    - flujo_uw_S: calculate contribution of each quadrant to total turbulent covariances for momentum covariance for all vertical levels.

 5. **func_wT_cuad.py** contains auxiliar functions to compute 2.i for temperature covariance.
    - flujo_wT_cuad: separates instantaneous turbulent covariances according quadrant contribution for temperature covariance for all vertical levels.  

 6. **func_wT_S.py** contains auxiliar functions to compute 2.ii for temperature covariance.
    - flujo_wT_S: calculate contribution of each quadrant to total turbulent covariances for temperature covariance for all vertical levels.

 7. **func_wc_cuad.py** contains auxiliar functions to compute 2.i for scalar covariance.
    - flujo_wc_cuad: separates instantaneous turbulent covariances according quadrant contribution for carbon dioxide and specific humidity for the verticla level of 3 m. 

 8. **func_wc_S.py** contains auxiliar functions to compute 2.ii for scalar covariance.
    - flujo_wc_S: calculate contribution of each quadrant to total turbulent covariances for carbon dioxide and specific humidity for the verticla level of 3 m.   
