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

---
## Format of input text files

This script works with text files separated by commas.

The following files are required by the code (see the code for requirements as input):

1. **missing data** for each high-frequancy micrometeorological, a file with the same denomination, with \% of missing data for every variable:
   
   - data: date and time of acquisition.

   For h= 1.5m, 3m, 5m and 7m:
   - u_h:  streamwise velocity component
   - v_h:  cross-stream velocity component
   - w_h:  vertical velocity component
   - T_h:  sonic temperature

    For 3 m:
   - CO2_3m: carbon dioxide density
   - H2O_3m: water vapor density
   - p_3m: pressure

2. **stationary test** for each turbulent covariance, a file with the same denomination as each high-frequancy micrometeorological:

   For h= 1.5m, 3m, 5m and 7m:
   - cov_uw_h: covariance of streamwise velocity component
   - cov_vw_h: covariance of cross-stream velocity component
   - cov_wT_h: covariance of vertical velocity component

    For 3 m:
   - cov_wCO2_3m: covariance of carbon dioxide density
   - cov_wH2O_3m: covariance of water vapor density
   - cov_wq_3m: covariance of specific humidity

3. **desvios** for each high-frequancy micrometeorological variable and covariance, a file with the same denomination as each high-frequancy micrometeorological:

   - time: date and time of acquisition.
      
   For h= 1.5m, 3m, 5m and 7m:
   - u_desvio_h: perturbed streamwise velocity component (u')
   - v_desvio_h: perturbed cross-stream velocity component (v')
   - w_desvio_h: perturbed vertical velocity component (w')
   - T_desvio_h: perturbed sonic temperature (T')
   - cov_uw_h: covariance of streamwise velocity component (u'w')
   - cov_vw_h: covariance of cross-stream velocity component (v'w')
   - cov_wT_h: covariance of vertical velocity component (w'T')

    For 3 m:
   - CO2_3m: perturbed carbon dioxide density (CO2')
   - H2O_3m: perturbed water vapor density (H2O')
   - q_3m: perturbed specific humidity (q')
   - cov_wCO2_3m: covariance of carbon dioxide density (w'CO2')
   - cov_wH2O_3m: covariance of water vapor density (w'H2O')
   - cov_wq_3m: covariance of specific humidity (w'q')
   - cov_qCO2_3m: covariance of q'CO2'
   - cov_qT_3m: covariance of q'T'
   - cov_CO2T_3m: covariance of CO2'T'

4. **medios** mean values for each high-frequancy micrometeorological variable and covariance, a file with the same denomination as each high-frequancy micrometeorological:
      
   For h= 1.5m, 3m, 5m and 7m:
   - u_medio_h: mean value of streamwise velocity component (u)
   - v_medio_h: mean value of cross-stream velocity component (v)
   - w_medio_h: mean value of vertical velocity component (w)
   - T_medio_h: mean value of sonic temperature (T)
   - u_std_h: standar deviation of streamwise velocity component (u)
   - v_std_h: standar deviation value of cross-stream velocity component (v)
   - w_std_h: standar deviation value of vertical velocity component (w)
   - T_std_h: standar deviation value of sonic temperature (T)
   - cov_uw_h: mean value of covariance of streamwise velocity component (u'w')
   - cov_vw_h: mean value of covariance of cross-stream velocity component (v'w')
   - cov_wT_h: mean value of covariance of vertical velocity component (w'T')

    For 3 m:
   - CO2_medio_3m: mean value of carbon dioxide density (CO2)
   - H2O_medio_3m: mean value of water vapor density (H2O)
   - q_medio_3m: mean value of specific humidity (q)
   - CO2_std_3m: standar deviation value of carbon dioxide density (CO2)
   - H2O_std_3m: standar deviation value of water vapor density (H2O)
   - q_std_3m: standar deviation value of specific humidity (q)
   - cov_wCO2_3m: mean value of covariance of carbon dioxide density (w'CO2')
   - cov_wH2O_3m: mean value of covariance of water vapor density (w'H2O')
   - cov_wq_3m: mean value of covariance of specific humidity (w'q')
   - cov_qCO2_3m: mean value of covariance of q'CO2'
   - cov_qT_3m: mean value of covariance of q'T'
   - cov_CO2T_3m: mean value of covariance of CO2'T'
